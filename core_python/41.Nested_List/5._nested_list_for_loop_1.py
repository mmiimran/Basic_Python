# Nested List - for loop

# Given nested list
a = [10, 20, 30, [50, 60]]

# Get the length of the list
n = len(a)

# Iterate through the elements of the list
for i in range(n):
    # Check if the element is a list
    if type(a[i]) is list: 
        # Check if the sublist has more than one element
        if len(a[i]) > 1:
            # Get the length of the sublist
            m = len(a[i])
            # Iterate through the elements of the sublist
            for j in range(m):
                print(i, j, a[i][j])  # Print the indices and the elements of the sublist
    else:
        print(i, a[i])  # Print the index and the element if it's not a sublist
