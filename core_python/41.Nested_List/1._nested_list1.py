# Nested List Examples

# Example 1: Accessing elements in a nested list directly
a = [10, 20, 30, [50, 60]]
print(a)         # Complete list
print(a[0])      # First element of the outer list
print(a[1])      # Second element of the outer list
print(a[2])      # Third element of the outer list
print(a[3])      # Fourth element of the outer list (which is itself a list)
print(a[3][0])   # First element of the inner list
print(a[3][1])   # Second element of the inner list

# Example 2: Using a separate list as an element in a nested list
b = [50, 60]     # Separate list
a = [10, 20, 30, b]
print("A:", a)   # Complete list 'a'
print("B:", b)   # Separate list 'b'
print(a[0])      # First element of the outer list
print(a[1])      # Second element of the outer list
print(a[2])      # Third element of the outer list
print(a[3])      # Fourth element of the outer list (which is the separate list 'b')
print(a[3][0])   # First element of the inner list 'b'
print(a[3][1])   # Second element of the inner list 'b'
