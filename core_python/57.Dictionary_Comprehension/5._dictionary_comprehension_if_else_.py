# Dictionary Comprehension

# Without Dictionary Comprehension (If Else)
dict1 = {}
for n in range(10):
    if n % 2 == 0:
        dict1[n] = n
    else:
        dict1[n] = "Invalid"
print(dict1)

# With Dictionary Comprehension (If Else)
dict2 = {n: (n if n % 2 == 0 else "Invalid") for n in range(10)}
print(dict2)
