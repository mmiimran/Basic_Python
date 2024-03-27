# Importing the reduce function from functools module
from functools import reduce

# Given list
a = [10, 20, 30, 40, 50]

# Using reduce function with Lambda
result = reduce(lambda n, m: m + n, a)
print("Reduced Result with Lambda Function:", result)
print("Type of Reduced Result with Lambda Function:", type(result))
