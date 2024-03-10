# 1D Array using arange Function Numpy
from numpy import *

# Create a 1D array using arange function
a = arange(5)

# Print individual elements of the array
print("**** Accessing Individual Elements ****")
print(a[0])  # Accessing the first element
print(a[1])  # Accessing the second element
print(a[2])  # Accessing the third element
print(a[3])  # Accessing the fourth element
print(a[4])  # Accessing the fifth element
print()

# Accessing elements using a for loop
print("**** Accessing by For Loop ****")
for el in a:
    print(el)
print()

# Accessing elements using a for loop with index
print("**** Accessing by For Loop with Index ****")    
n = len(a)
for i in range(n):
    print('index',i,'=',a[i])
print()

# Accessing elements using a while loop with index
print("**** Accessing by While Loop ****")    
n = len(a)
i = 0
while i < n:
    print('index',i,'=',a[i])
    i += 1
