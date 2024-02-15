# Getting input from Users using while Loop
from array import *  # Importing all symbols from the array module

# Initializing an empty array of integers
stu_roll = array('i', [])

# Getting the number of elements from the user
n = int(input("Enter Number of Elements: "))

# Initializing a counter variable for input loop
i = 0

# Initializing a counter variable for printing loop
j = 0

# Looping through until the counter reaches the specified number of elements
while i < n:
    # Getting each element from the user and appending it to the array
    stu_roll.append(int(input("Enter Element: ")))
    i += 1  # Incrementing the input counter

# Looping through the array elements and printing them
while j < len(stu_roll):
    print(stu_roll[j])  # Printing the current array element
    j += 1  # Incrementing the printing counter
