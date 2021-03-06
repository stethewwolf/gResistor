#!/usr/bin/env python3
from gresistor3.gresistor import app_name, app_version
from setuptools import find_packages, setup
import sys, os

setupdir = os.path.dirname(__file__)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

if sys.version_info < (3, 8):
    raise RuntimeError("GResistor3 requires Python 3.8 or later")

setup(
    name=app_name,
    version=app_version,
    description      = 'Resistor color code calculator',
    author           = 'Stefano Prina',
    author_email     = 'stethewwolf@gmail.com',
    url              = 'https://gresistor.stethewwolf.eu',
    license          = 'LGPL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=['gresistor3'],
    entry_points={'console_scripts': ['gresistor3=gresistor3.gresistor:main']},
    data_files = [
    	('share/gresistor',['gresistor3/gresistor.glade','gresistor3/pixmaps/48x48/eu.stethewwolf.gresistor.png']),
    	('share/applications', ['eu.stethewwolf.gresistor.desktop']),
    	('share/icons/', ['gresistor3/pixmaps/128x128/eu.stethewwolf.gresistor.png']),
        ('share/metainfo/', ['eu.stethewwolf.gresistor.metainfo.xml']),
    	]
    )


