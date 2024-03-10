# Accessing 2D Array using While Loop
from numpy import *

# Creating a 2D numpy array 'a'
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

# Getting the number of rows in the array
n = len(a)

# Initializing the outer loop counter
i = 0

# Iterating over each row in the array using a while loop
while i < n:
    # Initializing the inner loop counter
    j = 0
    # Iterating over each element in the current row using a while loop
    while j < len(a[i]):
        print('index',i,j,"=",a[i][j])  # Printing the indices and corresponding element
        j += 1  # Incrementing the inner loop counter
    i += 1  # Incrementing the outer loop counter
    print()  # Printing an empty line after printing all elements in a row
