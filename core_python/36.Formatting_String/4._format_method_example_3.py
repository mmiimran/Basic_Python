# Comma as thousand Separator
print("{:,}".format(1234567890))

# Variable
name = "Mamun"  # Assigning the name "Mamun" to the variable 'name'
age = 62  # Assigning the value 62 to the variable 'age'
print("My name is {} and age {}".format(name, age))  # Printing a formatted string with 'name' and 'age'

# Expressing a Percentage
a = 50  # Assigning the value 50 to the variable 'a'
b = 3  # Assigning the value 3 to the variable 'b'
print("{:.2%}".format(a / b))  # Printing a formatted percentage with two decimal places

# Accessing arguments' items
value = (10, 20)  # Creating a tuple 'value' with elements 10 and 20
print("{0[0]} {0[1]}".format(value))  # Accessing items of the tuple and printing them

# Format with Dict
data1 = {'imran': 2000, 'mamun': 3000}  # Creating a dictionary 'data1' with keys and values
print("{0[imran]:d} {0[mamun]:d}".format(data1))  # Printing formatted dictionary values using index-based formatting

# Format with Dict
data2 = {'imran': 2000, 'mamun': 3000}  # Creating a dictionary 'data2' with keys and values
print("{d[imran]:d} {d[mamun]:d}".format(d=data2))  # Printing formatted dictionary values using key-based formatting

# Accessing arguments by name:
data3 = {'imran': 2000, 'mamun': 3000}  # Creating a dictionary 'data3' with keys and values
print("{imran} {mamun}".format(**data3))  # Accessing dictionary values by name and printing them

# ** is a format parameter (minimum field width)
