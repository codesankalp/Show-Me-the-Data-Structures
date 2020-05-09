# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:16:16 2020

@author: sankalp
"""

import os

file_ls = []
def find_files(suffix, path):
    dir_ls = []
    path = os.path.abspath(".")
    path = os.path.realpath(path)
    ls = os.listdir(path)
    for i in ls:
        if os.path.isdir(i):
            dir_ls.append(i)
        else:
            if i.endswith(".c"):
                file_ls.append(os.path.realpath(i))
    for i in dir_ls:
        new_path = os.path.join(path,i)
        os.chdir(new_path)
        find_files(".c",new_path)
    return file_ls

path = os.path.abspath("testdir")
path = os.path.realpath(path)
suffix = ".c"
print(find_files(suffix,path)) #ans
# to get back to the current working dir
while os.getcwd() != path:     
    os.chdir("../")
os.chdir("../")
        
                    