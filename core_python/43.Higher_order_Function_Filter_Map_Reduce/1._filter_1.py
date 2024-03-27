# List Filtering with and without Lambda Function

# Given list
a = [10, 50, 60, 80, 90, 5, 45, 65]

# Without Lambda Function
def high_marks(n):
    """
    Function to check if a number is greater than or equal to 60.

    Args:
    n (int): The number to be checked.

    Returns:
    bool: True if the number is greater than or equal to 60, False otherwise.

    """
    if n >= 60:
        return True

# Filtering using the high_marks function
result = list(filter(high_marks, a))
print("Filtered List without Lambda:", result)
print("Type of Filtered List:", type(result))
print()

# With Lambda Function
result = list(filter(lambda n: (n >= 60), a))
print("Filtered List with Lambda:", result)
print("Type of Filtered List:", type(result))
