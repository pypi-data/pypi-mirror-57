# Always prefer setuptools over distutils
import setuptools

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open("README.md", "r") as fh:
    # Get the long description from the README file
    long_description = fh.read()

setuptools.setup(
    name="xidpy",
    version="1.1",
    author="Darwin Smith II",
    author_email="xidpy@dwin.fastmail.com",
    description="Python implementation of XID globally unique id generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dwin/xidpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
