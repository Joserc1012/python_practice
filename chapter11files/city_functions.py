# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 07:59:55 2020

@author: jrrivera
"""

def city_country(city, country, population=None):
    if population:
        string = f'{city.title()}, {country.title()} - population {population}'
    else:
        string = f'{city.title()}, {country.title()}'
    return string