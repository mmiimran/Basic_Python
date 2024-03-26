# Pass/Call by Object Reference

# Function to demonstrate pass/call by object reference
def val(x):
    x = 15  # Modifying the value of parameter 'x'
    print(x, id(x))  # Printing the modified value and its memory address

x = 10  # Variable 'x' with initial value
val(x)  # Calling the function with 'x' as argument
print(x, id(x))  # Printing the original value of 'x' and its memory address
