#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')

setup(
    name = "django-periodically",
    version = "0.3.1",
    description='Periodic task management for your Django projects.',
    url = 'https://github.com/hzdg/django-periodically',
    long_description=README,

    author = 'Matthew Tretter',
    author_email = 'matthew@exanimo.com',
    packages = find_packages()
)
