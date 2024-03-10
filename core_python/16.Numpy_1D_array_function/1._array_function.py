# Importing the numpy module
import numpy

# Creating a 1D array using the array function from numpy (Example 1)
stu_roll = numpy.array([101, 102, 103, 104, 105])

# Printing the array
print(stu_roll)

# Printing the data type of the array elements
print(stu_roll.dtype)

# Accessing and printing specific elements of the array
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Creating a 1D array with float numbers using the array function from numpy (Example 2)
stu_roll = numpy.array([101, 102, 103, 104, 105], dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Creating a 1D array with implicit float conversion using the array function from numpy (Example 3)
stu_roll = numpy.array([101, 102, 103, 104, 10.5])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Creating a 1D array with characters using the array function from numpy (Example 4)
stu_roll = numpy.array(['a', 'b', 'c', 'd', 'e'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Creating a 1D array with strings using the array function from numpy (Example 5)
stu_roll = numpy.array(['Imran', 'Mejbah', 'Raju', 'Mina', 'Shakil'])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Creating a 1D array using array function from numpy (Example 6)
from numpy import *
stu_roll = array([101, 102, 103, 104, 105])
print(stu_roll)
print(stu_roll.dtype)
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
