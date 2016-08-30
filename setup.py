# -*- coding: utf-8 -*-


import os
from setuptools import setup
from setuptools import find_packages


with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='django-search-listview',
    version='0.1.1',
    packages=find_packages(),
    long_description=long_description,
    description='Searchable and paginable ListView',
    author='Quentin Schroter',
    author_email='qschroter@gmail.com',
    maintainer='Quentin Schroter',
    maintainer_email='qschroter@gmail.com',
    url='https://github.com/SchroterQuentin/django-search-listview',
    download_url='https://github.com/SchroterQuentin/django-search-listview/tarball/0.1',
    license='PSF',
    keywords=['django', 'listView', 'search'],
    include_package_data=True,
)
