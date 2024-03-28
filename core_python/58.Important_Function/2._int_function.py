# int() Function
a = 10.56
print("Float:", a)
print(type(a))
new_a = int(a)
print("Int:", new_a)
print(type(new_a))
print()

b = "10"
print("String:", b)
print(type(b))
new_b = int(b)
print("Int:", new_b)
print(type(new_b))
print()

# Below code will show error 
c = "imranShows"
print("String:", c)
print(type(c))
new_c = int(c)  # Error will occur here
print("Int:", new_c)
print(type(new_c))
