def disp(a, b):
    yield a  # Yielding the first value
    yield b  # Yielding the second value

# Calling the disp function and obtaining a generator object
result = disp(10, 20)

# Printing the generator object and its type
print("Generator object:", result)
print("Type of result:", type(result))

# Accessing the elements of the generator using next() function
print("Next element:", next(result))  # Accessing the first yielded value
print("Next element:", next(result))  # Accessing the second yielded value
