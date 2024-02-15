# Getting input from Users using for Loop
from array import *  # Importing all symbols from the array module

# Initializing an empty array of integers
stu_roll = array('i', [])

# Getting the number of elements from the user
n = int(input("Enter Number of Elements: "))

# Looping through the range specified by the user input
for i in range(n):
    # Getting each element from the user and appending it to the array
    stu_roll.append(int(input("Enter Element: ")))

# Looping through the array elements and printing them
for i in range(len(stu_roll)):
    print(stu_roll[i])
