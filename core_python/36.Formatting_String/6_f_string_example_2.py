# Integer
print("******** Integer ********")  # Printing section header for integers
num = 15  # Assigning the value 15 to variable 'num'
print(f"{num}")  # Printing 'num' using f-string format (default: treated as string)
print(f"{num:d}")  # Printing 'num' as integer using f-string format
print(f"{num:5d}")  # Printing 'num' as integer with minimum width 5 using f-string format
print(f"{num:05d}")  # Printing 'num' as integer with zero padding and minimum width 5 using f-string format
print(f"{num:+5d}")  # Printing 'num' as integer with sign and minimum width 5 using f-string format
print(f"{num:<5d}")  # Printing 'num' as integer with left align and minimum width 5 using f-string format
print(f"{num:*<5d}")  # Printing 'num' as integer with left align, filled with '*' and minimum width 5 using f-string format
print(f"{num:*>5d}")  # Printing 'num' as integer with right align, filled with '*' and minimum width 5 using f-string format
print(f"{num:^5d}")  # Printing 'num' as integer with center align and minimum width 5 using f-string format
print(f"{num:*^5d}")  # Printing 'num' as integer with center align, filled with '*' and minimum width 5 using f-string format

# Float
print("******** Float ********")  # Printing section header for floats
num = 15.65  # Assigning the value 15.65 to variable 'num'
price = 15.65123456789  # Assigning the value 15.65123456789 to variable 'price'
print(f"{num}")  # Printing 'num' using f-string format (default: treated as string)
print(f"{num:f}")  # Printing 'num' as float using f-string format
print(f"{num:8f}")  # Printing 'num' as float with minimum width 8 using f-string format
print(f"{price:.20f}")  # Printing 'price' as float with precision 20 using f-string format
print(f"{num:8.3f}")  # Printing 'num' as float with 3 decimal places and minimum width 8 using f-string format
print(f"{num:+8.2f}")  # Printing 'num' as float with sign, 2 decimal places, and minimum width 8 using f-string format
print(f"{num:<8.2f}")  # Printing 'num' as float with left align, 2 decimal places, and minimum width 8 using f-string format
print(f"{num:*<8.2f}")  # Printing 'num' as float with left align, filled with '*', 2 decimal places, and minimum width 8 using f-string format
print(f"{num:*>8.2f}")  # Printing 'num' as float with right align, filled with '*', 2 decimal places, and minimum width 8 using f-string format
print(f"{num:^8.2f}")  # Printing 'num' as float with center align, 2 decimal places, and minimum width 8 using f-string format
print(f"{num:*^8.2f}")  # Printing 'num' as float with center align, filled with '*', 2 decimal places, and minimum width 8 using f-string format

# String
print("******** String ********")  # Printing section header for strings
name = "imran"  # Assigning the value "imran" to variable 'name'
print(f"{name}")  # Printing 'name' using f-string format (default: treated as string)
print(f"{name:s}")  # Printing 'name' using f-string format (explicitly as string)
print(f"{name:8s}")  # Printing 'name' with minimum width 8 using f-string format
print(f"{name:<8}")  # Printing 'name' with left align and minimum width 8 using f-string format
print(f"{name:*<8}")  # Printing 'name' with left align, filled with '*', and minimum width 8 using f-string format
print(f"{name:>8}")  # Printing 'name' with right align and minimum width 8 using f-string format
print(f"{name:*>8s}")  # Printing 'name' with right align, filled with '*', and minimum width 8 using f-string format
print(f"{name:^8s}")  # Printing 'name' with center align and minimum width 8 using f-string format
print(f"{name:*^8s}")  # Printing 'name' with center align, filled with '*', and minimum width 8 using f-string format

print("******** Truncating String ********")  # Printing section header for truncated strings
name = "imranShows"  # Assigning the value "imranShows" to variable 'name'
print(f"{name:.3s}")  # Printing 'name' with first 3 characters using f-string format
print(f"{name:8.3s}")  # Printing 'name' with first 3 characters and minimum width 8 using f-string format
print(f"{name:*<8.3s}")  # Printing 'name' with first 3 characters,
