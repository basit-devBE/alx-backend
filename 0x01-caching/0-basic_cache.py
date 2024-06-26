#!/usr/bin/env python3
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """Add an item to a cache"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from a cache"""
        if key is None:
            return
        else:
            return self.cache_data.get(key)
