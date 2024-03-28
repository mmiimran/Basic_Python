# Passing Set to Function

# Define a function to display the set
def show(s):
    print(s)
    print(type(s))
    for i in s:
        print(i)

# Define a set
st = {10, 20, 30, 'ImranShows'}

# Call the function and pass the set as an argument
show(st)
