# If elif else Statement
# Defining the variable 'day' with a string value
day = "Friday"

# Checking if 'day' is equal to "Monday"
if (day == "Monday"):
    print("Today is Monday")
# If 'day' is not "Monday", checking if 'day' is equal to "Tuesday"
elif (day == "Tuesday"):
    print("Today is Tuesday")
# If 'day' is not "Monday" or "Tuesday", checking if 'day' is equal to "Wednesday"
elif (day == "Wednesday"):
    print("Today is Wednesday")
# If 'day' is none of the specified days, executing the else block
else:
    print("Today is Holiday")


# If elif else with User Input
# Prompting the user to enter the day and storing it in the variable 'day'
day = input("Enter Day: ")

# Checking if 'day' entered by the user is "Monday"
if day == "Monday":
    print("Today is Monday")
# If 'day' is not "Monday", checking if it is "Tuesday"
elif day == "Tuesday":
    print("Today is Tuesday")
# If 'day' is not "Monday" or "Tuesday", checking if it is "Wednesday"
elif day == "Wednesday":
    print("Today is Wednesday")
# If 'day' is none of the specified days, executing the else block
else:
    print("Today is Holiday")
