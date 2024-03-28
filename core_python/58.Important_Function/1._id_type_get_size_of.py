a = 10
b = 30.23
c = "String"
d = [10, 20, 30]
e = (10, 20, 30)
f = {10, 20, 30}
g = {101:'imran', 102:'mamun', 103:'shaon'}

# id() Function
print(id(a))
print()

# type() Function
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print()

# getsizeof() Function
from sys import getsizeof
print(getsizeof(a))
print(getsizeof(b))
print(getsizeof(c))
print(getsizeof(d))
print(getsizeof(e))
print(getsizeof(f))
print(getsizeof(g))
