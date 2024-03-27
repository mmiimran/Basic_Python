# Nested List - for loop
a = [[10, 20, 30], [40, 50, 60]]
	 
# Printing elements without indices
for r in a:
    for c in r:
        print(c)
    print()

# Printing elements with indices
n = len(a)
for i in range(n):
    for j in range(len(a[i])):
        print(i, j, a[i][j])
    print()
