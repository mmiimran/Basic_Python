# Nested Tuple - for loop
a = ((10, 20, 30), (40, 50, 60))
	 
# Iterating without index
for r in a:
    for c in r:
        print(c)  # Print each element of the nested tuple
    print()  # Print an empty line to separate nested tuples

# Iterating with index
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i, j, a[i][j])  # Print the indices and elements of each nested tuple
    print()  # Print an empty line to separate nested tuples
