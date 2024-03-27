# Accessing List Elements using a for loop

# Creating a list named 'a' containing different types of elements
a = [10, 20, -50, 21.3, 'Imranshows']

# Accessing List Elements without index using a for loop
print("Accessing List using for Loop without index")
for element in a:
    print(element)

print()

# Accessing List Elements with index using a for loop
print("Accessing List using for Loop with index")
n = len(a)  # Determining the length of the list 'a'
for i in range(n):
    print(i, "=", a[i])  # Printing the index and the corresponding element
