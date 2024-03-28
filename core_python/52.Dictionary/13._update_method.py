# Dictionary - update() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'fuad'}
print("Original Dict:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Updating dictionary with a single key-value pair
stu.update({104: 'Python'})
print("Updated Dict:")
print(stu)  # Print updated dictionary
print(id(stu))  # Print memory address of updated dictionary
print()

# Updating dictionary with multiple key-value pairs from another dictionary
vals = {'name': 'imran', 'Address': 'Ratul', 105: 'imranShows'}
stu.update(vals)
print("Updated Dict:")
print(stu)  # Print updated dictionary
print(id(stu))  # Print memory address of updated dictionary
print()
