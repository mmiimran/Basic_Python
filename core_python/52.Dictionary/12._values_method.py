# Dictionary - values() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'khairul'}
print("Original Dict:")
print(stu)  # Print original dictionary
print()

# Using values() method to get a view object containing values
all_values = stu.values()
print(all_values)  # Print the view object containing values
print()

# Converting the view object into a list
values_lst = list(all_values)
print(values_lst)  # Print the converted list
print()

# Accessing individual elements in the list
print(values_lst[0])  # Print the first value
print(values_lst[1])  # Print the second value
print(values_lst[2])  # Print the third value
print()

# Iterating through the list and printing each value
for v in values_lst:
    print(v)
