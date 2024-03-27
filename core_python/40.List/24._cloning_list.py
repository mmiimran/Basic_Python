# Creating list 'a'
a = [10, 20, 30, 40, 50]

# Cloning list 'a' into list 'b' using list slicing
b = a[:]

# Printing original lists 'a' and 'b'
print("A:", a)
print("B:", b)
print()

# Modifying list 'a'
print("Modifying A")
a[1] = 55
print("A:", a)
print("B:", b)
print()

# Modifying list 'b'
print("Modifying B")
b[2] = 66
print("A:", a)
print("B:", b)
