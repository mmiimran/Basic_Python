# Passing Array to Function

# Importing the 'array' module
from array import *

# Function to demonstrate passing an array to another function
def show(ar):
    print(ar)  # Printing the array
    print(type(ar))  # Printing the type of the array
    for i in ar:
        print(i)  # Printing each element of the array

# Creating an array of integers ('i') with initial values
a = array('i', [101, 102, 103, 104])

# Calling the function 'show' and passing the array 'a' as an argument
show(a)
