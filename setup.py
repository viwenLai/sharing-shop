# import sys

from setuptools import setup, find_packages

from mwtk_auth import __version__

install_requires = open('requirements').read().split()

setup(
    name='westsnow',
    version=__version__,
    install_requires=install_requires,
    scripts=['bin/ws-run'],
    packages=find_packages(exclude=["tests"]),
    author='null',
    author_email='admin@null.com',
    description='Component of the eshop project, code westsnow',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
