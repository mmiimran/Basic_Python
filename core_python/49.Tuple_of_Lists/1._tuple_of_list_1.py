# Tuple of Lists
a = (10, 20, [30, 40])

# Displaying the original tuple and its memory address
print("Original Tuple A:", a)
print(id(a))
print()

# Modifying the tuple
a[2][0] = 90
print("After Modifying Tuple:", a)
print(id(a))

# Accessing elements of the tuple of lists using for loop
n = len(a)
for i in range(n):
    if type(a[i]) is list:
        if len(a[i]) > 1:
            m = len(a[i])
            for j in range(m):
                print(i, j, a[i][j])
    else:
        print(i, a[i])
