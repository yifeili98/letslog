#!/usr/bin/env python
# coding: utf-8

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='letslog',
    packages = ['letslog'],
    version='0.0.3',
    license='MIT',
    author='YiFei Li',
    author_email='yifeil@berkeley.edu',
    description='A logger package',
    url='https://github.com/yifeili98/letslog',
    download_url='https://github.com/yifeili98/letslog/archive/0.0.3.tar.gz',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
          'datetime',
          'pathlib',
      ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)