# Access Tuple using for Loop
a = (10, 21.3, 'imranshows')

# Without Index
print("Access Without Index")
for element in a:
    print(element)

print()
    
# With Index
print("Access With Index")
n = len(a)
for i in range(n):
    print(i, a[i])
