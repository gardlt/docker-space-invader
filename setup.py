from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

# import io, codecs, os

class Tox(TestCommand):
    """Runs Tox comands"""
    def finalize_options(self):
        """preps test suite"""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """runs test suite"""
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

class PyTest(TestCommand):
    """Runs Python test comands with this test_* infront of it."""
    def finalize_options(self):
        """preps test suite"""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """runs test suite"""
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='python-app-template',
    version='0.0.1',
    description='Implementation of a a basic space invader game',
    author='Tetrasol',
    author_email='garivera89@gmail.com',
    url='https://github.com',
    platforms='any',
    test_require=['tox'],
    cmdclass={'test': Tox},
    extras_require={'testing': ['pytest']},
    packages=['pyapp']
)
