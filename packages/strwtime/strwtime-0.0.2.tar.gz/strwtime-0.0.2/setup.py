#!/usr/bin/env python

from distutils.core import setup

setup(name='strwtime',
  version='0.0.2',
  description='Helloworld package',
  author='Anybody Anybody',
  author_email='meechanic.design@gmail.com',
  url='https://github.com/meechanic/strwtime',
  download_url = 'https://github.com/meechanic/strwtime/archive/v0_0_2.tar.gz',
  license="MIT",
  scripts=['bin/strwtime_runserver.py'],
  packages=['strwtime']
)
