# Global Keyword

# Example 1: Function to demonstrate local variable masking global variable
a = 50  # Global Variable

def show():
    a = 10  # Local Variable
    print("A:", a)  # It will show local variable value

# Calling the function
show()

# Accessing Global Variable outside Function (will show global variable value)
print("A:", a)

# Example 2: Function to demonstrate global keyword for modifying global variable
a = 50  # Global Variable

def show():
    global a  # Using global keyword to access and modify global variable 'a'
    print("A:", a)  # It will show global variable value
    a = 20  # Modifying Global Variable value
    print("A:", a)  # It will show modified global variable value

# Calling the function
show()

# Accessing Global Variable outside Function (will show modified global variable value)
print("A:", a)
