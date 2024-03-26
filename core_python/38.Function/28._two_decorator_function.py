# Two Decorator Functions on the same function

# Example 1: Using two decorator functions without '@' symbol
def decor(fun):
    def inner():
        # Calling the original function 'fun'
        a = fun()
        # Adding 5 to the result of 'fun'
        add = a + 5
        return add
    return inner

def decor1(fun):
    def inner():
        # Calling the original function 'fun'
        b = fun()
        # Multiplying the result of 'fun' by 5
        multi = b * 5
        return multi
    return inner

# Function to be decorated
def num():
    return 10

# Decorating the function 'num' with two decorator functions manually
result_fun = decor(decor1(num))
# Calling the decorated function and printing the result
print(result_fun())

# Example 2: Using two decorator functions with '@' symbol
def decor(fun):
    def inner():
        # Calling the original function 'fun'
        a = fun()
        # Adding 5 to the result of 'fun'
        add = a + 5
        return add
    return inner

def decor1(fun):
    def inner():
        # Calling the original function 'fun'
        b = fun()
        # Multiplying the result of 'fun' by 5
        multi = b * 5
        return multi
    return inner

@decor
@decor1
def num():
    return 10

# Directly calling the decorated function and printing the result
print(num())
