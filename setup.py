# -*- coding: utf-8 -*-
from setuptools import setup

import papis_rofi

with open('README.rst') as fd:
    long_description = fd.read()

setup(
    name='papis-rofi',
    version=papis_rofi.__version__,
    author='Alejandro Gallo',
    author_email='aamsgallo@gmail.com',
    license='GPLv3',
    url='https://github.com/papis/papis-rofi',
    install_requires=[
        "papis>=0.11.1",
        "papis-python-rofi==1.0.3",
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    description='Rofi based inerface for papis',
    long_description=long_description,
    extras_require=dict(
        develop=[
            "sphinx",
            'sphinx-click',
            'sphinx_rtd_theme',
            'pytest',
            'pytest-cov',
        ]
    ),
    keywords=[
        'papis', 'rofi', 'bibtex',
        'management', 'cli', 'biliography'
    ],
    packages=[
        "papis_rofi",
    ],
    entry_points={
        'papis.command': [
            'rofi=papis_rofi.main:main'
        ],
        'papis.picker': [
            'rofi=papis_rofi.main:Picker'
        ]
    },
    platforms=['linux', 'osx'],
)
