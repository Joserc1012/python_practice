# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 09:01:52 2020

@author: jrrivera
"""

import unittest as u
from employee import Employee

class EmployeeTestCase(u.TestCase):
    """Class for testing employee class"""
    def setUp(self):
        """Creates employee object for testing"""
        self.employee = Employee('Jose', 'Rivera', 23000)
    
    def test_give_default_raise(self):
        """Tests the default of the give_raise method"""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 28000 )
    
    def test_give_custom_raise(self):
        """Tests customs amount of the give_raise method"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.salary, 33000 )
    
if __name__ == '__main__':
    u.main()