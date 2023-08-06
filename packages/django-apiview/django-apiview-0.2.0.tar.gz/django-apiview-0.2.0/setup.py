# -*- coding: utf-8 -*-
import os
from io import open
from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), "r", encoding="utf-8") as fobj:
    long_description = fobj.read()

requires = [
    "django",
    "fastutils>=0.5.3",
    "bizerror>=0.2.3",
]

setup(
    name="django-apiview",
    version="0.2.0",
    description="Restful API view utils.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="zencore",
    author_email="dobetter@zencore.cn",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords=['django-apiview'],
    install_requires=requires,
    packages=find_packages(".", exclude=("example", "example.migrations", "example.tests" "examplepro")),
    py_modules=["apiview"],
    zip_safe=False,
)