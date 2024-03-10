# Importing required functionality from numpy
from numpy import *

# Creating numpy arrays 'a' and 'b' with given elements
a = array([100, 200, 13, 400, 500])
b = array([100, 20, 30, 400, 50])

# Comparing arrays 'a' and 'b' element-wise for equality
result1 = a == b

# Comparing arrays 'a' and 'b' element-wise for less than
result2 = a < b

# Comparing arrays 'a' and 'b' element-wise for greater than
result3 = a > b

# Comparing arrays 'a' and 'b' element-wise for less than or equal to
result4 = a <= b

# Comparing arrays 'a' and 'b' element-wise for greater than or equal to
result5 = a >= b

# Comparing arrays 'a' and 'b' element-wise for inequality
result6 = a != b

# Printing the arrays and comparison results
print("a", a)
print("b", b)
print("a==b",result1)
print("a<b",result2)
print("a>b",result3)
print("a<=b",result4)
print("a>=b",result5)
print("a!b",result6)
