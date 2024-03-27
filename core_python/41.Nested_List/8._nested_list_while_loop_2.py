# Nested List - While loop
a = [[10, 20, 30],[40, 50, 60]]
	 
# Get the length of the outer list
n = len(a)
i = 0
# Iterate through the outer list
while i < n:
    j = 0
    # Iterate through the inner list
    while j < len(a[i]):
        # Print the indices and elements of the nested list
        print(i, j, a[i][j])
        j += 1
    i += 1
