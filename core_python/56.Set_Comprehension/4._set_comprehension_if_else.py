# Set Comprehension

# Without Set Comprehension (if else)
set1 = set()
for i in range(10):
    if(i%2==0):
        set1.add(i)
    else:
        set1.add(i*1000)
print(set1)
print(type(set1))

# With Set Comprehension (if else)
set2 = {i if i%2==0 else i*1000 for i in range(10)}
print(set2)
print(type(set2))
