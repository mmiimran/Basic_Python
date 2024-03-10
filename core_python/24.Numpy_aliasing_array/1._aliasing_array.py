# Importing required functionality from numpy
from numpy import *

# Creating a numpy array 'a' with given elements
a = array([10, 20, 30, 40, 50])

# Assigning array 'a' to array 'b' (b references the same memory location as a)
b = a

# Printing arrays 'a' and 'b'
print(a)
print(b)

# Printing the memory location of arrays 'a' and 'b'
print("a", id(a))
print("b", id(b))
