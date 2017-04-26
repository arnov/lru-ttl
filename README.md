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

```python
>>> cache = LRUCache(2)
>>> cache.set('key1', 'val1')
>>> cache.set('key2', 'val2')
>>> cache.set('key3', 'val3')
>>> 'key1' in cache
False
>>> 'key2' in cache
True
>>> 'key3' in cache
True
```

The TTL does **not** have precedence, so the last recently used keys will be evicted first!


```python
>>> cache = LRUCache(2)
>>> cache.set('key1', 'val1')
>>> cache.set('key2', 'val2', 10000)
>>> cache.set('key3', 'val3')
>>> 'key1' in cache
False
>>> 'key2' in cache
True
```
