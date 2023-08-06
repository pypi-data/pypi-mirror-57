#!/usr/bin/env python

from setuptools import setup

from libyear.utils import load_requirements

setup(
    name='libyear',
    version='0.0.7',
    description='A simple measure of software dependency freshness.',
    long_description=open('README.md').read(),
    author='nasirhjafri',
    url='https://github.com/nasirhjafri/libyear',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['libyear', 'requirements'],
    py_modules=['libyear'],
    scripts=['libyear/libyear'],
    dependency_links=[
    ],
    install_requires=[load_requirements('requirements/requirements.txt')],
)
