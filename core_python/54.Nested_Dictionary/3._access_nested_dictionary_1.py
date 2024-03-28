# Accessing Nested Dictionary using For loop
a = {1: {'course': 'Python', 'fees':15000},
     2: {'course': 'JavaScript', 'fees': 10000 } }
     
# Accessing ID
print("ID:")
for id in a:
    print(id)
print()

# Accessing each id keys
for id in a:
    for k in a[id]:
        print(k)
print()

# Accessing each id keys -- value
for id in a:
    for k in a[id]:
        print(id,'=',k,'=',a[id][k])
