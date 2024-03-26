# Variable Length Arguments

# Example 1: Function to add two numbers
def add(x, y):
    z = x + y
    print("Addition:", z)

# Calling the function with two arguments
add(5, 2)

# Example 2: Function to add variable length of numbers
def add(*num):
    z = num[0] + num[1] + num[2]  # Adding first three numbers from the variable-length argument
    print("Addition:", z)

# Calling the function with three arguments
add(5, 2, 4)

# Example 3: Function with one fixed argument and variable length of additional numbers
def add(x, *num):
    z = x + num[0] + num[1]  # Adding the first two additional numbers to the fixed argument
    print("Addition:", z)

# Calling the function with one fixed argument and two additional arguments
add(5, 2, 4)
