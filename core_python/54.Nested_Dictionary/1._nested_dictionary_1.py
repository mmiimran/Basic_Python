# Nested Dictionary
a = {'course': 'Python', 'fees':15000, 1: {'course': 'JavaScript', 'fees': 10000 } }

# Accessing Nested Dictionary
print(a['course'])              # Output: Python
print(a['fees'])                # Output: 15000
print(a[1]['course'])           # Output: JavaScript
print(a[1]['fees'])             # Output: 10000
print()

print("Original: ")
print(a)
print()

# Modifying Nested Dictionary
a['course'] = 'Machine Learning'
a[1]['fees'] = 200000
print("After Modification: ")
print(a)
print()

# Deletion
del a[1]['course']
print("After Deletion: ")
print(a)
print()

# Adding New item
a['duration'] = '6 months'
a[1]['Teacher'] = 'imranShows'
print("After Addition: ")
print(a)
print()

# Adding Dictionary inside Dictionary
a[2] = {'course': 'ReactJS', 'fees': 30000}
print("After Adding a Dict: ")
print(a)
print()
