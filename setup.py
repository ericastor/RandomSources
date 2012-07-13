#!/usr/bin/env python

from distutils.core import setup

setup(
    name='RandomSources',
    version='0.1.1',
    author='Eric Astor',
    author_email='eric.astor@gmail.com',
    packages=['randomSources'],
    url='https://github.com/ericastor/RandomSources/',
    license='LICENSE.txt',
    description='Drop-in replacements for Random, providing remote random-number sources.',
    long_description=open('README.rst').read()
)