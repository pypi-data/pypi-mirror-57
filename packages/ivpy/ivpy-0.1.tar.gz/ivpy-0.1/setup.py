from setuptools import find_packages
from distutils.core import setup, Extension
import numpy

sources = [f"src/{x}.c" for x in ['_core', 'variable', 'xtab', 'queue']]

extension = Extension('_core', sources=sources, include_dirs=[numpy.get_include(), 'src'])

setup(name='ivpy',
      version='0.1',
      author='Eric E. Graves',
      author_email='gravcon5+ivpy@gmail.com',
      license='LICENSE.txt',
      packages=find_packages(),
      description='Discretize continuous arrays using information value.',
      ext_modules=[extension])
