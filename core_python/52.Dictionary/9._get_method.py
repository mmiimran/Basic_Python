# Dictionary - get() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'ehan'}
print("Original Dict:")
print(stu)  # Print original dictionary
print()

# Using get() method to retrieve value for key 101
print(stu.get(101))

# Using get() method to retrieve value for non-existent key 104
print(stu.get(104))

# Using get() method with default value to retrieve value for non-existent key 104
print(stu.get(104, 'imranShows'))
