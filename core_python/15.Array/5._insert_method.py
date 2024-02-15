# Insert
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105])

# Getting the length of the array
n = len(stu_roll)

# Initializing a counter variable for printing initial array elements
i = 0

# Looping through the array elements and printing them
while i < n:
    print(stu_roll[i])  # Printing the current array element
    i += 1  # Incrementing the counter variable

# Outputting a message indicating the array will be modified
print("Array After Insert")

# Inserting elements at specific indices
stu_roll.insert(1, 106)  # Inserting 106 at index 1
stu_roll.insert(3, 107)  # Inserting 107 at index 3

# Updating the length of the array
n = len(stu_roll)

# Resetting the counter variable for printing modified array elements
i = 0

# Looping through the updated array elements and printing them
while i < n:
    print(stu_roll[i])  # Printing the current array element
    i += 1  # Incrementing the counter variable
