# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:32:56 2022

@author: ferraz
"""

# input base level as a float
base_level = float(input('type the value for the base level:\n'))
# input distance from floor to floor as a float
ftf = float(input('type the floor to floor distance:\n'))
# input number of floors as a integer
num_f = int(input('number of floor:\n'))


for i in range(num_f):
    # Print the floor number
    print ('Floor number: ', i)
    # Print the level value
    current_f = base_level + (ftf * i)
    print ('level: ', current_f)
    # print a line to separate the values
    print('----------')
    