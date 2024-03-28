# Nested Tuple - for loop
a = (10, 20, 30, (50, 60))

# Get the length of the tuple
n = len(a)

# Iterate through the elements of the tuple
for i in range(n):
    # Check if the element is a tuple
    if type(a[i]) is tuple: 
        # Check if the nested tuple has more than one element
        if len(a[i]) > 1:
            # Get the length of the nested tuple
            m = len(a[i])
            # Iterate through the elements of the nested tuple
            for j in range(m):
                print(i, j, a[i][j])  # Print the indices and the elements of the nested tuple
    else:
        print(i, a[i])  # Print the index and the element if it's not a nested tuple
