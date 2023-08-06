#!/usr/bin/env python
import os
import sys
import platform
import re
from setuptools import setup

version = "0.1.1"

if sys.argv[-1] == 'safeu':

    version = platform.python_version()

    if not (re.search('3.6.*', version) or re.search('3.7.*', version)):
        os.system("python safeu/data_quality/setup.py build")

    os.system("python setup.py sdist build")
    os.system("python setup.py bdist_wheel --universal")
    sys.exit()


setup(
    name='safeu',
    version='0.1.0',
    description='Safe learning for unlabeled data',
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding='UTF-8').read(),
    author='De-Ming Liang, Yu-Feng Li',
    author_email='liangdm@lamda.nju.edu.cn, liyf@lamda.nju.edu.cn',
    url='https://git.nju.edu.cn/lamda/safeu',
    setup_requires=[],
    install_requires=[
            'numpy>=1.15.1',
            'scipy>=1.1.0',
            'scikit-learn>=0.19.2',
            'cvxopt>=1.2.0',
            
    ],
    packages=[
        'safeu',
        'safeu.classification',
        'safeu.datasets',
        'safeu.data_quality',
        'safeu.ensemble',
        'safeu.metrics',
        'safeu.model_uncertainty',
        'safeu.utils',
        'safeu.libs',
    ],
    package_dir={
        'safeu': 'safeu',
        'safeu.classification': 'safeu/classification',
        'safeu.datasets': 'safeu/datasets',
        'safeu.data_quality': 'safeu/data_quality',
        'safeu.ensemble': 'safeu/ensemble',
        'safeu.metrics': 'safeu/metrics',
        'safeu.model_uncertainty': 'safeu/model_uncertainty',
        'safeu.utils': 'safeu/utils',
        'safeu.libs': 'safeu/libs',
    },
    package_data={
        '': ['*.txt', '*.rst'],
        'safeu': ['data_quality/*',
               'data_quality/*/*',
               'datasets/data/*/*',
               'datasets/data/*',
               'datasets/descr/*',
               'libs/*',
               'libs/*/*',
               'libs/*/*/*',
               'libs/*/*/*/*'],
    }
)
