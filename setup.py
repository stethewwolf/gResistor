from distutils.core import setup
from gresistor import app_name, app_version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=app_name,
    version=app_version,
    description      = 'Resistor color code calculator',
    author           = 'Stefano Prina',
    author_email     = 'stefano-prina@outlook.it',
    url              = 'https:/stefano-prina.it/gresistor',
    license          = 'GPL',
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=['gresistor.py'],
    data_files = [('share/gresistor',['gresistor.glade']),('share/applications',
                       ['gresistor.desktop']),('share/gresistor',
                       ['pixmaps/icon.png'])],
      )
