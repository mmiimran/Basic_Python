# Modifying Tuple

# Original tuple
a = (10, 20, -50, 21.3, 'imranShows')
print(a)
print()

# Not Possible to Modify like below line
# a[1] = 40		# Show TypeError

# It is not possible to modify a tuple but we can concatenate or slice
# to achieve the desired tuple modifications

# Modifying by concatenation
print("Modification by Concatenation")
b = (40, 50)
tup1 = a + b
print(tup1)

print()

# Modifying by slicing
print("Modification by Slicing")
tup2 = a[0:3]
print(tup2)

print()

# Modifying by concatenation and slicing
print("Modification by Concatenation and Slicing")
c = (101, 102)
s1 = a[0:2]
s2 = a[3:]
tup3 = s1 + c + s2
print(tup3)

print()
