# Nested While Loop
# Initializing variable 'i' to 1 for the outer loop
i = 1

# Outer loop: iterating while 'i' is less than or equal to 3
while i <= 3:
    # Printing the current value of 'i' for the outer loop
    print("Outer Loop", i)
    # Incrementing 'i' by 1
    i += 1
    
    # Initializing variable 'j' to 1 for the inner loop
    j = 1
    # Inner loop: iterating while 'j' is less than or equal to 5
    while j <= 5:
        # Printing the current value of 'j' for the inner loop
        print("Inner Loop", j)
        # Incrementing 'j' by 1
        j += 1

# Printing a message after both loops finish executing
print("Rest of Code")
