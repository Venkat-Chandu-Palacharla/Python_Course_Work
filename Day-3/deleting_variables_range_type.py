# Day 3: del, range(), and type()

value = 10
print("Before deletion:", value)
del value
# print(value)  # Uncomment to see NameError: value no longer exists.

print("range(5):", list(range(5)))
print("range(2, 8):", list(range(2, 8)))
print("range(0, 10, 2):", list(range(0, 10, 2)))

student_name = "Raju"
student_age = 23
marks = 97.5
print(type(student_name))
print(type(student_age))
print(type(marks))
