# Passing and Returning Numpy Array

# Importing the 'numpy' module
from numpy import *

# Function to demonstrate passing and returning a numpy array
def show(ar):
    print("Passed Array ar:", ar)  # Printing the passed array 'ar'
    print(type(ar))  # Printing the type of the array 'ar'
    for i in ar:
        print(i)  # Printing each element of the array 'ar'
    return ar  # Returning the array 'ar'

# Creating a numpy array with the specified values
a = array([101, 102, 103, 104])

# Calling the function 'show' and passing the numpy array 'a' as an argument
y = show(a)

print("Returning Array Y:", y)  # Printing the returned array 'y'
print(type(y))  # Printing the type of the returned array 'y'
for i in y:
    print(i)  # Printing each element of the returned array 'y'
