# Importing required functionality from numpy
from numpy import *

# Creating a numpy array 'a' with given elements
a = array([100, 200, 13, 0, 400, 500, 0])

# Finding the indices of non-zero elements in array 'a'
result = nonzero(a)

# Printing the indices of non-zero elements
print(result)
