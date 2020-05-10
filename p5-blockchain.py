# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:09:31 2020

@author: sankalp
"""

import hashlib
from datetime import datetime
  
class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      
    def calc_hash(self,data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

def get_utc():
    
    utc = datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")
#"We are going to encode this string of data!"
block1 = Block(get_utc(), "Test 1", 0)
block2 = Block(get_utc(), "Test 2", block1)
block3 = Block(get_utc(), "Test 3", block2)

print(block1.data)
print(block1.hash)
print(block1.timestamp)
print(block2.previous_hash.data)