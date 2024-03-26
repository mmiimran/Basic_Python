# Return Statement Single Value

# Defining a Function to calculate the sum of two numbers
def add():
    x = 10
    y = 20
    c = x + y
    return c
    
# Calling the function and storing the result in a variable
sum = add()
print(sum)

# Defining a Function (alternative implementation) with implicit return
def add():
    x = 10
    y = 20
    return x + y
    
# Calling the function and storing the result in a variable
sum = add()
print(sum)

# Defining a Function with Parameter to add a number to 10
def add(y):
    x = 10
    return x + y
    
# Calling the function with an argument and storing the result in a variable
sum = add(20)
print(sum)

# Return Statement Multiple Values

# Defining a Function to calculate the sum and difference of two numbers
def add(y):
    x = 10
    c = x + y
    d = y - x
    return c, d, 50  # Returning multiple values
    
# Calling the function with an argument and unpacking the returned values
sum, sub, a = add(20)
print(sum)
print(sub)
print(a)
