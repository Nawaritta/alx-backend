#!/usr/bin/env python3
"""This module contains LIFOCache class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """assign item to key"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data)[-2]
                self.cache_data.pop(last_key)
                print("DISCARD: {}".format(last_key))
        pass

    def get(self, key):
        """gets the key value"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
