# Function Decorator

# Example 1: Using function decorator without '@' symbol
def decor(fun):
    def inner():
        # Calling the original function 'fun'
        a = fun()
        # Adding 5 to the result of 'fun'
        add = a + 5
        return add
    return inner

# Function to be decorated
def num():
    return 10

# Decorating the function 'num' manually
result_fun = decor(num)
# Calling the decorated function and printing the result
print(result_fun())

# Example 2: Using function decorator with '@' symbol
def decor(fun):
    def inner():
        # Calling the original function 'fun'
        a = fun()
        # Adding 5 to the result of 'fun'
        add = a + 5
        return add
    return inner

@decor
def num():
    return 10

# Directly calling the decorated function and printing the result
print(num())
