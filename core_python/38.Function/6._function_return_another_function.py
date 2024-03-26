# Function Returns Another Function

# Example 1: Returning a nested function
def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show  # Returning the nested function

# Assigning the returned function to a variable and calling it
r_sh = disp()
print(r_sh())

# Example 2: Returning a function passed as an argument
def disp(sh):
    print("Disp Function")
    return sh  # Returning the passed function

def show():
    return "Show Function"

# Calling disp with another function as an argument and assigning the returned function to a variable, then calling it
r_sh = disp(show)
print(r_sh())
