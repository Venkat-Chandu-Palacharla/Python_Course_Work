# Day 7: String slicing
# Syntax: text[start:end:step]
# The start index is included; the end index is excluded.

s = "codegnan"
print(s[:])          # full string
print(s[:4])         # code
print(s[4:])         # gnan
print(s[::2])        # every second character
print(s[-4:-1])      # gna
print(s[::-1])       # reversed string
print(s[7:3:-1])     # reverse from index 7 to before index 3
print(s[5:2:1])      # empty string: direction does not match
