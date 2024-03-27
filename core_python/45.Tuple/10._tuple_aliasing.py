# Assigning a Tuple to Another Variable
a = (10, 20, 30, 40, 50)
b = a

# Displaying the original tuples and their ids
print("A:", a)
print("B:", b)
print("Id of A:", id(a))
print("Id of B:", id(b))

print()

# Slicing the 'a' tuple
a = a[:3]

# Displaying the updated tuple 'a' and its id
print("Updated A:", a)
print("Id of Updated A:", id(a))
print("Id of B:", id(b))
