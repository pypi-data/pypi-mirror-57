#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)

setup(
    name='pan-sdk-python',
    version='1.0.1',
    description='Panorama SDK for Python',
    long_description=open('README.rst').read(),
    author='tim.wang',
    author_email='317302030@qq.com',
    url='https://gogs.analyticservice.net/AASRND/pan-python-sdk',
    scripts=[],
    packages=find_packages(exclude=["tests*"]),
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
