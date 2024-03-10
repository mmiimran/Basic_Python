# Accessing 2D Array using for Loop
from numpy import *

# Creating a 2D numpy array 'a'
a = array([[10, 20, 30, 40], [50, 60, 70, 80]])

# Iterating over each row in the array
for r in a:
    # Iterating over each element in the row
    for c in r:
        print(c)  # Printing each element
    print()  # Printing an empty line after printing all elements in a row
