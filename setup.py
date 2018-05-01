import os
from distutils.core import setup
from setuptools import find_packages


readme = ''
if os.path.isfile('README.md'):
    with open('README.md') as f:
        readme = f.read()

setup(
    name='lru-ttl',
    version='0.0.6',
    py_modules=['lruttl'],
    packages=find_packages(),
    description='A least recently used (LRU) cache implementation with time to live (TTL)',
    long_description=readme + '\n',
    long_description_content_type='text/markdown',
    author='Arno Veenstra',
    author_email='arnoveenstra@gmail.com',
    url='https://github.com/arnov/lru-ttl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ])
