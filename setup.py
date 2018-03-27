#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

import scdl

setup(
    name='pyscdl',
    version=scdl.__version__,
    packages=find_packages(),
    author='DarkArt3k',
    author_email='luca@ahsubs-design.com',
    description='Download Music from Souncloud',
    long_description="https://github.com/AHSubsDesign/pyscdl/README",
    install_requires=[
        'docopt',
        'mutagen',
        'termcolor',
        'requests',
        'clint'
    ],
    url='https://github.com/AHSubsDesign/pyscdl',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Multimedia :: Sound/Audio',
    ],
    entry_points={
        'console_scripts': [
            'scdl = scdl.scdl:main',
        ],
    },
)
