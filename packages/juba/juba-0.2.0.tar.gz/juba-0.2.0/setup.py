#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup,find_packages

setup(name='juba',
      version='0.2.0',
      description='Juba Chinese Natural Language Processing',
      author='Hanju Li',
      author_email='99959828@qq.com',
      url='https://github.com/lihanju/juba',
      packages=find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'numpy',
        'matplotlib',
        'jieba',
        'requests',
        ]
      )