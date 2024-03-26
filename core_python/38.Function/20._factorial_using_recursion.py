# Factorial using Recursion

# Function to calculate factorial of a number recursively
def fact(n):
    if n == 0:  # Base case: factorial of 0 is 1
        return 1
    return n * fact(n - 1)  # Recursive call to calculate factorial

# Calling the function and printing the result
print(fact(3))  # Output: 6 (3 * 2 * 1)
