# Local Variable

# Example 1: Function to demonstrate local variable
def show():
    x = 10       # Local Variable
    print(x)     # Accessing Local Variable inside Function

# Calling the function
show()

# Attempting to access Local Variable outside Function (will result in error)
# print(x)     # It will show error

# Example 2: Function with a parameter to demonstrate local variable
def add(y):
    x = 10       # Local Variable
    print(x)     # Accessing Local Variable inside Function
    print(x + y) # Accessing Local Variable inside Function

# Calling the function with an argument
add(20)

# Attempting to access Local Variable outside Function (will result in error)
# print(x)     # It will show error
