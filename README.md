# Introduction

This is a Python LRU cache implementation with TTL support, this way you can ensure you will not get results older than the specified TTL.

# Installation

pip install lru-ttl

# How to use

```python
>>> from lruttl import LRUCache
>>> cache = LRUCache(10)
>>> cache.set('key1', ['some object'], 5)
>>> cache['key1']
['some object']
>>> # wait a couple of seconds
>>> cache['key1']

```
