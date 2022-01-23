# input base level as a float
base_level = float(input('type the value for the base level:\n'))
# input distance from floor to floor as a float
ftf = float(input('type the floor to floor distance:\n'))
# input number of floors as a integer
num_f = int(input('number of floor:\n'))
# Before the loop start we need to prepare some variables
# set the current floor levels as the base level
current_f = base_level
# set the floor cout to zero
count = 0
# Loop:
# while the count varabel is less than the number of floors
while count < num_f:
    # Print the floor number
    print ('Floor number: ', count)
    # Print the level value
    print ('level: ', current_f)
    # print a line to separate the values
    print('----------')
    # Update the floor count
    count = count + 1
    # Update the valur of the current floor
    current_f = current_f + ftf
    

