#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.1.5'

setup(
    name='github_release_notifier',
    python_requires=">=3",
    version=__version__,
    packages=find_packages(),
    author="Jay MOULIN",
    author_email="jaymoulin+github-release-notifier@gmail.com",
    description="Github Notifier",
    long_description=open('README.rst').read(),
    install_requires=["feedparser", "requests"],
    include_package_data=True,
    url='http://github.com/femtopixel/github-release-notifier/',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Internet",
        "Topic :: Software Development :: Pre-processors",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
    ],
    entry_points={
        'console_scripts': [
            'github-release-notifier = github_release_notifier.cli:main',
        ],
    },
    license="MIT",
)
