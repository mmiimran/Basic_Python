# Importing required functionality from numpy
from numpy import *

# Getting the number of elements from the user
n = int(input("Enter Number of Elements: "))

# Creating a numpy array 'a' filled with zeros of length 'n' and integer data type
a = zeros(n, dtype=int)

# Initializing variables for the first while loop
u = len(a)
i = 0

# Iterating through the array to get input from the user for each element using a while loop
while i < u:
    x = int(input("Enter Element: "))  # Getting input for each element
    a[i] = x  # Assigning the input value to the corresponding element in the array
    i += 1

# Initializing variables for the second while loop
j = 0

# Printing the elements of the array using a while loop
while j < len(a):
    print(a[j])  # Printing each element of the array
    j += 1

# Printing the type of the array
print(type(a))
