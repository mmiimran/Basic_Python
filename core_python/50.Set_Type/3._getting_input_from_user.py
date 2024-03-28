# Getting input from user

# Creating an empty Set
a = set()
print(id(a))
n = int(input("Enter number of Elements: "))

# Adding elements to the set
for i in range(n):
    el = input("Enter Element: ")
    a.add(el)

# Accessing set 
for i in a:
    print(i)

print(id(a))
