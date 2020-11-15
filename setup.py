# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='pysecurebox',
    packages=find_packages(include=['pysecurebox']),
    version='1.0.0',
    description='',
    author='Simone Perini',
    author_email='perinisimone98@gmail.com',
    url='https://github.com/CoffeePerry/securebox-py',
    license='MIT',
    install_requires=['pycryptodomex==3.9.9'],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
