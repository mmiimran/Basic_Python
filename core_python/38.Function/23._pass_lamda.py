# Passing Lambda Function to Another Function

# Function to demonstrate passing a lambda function as an argument to another function
def show(a):
    print(a)         # Printing the lambda function itself
    print(a(8))      # Calling the lambda function with argument 8 and printing the result

# Calling the show function and passing a lambda function as argument
show(lambda x: x)
