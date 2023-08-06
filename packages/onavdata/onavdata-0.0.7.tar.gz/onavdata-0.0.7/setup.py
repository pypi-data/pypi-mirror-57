import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "onavdata",
    version = "0.0.7",
    author = "Organic Navigation",
    author_email = "hamid@organicnavigation.com",
    description = ("Quickly import reference data sets for navigation system design and testing."),
    packages = ['onavdata'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['bin/onavdata-print-shortnames'],
    install_requires=[
          'toml',
          'pandas'
      ],
)
