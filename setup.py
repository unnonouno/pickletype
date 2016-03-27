#!/usr/bin/env python

from setuptools import setup


setup(
    name='pickletype',
    version='0.0.0',
    description='pickletype',
    author='Yuya Unno',
    author_email='unno@preferred.jp',
    packages=[
        'pickletype',
    ],
    install_requires=[
        'six',
    ],
    scripts=[
        'scripts/showtype.py',
    ],
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
)
