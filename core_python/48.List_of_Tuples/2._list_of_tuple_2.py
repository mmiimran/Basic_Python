# List of Tuples
a = [(10, 20), (30, 40)]

# Displaying the original list and its memory address
print("Original List A:", a)
print(id(a))
print()

# Appending a new tuple to the list and displaying the updated list and its memory address
a.append((50, 60))
print("After Appending a tuple A:", a)
print(id(a))

# Accessing elements of the list of tuples using for loop
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()
