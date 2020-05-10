# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:23:15 2020

@author: sankalp
"""

import sys

def huffman_encoding(data):
    freq = {}
    code = {}
    
    for char in data:
        freq[char] = freq.get(char,0) + 1
    
    start = '0'
    for k in sorted(freq.items(), key = lambda x:x[1]):
        code[k[0]] = start
        start = '1' + start
    
    compressed_mess = ''
    for d in data:
        compressed_mess += code[d]
    
    return compressed_mess,code

def huffman_decoding(data,tree):
    reverse = dict()
    for i in tree:
        reverse[tree[i]] = i
    rev = ''
    decode = ''
    for d in data:
        if d == '0':
            decode += reverse[rev + d]
            rev = ''
        else:
            rev += d
    return decode

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))