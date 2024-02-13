# If Else statement
if 5<2:  # If 5 is less than 2
    print("Greater")  # Print "Greater"
else:
    print("Smaller")  # Print "Smaller"

# If Else Statement in Single Line
print("Greater") if 5<2 else print("Smaller")  # If 5 is less than 2, print "Greater", else print "Smaller"

# If Else Statement with Rest of the Code
if 5<2:  # If 5 is less than 2
    print("Greater")  # Print "Greater"
else:
    print("Smaller")  # Print "Smaller"
print("Rest of The Code")  # Print "Rest of The Code"

# If Else Statement with Group of Statement
if 5<2:  # If 5 is less than 2
    print("Greater")  # Print "Greater"
    print("5 is greater than 2")  # Print "5 is greater than 2"
else:
    print("Smaller")  # Print "Smaller"
    print("Statement 2")  # Print "Statement 2"
print("Rest of The Code")  # Print "Rest of The Code"

# Nested If Else Statement
a = 5
b = 2
c = 6
d = 3
if a>b:  # If a is greater than b
    print("a is greater than b")  # Print "a is greater than b"
    if c>d:  # If c is greater than d
        print("c is Greater than d")  # Print "c is Greater than d"
    else:
        print("d is Greater than c")  # Print "d is Greater than c"
else:
    print("b is greater than a")  # Print "b is greater than a"
print("Rest of The Code")  # Print "Rest of The Code"

# If Else statement with Logical Operator
if 5>2 and 7<3:  # If 5 is greater than 2 and 7 is less than 3
    print("If statement with Logical Operator")  # Print "If statement with Logical Operator"
    print("Statement 2")  # Print "Statement 2"
else:
    print("Else Statement")  # Print "Else Statement"
print("Rest of the Code")  # Print "Rest of the Code"
