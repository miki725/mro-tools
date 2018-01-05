#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import os

from setuptools import find_packages, setup

from mro_tools import __author__, __description__, __version__


def read(fname):
    return (open(os.path.join(os.path.dirname(__file__), fname), 'rb')
            .read().decode('utf-8'))


authors = read('AUTHORS.rst')
history = read('HISTORY.rst').replace('.. :changelog:', '')
licence = read('LICENSE.rst')
readme = read('README.rst')

requirements = read('requirements.txt').splitlines() + [
    'setuptools',
]

test_requirements = (
    read('requirements.txt').splitlines() +
    read('requirements-dev.txt').splitlines()[1:]
)

setup(
    name='mro-tools',
    version=__version__,
    author=__author__,
    description=__description__,
    long_description='\n\n'.join([readme, history, authors, licence]),
    url='https://github.com/miki725/mro-tools',
    license='MIT',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=requirements,
    test_suite='tests',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'mro-tools = mro_tools.__main__:cli',
        ]
    },
    keywords=' '.join([
        'mro',
    ]),
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 2 - Pre-Alpha',
    ],
)
