# Getting input from users - Tuple

# Initialize an empty list
a = []

# Get the number of elements from the user
n = int(input("Enter Number of Elements: "))

# Iterate to get elements from the user and append them to the list
for i in range(n):
    a.append(int(input("Enter Element:")))

# Check the type before conversion
print(type(a))

# Convert the list to a tuple
a = tuple(a)

# Check the type after conversion
print(type(a))

print("Tuple:")
# Print the elements of the tuple
for element in a:
    print(element)
