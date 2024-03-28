# Nested Tuple - Example 1
a = (10, 20, 30, (50, 60))
print(a)
print(a[0])       # Accessing the first element of the tuple
print(a[1])       # Accessing the second element of the tuple
print(a[2])       # Accessing the third element of the tuple
print(a[3])       # Accessing the fourth element of the tuple (which is another tuple)
print(a[3][0])    # Accessing the first element of the nested tuple
print(a[3][1])    # Accessing the second element of the nested tuple
print()

# Nested Tuple - Example 2
b = (50, 60)
a = (10, 20, 30, b)
print("A:", a)
print("B:", b)
print(a[0])       # Accessing the first element of tuple a
print(a[1])       # Accessing the second element of tuple a
print(a[2])       # Accessing the third element of tuple a
print(a[3])       # Accessing the fourth element of tuple a (which is another tuple)
print(a[3][0])    # Accessing the first element of the nested tuple
print(a[3][1])    # Accessing the second element of the nested tuple
