# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:51:55 2020

@author: jrrivera
"""

print("Please insert two numbers to add!")

try:
    num1 = int(input('first number: '))
    num2 = int(input('second number: '))
    sum = num1 + num2 
except ValueError:
    print('Input is not a number, please try again.')
    
else:
    print('Your sum is: {}'.format(sum))