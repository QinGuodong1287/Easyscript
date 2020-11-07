from distutils.core import setup
from subprocess import Popen
import os
from sys import stdin, stdout, stderr
from Cython.Build import cythonize

setup(
    name="cursor_contorl", 
    ext_modules=cythonize(
        os.path.dirname(os.path.abspath(__file__)) + "/source_codes/cursor_contorl.py"
    )
)
Popen("mv cursor_contorl.c source_codes/", shell=True, stdin=stdin, stdout=stdout, stderr=stderr).wait()
