# Adding new item to Dictionary

# Initial dictionary
stu = {101: 'imran', 102: 'mamun', 103: 'mejbah'}
print("Before Adding:")
print(stu)  # Print original dictionary
print(id(stu))  # Print memory address of original dictionary
print()

# Adding a new key-value pair to the dictionary
stu[104] = 'imranShows'
print("After Adding:")
print(stu)  # Print modified dictionary
print(id(stu))  # Print memory address of modified dictionary
print()
