#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='terminalgame',
    version='0.0.5',
    description=(
        'Terminalgame is a Python wrapper module for developing games'
    ),
    long_description=open('README.rst').read(),
    author='phlix',
    author_email='feijiawei11@nudt.edu.cn',
    maintainer='phlix',
    maintainer_email='feijiawei11@nudt.edu.cn',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Phlix1/terminalgame',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries'
    ],
)