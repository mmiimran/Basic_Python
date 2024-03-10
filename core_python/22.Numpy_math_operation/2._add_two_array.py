# Importing required functionality from numpy
from numpy import *

# Creating numpy arrays 'a' and 'b' with given elements
a = array([101, 102, 103, 104, 105])
b = array([1, 2, 3, 4, 5])

# Performing element-wise addition of arrays 'a' and 'b'
c = a + b

# Iterating through each element in the resulting array 'c' and printing them
for el in c:
    print(el)
