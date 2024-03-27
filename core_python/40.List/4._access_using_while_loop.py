# Accessing List Elements using a while loop

# Creating a list named 'a' containing different types of elements
a = [10, 20, -50, 21.3, 'Imranshows']

# Accessing List Elements using a while loop
print("Accessing List using while Loop")
n = len(a)  # Determining the length of the list 'a'
i = 0  # Initializing index to 0
while i < n:
    print(i, "=", a[i])  # Printing the index and the corresponding element
    i += 1  # Incrementing index to move to the next element
