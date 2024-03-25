# Printing the header for the replace function
print("****** replace Function ******")

# Assigning the value "Imranshow" to variable 'name'
name = "Imranshow"
# Assigning the value "Imran" to variable 'old'
old = "Imran"
# Assigning the value "My" to variable 'new'
new = "My"
# Applying the replace() function to replace 'old' with 'new' in 'name'
str1 = name.replace(old, new)

# Printing the original 'name' and the result of the replace() function
print(name)
print(str1)

# Printing the header for the split function
print("****** split Function ******")

# Assigning the value "Hello-how-are-you" to variable 'name'
name = "Hello-how-are-you"
# Applying the split() function to split 'name' using '-' as the separator
str1 = name.split('-')

# Printing the original 'name' and the result of the split() function
print(name)
print(str1)

# Printing the header for the join function
print("****** join Function ******")

# Assigning the tuple ('Hello', 'How', 'Are', 'You') to variable 'name'
name = ('Hello', 'How', 'Are', 'You')
# Applying the join() function to join elements of 'name' using '_' as the separator
str1 = "_".join(name)

# Printing the original 'name' and the result of the join() function
print(name)
print(str1)
