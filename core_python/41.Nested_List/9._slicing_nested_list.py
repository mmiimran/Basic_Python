# Slicing Nested List
x = [[10, 20, 30], 
	 [40, 50, 60], 
	 [70, 80, 90],
	 [11, 22, 33],
	 [44, 55, 66],
	 [77, 88, 99],
	 [12, 13, 14]]

# Original List
print("Original List")
print(x)
print()

# From 1st Position to 4th Position
print("From 1st Position to 4th Position")
a = x[1:5]
print(a)
print()	
	
# From 0th Position to last Position
print("From 0th Position to last Position")
b = x[0:]
print(b)
print()	
	
# From 0th Position to 4th Position
print("From 0th Position to 4th Position")
c = x[:5]
print(c)
print()	

# Last 4 Lists
print("Last 4 List")
d = x[-4:]
print(d)
print()	
	
# From 0th Position to 6th Position stepsize 2
print("From 0th Position to 6th Position stepsize 2")
e = x[0:7:2]
print(e)
print()	
	
# Last 5 Lists with [-5-(-3)]= 2 Lists towards right
print("Last 5 Lists with [-5-(-3)]= 2 Lists towards right")
f = x[-5:-3]
print(f)
print()

print("*****************************************************")
print("Slice Nested 2nd position, 0th position")
m = x[2:3]
print(m)
g = x[2:3][0]
print(g)
print()	

print("Slice 2nd List then extract elements")
# Extracting only one specific element
h = x[2:3][0][0]
print(h)
# Extracting all elements of 2nd List
i = x[2:3][0]
for el in i:
	print(el)
print()	

print("Last Nested 4 Lists then 1st position")
n = x[-4:]
print(n)
j = x[-4:][1]
print(j)
print()	

print("Last Nested 4 Lists then 1st position then extract elements")
# Extracting only one specific element
k = x[-4:][1][0]
print(k)
# Extracting all elements of 2nd position
l = x[-4:][1]
for el in l:
	print(el)
print()	
