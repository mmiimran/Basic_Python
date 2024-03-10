# Importing required functionality from numpy
from numpy import *

# Getting the number of elements from the user
n = int(input("Enter Number of Elements: "))

# Creating a numpy array 'a' filled with zeros of length 'n' and integer data type
a = zeros(n, dtype=int)

# Looping through the array to get input from the user for each element
for i in range(len(a)):
    x = int(input("Enter Element: "))  # Getting input for each element
    a[i] = x  # Assigning the input value to the corresponding element in the array

# Printing the elements of the array
for i in range(len(a)):
    print(a[i])  # Printing each element of the array
