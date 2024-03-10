# Importing required functionality from numpy
from numpy import *

# Creating a numpy array 'a' with given elements
a = array([10, 20, 30, 40, 50])

# Creating a deep copy of array 'a' and assigning it to array 'b'
b = copy(a)

# Modifying the second element of array 'a'
a[1] = 80

# Modifying the third element of array 'b'
b[2] = 300

# Printing arrays 'a' and 'b' after modification
print(a)
print(b)

# Printing the memory location of arrays 'a' and 'b'
print("a", id(a))
print("b", id(b))
