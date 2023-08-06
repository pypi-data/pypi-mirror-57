#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="ai-django-fileupload",
    version="0.1.1",
    author=u'Ambient Innovation GmbH',
    author_email='info@ambient-innovation.com',
    packages=find_packages(),
    include_package_data=True,
    url="https://gitlab.ambient-innovation.com/ai/ai-django-fileupload",
    download_url="https://gitlab.ambient-innovation.com/ai/ai-django-fileupload.git",
    license="The MIT License (MIT)",
    description="Integrate jQuery fileupload",
    long_description="A minimal django package with a working jquery file upload and list of files",
    zip_safe=False,
    install_requires=['pillow'],
)
