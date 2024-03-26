# Passing and Returning Array

# Importing the 'array' module
from array import *

# Function to demonstrate passing and returning an array
def show(ar):
    print("Passed Array ar:", ar)  # Printing the passed array 'ar'
    print(type(ar))  # Printing the type of the array 'ar'
    for i in ar:
        print(i)  # Printing each element of the array 'ar'
    return ar  # Returning the array 'ar'

# Creating an array of integers ('i') with initial values
a = array('i', [101, 102, 103, 104])

# Calling the function 'show' and passing the array 'a' as an argument
y = show(a)

print("Returning Array Y:", y)  # Printing the returned array 'y'
print(type(y))  # Printing the type of the returned array 'y'
for i in y:
    print(i)  # Printing each element of the returned array 'y'
