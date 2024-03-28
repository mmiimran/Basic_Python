# List Comprehension

# Without List Comprehension
lst1 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst1 =[]
for i in lst1:
    new_lst1.append(i+1)
print(new_lst1)

# With List Comprehension
lst2 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
new_lst2 =[i+1 for i in lst2]
print(new_lst2)
print()

# Same as above in different way

# Without List Comprehension
lst1 =[]
for i in range(20):
    lst1.append(i+1)
print(lst1)

# With List Comprehension
lst2 =[i+1 for i in range(20)]
print(lst2)
