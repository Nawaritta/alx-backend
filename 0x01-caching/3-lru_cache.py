#!/usr/bin/env python3
"""This module contains LRUCache class"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """assign item to key"""
        if key and item:
            if self.cache_data:
                lru_key = list(self.cache_data)[0]
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(lru_key)
                print("DISCARD: {}".format(lru_key))
        pass

    def get(self, key):
        """gets the key value"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
