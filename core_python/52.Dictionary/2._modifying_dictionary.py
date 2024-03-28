# Modifying Dictionary

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'fuad'}
print("Before Modification:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Modifying value of key 102
stu[102] = 'Python'
print("After Modification:")
print(stu)  # Print modified dictionary
print(id(stu))  # Print memory address of modified dictionary
print()
