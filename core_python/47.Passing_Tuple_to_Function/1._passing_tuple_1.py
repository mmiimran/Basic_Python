# Passing Tuple to Function
def show(t):
    """
    Function to display the tuple and its type.

    Parameters:
        t (tuple): The tuple to be displayed.

    Returns:
        None
    """
    print(t)
    print(type(t))
    for i in t:
        print(i)

# Example of passing a tuple to the show function
tup = (10, 20, 30, 'imranShows')
show(tup)
