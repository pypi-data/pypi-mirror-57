#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='pyyaml-include',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    description='Extending PyYAML with a custom constructor for including YAML files within YAML files',
    url='https://github.com/tanbro/pyyaml-include',
    license='GNU General Public License v3 or later (GPLv3+)',
    author='liu xue yan',
    author_email='liu_xue_yan@foxmail.com',
    keywords='yaml PyYAML include',

    use_scm_version={
        # guess-next-dev: automatically guesses the next development version (default)
        # post-release:   generates post release versions (adds postN)
        'version_scheme': 'guess-next-dev',
        'write_to': 'src/yamlinclude/version.py',
    },

    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',

    setup_requires=['toml', 'setuptools_scm', 'setuptools_scm_git_archive'],
    extras_require={
        'all': ['toml'],
        'toml': ['toml'],
    },

    install_requires=['PyYAML>=3.12,!=4.*,<6.0'],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup',
    ],
)
