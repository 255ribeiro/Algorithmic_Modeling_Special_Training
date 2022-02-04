# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:03:03 2022

@author: ferraz
"""

a = [1,3,4, True, 2.4, 'text']

print(a)


a[2] = 10

print('size of list a: ',len(a))

for element in a:
    print('value: ' , element, ' of type: ' ,type(element))
    
c = list(range( 10))

print (c)
    



