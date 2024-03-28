# Passing and Returning Dictionary
def show(d):
    # Print the dictionary
    print(d)
    # Print the type of the dictionary
    print(type(d))
    # Iterate through the dictionary
    for k in d:
        # Print key-value pairs
        print(k,'=',d[k])
    # Return the dictionary
    return d

# Dictionary containing key-value pairs
dc = {101:'imran', 102:'mamun', 103:'fuad'}
# Call the function and pass the dictionary as an argument
new_dc = show(dc)
# Print the returned dictionary
print(new_dc)
# Print the type of the returned dictionary
print(type(new_dc))
