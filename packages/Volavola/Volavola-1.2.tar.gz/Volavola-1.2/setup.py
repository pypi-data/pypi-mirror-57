# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:37:16 2019

@author: dhk13
"""

import setuptools

setuptools.setup(
    name="Volavola",
    version="v1.2",
    license='CPL v3.0',
    author="dhk1349",
    author_email="dhk1349@naver.com",
    description="Volvola is memory forensic tool based on Volatility2",
    long_description=open('README.md').read(),
    url="https://github.com/dhk1349/Volavola",
    packages=setuptools.find_packages(),
    classifiers=[
        # 패키지에 대한 태그
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows"
    ],
)