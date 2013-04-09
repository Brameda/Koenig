#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='koenig',
    version='0.0.1-beta',
    description='Document & Printing app for Django.',
    author='Merijn Bertels',
    author_email='merijn.bertels@brameda.nl',
    long_description=open('README.rst', 'r').read(),
    url='http://brameda.nl/',
    packages=[
        'koenig',
        'koenig.backends',
        ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    zip_safe=False,
)