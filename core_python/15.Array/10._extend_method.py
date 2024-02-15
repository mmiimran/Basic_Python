# extend ()
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105])

# Initializing another array of integers
arr = array('i', [107, 108, 109])

# Getting the length of the initial array
n = len(stu_roll)

# Initializing a counter variable for printing initial array elements
i = 0

# Looping through the array elements and printing them
while i < n:
    print(stu_roll[i])  # Printing the current array element
    i += 1  # Incrementing the counter variable

# Outputting a message indicating the array will be modified
print("Array After Extend")

# Extending the initial array with the elements of the second array
stu_roll.extend(arr)

# Updating the length of the modified array
n = len(stu_roll)

# Resetting the counter variable for printing modified array elements
i = 0

# Looping through the updated array elements and printing them
while i < n:
    print(stu_roll[i])  # Printing the current array element
    i += 1  # Incrementing the counter variable
