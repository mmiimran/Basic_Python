# Import all functions from the numpy library
from numpy import *

# 1D to 2D example
# Create a 1D array 'a' with 6 elements
a = array([1, 2, 3, 4, 5, 6])
# Reshape the 1D array 'a' into a 2D array with 2 rows and 3 columns
b = reshape(a, (2, 3))
# Print the original 1D array
print(a)
# Print the reshaped 2D array
print(b)
print()  # Print an empty line for better readability

# 1D to 3D example
# Create a 1D array 'c' with 12 elements
c = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# Reshape the 1D array 'c' into a 3D array with 2 blocks, 3 rows, and 2 columns
d = reshape(c, (2, 3, 2))
# Print the original 1D array
print(c)
# Print the reshaped 3D array
print(d)
print()  # Print an empty line for better readability

# 2D to 1D example
# Create a 2D array 'e' with 2 rows and 3 columns
e = array([[1, 2, 3], [4, 5, 6]])
# Reshape the 2D array 'e' into a 1D array with 6 elements
f = reshape(e, (6))
# Print the original 2D array
print(e)
# Print the reshaped 1D array
print(f)

