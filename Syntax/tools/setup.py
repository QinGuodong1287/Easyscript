from distutils.core import setup, Extension

setup(name="cursor_contorl", ext_modules=[Extension("cursor_contorl", sources=["cursor_contorl_module.c"])])
