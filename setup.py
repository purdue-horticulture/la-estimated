# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


setup(
    name='la-estimated',
    version='0.1.0',
    description='Get Leaf Area Estimate',
    url='https://github.com/purdue-horticulture/la-estimated',
    author='purdue-horticulture',
    author_email='kkalbaug@purdue.edu',
    license='GNU General Public License v3.0',
    install_requires=[
        'opencv-python'
    ],
)