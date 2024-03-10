# Accessing 2D Array using for Loop with Index
from numpy import *

# Creating a 2D numpy array 'a'
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

# Getting the number of rows in the array
n = len(a)

# Iterating over each row in the array using row indices
for i in range(n):
    # Iterating over each element in the current row using column indices
    for j in range(len(a[i])):
        print('index',i,j,"=",a[i][j])  # Printing the indices and corresponding element
    print()  # Printing an empty line after printing all elements in a row
