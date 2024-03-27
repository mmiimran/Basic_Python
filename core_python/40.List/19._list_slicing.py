# Original list
x = [101, 102, 103, 104, 105, 106, 107]

# Printing the original list with indices
print("Original List")
n = len(x)
for i in range(n):
    print(i, "=", x[i])
print()

# Slicing from 1st position to 4th position
print("From 1st Position to 4th Position")
a = x[1:5]
for i in a:
    print(i)
print()

# Slicing from 0th position to last position
print("From 0th Position to last Position")
b = x[0:]
for i in b:
    print(i)
print()

# Slicing from 0th position to 4th position
print("From 0th Position to 4th Position")
c = x[:5]
for i in c:
    print(i)
print()

# Slicing the last 4 elements
print("Last 4 Elements")
d = x[-4:]
for i in d:
    print(i)
print()

# Slicing from 0th position to 6th position with a stride of 2
print("From 0th Position to 6th Position stride 2")
e = x[0:7:2]
for i in e:
    print(i)
print()

# Slicing the last 5 elements with 2 elements towards the right
print("Last 5 Elements with [-5-(-3)]= 2 elements towards right")
f = x[-5:-3]
for i in f:
    print(i)
