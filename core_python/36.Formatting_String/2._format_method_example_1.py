# Integer
print("******** Integer *********")
print("{}".format(10))                # Single integer value
print("{} {}".format(10, 20))         # Multiple integer values
print("{0}".format(10))               # Integer value with positional formatting
print("{0} {1}".format(10, 20))       # Integer values with positional formatting
print("{1} {0}".format(10, 20))       # Integer values with positional formatting
print("{num1}".format(num1=10))      # Integer value with keyword formatting
print("{num1} {num2}".format(num1=10, num2=20))  # Multiple integer values with keyword formatting
print("{num2} {num1}".format(num1=10, num2=20))  # Multiple integer values with keyword formatting

# Float
print("******** Float *********")
print("{}".format(10.56))              # Single float value
print("{} {}".format(10.56, 20.42))    # Multiple float values
print("{0}".format(10.56))             # Float value with positional formatting
print("{0} {1}".format(10.56, 20.42))  # Float values with positional formatting
print("{1} {0}".format(10.56, 20.42))  # Float values with positional formatting
print("{num1}".format(num1=10.56))     # Float value with keyword formatting
print("{num1} {num2}".format(num1=10.56, num2=20.42))  # Multiple float values with keyword formatting
print("{num2} {num1}".format(num1=10.56, num2=20.42))  # Multiple float values with keyword formatting

# String
print("******** String *********")
print("{}".format("code_2_learn"))           # Single string value
print("{} {}".format("code_2", "learn"))     # Multiple string values
print("{0}".format("code_2"))                 # String value with positional formatting
print("{0} {1}".format("code_2", "learn"))    # String values with positional formatting
print("{1} {0}".format("code_2", "learn"))    # String values with positional formatting
print("{str1}".format(str1="code_2_learn"))   # String value with keyword formatting
print("{str1} {str2}".format(str1="code_2", str2="learn"))  # Multiple string values with keyword formatting
print("{str2} {str1}".format(str1="code_2", str2="learn"))  # Multiple string values with keyword formatting

# Integer and String
print("Hello My Name is {}".format("code_2_learn"))          # String with formatting
print("{} {}".format(10, "learn"))                            # Integer and string values
print("{0} {1}".format(10, "learn"))                          # Integer and string values with positional formatting
print("{1} {0}".format(10, "learn"))                          # Integer and string values with positional formatting
print("{num1} {str1}".format(num1=10, str1="learn"))          # Integer and string values with keyword formatting
print("{str1} {num1}".format(num1=10, str1="learn"))          # Integer and string values with keyword formatting
