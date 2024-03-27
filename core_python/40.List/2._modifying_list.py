# Modifying elements of a list and observing memory address

# Creating a list named 'a' containing different types of elements
a = [10, 20, -50, 21.3, 'Imranshows']

# Printing the list 'a' along with its memory address
print(a, id(a))

# Accessing and printing the second element of the list
print(a[1])

# Modifying the second element of the list
a[1] = 40

# Accessing and printing the second element of the list after modification
print(a[1])

# Printing the modified list 'a' along with its memory address
print(a, id(a))
