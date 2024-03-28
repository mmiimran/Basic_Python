# Set Methods

# Defining sets
a = {'Fuad', 'Imran', 'Mamun', 'Ehan'}
b = {'Ehsan', 'Mamun', 'kaka', 'Python', 'JavaScript'}

# Displaying sets
print("A:", a)
print("B:", b)
print()

# intersection() Method
# Returns items that exist in both sets
intersection_result = a.intersection(b)
print("Intersection:", intersection_result)
print()

# union() Method
# Returns all items from the original set and all items from the specified set
union_result = a.union(b)
print("Union:", union_result)
print()

# difference() Method
# Returns items that exist only in the first set, and not in both sets
difference_result = a.difference(b)
print("Difference:", difference_result)
print()

# issubset() Method
# Returns True if all items in the set exist in the specified set
issubset_result = a.issubset(b)
print("issubset:", issubset_result)
print()

# issuperset() Method
# Returns True if all items in the specified set exist in the original set
issuperset_result = a.issuperset(b)
print("issuperset:", issuperset_result)
print()
