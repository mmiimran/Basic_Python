# extend() Method
# Creating lists 'a' and 'b' containing integers and a string
a = [10, 20, 30, 10, 90, 'Imranshows']
b = [100, 200, 300]

# Printing the list 'a' before extending
print("Before Extend:", a)

# Extending the list 'a' with the elements of the list 'b'
a.extend(b)

# Printing the list 'a' after extending
print("After Extend:", a)

# Printing each element of the modified list 'a'
for element in a:
    print(element)
