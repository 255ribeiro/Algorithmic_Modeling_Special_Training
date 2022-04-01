# -*- coding: utf-8 -*-

#imports
#import math
#import math as m
from math import ceil, sqrt


def blondel(total_height, max_riser, dec_places = 3):
    # the number of steps
    n_steps = total_height / max_riser
    #print(n_steps)

    # ceil the number of steps to the next integer
    n_steps = ceil(n_steps)

    #print(n_steps)

    # calculate the real raiser
    real_riser = total_height / n_steps

    #print(real_raiser)
    # round the real_raiser value to the number of decimal places set
    real_riser = round(real_riser, dec_places)
   

    #print(real_riser)
    # calculate the tread value based on the Blondel Formula
    tread  = round( .63 - (2 * real_riser) , dec_places)
    
    return n_steps, real_riser, tread

