# Day 6: Output formatting with print()

name = "Ravi"
age = 21
marks = 92.5

print("Name:", name, "Age:", age)
print("Python", "Java", "C", sep=" | ")
print("Loading", end="...")
print("done")

# f-string formatting
print(f"{name} is {age} years old.")
print(f"Marks: {marks:.1f}")

price = 1250
quantity = 2
print(f"Total bill: {price * quantity}")
