#!/usr/bin/env python3
"""This module contains MRUCache class"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """assign item to key"""
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = list(self.cache_data)[-2]
                self.cache_data.pop(mru_key)
                print("DISCARD: {}".format(mru_key))
        pass

    def get(self, key):
        """gets the key value"""
        if key and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.put(key, value)
            return self.cache_data[key]
        return None
