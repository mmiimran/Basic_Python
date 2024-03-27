def show(a, b):
    while a <= b:
        yield a  # Yielding the current value of 'a'
        a += 1   # Incrementing 'a' for the next iteration

# Creating a generator object by calling the 'show' function
result = show(1, 5)

# Printing the generator object and its type
print("Generator object:", result)
print("Type of result:", type(result))

# Accessing the elements of the generator using next() function
print("Next element:", next(result))  # Accessing the first yielded value
print("Next element:", next(result))  # Accessing the second yielded value
print("Next element:", next(result))  # Accessing the third yielded value

# Iterating over the remaining values using a for loop
for i in result:
    print(i)  # Printing the remaining yielded values
