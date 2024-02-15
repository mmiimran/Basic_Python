# Importing all symbols from the array module
from array import *

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107])

# Outputting a message indicating the original array
print("Original Array")

# Getting the length of the array
n = len(stu_roll)

# Looping through the array elements and printing their indices and values
for i in range(n):
    print(i, "=", stu_roll[i])

# Outputting a message for slicing from 1st to 4th position
print("From 1st Position to 4th Position")

# Slicing the array from index 1 to index 4
a = stu_roll[1:5]

# Printing the sliced elements
for i in a:
    print(i)

# Outputting a message for slicing from 0th to last position
print("From 0th Position to last Position")

# Slicing the array from index 0 to the last index
b = stu_roll[0:]

# Printing the sliced elements
for i in b:
    print(i)

# Outputting a message for slicing from 0th to 4th position
print("From 0th Position to 4th Position")

# Slicing the array from index 0 to index 5 (exclusive)
c = stu_roll[:5]

# Printing the sliced elements
for i in c:
    print(i)

# Outputting a message for slicing the last 4 elements
print("Last 4 Elements")

# Slicing the array to get the last 4 elements
d = stu_roll[-4:]

# Printing the sliced elements
for i in d:
    print(i)

# Outputting a message for slicing from 0th to 6th position with a stride of 2
print("From 0th Position to 6th Position stride 2")

# Slicing the array from index 0 to index 7 (exclusive) with a stride of 2
e = stu_roll[0:7:2]

# Printing the sliced elements
for i in e:
    print(i)

# Outputting a message for slicing the last 5 elements with a specific range
print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")

# Slicing the array to get elements from the 5th to the 3rd last element
f = stu_roll[-5:-3]

# Printing the sliced elements
for i in f:
    print(i)
