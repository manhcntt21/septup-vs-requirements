from distutils.core import setup
# root package is src
setup(
    name='animals-package',
    version='1.0',
    description='a package for animals-related utilities and functionalities',
    author='David Do',
    package_dir={'': 'src'},
    packages=['animals', 'animals.dog']
)