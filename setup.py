from setuptools import setup, find_packages

setup(
    name="visa",
    version="0.0.0",
    author="mp",
    author_email="learnermp@gmail.com",
    packages=find_packages()
)
'''
Purpose of setup.py

The setup.py file tells Python:

what the project name is

what version it is

who the author is

which packages should be included

how the project should be installed

This allows you to install your project using: pip install -e .

pip install -e . will be run with "pip install -r requirements.txt"

The setup() Function
setup(
    name="visa",

Defines the package name.

After installation you can import like:

import visa
'''