#!/usr/bin/env python3
"""This module contains BasicCache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    MAX_ITEMS = float('inf')

    def __init__(self):
        """constructor"""
        super().__init__()

    def put(self, key, item):
        """assign item to key"""
        if key and item:
            self.cache_data[key] = item
        pass

    def get(self, key):
        """gets the key value"""
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
