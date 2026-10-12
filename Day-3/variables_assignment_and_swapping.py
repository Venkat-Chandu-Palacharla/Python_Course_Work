# Day 3: Variables, assignment, reassignment, and swapping

name = "Jani"
age = 21
print(name, age)

# Multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)

# Same value assigned to multiple variables
x = y = z = 100
print(x, y, z)

# Reassignment
x = 5
x = 10
print("Reassigned x:", x)

# Pythonic swapping
a = 10
b = 20
a, b = b, a
print("After swapping:", a, b)
