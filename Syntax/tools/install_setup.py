from distutils.core import setup
import os, sys
from Cython.Build import cythonize

setup(
    name="cursor_contorl", 
    ext_modules=cythonize("cursor_contorl.py")
)
