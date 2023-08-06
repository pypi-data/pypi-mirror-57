from distutils.core import setup
from setuptools import find_packages, setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

print(long_description)
setup(name='pypfm',
      version='1.4.2',
      description='Python pfm files reader',
      author='Wats0ns',
      author_email='Wats0ns@github.com',
      url='https://github.com/Wats0ns/pypfm',
      packages=['pypfm'],
      install_requires=['pyzfp', 'numpy'],
      include_package_data=True,
      long_description_content_type='text/markdown',
      long_description=long_description,
     )
