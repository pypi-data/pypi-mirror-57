import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mroi-fd", # Replace with your own username
    version="0.0.5",
    author="ailabuser",
    author_email="lab@ailab.space",
    description=\
        """
        Face detection wrapper using hybrid margin-based region of interest
        (MROI) approach."
        """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ailabuser/bacha-hybrid-mroi-face-detection",

    packages=setuptools.find_packages(),

    # Refer to  https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Unix"
    ],
    python_requires='>=3.7.4',
)
