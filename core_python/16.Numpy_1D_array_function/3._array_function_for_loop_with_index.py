# Importing all functions and objects from the numpy module
from numpy import *

# Creating a 1D array using the array function from numpy
stu_roll = array([101, 102, 103, 104, 105])

# Getting the length of the array
n = len(stu_roll)

# Iterating through each index of the array and printing the index and corresponding element
for i in range(n):
    print(f'index, {i} = {stu_roll[i]}')
