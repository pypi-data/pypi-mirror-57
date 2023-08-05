#!/usr/bin/env python

from setuptools import setup
from m2r import convert

import koradctl as me
from koradctl.psu import tested_firmware

with open('./README.md', 'r', encoding='utf-8') as f:
    long_description = convert(f.read())

setup(
    name=me.__proj_name__,
    version=me.__version__,
    description='Control utility for Korad / Tenma power supplies',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Attie Grande',
    author_email='attie@attie.co.uk',
    url='https://github.com/attie/koradctl',
    license='BSD-3-Clause',
    packages=[ 'koradctl' ],
    install_requires=[
        'pyserial',
    ],
    entry_points={
        'console_scripts': [
            'koradctl = koradctl.__main__:cli',
        ]
    },
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: Freely Distributable',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Utilities',
    ],
)
