#!/usr/bin/env python

import os

from setuptools import setup

with open("README.rst", "r") as f:
    readme = f.read()


def get_packages(package):
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name="djoser-edge",
    version="2.0.4",
    packages=get_packages("djoser"),
    license="MIT",
    author="SUNSCRAPERS",
    description="REST version of Django authentication system.",
    author_email="info@sunscrapers.com",
    long_description=readme,
    install_requires=["django-templated-mail","drf-yasg-edge>=2.0"],
    setup_requires=["Babel>=2.6.0"],
    include_package_data=True,
    url="https://github.com/sunscrapers/djoser",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
