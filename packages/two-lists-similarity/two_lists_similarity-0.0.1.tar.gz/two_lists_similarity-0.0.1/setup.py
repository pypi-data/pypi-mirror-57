# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:04:31 2019

@author: Praneeth Ponnekanti, (praneeth.ponnekanti@gmail.com)
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="two_lists_similarity",
    version="0.0.1",
    author="Praneeth Ponnekanti",
    author_email="praneeth.ponnekanti@gmail.com",
    description="A package to implement fuzzy matching between items in two different lists (an input list and a reference list.) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="",
    packages=setuptools.find_packages(),
    py_modules = ["two_lists_similarity"],
    package_dir = {'' : 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)