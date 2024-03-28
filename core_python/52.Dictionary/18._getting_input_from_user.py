# Getting input from user

# Creating an empty dictionary
a = {}

# Asking the user for the number of elements
n = int(input("Number of Elements: "))

# Iterating 'n' times to get input for keys and values from the user
for i in range(n):
    k = input("Enter Key: ")  # Prompting user to input a key
    v = input("Enter Value: ")  # Prompting user to input a value
    a.update({k: v})  # Updating the dictionary with the key-value pair

# Printing the resulting dictionary
print(a)
