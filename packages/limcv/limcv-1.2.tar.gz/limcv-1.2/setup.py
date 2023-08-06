#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import path as os_path
from six import PY3
from setuptools import setup, find_packages

this_directory = os_path.abspath(os_path.dirname(__file__))

# 读取文件内容
def read_file(filename):
    if PY3:
        with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
            long_description = f.read()
    else:
        with open(os_path.join(this_directory, filename)) as f:
            long_description = f.read()
    return long_description

def parse_requirements(filename):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')
setup(
    name="limcv",
    version="1.2",
    author="Lim Chung",
    author_email='923739605@qq.com',
    packages=find_packages(),
    url='https://github.com/JamesChungZLL/limcv',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=reqs,
    scripts=[],
)

