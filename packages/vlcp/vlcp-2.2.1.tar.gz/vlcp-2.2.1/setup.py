#!/usr/bin/env python
'''
Created on 2015/11/17

:author: hubo
'''
try:
    import ez_setup
    ez_setup.use_setuptools()
except Exception:
    pass
from setuptools import setup, find_packages

VERSION = '2.2.1'

setup(name='vlcp',
      version=VERSION,
      description='Full stack framework for SDN Controller, support Openflow 1.0, Openflow 1.3, and Nicira extensions. Also a powerful coroutine-based web server.',
      author='Hu Bo',
      author_email='hubo1016@126.com',
      license="http://www.apache.org/licenses/LICENSE-2.0",
      url='http://github.com/hubo1016/vlcp',
      keywords=['SDN', 'VLCP', 'Openflow'],
      test_suite = 'tests',
      use_2to3=False,
      install_requires = ["nstruct>=1.3.1", "pychecktype>=1.4.0"],
      packages=find_packages(exclude=("tests","tests.*","misc","misc.*")),
      entry_points={'console_scripts': ['vlcp-start = vlcp.start:default_start']},
      python_requires='>=3.5'
)
