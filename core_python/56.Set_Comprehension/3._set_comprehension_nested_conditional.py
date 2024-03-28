# Set Comprehension

# Without Set Comprehension (Conditional)
set1 = set()
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            set1.add(i)
print(set1)
print(type(set1))

# With Set Comprehension (Conditional)
set2 = {i for i in range(20) if i%2==0 if i%3==0}
print(set2)
print(type(set2))
