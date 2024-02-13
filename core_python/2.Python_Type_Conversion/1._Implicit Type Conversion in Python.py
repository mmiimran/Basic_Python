# Implicit Type Conversion Examples

# Division operation with integers
# Result will be a float due to implicit type conversion
a = 5
b = 2
value = a / b
print(value)
print(type(value))

# Addition operation with integer and float
# Result will be a float due to implicit type conversion
x = 10
y = 5.5
total = x + y 
print(total)
print(type(total))

# Concatenation operation with strings
# Result will be a string due to implicit type conversion
j = "Hello"
k = "code2learn"
p = j + k
print(p)
print(type(p))

# Addition operation with integer and string
# Will raise a TypeError due to incompatible types
q = 20
u = '10'
r = q + u 
print(r)

# Addition operation with integer and string
# Will raise a TypeError due to incompatible types
m = 20
n = "code2learn"
t = m + n 
print(t)
