# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:27:53 2020

@author: jrrivera
"""

def ask():
    """Prompts the user for their name"""
    print('What is your name? ')
    name = input('Name: ')
    return name

def write_guest(name):
    """Writes users name to a file"""
    with open('guest.txt', 'w') as file:
        file.write(name)

name = ask()
write_guest(name)