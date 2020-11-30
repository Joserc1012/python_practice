# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:52:13 2020

@author: jrrivera
"""

def word_count(file, word):
    """Counts the number of time a word is repeated in file"""
    try:
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        count = contents.lower().count(word)
        print(f'The word "{word}" is found {count} in "{file}".')

files = ['captain_chaos.txt', 'dracula.txt','conjurer_of_venus.txt' ]

for file in files:
    word_count(file, 'the')