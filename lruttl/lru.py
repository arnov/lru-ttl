from datetime import datetime, timedelta
from collections import OrderedDict


class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def __contains__(self, key):
        return self.get(key) is not None

    def __getitem__(self, key):
        return self.get(key)

    def set(self, key, value, ttl=None):
        if len(self.cache) == self.size:
            self.cache.popitem(last=False)

        now = datetime.now()
        expires = None

        if ttl:
            expires = now + timedelta(seconds=ttl)

        item = {'value': value,
                'expires': expires}
        self.cache[key] = item
        
    if hasattr(OrderedDict, 'move_to_end'):
        # python 3.2+
        def _move_to_end(self, key):
            self.cache.move_to_end(key)
    else:
        # python 2.7
        def _move_to_end(self, key):
            self.cache[key] = self.cache.pop(key)

    def get(self, key):
        if key in self.cache:
            now = datetime.now()
            self._move_to_end(key)  # Mark as most recently used

            item = self.cache[key]
            if item['expires'] and item['expires'] < now:
                del self.cache[key]
            else:
                return item['value']


if __name__ == '__main__':
    cache = LRUCache(10)
    cache.set('id', ['some object'], 1)
    print('id' in cache)
    print(cache.get('id'))
