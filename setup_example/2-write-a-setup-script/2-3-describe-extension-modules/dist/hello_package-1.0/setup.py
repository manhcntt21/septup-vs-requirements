from distutils.core import setup, Extension

# Define a simple extension module
hello_module = Extension('hello',
                        sources=['hello.c'])

setup(
    name='hello_package',
    version='1.0',
    description='A simple extension module example',
    ext_modules=[hello_module]
)