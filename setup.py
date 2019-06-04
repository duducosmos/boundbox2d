#!/usr/bin/env python3
# -*- Coding: UTF-8 -*-
import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="boundbox2d",
    license="Apache License 2.0",
    version='1.0',
    author='Eduardo S. Pereira',
    author_email='pereira.somoza@gmail.com',
    packages=find_packages("src"),
    package_dir={"":"src"},
    description="Bound Box 2D",
    lond_description=read("README.md"),
    install_requires=["numpy",
                      "matplotlib",
                      ]
)