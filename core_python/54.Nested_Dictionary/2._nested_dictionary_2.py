# Nested Dictionary
a = {1: {'course': 'Python', 'fees':15000},
     2: {'course': 'JavaScript', 'fees': 10000 } }

# Accessing Nested Dictionary
print(a[1]['course'])   # Output: Python
print(a[2]['fees'])     # Output: 10000
print()

print("Original: ")
print(a)
print()

# Modifying Nested Dictionary
a[1]['course'] = 'Machine Learning'
a[2]['fees'] = 200000
print("After Modification: ")
print(a)
print()

# Deletion
del a[1]['course']
print("After Deletion: ")
print(a)
print()

# Adding New item
a[1]['duration'] = '6 months'
a[2]['Teacher'] = 'imranShows'
print("After Addition: ")
print(a)
print()

# Adding Dictionary inside Dictionary
a[3] = {'course': 'ReactJS', 'fees': 30000}
print("After Adding a Dict: ")
print(a)
print()
