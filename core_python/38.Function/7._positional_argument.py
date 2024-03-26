# Positional Arguments

# Example 1: Function to calculate power with 5 as base and 2 as exponent
def pw(x, y):
    z = x ** y  # Calculate power
    print(z)

# Calling the function with arguments 5 and 2
pw(5, 2)

# Example 2: Function to calculate power with 2 as base and 5 as exponent
def pw(x, y):
    z = x ** y  # Calculate power
    print(z)

# Calling the function with arguments 2 and 5
pw(2, 5)

# Example 3 will show Error
# def pw(x, y):
#     z = x ** y
#     print(z)
# 
# pw(5, 2, 3)
# The above code will show an error because the function pw() expects only two arguments but three are provided.
