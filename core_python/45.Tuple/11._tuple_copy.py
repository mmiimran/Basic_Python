# Copying a Tuple
a = (10, 20, 30, 40, 50)
b = a

# Displaying the original tuples and their ids
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

# If the data is the same, the objects have the same id.
# If the data is modified, it creates a new object with a new id.

print()

# Creating a copy of tuple 'a' using slicing
b = a[0:5]

# Displaying the updated tuples and their ids
print("Updated A:", a)
print("Updated B:", b)
print("Id of Updated A:", id(a))
print("Id of Updated B:", id(b))
