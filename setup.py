from distutils.core import setup

setup(
    name='lru-ttl',
    version='0.0.1',
    py_modules=['lruttl'],
    description='A least recently used (LRU) cache implementation with time to live (TTL)',
    author='Arno Veenstra',
    author_email='arnoveenstra@gmail.com',
    url='https://github.com/arnov/lru-ttl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ])
