#!/usr/bin/env python
import os
from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()



with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='tensorboard_aggregator',
      version='0.0.1',
      description='Aggregate results from multiple Tensorflow runs',
      long_description= "" if not os.path.isfile("README.md") else read_md('README.md'),
      author='Spenhouet',
      author_email='Spenhouet',
      url='https://github.com/Spenhouet/tensorboard-aggregator',
      setup_requires=['pytest-runner',],
      tests_require=['pytest','python-coveralls'],
      install_requires=[
          requirements,
      ],
      license=['MIT'],
	packages=['tensorboard_aggregator'],
      scripts=[],
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
     )
