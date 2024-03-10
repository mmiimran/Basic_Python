# Importing required functionality from numpy
from numpy import *

# Creating numpy arrays 'a' and 'b' with given elements
a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])

# Comparing arrays 'a' and 'b' element-wise for equality
result = a == b

# Checking if any element-wise comparison result is True
print(any(result))

# Checking if all element-wise comparison results are True
print(all(result))
