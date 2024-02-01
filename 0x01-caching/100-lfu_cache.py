#!/usr/bin/env python3
"""This module contains LFUCache class"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """constructor"""
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """assign item to key"""
        if key and item:
            for k in self.cache_data:
                if k not in self.freq:
                    self.freq[k] = 1
                else:
                    self.freq[k] += 1

            mlfu = 0
            lfu_key = None
            for k in self.freq:
                if self.freq[k] > mlfu:
                    mlfu = self.freq[k]
                    lfu_key = k

            if lfu_key and lfu_key in self.cache_data:
                self.cache_data.pop(lfu_key)
                print("DISCARD: {}".format(lfu_key))

            if key in self.cache_data:
                self.freq[key] += 1
            else:
                self.freq[key] = 1

            self.cache_data[key] = item

    def get(self, key):
        """gets the key value"""
        if key and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.freq[key] += 1
            self.put(key, value)

            return self.cache_data[key]
        return None
