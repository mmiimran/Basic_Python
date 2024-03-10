# Getting input from user in 2D Array using for Loop Numpy
from numpy import *

# Getting the number of rows and columns from the user
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))

# Creating a 2D numpy array 'a' filled with zeros
a = zeros((m, n), dtype=int)
u = len(a)  # Length of array 'a'

# Input from user
for i in range(u):
    for j in range(len(a[i])):
        x = int(input("Enter Element: "))
        a[i][j] = x

# Accessing 2D Array with index
print("**** Accessing 2D Array with Index ****")
for i in range(u):
    for j in range(len(a[i])):
        print('index',i,j,"=",a[i][j])

# Accessing 2D Array without index
print("**** Accessing 2D Array without Index ****")
for r in a:
    for c in r:
        print(c)

# Printing the data type of array 'a'
print(type(a))
