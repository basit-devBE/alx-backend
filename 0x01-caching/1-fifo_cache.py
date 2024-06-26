#!/usr/bin/env python3
from base_caching import BaseCaching
from collections import OrderedDict
class FIFOCache(BaseCaching):
    """
    FIFOCache defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self,key,item):
        """Add an item to a cache"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item
        
        leng = len(self.cache_data)
        if leng > BaseCaching.MAX_ITEMS:
            first_key,_ = self.cache_data.popitem(False)
            print(f"DISCARD: {first_key}")

    def get(self,key):
        """Get an item from a cache"""
        if key is None or self.cache_data[key] is None:
            return None
        else:
            return self.cache_data[key]
