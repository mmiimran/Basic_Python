# Passing Dictionary to Function
def show(d):
    # Print the dictionary
    print(d)
    # Print the type of the dictionary
    print(type(d))
    # Iterate through the dictionary
    for k in d:
        # Print key-value pairs
        print(k,'=',d[k])

# Dictionary containing key-value pairs
dc = {101:'imran', 102:'mamun', 103:'fuad'}
# Call the function and pass the dictionary as an argument
show(dc)
