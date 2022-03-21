# -*- coding: utf-8 -*-

#imports
#import math
#import math as m
from math import ceil




def blondel(total_height, max_riser, dec_places = 3):
    # the number of steps
    n_steps = total_height / max_riser
    #print(n_steps)

    # ceil the number of steps to the next integer
    n_steps = ceil(n_steps)

    #print(n_steps)

    # calculate the real riser
    real_riser = total_height / n_steps

    #print(real_riser)
    # round the real_riser value to the number of decimal places set
    real_riser = round(real_riser, dec_places)
   
    x = 7
    #print(real_riser)
    # calculate the tread value based on the Blondel Formula
    tread  = round( .63 - (2 * real_riser) , dec_places)
    
    return n_steps, real_riser, tread



def main():
    # input the total height os the stair
    t_height = float(input('Set the total height of the stair:\n'))
    # input the maximum value for the riser
    max_r = float(input('Enter the maximum value for the riser:\n'))
    # Numer of decimal places to round the values

    result = blondel(t_height, max_r, 2)

    # show the results
    print('Number of Steps: {}\nTread : {}\nRiser : {}'.format(result[0], result[2], result[1] ))
    
x = 3   
if __name__ == "__main__": main()




