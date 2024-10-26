#!/usr/bin/env python
from setuptools import setup

setup(
    name='skautis-py',
    version='1.1.29',
    description='Python library for interaction with the Skautis API',
    author='Jakub Kulik',
    author_email='kulikjak@gmail.com',
    url='https://github.com/skaut/skautis-py',
    license='BSD',
    packages=["skautis"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
	'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
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
