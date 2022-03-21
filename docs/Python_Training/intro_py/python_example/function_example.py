# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:58:52 2022

@author: ferraz
"""

from staircase_example import blondel


result = blondel(3.25, .178, 2)


print('Number of Steps: {}\nTread : {}\nRiser : {}'.format(result[0], result[2], result[1] ))