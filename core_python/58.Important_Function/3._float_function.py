# float() Function
a = 10
print("Int:", a)
print(type(a))
new_a = float(a)
print("Float:", new_a)
print(type(new_a))
print()

b = "10.56"
print("String:", b)
print(type(b))
new_b = float(b)
print("Float:", new_b)
print(type(new_b))
print()

# Below code will show error 
c = "imranShows"
print("String:", c)
print(type(c))
new_c = float(c)  # Error will occur here
print("Float:", new_c)
print(type(new_c))
