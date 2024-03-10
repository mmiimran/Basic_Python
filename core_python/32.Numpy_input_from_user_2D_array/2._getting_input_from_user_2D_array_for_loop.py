# Getting input from user in 2D Array using while Loop Numpy
from numpy import *

# Getting the number of rows and columns from the user
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))

# Creating a 2D numpy array 'a' filled with zeros
a = zeros((m, n), dtype=int)
u = len(a)  # Length of array 'a'

# Input from user using while loops
i = 0
while(i < u):
    j = 0
    while j < len(a[i]):
        x = int(input("Enter Element: "))
        a[i][j] = x
        j += 1
    i += 1

# Accessing and printing 2D array elements with indices using while loops
i = 0
while i < u :
    j = 0
    while j < len(a[i]):
        print('index',i,j,"=",a[i][j])
        j += 1
    i += 1

# Printing the data type of array 'a'
print(type(a))
