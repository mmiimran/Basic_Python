# Passing and Returning Set 

# Define a function to display the set and return it
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)
    return s

# Define a set
st = {10, 20, 30, 'ImranShows'}

# Call the function and pass the set as an argument
# Also, assign the returned set to a new variable
new_st = show(st)

# Print the returned set and its type
print(new_st)
print(type(new_st))
