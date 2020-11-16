# coding=utf-8

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='pysecurebox',
    packages=find_packages(include=['pysecurebox']),
    version='1.0.0',
    description='securebox-py (SecureBox for Python) is a lightweight package to create and manage consistent, '
                'encrypted and authenticated files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['security', 'files', 'encryption', 'authentication'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Security :: Cryptography',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],  # https://pypi.org/classifiers/
    author='Simone Perini',
    author_email='perinisimone98@gmail.com',
    license='MIT',
    url='https://github.com/CoffeePerry/securebox-py',
    download_url='https://github.com/CoffeePerry/securebox-py/archive/1.0.0.tar.gz',
    install_requires=['pycryptodomex==3.9.9'],
    setup_requires=['pytest-runner==5.2'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
