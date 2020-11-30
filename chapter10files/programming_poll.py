# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 09:41:54 2020

@author: jrrivera
"""
def append_poll(name, reason):
    with open('poll.txt', 'a') as file:
        file.write('{} says: {}\n'.format(name, reason))

def poll(name):
    reason = input('Hi {}, what do you like about programming? \n'.format(name))
    append_poll(name, reason)


flag = ''

while flag != 'n':
    name = input("What is your name? \n")
    poll(name.title())
    flag = input('Keep Going?(y/n)\n')
    