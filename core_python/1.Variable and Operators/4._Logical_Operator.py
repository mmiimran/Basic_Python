# Assigning values to variables
a = 7
b = 2
c = 3
d = 300

# Logical and operator
print("******* Logical and *******")
# Checking if a is greater than b and a is greater than c
print(a > b and a > c)
# Checking if a is greater than b and a is less than c
print(a > b and a < c)
# Checking if a is less than b and a is greater than c
print(a < b and a > c)
# Checking if a is less than b and a is less than c
print(a < b and a < c)
# Checking if a is greater than b and c (no comparison with a)
print(a > b and c)
# Checking if a is greater than b and both c and d
print(a > b and c and d)
# Checking if a is less than b and c (no comparison with d)
print(a < b and c)
# Checking if a is less than b and both c and d
print(a < b and c and d)

# Logical or operator
print("####### Logical or #######")
# Checking if a is greater than b or a is greater than c
print(a > b or a > c)
# Checking if a is greater than b or a is less than c
print(a > b or a < c)
# Checking if a is less than b or a is greater than c
print(a < b or a > c)
# Checking if a is less than b or a is less than c
print(a < b or a < c)
# Checking if a is greater than b or c (no comparison with a)
print(a > b or c)
# Checking if a is greater than b or both c and d
print(a > b or c or d)
# Checking if a is less than b or c (no comparison with d)
print(a < b or c)
# Checking if a is less than b or both c and d
print(a < b or c or d)

# Logical not operator
print("******* Logical not *******")
# Negating the result of a < b
print(not(a < b))
# Negating the result of a > b
print(not(a > b))
