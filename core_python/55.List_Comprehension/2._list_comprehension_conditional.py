# List Comprehension

# Without List Comprehension (Conditional)
lst1 =[]
for i in range(20):
    if(i%2==0):
        lst1.append(i)
print(lst1)

# With List Comprehension (Conditional)
lst2 =[i for i in range(20) if i%2==0]
print(lst2)
