# Recursion

# Example 1: Function demonstrating recursion
i = 0

def myfun():
    global i
    i += 1
    print("My Function", i)
    myfun()  # Calling the function recursively

myfun()  # Calling the function initially

# Example 2: Setting and getting recursion limit
import sys

# Getting the default recursion limit
print("Default Recursion Limit:", sys.getrecursionlimit())

# Setting the recursion limit to 3000
sys.setrecursionlimit(3000)

# Printing the updated recursion limit
print("After setting Recursion Limit:", sys.getrecursionlimit())
