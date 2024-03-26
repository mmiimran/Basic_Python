# Pass/Call by Object Reference

# Function to demonstrate pass/call by object reference
def val(lst):
    print("Inside Function Before Append:", lst, id(lst))  # Printing the list and its memory address before append
    lst.append(4)  # Modifying the list by appending an element
    print("Inside Function After Append:", lst, id(lst))  # Printing the list and its memory address after append

lst = [1, 2, 3]  # List with initial values
print("Before Calling Func:", lst, id(lst))  # Printing the list and its memory address before calling the function
val(lst)  # Calling the function with the list as an argument
print("After Calling Func:", lst, id(lst))  # Printing the list and its memory address after calling the function
