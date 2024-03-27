# List Mapping with map and Lambda

# Given list
a = [10, 20, 30, 40, 50]

# Mapping using map and a custom function
def inc(n):
    return n + 2

result = list(map(inc, a))
print("Mapped List with Custom Function:", result)
print("Type of Mapped List with Custom Function:", type(result))

# Mapping using map and Lambda function
result = list(map(lambda n: n + 2, a))
print("Mapped List with Lambda Function:", result)
print("Type of Mapped List with Lambda Function:", type(result))
