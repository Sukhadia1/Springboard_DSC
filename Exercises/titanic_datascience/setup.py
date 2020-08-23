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
      	'pypandoc>=1.4',
        'watermark>=1.8.1',
        'pandas>=0.24.2',
        'scikit-learn>=0.20.3',
        'scipy>=1.2.1',
        'matplotlib>=3.0.3',
        'pytest>=4.3.1',
        'pytest-runner>=4.4',
        'click>=7.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://github.com/Sukhadia1/Springboard_DSC/tree/master/Exercises/titanic_datascience',
    author='Abhishek Sukhadia',  # Substitute your name
    author_email='abhi.sukhadia153@gmail.com',  # Substitute your email
    license='MIT',
    packages=['titanic'],
    entry_points='''
        [console_scripts]
        titanic_analysis=titanic.command_line:titanic_analysis
    '''
)
