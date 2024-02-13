# Infinite While Loop
# This loop will run indefinitely since the condition is always True
while True:
    # Printing "Code2learn" repeatedly
    print("Code2learn")
# The following line will never be executed because the loop above is infinite
print("Rest of the Code")

# Infinite While Loop with Break Statement
# Initializing variable 'i' to 0
i = 0

# This loop will run indefinitely since the condition is always True
while True:
    # Incrementing 'i' by 1 and printing its value
    i += 1
    print(i)
    # Checking if 'i' has reached 5
    if i == 5:
        # Exiting the loop when 'i' equals 5
        break

# Printing a message after the loop finishes
print("Rest of the Code")
