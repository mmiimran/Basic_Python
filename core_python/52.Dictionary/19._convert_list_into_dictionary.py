# Converting Lists into Dictionary

# Lists of roll numbers and corresponding names
roll = [101, 102, 103]
name = ['imran', 'mamun', 'ehan']

# Creating a dictionary from the lists
z = zip(roll, name)  # Zipping the lists together
d = dict(z)  # Converting the zipped object into a dictionary

# Printing key-value pairs from the dictionary
for k in d:
    print(k, '=', d[k])  # Printing each key-value pair in the dictionary
