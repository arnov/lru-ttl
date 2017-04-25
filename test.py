import unittest
from lruttl import LRUCache
from time import sleep


class TestCache(unittest.TestCase):
    def test_basic(self):
        cache = LRUCache(10)
        cache.set('id', ['some object'], 1)

        self.assertEqual(cache.get('id'), ['some object'])

    def test_ttl(self):
        cache = LRUCache(10)
        cache.set('id', ['some object'], 1)
        sleep(3)
        self.assertEqual(cache.get('id'), None)

    def test_size(self):
        cache = LRUCache(10)

        for i in range(12):
            # Do a get so the item is moved down in the stack
            cache.get(0)
            cache.set(i, 'object {}'.format(i))

        self.assertTrue(0 in cache)
        self.assertTrue(1 not in cache)
        self.assertTrue(11 in cache)


if __name__ == '__main__':
    unittest.main()
