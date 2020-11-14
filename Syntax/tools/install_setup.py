from distutils.core import setup
import os
from Cython.Build import cythonize

program_path = os.path.dirname(os.path.abspath(__file__))

from .contorl import execute

setup(
    name="cursor_contorl", 
    ext_modules=cythonize(
        program_path + "/source_codes/cursor_contorl.py"
    )
)
execute("mv cursor_contorl.c source_codes/", output=False)
