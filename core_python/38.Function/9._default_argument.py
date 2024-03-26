# Default Arguments

# Example 1: Function to display name and age with specified arguments
def show(name, age):
    print(f"Name: {name} Age: {age}")

# Calling the function with specified arguments
show(name="ImranShows", age=62)

# Example 2: Function to display name and age with default age
def show(name, age=27):
    print(f"Name: {name} Age: {age}")

# Calling the function with default age
show(name="ImranShows")

# Example 3: Function to display name and age with default age overridden
def show(name, age=27):
    print(f"Name: {name} Age: {age}")

# Calling the function with specified age overriding the default
show(name="ImranShows", age=62)

# Example 4 will show Error
# def show(name, age=27):
#     print(f"Name: {name} Age: {age}")
# 
# show(name="ImranShows", age=62, roll=101)
# The above code will show an error because the function show() does not expect a keyword argument 'roll'.
