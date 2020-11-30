# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:34:00 2020

@author: jrrivera
"""

file1 = 'dogs.txt'
file2 = 'cats.txt'

def display(file):
    try:    
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(contents + '\n')

display(file1)
display(file2)