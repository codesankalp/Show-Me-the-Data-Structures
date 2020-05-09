# -*- coding: utf-8 -*-
"""
Created on Sat May  9 08:33:05 2020

@author: sankalp
"""
from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.length = capacity
        self.cache = {}
        self.lst = deque([]) #to store recently used in queue
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1       #if key not found
        else:
            self.lst.remove(key)
            self.lst.append(key)
            return self.cache[key]            

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) <  self.length:
            self.cache[key] = value
            self.lst.append(key)
        else:
            to_remove = self.lst[0]
            self.cache.pop(to_remove)
            self.cache[key] = value


#tests

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);



print("pass") if our_cache.get(1) == 1  else print("fail")      # returns 1
print("pass") if our_cache.get(2) == 2 else print("fail")       # returns 2
print("pass") if our_cache.get(9) == -1 else print("fail")     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print("pass") if our_cache.get(3) == -1 else print("fail")     # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print()