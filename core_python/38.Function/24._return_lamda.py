# Return Lambda Function

# Function to return a lambda function
def add():
    y = 20
    return (lambda x: x + y)

# Calling the function and assigning the returned lambda function to variable 'a'
a = add()

# Calling the lambda function with argument 10 and printing the result
print(a(10))
