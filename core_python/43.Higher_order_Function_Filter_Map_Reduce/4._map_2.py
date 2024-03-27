# List Mapping with map and Lambda

# Given lists
a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

# Mapping using map and Lambda function
result = list(map(lambda n, m: m + n, a, b))
print("Mapped List with Lambda Function:", result)
print("Type of Mapped List with Lambda Function:", type(result))
