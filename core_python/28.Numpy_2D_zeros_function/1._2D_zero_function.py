# 2D Array using zeros Function Numpy
from numpy import *

# Creating a 2D numpy array 'a' filled with zeros
a = zeros((3,2))

# Printing Individual Elements
print("**** Accessing Individual Elements ****")
print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])
print(a[2][0])
print(a[2][1])
print()

# Accessing by For Loop
print("**** Accessing by For Loop ****")
for r in a:
    for c in r:
        print(c)
    print()

# Accessing by For Loop with Index
print("**** Accessing by For Loop with Index ****")    
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print('index',i,j,"=",a[i][j])
    print()

# Accessing by While Loop
print("**** Accessing by While Loop ****")    
n = len(a)
i = 0
while i < n :
    j = 0
    while j < len(a[i]):
        print('index',i,j,"=",a[i][j])
        j += 1
    i += 1
    print()
