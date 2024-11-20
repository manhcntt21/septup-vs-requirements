from distutils.core import setup

setup(
    name='my-calculator',
    version='1.0',
    author='David Do',
    package_dir={'': 'src'},
    py_modules=['introduction', 'utils.add', 'utils.subtract'],
)