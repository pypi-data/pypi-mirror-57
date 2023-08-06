import pathlib
from distutils.core import setup
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='pypfm',
      version='1.3',
      description='Python pfm files reader',
      long_description=README,
      long_description_content_type="text/markdown",

      author='Wats0ns',
      author_email='Wats0ns@github.com',
      url='https://github.com/Wats0ns/pypfm',
      packages=['pypfm'],
      install_requires=['pyzfp', 'numpy'],
      include_package_data=True,
     )
