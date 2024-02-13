# Expression: value = (1+1)*2**4//3+4-1

# Operator precedence: ()
# Inside the parentheses, the addition operation is performed first
# Result: (1+1) -> 2

# Operator precedence: **
# Exponentiation operation is performed next
# Result: 2**4 -> 16

# Operator precedence: //, /
# Division operation is performed next, with floor division taking precedence over regular division
# Result: 16//3 -> 5 (since floor division always rounds down to the nearest integer)

# Operator precedence: *, /
# Multiplication operation is performed next
# Result: (1+1)*5 -> 10

# Operator precedence: +, -
# Addition and subtraction operations are performed next, from left to right
# Result: 10+4 -> 14, then 14-1 -> 13

# Final result: 13
value = (1+1)*2**4//3+4-1

# Printing the result
print(value)
