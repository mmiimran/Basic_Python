# Passing List to Function
def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)

lst = [10, 20, 30, 'ImranShows']
show(lst)  # Corrected the function call from "ls" to "lst"
