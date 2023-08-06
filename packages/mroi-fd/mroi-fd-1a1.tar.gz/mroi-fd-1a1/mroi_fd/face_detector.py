import logging
import cv2
import threading
import queue
import time
import llist
import numpy as np
from mtcnn.mtcnn import MTCNN
from . import _utils

def _template_matching(source, template, thres):

    assert 0.0 < thres <= 1.0

    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(source, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # Using TM_SQDIFF_NORMED method, the pixel location of the correlation map
    # with min_val gives the best match.
    if min_val < thres:
        h, w = template.shape[:2]
        x, y = min_loc
        return (x, y, w, h)

    return None

class RoutineManager:

    def __init__(self):
        self.__routine_funcs = {}
        self.__routine_args = {}
        self.__routine_kwargs = {}
        self.__running_thread = None
        self.__running_routine = None

    def add_routine(self, name, func, args=[], kwargs={}):

        if name not in self.__routine_funcs.keys():
            self.__routine_funcs[name] = func
            self.__routine_args[name] = args
            self.__routine_kwargs[name] = kwargs
        else:
            logging.error('Routine {} already exists!'.format(name))

    def run(self, name):

        self.__running_thread = threading.Thread(name=name,\
            target=self.__routine_funcs[name],\
            args=self.__routine_args[name],\
            kwargs=self.__routine_kwargs[name])

        self.__running_thread.start()
        self.__running_routine = name

        logging.debug("Started thread: {}".format(name))

    def stop(self):

        name = self.__running_thread.name
        self.__running_thread.join()

        logging.debug('Stopped thread: {}'.format(name))

        self.__running_thread = None
        self.__running_routine = None

    def current_routine(self):

        if self.__running_routine is not None:
            return self.__running_routine
        else:
            return 'None'

class FrameSequence:

    """
    This class can be used to keep track of any data within n-size window
    frames. For example, this can be used to record 10 most recent ROI from the
    previous 10 frames, or 10 most recent images.
    """

    class OutOfFrame(Exception):
        pass

    def __init__(self, maxsize):
        self.__dllist = llist.dllist()
        self.__maxsize = maxsize

    def add(self, item):

        """
        Add new (recent) item. If the max size is reached, the most oldest item
        in the list will be popped out of the list.
        """

        if self.__dllist.size + 1 > self.__maxsize:
            self.__dllist.popleft() # Push out oldest item in the list.
        self.__dllist.appendright(item)

    def prev(self, num_frames=1):
        assert num_frames >= 1 and type(num_frames) == int

        if num_frames > self.__dllist.size:
            raise FrameSequence.OutOfFrame

        size = self.__dllist.size
        for i in range(num_frames):
            yield self.__dllist.nodeat(size - i - 1).value

    def __str__(self):
        out = []
        for i in range(self.__dllist.size):
            out.append(self.__dllist.nodeat(i).value)
        return str(out)

    def __repr__(self):
        return self.__str__()


class FaceDetector:

    FD_HAAR_CASCADE = 0
    FD_JOINT_CASCADE = 1
    FD_MTCNN = 2

    MODE_N = 100
    MODE_FM = 102
    MODE_DM = 103
    MODE_NTM = 104
    MODE_FMTM = 105
    MODE_DMTM = 106

    ROUTINE_N = 200
    ROUTINE_FM = 201
    ROUTINE_DM = 202
    ROUTINE_TM = 203

    ROUTINE_STR = {\
        ROUTINE_N   : "ROUTINE_N",\
        ROUTINE_FM  : "ROUTINE_FM",\
        ROUTINE_DM  : "ROUTINE_DM",\
        ROUTINE_TM  : "ROUTINE_TM"\
    }

    def __init__(self, fd_obj, mode=MODE_FMTM):

        self.__mode = mode
        self.__lifo_out = queue.LifoQueue(maxsize=360)
        self.__lifo_in = queue.LifoQueue(maxsize=1)
        self.__fifo_switch_call = queue.Queue(maxsize=1)
        self.__template = None
        self.__lifo_out_template = queue.LifoQueue(maxsize=1)
        self.__rtn_mgr = RoutineManager()
        self.__frseq_ROI = FrameSequence(10)
        self.__fd_obj = fd_obj

        # Initializing routines and main thread.
        ##################################################

        # Normal routine.
        self.__rtn_mgr.add_routine(\
            FaceDetector.ROUTINE_N, self.__normal)

        # Fixed-margin-based routine.
        self.__rtn_mgr.add_routine(\
            FaceDetector.ROUTINE_FM, self.__fixed_margin)

        # Dynamic-margin-based routine.
        self.__rtn_mgr.add_routine(\
            FaceDetector.ROUTINE_DM, self.__dynamic_margin)

        # Template matching routine.
        self.__rtn_mgr.add_routine(\
            FaceDetector.ROUTINE_TM, self.__template_matching)

        # Main thread, where threads are invoked to start and join.
        self.__main_thread = threading.Thread(name='main',\
            target=self.__main, args=[FaceDetector.ROUTINE_N])

    def __main(self, routine):

        """
        This thread is responsible in waiting for routine switch invocation.
        When a routine switch is invoked (i.e., by the switch_routine() function
        call), the currently running routine thread is stopped and the next
        routine is run.
        """

        self.__rtn_mgr.run(routine)

        while True:

            # Blocking.
            item = self.__fifo_switch_call.get()
            if item is None:
                break
            current_routine, next_routine = item
            logging.debug("Switch: {} ({}) -> {} ({})".format(\
                current_routine, FaceDetector.ROUTINE_STR[current_routine],\
                next_routine, FaceDetector.ROUTINE_STR[next_routine])\
            )

            self.__rtn_mgr.stop()
            self.__rtn_mgr.run(next_routine)

    def run(self):

        self.__main_thread.start()

    def set_mode(self, mode):

        assert mode in [\
            FaceDetector.MODE_N,\
            FaceDetector.MODE_FM,\
            FaceDetector.MODE_DM,\
            FaceDetector.MODE_NTM,\
            FaceDetector.MODE_FMTM,\
            FaceDetector.MODE_DMTM]

        self.__mode = mode

        logging.debug('Mode set to %s' % mode)

    def __switch_routine(self, routine):

        assert routine in [\
            FaceDetector.ROUTINE_N,\
            FaceDetector.ROUTINE_FM,\
            FaceDetector.ROUTINE_DM,\
            FaceDetector.ROUTINE_TM]

        logging.debug("Invoke switch: {} ({}) -> {} ({})".format(\
            self.__rtn_mgr.current_routine(),\
            FaceDetector.ROUTINE_STR[self.__rtn_mgr.current_routine()],\
            routine,\
            FaceDetector.ROUTINE_STR[routine]\
        ))

        self.__fifo_switch_call.put(\
            (self.__rtn_mgr.current_routine(), routine))

    def __post_face_detection(self, face_rect, img, t_x=0, t_y=0,
            save_template=True):

        """__post_face_detection

        @param face_rect:
            The bounding box (x, y, w, h) containing the face detected.
        @param img:
            The image frame.
        @param t_x:
            Translation of face_rect along x.
        @param t_y:
            Translation of face_rect along y.
        @param save_template:
            If this is set to true, the image within face_rect is saved as
            template, used for template matching (TM) routine.
        """

        face_found = face_rect is not None

        if face_found:

            if t_x > 0 or t_y > 0:
                x, y, w, h = face_rect
                global_ROI = (t_x + x, t_y + y, w, h)
                face_rect = global_ROI

            if save_template:
                self.__template = _utils.crop_image(face_rect, img)
            self.__frseq_ROI.add(face_rect)
            self.__lifo_out.put(face_rect)

        return face_found

    @staticmethod
    def detect(fd_obj, image):

        """
        Returns ROI (size-4 tuple of (x, y, w, h)) of the face detected, or None
        if no face detected.

        This method may be overridden by a derived class to use your own custom
        face detector as the main routine. Simply make sure this method returns
        a face ROI is a face is detected, or None if no face is detected.
        """

        return None

    def __normal(self):

        """
        Run the normal main routine for face detection.
        """

        while True:

            image = self.__lifo_in.get()
            face_rect = None

            if image is None:
                break

            face_rect = self.detect(self.__fd_obj, image)
            self.__post_face_detection(face_rect, image)

            if self.__mode == FaceDetector.MODE_FM:
                if face_rect is not None:
                    self.__switch_routine(FaceDetector.ROUTINE_FM)
                    break
            if self.__mode == FaceDetector.MODE_DM:
                if face_rect is not None:
                    self.__switch_routine(FaceDetector.ROUTINE_DM)
                    break
            if self.__mode == FaceDetector.MODE_NTM:
                if face_rect is None:
                    self.__switch_routine(FaceDetector.ROUTINE_TM)
                    break
            if self.__mode == FaceDetector.MODE_FMTM:
                if face_rect is not None:
                    self.__switch_routine(FaceDetector.ROUTINE_FM)
                    break
            if self.__mode == FaceDetector.MODE_DMTM:
                if face_rect is not None:
                    self.__switch_routine(FaceDetector.ROUTINE_DM)
                    break

    def __fixed_margin(self):

        """
        Run fixed-margin-based ROI face detection routine.
        """

        while True:

            image = self.__lifo_in.get()
            face_rect = None

            if image is None:
                break

            img_ROI, = self.__frseq_ROI.prev()
            img_ROI = _utils.expand_rectangle(img_ROI, 0.25)
            sub_image = _utils.crop_image(img_ROI, image)

            face_rect = self.detect(self.__fd_obj, sub_image)
            t_x, t_y, _, _ = img_ROI
            self.__post_face_detection(face_rect, image, t_x, t_y)

            if self.__mode == FaceDetector.MODE_FM:
                if face_rect is None:
                    self.__switch_routine(FaceDetector.ROUTINE_N)
                    break
            if self.__mode == FaceDetector.MODE_FMTM:
                if face_rect is None:
                    self.__switch_routine(FaceDetector.ROUTINE_TM)
                    break

    def __dynamic_margin(self):

        """
        Run dynamic-margin-based ROI face detection routine.
        """

        while True:

            image = self.__lifo_in.get()
            face_rect = None

            if image is None:
                break

            # Get previous 2 frames.
            try:
                prev1, prev2 = self.__frseq_ROI.prev(2)
            except FrameSequence.OutOfFrame:
                logging.debug("Frame sequence has no previous two frames.")
                prev1, = self.__frseq_ROI.prev()
                prev2 = None

            # Increase the rectangle size by a fixed value.
            img_ROI = _utils.expand_rectangle(prev1, 0.20)

            # Increase the rectangle size proportional to the head movement in
            # previous two frames.
            if prev2 is not None:
                x2, y2, _, _ = prev2
                x1, y1, _, _ = prev1

                dx = abs(x2 - x1)
                dy = abs(y2 - y1)

                logging.debug("dx: {}   dy: {}".format(dx, dy))

                img_ROI = _utils.pad_rectangle(img_ROI, dx, dy)

            sub_image = _utils.crop_image(img_ROI, image)

            face_rect = self.detect(self.__fd_obj, sub_image)
            t_x, t_y, _, _ = img_ROI
            self.__post_face_detection(face_rect, image, t_x, t_y)

            if self.__mode == FaceDetector.MODE_DM:
                if face_rect is None:
                    self.__switch_routine(FaceDetector.ROUTINE_N)
                    break
            if self.__mode == FaceDetector.MODE_DMTM:
                if face_rect is None:
                    self.__switch_routine(FaceDetector.ROUTINE_TM)
                    break

    def __template_matching(self):

        """
        Run template matching routine.
        """

        frame_counter = 0

        # Process 10 frames using template matching.
        while frame_counter != 10:

            image = self.__lifo_in.get()
            face_rect = None

            frame_counter += 1

            if image is None:
                break

            if self.__template is not None:
                face_rect = _template_matching(image, self.__template, 0.2)
            else:
                logging.warning(\
                    "Empty template. Exiting template matching routine.")
                break

            self.__post_face_detection(face_rect, image, save_template=False)

        self.__switch_routine(FaceDetector.ROUTINE_N)

    def input_image(self, image):

        try:
            self.__lifo_in.put(image)
            return True
        except queue.Full:
            return False

    def get_face_region(self):

        try:
            return self.__lifo_out.get(timeout=1e-3)
        except queue.Empty:
            return None

    def get_face_template(self):

        try:
            return self.__lifo_out_template.get(timeout=1e-3)
        except queue.Empty:
            return None

    def get_routine_name(self):

        routine_str = {
            FaceDetector.ROUTINE_N: "Normal Routine",
            FaceDetector.ROUTINE_FM: "Fixed Margin",
            FaceDetector.ROUTINE_DM: "Dynamic Margin",
            FaceDetector.ROUTINE_TM: "Template Matching",
            'None': 'None'
        }

        return routine_str[self.__rtn_mgr.current_routine()]

    def clean(self):

        logging.debug("Cleaning FaceDetector...")

        # Empty remaining image input.
        while True:
            try:
                self.__lifo_in.get(block=False)
            except queue.Empty:
                break

        self.__lifo_in.put(None)
        self.__fifo_switch_call.put(None)
        self.__rtn_mgr.stop()

        logging.debug("FaceDetector cleaned.")

class MROI_HaarCascade(FaceDetector):

    """
    Haar Cascade using hybrid MROI face detectiona technique. This uses OpenCV
    Haar Cascade implementation.
    """

    def __init__(self, mode=FaceDetector.MODE_N):

        fd_obj = cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
        super().__init__(fd_obj, mode)

    @staticmethod
    def detect(fd_obj, image):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        out = fd_obj.detectMultiScale(\
            gray,
            scaleFactor=1.05,
            minNeighbors=3,
            flags=cv2.CASCADE_SCALE_IMAGE,
            minSize=(int(30), int(30)),
        )

        if len(out) > 0:
            return out[0]
        else:
            return None

class MROI_MTCNN(FaceDetector):

    """
    MTCNN using hybrid MROI face detection technique. This uses implementation
    an implementation from https://github.com/ipazc/mtcnn.
    """

    def __init__(self, mode=FaceDetector.MODE_N):
        fd_obj = MTCNN()
        super().__init__(fd_obj, mode)

    @staticmethod
    def detect(fd_obj, image):

        rgb_src = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = fd_obj.detect_faces(rgb_src)

        if len(result) > 0:
            return result[0]['box']
        else:
            return None
