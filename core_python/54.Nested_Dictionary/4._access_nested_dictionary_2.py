# Accessing Nested Dictionary using For loop
a = {'course': 'Python', 'fees':15000, 1: {'course': 'JavaScript', 'fees': 10000 } }
     
# Accessing each id keys -- value
for i in a:
    if type(a[i]) is dict:  # Checking if the value is a dictionary
        for k in a[i]:
            print(k,'=',a[i][k])
    else:
        print(i,'=',a[i])
