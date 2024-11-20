from distutils.core import setup

setup(
    name='pgk-data',
    version='1.0.0',
    package_dir={'': 'src'},
    packages=['mypkg'],
    package_data={
        'mypkg': ['data/*.dat'],
    }
)