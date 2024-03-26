# Nested Lambda Function

# Lambda function with default argument x=10, returning another lambda function
add = lambda x=10: (lambda y: x + y)

# Calling the outer lambda function without arguments
a = add()

# Printing the result (inner lambda function)
print(a)

# Calling the inner lambda function with argument 20
print(a(20))
