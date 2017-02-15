# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='slgFramework',
    version='0.1.0',
    description='package for interactive media in Python',
    long_description=readme,
    author='Sylvain Le Groux',
    author_email='slegroux@ccrma.stanford.edu',
    url='https://github.com/slegroux/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

