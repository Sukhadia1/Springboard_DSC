# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:58:25 2020

@author: Abhishek Sukhadia
"""

from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='titanic',
    version='0.1',
    description='Analysis of the Titanic dataset',
    long_description=readme(),
    install_requires=[
      	'pypandoc>=1.4'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/Sukhadia1/Springboard_DSC/tree/master/Exercises/titanic_datascience',
    author='Abhishek Sukhadia',  # Substitute your name
    author_email='abhi.sukhadia153@gmail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
)
