# Deleting Elements from a List

# Creating a list named 'a' containing different types of elements
a = [10, 20, -50, 21.3, 'Imranshows']

# Printing the list 'a' before deletion
print("Before Deletion: ")
print(a)
print()

# Deleting a single element from the list
print("After Deletion:")
del a[2]  # Deleting the element at index 2
print(a)
print()

# Deleting the entire list
del a
print(a)  # Attempting to print the list 'a' after deletion will raise an error as 'a' has been deleted
