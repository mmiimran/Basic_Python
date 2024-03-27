# Example 1: Using yield to return values individually
def disp(a, b):
    yield a
    yield b

# Calling the disp function and unpacking the yielded values
x, y = disp(10, 20)
print("Values returned individually:")
print("x:", x)
print("y:", y)
print()

# Example 2: Using yield to return a generator object
def disp(a, b):
    yield a
    yield b

# Calling the disp function
result = disp(10, 20)
print("Generator object:")
print(result)
print("Type of result:", type(result))

# Converting the generator object to a list
lst = list(result)
print("Converted to list:")
print(lst)
print("Type of lst:", type(lst))
