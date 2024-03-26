# Global Variable

# Example 1: Function to demonstrate access to global variables
a = 50  # Global Variable

def show():
    x = 10      # Local Variable
    print(x)    # Accessing Local Variable inside Function
    print(a)    # Accessing Global Variable inside Function

# Calling the function
show()

# Accessing Global Variable outside Function
print("Global Variable A:", a)   

# Attempting to access Local Variable outside Function (will result in error)
# print("Global Variable X:", x)

# Example 2: Function to demonstrate global variable shadowing
i = 0  # Global Variable

def myfun():
    a = i + 1  # 'i' is treated as a global variable here
    print("My Function", a)

# Calling the function
myfun()

# Example 3: Function to demonstrate attempt to modify global variable without declaration
i = 0  # Global Variable

def myfun():
    # Attempting to increase global variable 'i' without declaration
    # Here, 'i' is treated as a local variable with the same name
    # Trying to access 'a' will result in error as it's not defined within the function
    i = i + 1  
    print("My Function", a)  # This line will raise an error

# Calling the function
myfun()
