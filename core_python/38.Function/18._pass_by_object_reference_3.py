# Pass/Call by Object Reference

# Example 3: Function to demonstrate pass/call by object reference
def val(lst):
    print("Inside Function Before New:", lst, id(lst))  # Printing the list and its memory address before creating new list
    # Create a new list object
    lst = [11, 22, 33]
    print("Inside Function After New:", lst, id(lst))  # Printing the new list and its memory address

lst = [1, 2, 3]  # List with initial values
print("Before Calling Func:", lst, id(lst))  # Printing the list and its memory address before calling the function
val(lst)  # Calling the function with the list as an argument
print("After Calling Func:", lst, id(lst))  # Printing the list and its memory address after calling the function
