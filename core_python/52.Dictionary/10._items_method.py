# Dictionary - items() Method

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'hasan'}
print("Original Dict:")
print(stu)  # Print original dictionary
print()

# Using items() method to get a view object containing key-value pairs
it = stu.items()
print(it)  # Print the view object
print()

# Converting the view object into a list
lst = list(it)
print(lst)  # Print the converted list
print()

# Accessing individual elements in the list
print(lst[0])  # Print the first key-value pair
print(lst[0][0])  # Print the key of the first pair
print(lst[0][1])  # Print the value of the first pair
print()

# Iterating through the list and printing each element
for r in lst:
    for c in r:
        print(c)
