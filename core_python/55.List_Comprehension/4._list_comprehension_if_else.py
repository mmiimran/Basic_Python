# List Comprehension

# Without List Comprehension (if else)
lst1 =[]
for i in range(10):
    if(i%2==0):
        lst1.append(i)
    else:
        lst1.append("Invalid")
print(lst1)

# With List Comprehension (if else)
lst2 =[i if i%2==0 else "Invalid" for i in range(10)]
print(lst2)
