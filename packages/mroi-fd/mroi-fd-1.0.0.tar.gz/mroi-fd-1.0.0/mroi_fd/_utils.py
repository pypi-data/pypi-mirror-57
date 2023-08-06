import math

def expand_rectangle(rect, scale):

    """
    Increase each side of the rectangle by scale.
    """

    x, y, w, h = rect
    w_new = int(w + w*scale*2)
    h_new = int(h + h*scale*2)
    x_new = max(0, int(x - w*scale))
    y_new = max(0, int(y - h*scale))

    return (x_new, y_new, w_new, h_new)

def pad_rectangle(rect, dx, dy):

    """
    Increase width of the rectangle by dx, and height by dy.
    """

    x, y, w, h = rect
    w_new = int(w + 2*dx)
    h_new = int(h + 2*dy)
    x_new = max(0, int(x - dx))
    y_new = max(0, int(y - dy))

    return (x_new, y_new, w_new, h_new)

def euclidean_distance(p0, p1):

    x0, y0 = p0
    x1, y1 = p1

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

def crop_image(rect, image):

    x, y, w, h = rect

    return image[y:y+h, x:x+w]

def change_ext(filename, new_ext):

    tmp = filename.rsplit('.')
    tmp[1] = new_ext
    return '.'.join(tmp)

