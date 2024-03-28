# Passing and Returning Tuple
def show(t):
    """
    Function to display the tuple and its type, and return the same tuple.

    Parameters:
        t (tuple): The tuple to be displayed and returned.

    Returns:
        tuple: The same tuple passed as input.
    """
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t

# Example of passing a tuple to the show function and returning the same tuple
tup = (10, 20, 30, 'ImranShows')
new_tup = show(tup)
print(new_tup)
print(type(new_tup))
