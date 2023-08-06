import codecs
import os
import re
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")

setup(
    name='aiofiles38',
    version=find_version('aiofiles', '__init__.py'),
    packages=find_packages(),
    url='https://github.com/kasheemlew/aiofiles',
    license='Apache 2.0',
    author='Tin Tvrtkovic',
    author_email='tinchester@gmail.com',
    description='this will be removed after the origin aiofiles38 supports new versions of Python ',
    long_description=readme,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: System :: Filesystems",
    ]
)
