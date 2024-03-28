# Dictionary - setdefault() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'fuad'}
print("Original Dict:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Setting default value for a key using setdefault() method
# If the key exists, it returns the corresponding value
# If the key doesn't exist, it adds the key with the specified default value
# and returns the default value
# returned_value = stu.setdefault(102)
returned_value = stu.setdefault(109, 'Robin')
print("After Set Default Dict:")
print(stu)  # Print dictionary after setting default value
print(id(stu))  # Print memory address of dictionary after setting default value
print("Returned Value:", returned_value)  # Print the returned value
print()
