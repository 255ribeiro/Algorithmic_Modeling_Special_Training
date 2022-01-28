# input of the number
number = int(input('Type some number:\n'))

"""
every text inside this cotation marks is a comment
even this one

"""

# test if the number is even
if number % 2 == 0:
    print(number, ' is even') # if the number is even, print this line
    print( 'still in the code block')
    # test if the number is also divided by 3
    if number % 3 == 0:
        print ( number, ' is divided by 6')

    # some meaningless oparatos to ilustrate the concept of code blocks
    number = number + 1
    print(number)
# elif only runs if the if logical test is False
elif number % 3 == 0:
    print (number, 'is an odd number divided by 3')
# any number of  elifs can be used
# this second elif is only tested if
# the if and the elif before it returns False
elif number % 7 == 0:
    print (number, 'is an odd number, not divided by 3, but divided by 7')
    
# only if every if and elif returns false,
# the else block runs
else: # the else statement does not eval any expression
    print(number, ' is odd and not divided by 3 nor 7')
    number = number - 1
    print(number)
