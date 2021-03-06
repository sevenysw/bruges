#!/usr/bin/env python
# -*- coding: utf 8 -*-
"""
Python installation file.
"""
from setuptools import setup
import re

verstr = 'unknown'
VERSIONFILE = "bruges/_version.py"
with open(VERSIONFILE, "r")as f:
    verstrline = f.read().strip()
    pattern = re.compile(r"__version__ = ['\"](.*)['\"]")
    mo = pattern.search(verstrline)
if mo:
    verstr = mo.group(1)
    print("Version "+verstr)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

REQUIREMENTS = ['numpy', 'scipy']

CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Intended Audience :: Science/Research',
               'Natural Language :: English',
               'License :: OSI Approved :: Apache Software License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               ]

setup(name='bruges',
      version=verstr,
      author='Agile Geoscience',
      author_email='hello@agilegeoscience.com',
      packages=['bruges',
                'bruges.attribute',
                'bruges.filters',
                'bruges.noise',
                'bruges.reflection',
                'bruges.petrophysics',
                'bruges.rockphysics',
                'bruges.transform',
                'bruges.unit',
                'bruges.util',
                ],
      description='Useful geophysics functions',
      long_description=open('README.rst').read(),
      url='http://pypi.python.org/pypi/bruges/',
      install_requires=REQUIREMENTS,
      classifiers=CLASSIFIERS,
      license='Apache 2',
      )
