# Deleting Tuple

# Original tuple
a = (10, 20, -50, 21.3, 'imranShows')
print(a)
print()

# Not Possible to delete one element like below line
# del a[1] 		# Show TypeError

# We can delete the entire tuple
# del a
# print(a)		# after deleting entire tuple a becomes undefined

# It is not possible to delete one element, but we can concatenate or slice
# to achieve the desired tuple modifications

print()

# Deleting by slicing
print("Deletion by Slicing")
tup1 = a[0:3]
print(tup1)

print()

# Deleting by concatenation and slicing
print("Deletion by Slicing and Concatenation")
s1 = a[0:2]
s2 = a[4:]
tup2 = s1 + s2
print(tup2)

print()
