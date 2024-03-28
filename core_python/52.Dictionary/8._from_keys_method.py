# Dictionary - fromkeys() Method

# Define keys and value for dictionary creation
key = (101, 102, 103)
value = 'ImranShows'

# Creating a dictionary using fromkeys() method with specified keys and value
d = dict.fromkeys(key, value)
print("New Dict:")
print(d)  # Print newly created dictionary
print(id(d))  # Print memory address of the new dictionary
print()

# Creating a dictionary using fromkeys() method with specified keys but no value
n = dict.fromkeys(key)
print("New Dict:")
print(n)  # Print newly created dictionary
print(id(n))  # Print memory address of the new dictionary
