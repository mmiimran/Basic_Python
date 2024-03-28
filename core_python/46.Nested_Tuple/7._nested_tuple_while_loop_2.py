# Nested Tuple - While loop
a = ((10, 20, 30), (40, 50, 60))
	 
n = len(a)
i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(i, j, a[i][j])  # Print the indices and elements of the nested tuple
        j += 1
    i += 1
