#!/usr/bin/env python3
"""A caching algorithm for Last in first Out method"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """A caching algorithm for Last in first Out method"""
    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
