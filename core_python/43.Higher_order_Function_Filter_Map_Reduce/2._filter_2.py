# List Filtering with filter and None

# Given list
a = [True, False, False, True, False, True, True]

# Filtering using filter and None
result = list(filter(None, a))
print("Filtered List:", result)
print("Type of Filtered List:", type(result))
