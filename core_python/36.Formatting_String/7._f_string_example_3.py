# Thousand Separator
price = 1234567890
print(f"{price:,}")  # Printing 'price' with comma as thousand separator using f-string format
print(f"{price:_}")  # Printing 'price' with underscore as thousand separator using f-string format

# Variable
name = "Imran"  # Assigning the value "Imran" to variable 'name'
age = 62  # Assigning the value 62 to variable 'age'
print(f"My name is {name} and age {age}")  # Printing formatted string with 'name' and 'age' using f-string format

# Expression
print(f"{10*8}")  # Printing result of expression using f-string format

# Expressing a Percentage
a = 50  # Assigning the value 50 to variable 'a'
b = 3  # Assigning the value 3 to variable 'b'
print(f"{a/b:.2%}")  # Printing result of percentage expression with 2 decimal places using f-string format

# Accessing arguments’ items
value = (10, 20)  # Creating tuple 'value' with values 10 and 20
print(f"{value[0]} {value[1]}")  # Printing values of tuple 'value' using f-string format

# Format with Dict
data = {'imran': 2000, 'mamun': 3000}  # Creating dictionary 'data' with keys 'imran' and 'mamun'
print(f"{data['imran']:d} {data['mamun']:d}")  # Printing values from dictionary 'data' using f-string format

# Calling Function
name = "ImranShows"  # Assigning the value "ImranShows" to variable 'name'
print(f"{name}")  # Printing 'name' using f-string format
print(f"{name.upper()}")  # Printing 'name' in uppercase using f-string format

# Using object created from class
# print(f"{obj.name}")  # Example comment: This line uses an object created from a class, but is currently commented out.

# Curly Braces
print(f"{10}")  # Printing number 10 using f-string format
print(f"{{10}}")  # Printing curly braces with number 10 using f-string format

# Date and Time
from datetime import datetime  # Importing datetime class from datetime module
today = datetime(2019, 10, 5)  # Creating datetime object 'today' with date October 5, 2019
print(f"{today}")  # Printing 'today' using f-string format
print(f"{today:%d-%b-%Y}")  # Printing formatted date with day-month-year using f-string format
print(f"{today:%d/%b/%Y}")  # Printing formatted date with day/month/year using f-string format
print(f"{today:%b/%d/%Y}")  # Printing formatted date with month/day/year using f-string format



# Datetime Directive https://docs.python.org/3.11/library/datetime.html#strftime-and-strptime-behavior
