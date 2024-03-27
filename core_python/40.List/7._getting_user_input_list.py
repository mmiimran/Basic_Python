a = []  # Create an empty list

# Prompt the user to input the number of elements
n = int(input("Enter Number of Elements: "))

# Iterate through a loop to append elements to the list
for i in range(n):
    a.append(int(input("Enter Element: ")))

# Print the contents of the list
print("List:")
for element in a:
    print(element)
