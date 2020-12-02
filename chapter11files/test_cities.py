# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:02:27 2020

@author: jrrivera
"""

import unittest as u
from city_functions import city_country

class CityCountryTestCase(u.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Tests if city country format is correct"""
        self.assertEqual(city_country('santiago', 'chile'), 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Tests if city country population format is correct"""
        self.assertEqual(city_country('santiago', 'chile', 150000),
                         'Santiago, Chile - population 150000')
    
if __name__ == '__main__':
    u.main()