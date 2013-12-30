from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys
import re

import mvln

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()



def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='mvln',
    version='0.1.0',##find_version('mvln', '__init__.py'),
    url='http://github.com/rasmusprentow/mvln/',
    license='Apache Software License',
    author='Rasmus Prentow',
 #   tests_require=[],
 #   install_requires=[],
    scripts = ['mvln/mvln.py'],
    author_email='rasmus@prentow.dk',
    description='Combintion of mv and ln',
    long_description=long_description,
    packages=['mvln'],#find_packages(),
    platforms='linux',
    #test_suite='mvln.test.test_mvln',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: *nix',
        'Topic :: Software Development :: Libraries :: Python Modules',

        ],

    entry_points = {
        'console_scripts': [
            'mvln = mvln:main'
            
        ]
    }
)