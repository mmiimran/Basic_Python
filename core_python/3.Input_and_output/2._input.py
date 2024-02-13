# Getting user input without prompt
# The user input is assigned to the variable 'name'
name = input()
print(name)

# Getting user input with prompt
# The user is prompted to enter their name
nm = input("What is Your Name: ")
print(nm)

# Getting user input with prompt and displaying the name
nm = input("What is Your Name: ")
print(f"You name is: {nm}")

# Getting input and converting it into an integer
# The user is prompted to enter their mobile number
mobile = input("Enter Mobile Number: ")
print(type(mobile))  # Checking the type of 'mobile' before conversion
mb = int(mobile)  # Converting 'mobile' to an integer and assigning it to 'mb'
print(mb)
print(type(mb))  # Checking the type of 'mb' after conversion

# Getting input and converting it into an integer directly
# The user is prompted to enter their registration number
reg = int(input("Enter Registration Number: "))
print(reg)
