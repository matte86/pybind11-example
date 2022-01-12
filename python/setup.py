from setuptools import setup

setup(
    name='hello_py',
    version='0.0.1',
    url='https://github.com/matte86/pybind11-example.git',
    author='Matteo Agnelli',
    author_email='agnelli.matteo@gmail.com',
    packages=['hello_py'],
    package_dir={"": "."},
    package_data={'': ['*.so', "*.dylib"]},
    include_package_data = True,
    description='An example python wrapper around a shared library',
)
