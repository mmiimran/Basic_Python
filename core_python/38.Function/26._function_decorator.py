# Function Decorator

# Example 1: Using function decorator without '@' symbol
def decor(fun):
    def inner():
        print("Inner Function: Before enhancing Function")
        fun()
        print("Inner Function: After enhancing Function")
    return inner

def num():
    print("We will use this function")
    print("and will enhance this in decorator")

# Decorating the function 'num' manually
result_fun = decor(num)
result_fun()

# Example 2: Using function decorator with '@' symbol
def decor(fun):
    def inner():
        print("Inner Function: Before enhancing Function")
        fun()
        print("Inner Function: After enhancing Function")
    return inner

@decor
def num():
    print("We will use this function")
    print("and will enhance this in decorator")

# Directly calling the decorated function
num()
