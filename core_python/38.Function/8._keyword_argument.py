# Keyword Arguments

# Example 1: Function to display name and age using keyword arguments
def show(name, age):
    print(f"Name: {name} Age: {age}")

# Calling the function with keyword arguments
show(name="Imran", age=62)

# Example 2: Function to display name and age using keyword arguments (order changed)
def show(name, age):
    print(f"Name: {name} Age: {age}")

# Calling the function with keyword arguments (order changed)
show(age=62, name="Imran")

# Example 3 will show Error
# def show(name, age):
#     print(f"Name: {name} Age: {age}")
# 
# show(name="Imran", age=62, roll=101)
# The above code will show an error because the function show() does not expect a keyword argument 'roll'.
