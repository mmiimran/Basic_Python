# Print integer value using formatting
print("%d" % 432)

# Print multiple integer values using formatting
print("%d %d" % (432, 345))

# Print float value using formatting
print("%f" % 432.123)

# Print multiple float values using formatting
print("%f %f" % (432.123, 10.3))

# Print float value with high precision using formatting
print("%f" % 432.123456)

# Print float value with limited precision using formatting
print("%f" % 432.12345651)

# Print string value using formatting
print("%s" % "code_2_learn")

# Print multiple string values using formatting
print("%s %s" % ("Hello", "code_2_learn"))

# Print integer and string values using formatting
print("%d %s" % (432, "code_2_learn"))

# Print formatted string using dictionary
print("%(nm)s %(ag)d" % {'ag': 432, 'nm': "code_2_learn"})

# Print integer value with space padding
print("% d" % 432)

# Print integer value with space padding
print("%          d" % 432)

# Print integer value with sign
print("%+d" % 432)

# Print integer value with width
print("%8d" % 432)

# Print integer value with zero padding
print("%08d" % 432)

# Print float value with limited precision using formatting
print("%.3f" % 432.123)

# Print float value with limited precision using formatting
print("%.2f" % 432.123)

# Print float value with limited precision using formatting
print("%.2f" % 432.128)

# Print float value with width and precision
print("%9.2f" % 432.128)

# Print float value with zero padding, width, and precision
print("%09.2f" % 432.123)

# Print float value with width and precision
print("%9.2f" % 4388453232.124)
