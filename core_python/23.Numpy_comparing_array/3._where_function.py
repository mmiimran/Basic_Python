# Importing required functionality from numpy
from numpy import *

# Creating numpy arrays 'a' and 'b' with given elements
a = array([101, 12, 300, 4, 500])
b = array([100, 20, 30, 400, 50])

# Using the where function to create a new array where elements from 'a' are chosen if the condition 'a>b' is True, otherwise elements from 'b' are chosen
result = where(a > b, a, b)

# Printing the resulting array
print(result)
