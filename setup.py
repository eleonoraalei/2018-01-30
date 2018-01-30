#!/usr/bin/python2.7
from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Hello world app',
  ext_modules = cythonize("hello.pyx"),
)

# setup(
#     ext_modules = cythonize("primes.pyx")
# )
