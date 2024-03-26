# globals() Function

# Example: Function to demonstrate accessing and modifying global variable using globals() function
a = 50  # Global Variable

def show():
    a = 10  # Local Variable
    print("Local Variable A:", a)  # It will show local variable value
    x = globals()['a']  # Accessing global variable 'a' using globals() function
    print("X:", x)  # It will show global variable value
    x = 40  # Modifying 'x', which is a local variable
    print("X:", x)  # It will show modified value of 'x'

# Calling the function
show()

# Accessing Global Variable outside Function (will show global variable value)
print("Global Variable A:", a)

# Attempting to access local variable 'x' outside the function (will result in error)
# print("X:", x)
