# Deletion

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'shakil'}
print("Before Deletion:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Deleting a specific key-value pair from the dictionary
del stu[102]
print("After Deletion:")
print(stu)  # Print modified dictionary
print(id(stu))  # Print memory address of modified dictionary
print()

# Deleting the entire dictionary
del stu

# Attempting to access the dictionary after deletion will result in an error
print(stu)  # It will show error stu not defined
