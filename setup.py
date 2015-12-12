"""
ConfigParser subclass for config files
with no sections.

"""

from distutils.core import setup
import setuptools  # this import is needed so that some options and commands work

setup(
    name='simple-configparser',
    version='0.1.3.0',
    author='Brian E. Peterson',
    author_email='bepetersondev@gmail.com',
    url='https://github.com/bepetersn/simple-configparser',
    zip_safe=False,
    description=__doc__,
    packages=[
        'simple_configparser'
    ],
    install_requires=[
    ],
)
