# Day 4: Implicit and explicit type conversion

# Implicit conversion
a = 10
b = 12.5
print(a + b)  # 22.5

# Explicit conversion
integer_value = int("10")
float_value = float("10.5")
string_value = str(25)
boolean_value = bool("Python")

print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(string_value, type(string_value))
print(boolean_value, type(boolean_value))

# int() truncates the fractional part of a float; it does not round.
print(int(10.9))  # 10

# Boolean values behave like 1 and 0 in arithmetic.
print(True + 5)   # 6
print(int(False)) # 0
