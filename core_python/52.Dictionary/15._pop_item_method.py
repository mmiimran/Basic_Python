# Dictionary - popitem() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'fuad'}
print("Original Dict:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Removing the last key-value pair using popitem() method
removed_item = stu.popitem()
print("After Removing Dict:")
print(stu)  # Print dictionary after removal
print(id(stu))  # Print memory address of dictionary after removal
print("Removed Value:", removed_item)  # Print the removed key-value pair
print()
