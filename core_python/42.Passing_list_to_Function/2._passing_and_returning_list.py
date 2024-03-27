# Passing and Returning List
def show(l):
    """
    Function to print elements of a list and return the same list.

    Args:
    l (list): The list to be processed.

    Returns:
    list: The same list passed as input.

    """
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l

lst = [10, 20, 30, 'ImranShows']
new_lst = show(lst)
print(new_lst)
print(type(new_lst))
