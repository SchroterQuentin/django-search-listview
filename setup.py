# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


with open('README.md') as readme:
    long_description = readme.read()


def recursive_requirements(requirement_file, libs, links, path=''):
    if not requirement_file.startswith(path):
        requirement_file = os.path.join(path, requirement_file)
    with open(requirement_file) as requirements:
        for requirement in requirements.readlines():
            if requirement.startswith('-r'):
                requirement_file = requirement.split()[1]
                if not path:
                    path = requirement_file.rsplit('/', 1)[0]
                recursive_requirements(requirement_file, libs, links,
                                       path=path)
            elif requirement.startswith('-f'):
                links.append(requirement.split()[1])
            else:
                libs.append(requirement)

libraries, dependency_links = [], []
recursive_requirements('requirements.txt', libraries, dependency_links)

setup(
    name='django_search_model',
    version='0.1',
    packages=find_packages(),
    install_requires=libraries,
    dependency_links=dependency_links,
    long_description=long_description,
    description='',
    author='Quentin Schroter',
    author_email='qschroter@gmail.com',
    maintainer='Quentin Schroter',
    maintainer_email='qschroter@gmail.com',
    url='https://github.com/SchroterQuentin/Django-SearchableListView',
    download_url='https://github.com/SchroterQuentin/Django-SearchableListView',
    license='PSF',
    keywords=['django', 'listView', 'search'],
    include_package_data=True,
)
