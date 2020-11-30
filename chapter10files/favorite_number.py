# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 13:21:55 2020

@author: jrrivera
"""
import json

def ask_num():
    """Asks user for a favorite number and writes it to a file"""
    num = input('What is your favorite number?')
    to_file(num)
    

def to_file(num):
    """Takes user's favorite number and stores it"""
    with open('favorite_num.json', 'w') as f:
        json.dump(num, f)

def num_recall(file):
    """Remember number written by user"""
    try:
        with open(file, 'r') as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def remember():
    """Verifies if number is stored and prints to user if it is"""
    num = num_recall('favorite_num.json')
    if num:
        print(f'Your favorite number is {num}!')
    else:
        ask_num()
        
remember()
            
