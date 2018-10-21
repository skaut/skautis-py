#!/usr/bin/env python
from setuptools import setup

setup(
    name='skautis-py',
    version='1.11.9',
    description='Python library for interaction with the Skautis API',
    author='Jakub Kulik',
    author_email='kulikjak@gmail.com',
    url='https://github.com/kulikjak/skautis-py',
    license='BSD',
    packages=["skautis"],
    long_description=open("README.md").read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    install_requires=[
        'zeep',
    ],
)
