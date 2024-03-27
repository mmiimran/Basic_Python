# pop(position_number) method
a = [10, 20, 30, 10, 90, 'Imranshow']

print("Before POP:", a)

# Removing the element at index 2 from the list and storing it in variable n
n = a.pop(2)

print("After POP:", a)

# Printing each element of the modified list
for element in a:
    print(element)

# Printing the removed element
print("Removed Element:", n)
