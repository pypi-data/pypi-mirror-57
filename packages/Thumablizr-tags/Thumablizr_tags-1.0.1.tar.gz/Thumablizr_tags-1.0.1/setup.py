# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup, find_packages, Extension

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = ['thumbalizr']

setup(
    name='Thumablizr_tags',
    version='1.0.1',
    py_modules=['thumbalizr_tags'],
    scripts=['thumbalizr_tags.py', 'settings.py'],
    description='Use Thumbalizr in your Django templates',
    long_description=read('README'),
    url='https://github.com/juliensobrier/thumbalizr_django',
    license='Apache',
    author='Julien Sobrier',
    author_email='julien@sobrier.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages(exclude=('tests')),
    #namespace_packages=["thumbalizr"],
    install_requires=requirements,
    #test_suite = 'tests',
    long_description_content_type='text/markdown',
)
