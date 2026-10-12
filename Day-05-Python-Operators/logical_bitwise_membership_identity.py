# Day 5: Logical, bitwise, membership, and identity operators

age = 20
has_id = True
print("Eligible:", age >= 18 and has_id)
print("Either condition:", age < 18 or has_id)
print("Negation:", not has_id)

# Bitwise operations
a = 6
b = 3
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left shift:", a << 1)
print("Right shift:", a >> 1)

# Membership
ids = [101, 102, 103]
print(101 in ids)
print(105 not in ids)

# Identity
result = None
print(result is None)

first = [10]
second = [10]
print(first == second)  # equal values
print(first is second)  # different objects

# Ternary operator
marks = 75
status = "Pass" if marks >= 35 else "Fail"
print(status)
