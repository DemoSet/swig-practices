#!/usr/bin/env python3
import os
from shutil import move

from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext


class CustomExtension(Extension):
    def __init__(self, name, sources, base_dir, *args, **kw):
        super().__init__(name, sources, *args, **kw)
        self.base_dir = base_dir


class CustomBuild(build_ext):
    def build_extension(self, ext: CustomExtension):

        if isinstance(ext, CustomExtension):
            ext.sources = [os.path.join(ext.base_dir, each) for each in ext.sources]

        super().build_extension(ext)

        if isinstance(ext, CustomExtension):
            raw_output = self.get_ext_fullpath(ext.name)

            filename = os.path.basename(raw_output)
            pathname = os.path.dirname(raw_output)

            output = os.path.join(pathname, ext.base_dir, filename)

            move(raw_output, output)


custom_extension = CustomExtension(name='_demo',
                                   sources=['demo_wrap.cxx', 'demo.cpp'],
                                   base_dir='demo',
                                   extra_compile_args=['-std=c++11'])
setup(
    name='lucien-demo',
    version='0.0.5',
    author="Lucien Shui",
    packages=find_packages(),
    ext_modules=[custom_extension],
    cmdclass={'build_ext': CustomBuild},
)
