# Importing all functions and objects from the numpy module
from numpy import *

# Creating a 1D array using the array function from numpy
stu_roll = array([101, 102, 103, 104, 105])

# Getting the length of the array
n = len(stu_roll)

# Initializing a variable to keep track of the index
i = 0

# Looping through each index of the array
while i < n:
    # Printing the index and corresponding element
    print('index', i, '=', stu_roll[i])
    # Incrementing the index
    i += 1
