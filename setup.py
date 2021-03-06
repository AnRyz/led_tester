# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Led Functions',
    version='0.1.0',
    description='Assignment 3 on Software Development',
    long_description=readme,
    author='Anna Ryzova',
    author_email='anna.ryzova@ucd.ie',
    url='https://github.com/AnRyz/led_tester.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)