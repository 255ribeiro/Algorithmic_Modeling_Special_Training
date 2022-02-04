# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 12:49:56 2022

@author: ferraz
"""
x = 5
a = list(range(x))
b = list(range(x, 2*x))


c = []

print(a , len(a))
print(b, len(b))



for i in range(len(b)):
    c.append([a[i], b[i]])
    
print(c)



