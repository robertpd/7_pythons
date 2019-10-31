# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

# with open('LICENSE') as f:
    # license = f.read()

setup(
    name='7_pythons',
    version='0.1.0',
    description='Reinforcement learning to develop advanced strategies in board games',
    long_description=readme,
    author='Robert Dooley',
    author_email='email@address.com',
    url='https://github.com/robertpd/7_pythons',
    license='',
    packages=find_packages(exclude=('tests', 'docs'))
)
