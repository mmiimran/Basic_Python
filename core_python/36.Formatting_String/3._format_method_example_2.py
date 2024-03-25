# Integer
print("******** Integer ********")
print("{}".format(15))							# Printing as string 15
print("{:d}".format(15))						# Integer without any formatting
print("{0:d}".format(15))						# Integer with positional formatting
print("{num:d}".format(num=15))					# Integer with keyword formatting
print("{num:5d}".format(num=15))				# Integer with width formatting (right align)
print("{num:05d}".format(num=15))				# Integer with zero-padding (width 5)
print("{num:+5d}".format(num=15))				# Integer with sign prefix (+) and width formatting
print("{num:<5d}".format(num=15))				# Integer with left alignment and width formatting
print("{num:*<5d}".format(num=15))				# Integer with left alignment, width formatting, and fill
print("{num:*>5d}".format(num=15))				# Integer with right alignment, width formatting, and fill
print("{num:^5d}".format(num=15))				# Integer with center alignment and width formatting
print("{num:*^5d}".format(num=15))				# Integer with center alignment, width formatting, and fill

# Float
print("******** Float ********")
print("{}".format(15.65))						# Printing as string 15.65
print("{:f}".format(15.65))						# Float without any formatting
print("{0:f}".format(15.65))					# Float with positional formatting
print("{num:f}".format(num=15.65))				# Float with keyword formatting
print("{num:8f}".format(num=15.65))				# Float with width formatting (right align)
print("{num:8.3f}".format(num=15.65))			# Float with width and precision formatting
print("{num:+8.2f}".format(num=15.65))			# Float with sign prefix (+) and width formatting
print("{num:<8.2f}".format(num=15.65))			# Float with left alignment and width formatting
print("{num:*<8.2f}".format(num=15.65))			# Float with left alignment, width formatting, and fill
print("{num:*>8.2f}".format(num=15.65))			# Float with right alignment, width formatting, and fill
print("{num:^8.2f}".format(num=15.65))			# Float with center alignment and width formatting
print("{num:*^8.2f}".format(num=15.65))			# Float with center alignment, width formatting, and fill

# String
print("******** String ********")
print("{:8s}".format("code_2"))					# String with width formatting (right align)
print("{:<8}".format("code_2"))					# String with left alignment and width formatting
print("{:*<8}".format("code_2"))					# String with left alignment, width formatting, and fill
print("{:>8}".format("code_2"))					# String with right alignment and width formatting
print("{:*>8s}".format("code_2"))				# String with right alignment, width formatting, and fill
print("{:^8s}".format("code_2"))					# String with center alignment and width formatting
print("{:*^8s}".format("code_2"))					# String with center alignment, width formatting, and fill

print("******** Truncating String ********")
print("{:.3s}".format("code_2_learn"))			# Truncated string with 3 characters
print("{:8.3s}".format("code_2_learn"))			# Truncated string with 3 characters and width formatting (right align)
print("{:*<8.3s}".format("code_2_learn"))		# Truncated string with 3 characters, left alignment, width formatting, and fill
print("{:>8.3s}".format("code_2_learn"))			# Truncated string with 3 characters, right alignment, and width formatting
print("{:*>8.3s}".format("code_2_learn"))		# Truncated string with 3 characters, right alignment, width formatting, and fill
print("{:^8.3s}".format("code_2_learn"))			# Truncated string with 3 characters, center alignment, and width formatting
print("{:*^8.3s}".format("code_2_learn"))		# Truncated string with 3 characters, center alignment, width formatting, and fill
