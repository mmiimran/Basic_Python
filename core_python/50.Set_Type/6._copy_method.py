# Sets - copy() Method

# Defining a set
a = {10, 20, 'ImranShows'}

# Displaying set before copying
print("Before Copy", a)
print(id(a))
print()

# Copying the set
new_a = a.copy()

# Displaying the copied set
print("After Copy", new_a)
print(id(new_a))
