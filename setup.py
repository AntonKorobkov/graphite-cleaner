#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='graphite-cleaner',
    version='0.1.0',
    description='Graphite Whisper stale database files remover',
    author='Services Wroclaw Team',
    author_email='svc-code@opera.com',
    url='https://opera.com',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'graphite-cleaner = graphite_cleaner.main:main']
    },
    install_requires=[
        'argh==0.24.1'
    ]
)
