# Dictionary - copy() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'Fuad'}
print("Original Dict:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Creating a copy of the original dictionary
new_stu = stu.copy()
print("Copied Dict:")
print(new_stu)  # Print copied dictionary
print(id(new_stu))  # Print memory address of copied dictionary
