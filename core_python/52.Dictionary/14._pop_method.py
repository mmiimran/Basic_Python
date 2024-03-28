# Dictionary - pop() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'fuad'}
print("Original Dict:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Removing a key-value pair using pop() method
removed_value = stu.pop(102)
# Attempting to remove a key that does not exist (uncommenting the line below will raise a KeyError)
# removed_value = stu.pop(106)
print("After Removing Dict:")
print(stu)  # Print dictionary after removal
print(id(stu))  # Print memory address of dictionary after removal
print("Removed Value:", removed_value)  # Print the removed value
print()

# Removing a key with default value using pop() method
default_value = stu.pop(106, 'imranShows')
print("After Removing Dict:")
print(stu)  # Print dictionary after removal
print(id(stu))  # Print memory address of dictionary after removal
print("Default Value:", default_value)  # Print the default value returned
print()
