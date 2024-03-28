# Nested Tuple - While loop
a = (10, 20, 30, (50, 60))
	 
n = len(a)
i = 0
while i < n:
    # Checking if a[i] is a tuple type
    if type(a[i]) is tuple: 
        if len(a[i]) > 1:
            j = 0
            m = len(a[i])
            while j < m:
                print(i, j, a[i][j])  # Print the indices and elements of the nested tuple
                j += 1
            i += 1
    else:
        print(i, a[i])  # Print the index and the element if it's not a tuple
        i += 1
