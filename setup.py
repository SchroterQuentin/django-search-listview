# -*- coding: utf-8 -*-
import os
from setuptools import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='django-search-listview',
    version='0.2.1',
    packages = ["search_listview"],
    package_dir={'':'.'},
    include_package_data=True,
    package_data={
        "" : ["templates/search_listview/*.html", "static/search_listview/js/*.js"],
    },
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
    
)
