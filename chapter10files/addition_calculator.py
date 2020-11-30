# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:22:15 2020

@author: jrrivera
"""

print("Please insert two numbers to add!")
print('Insert "q" when you would like to quit.')

while True:
    num1 = input('first number: ')
    if num1 == 'q':
        print('Goodbye!')
        break
    num2 = input('second number: ')
    if num2 == 'q':
        print('Goodbye!')
        break
    try:
        num1 = int(num1)
        num2 = int(num2)
        sum = num1 + num2 
    except ValueError:
        print('Input is not a number, please try again.')
    
    else:
        print('Your sum is: {}'.format(sum))