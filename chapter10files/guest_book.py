# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 08:33:51 2020

@author: jrrivera
"""
def ask():
    """Prompts the user for their name"""
    print('What is your name? ')
    name = input('Name: ')
    return name

def record(name):
    """Writes the name of the guests into a file"""
    with open('guest_book.txt', 'a') as file:
        file.write('{} has paid a visit!\n'.format(name))

def greeting(name):
    """Greets Guests"""
    print('Hello {}!'.format(name))

flag = ''
    
while flag != 'n':
    name = ask()
    record(name)
    greeting(name)
    flag = input('Keep Going?(y/n)')

