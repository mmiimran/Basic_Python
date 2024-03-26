# Anonymous Function or Lambda Function

# Example 1: Lambda function with a single argument
show = lambda x: print(x)
show(5)

# Example 2: Lambda function with two arguments
add = lambda x, y: x + y
print(add(5, 2))

# Example 3: Lambda function returning multiple values
add_sub = lambda x, y: (x + y, x - y)
a, s = add_sub(5, 2)
print(a)
print(s)

# Example 4: Lambda function with default argument
add = lambda x, y=3: x + y
print(add(5))
