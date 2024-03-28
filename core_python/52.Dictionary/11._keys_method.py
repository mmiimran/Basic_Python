# Dictionary - keys() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'ehsan'}
print("Original Dict:")
print(stu)  # Print original dictionary
print()

# Using keys() method to get a view object containing keys
all_keys = stu.keys()
print(all_keys)  # Print the view object containing keys
print()

# Converting the view object into a list
keys_lst = list(all_keys)
print(keys_lst)  # Print the converted list
print()

# Accessing individual elements in the list
print(keys_lst[0])  # Print the first key
print(keys_lst[1])  # Print the second key
print(keys_lst[2])  # Print the third key
print()

# Iterating through the list and printing each key
for k in keys_lst:
    print(k)
