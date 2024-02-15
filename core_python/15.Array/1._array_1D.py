# Create Array Example 1
import array  # Importing the array module

# Initializing an array of integers with elements
stu_roll = array.array('i', [101, 102, 103, 104, 105])

# Printing individual elements
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 2
import array as ar  # Importing the array module with an alias 'ar'

# Initializing an array of integers with elements using the alias 'ar'
stu_roll = ar.array('i', [101, 102, 103, 104, 105])

# Printing individual elements
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 3
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements using wildcard import
stu_roll = array('i', [101, 102, 103, 104, 105])

# Printing individual elements
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array Example 4
from array import *  # Importing all symbols from the array module

# Initializing an array of floats with elements
stu_roll = array('f', [10, 20, 10.3, 40, 1.5])

# Printing individual elements
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# Create Array and iterate using for Loop
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105])

# Iterating through array elements using for loop
for element in stu_roll:
    print(element)

# Create Array and iterate using for Loop with index
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)

# Iterating through array elements with their indices using for loop
for i in range(n):
    print(i, "=", stu_roll[i])

# Create Array and iterate using while Loop with index
from array import *  # Importing all symbols from the array module

# Initializing an array of integers with elements
stu_roll = array('i', [101, 102, 103, 104, 105])
n = len(stu_roll)
i = 0

# Iterating through array elements with their indices using while loop
while(i < n):
    print(stu_roll[i])
    i += 1
