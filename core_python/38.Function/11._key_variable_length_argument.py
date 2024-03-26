# Keyword Variable Length Arguments

# Example 1: Function to add numbers using keyword variable length arguments
def add(**num):
    z = num['a'] + num['b'] + num['c']  # Adding values associated with keys 'a', 'b', and 'c'
    print("Addition:", z)

# Calling the function with keyword arguments
add(a=5, b=2, c=4)

# Example 2: Function with one fixed argument and keyword variable length arguments
def add(x, **num):
    z = x + num['a'] + num['b']  # Adding values associated with keys 'a' and 'b' to the fixed argument x
    print("Addition:", z)

# Calling the function with one fixed argument and keyword arguments
add(3, a=5, b=2)
