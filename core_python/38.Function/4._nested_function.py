# Nested Function

# Example 1: Nested function without a return statement
def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()

# Calling the outer function
disp()

# Example 2: Nested function with a return statement
def disp():
    def show():
        return "Show Function "
    # Calling the inner function and concatenating its return value with a string
    result = show() + "Disp Function"
    return result

# Calling the outer function and printing its return value
print(disp())

# Example 3: Nested function with a return statement and parameter
def disp(st):
    def show():
        return "Show Function "
    # Calling the inner function, concatenating its return value with the parameter and another string
    result = show() + st + " Disp Function"
    return result

# Calling the outer function with an argument and printing its return value
print(disp("Imranshowes"))
