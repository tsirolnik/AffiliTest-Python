#!/usr/bin/env python

from distutils.core import setup

setup(name='AffiliTest-Python',
      version='1.0',
      description='AffiliTest\'s API implemented in Python',
      author='Yehonatan Tsirolnik',
      author_email='yehonatan@affilitest.com',
      url='https://github.com/tsirolnik/AffiliTest-Python',
      packages=['affilitest'],
      install_requires=['requests'],
      license='MIT'
     )