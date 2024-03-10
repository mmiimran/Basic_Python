from numpy import *

# Creating a 1D numpy array 'a' and a 2D numpy array 'b'
a = array([101, 102, 103, 104, 105])
b = array([[10, 20, 30, 40], [50, 60, 70, 80]])

# Printing a blank line for better readability
print()

# ndim Attribute
# Printing the number of dimensions using the ndim attribute
print("1D Array ndim:", a.ndim)
print("2D Array ndim:", b.ndim)
print()

# shape Attribute 
# Printing the shape of arrays
# For 1D array, shape represents the number of elements
# For 2D array, shape specifies the number of rows and columns in each row
print("1D Array shape:", a.shape)
print("2D Array shape:", b.shape)
print()

# size Attribute
# Printing the number of elements in arrays using the size attribute
print("1D Array size:", a.size)
print("2D Array size:", b.size)
print()

# itemsize Attribute
# Printing the size of each element in bytes using the itemsize attribute
print("1D Array itemsize:", a.itemsize)
print("2D Array itemsize:", b.itemsize)
print()

# dtype Attribute
# Printing the data type of elements in arrays using the dtype attribute
print("1D Array dtype:", a.dtype)
print("2D Array dtype:", b.dtype)
print()

# nbytes Attribute
# Printing the total bytes consumed by arrays using the nbytes attribute
print("1D Array nbytes:", a.nbytes)
print("2D Array nbytes:", b.nbytes)
print()
