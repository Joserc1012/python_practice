# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:52:44 2020

@author: jrrivera
"""

class Employee():
    """Simple Employee class"""
    def __init__(self, firstn, lastn, salary):
        """Creates employee"""
        self.firstn = firstn
        self.lastn = lastn
        self.salary = salary
    
    def give_raise(self, amount=5000):
        """"Adds amount to annual salary of employee"""
        self.salary += amount