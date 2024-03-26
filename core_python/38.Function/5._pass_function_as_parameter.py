# Pass a Function as Parameter

# Example 1: Passing a function as a parameter and invoking it
def disp(sh):
    print(type(sh))  # Print the type of the passed parameter (function)
    print("Disp Function" + sh())  # Concatenate a string with the result of invoking the passed function

def show():
    return " Show Function"

# Calling the function disp and passing another function (show) as a parameter
disp(show)

# Example 2: Passing a function as a parameter and returning the result
def disp(sh):
    return "Disp Function" + sh()  # Concatenate a string with the result of invoking the passed function

def show():
    return " Show Function"

# Calling the function disp and passing another function (show) as a parameter, then storing the result
result = disp(show)
print(result)
