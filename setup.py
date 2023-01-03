#!/usr/bin/env python3
from setuptools import setup
import os

import zoomdl

# README as long_description
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    name="zoomdl",
    version=zoomdl.__version__,
    description="Download Zoom recorded meetings easily",
    url="https://github.com/Battleman/zoomdl",
    author="Olivier Cloux",
    license="MIT",
    packages=['zoomdl'],
    package_data={'zoomdl': ['zoomdl/*']},
    include_package_data=True,
    install_requires=['setuptools', 'requests~=2.23', 'demjson3~=3.0.5', 'tqdm~=4.50.2'],
    entry_points={
        "console_scripts": [
            "zoomdl=zoomdl:main",
        ]
    },
)
