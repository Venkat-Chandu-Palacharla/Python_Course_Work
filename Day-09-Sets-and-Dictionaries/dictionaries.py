# Day 9: Dictionaries

student = {
    "id": 101,
    "name": "Ravi",
    "course": "Python",
}

print(student["name"])
print(student.get("marks"))  # None when key is missing

student["marks"] = 85
student["course"] = "Python Programming"
print("Updated:", student)

print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

student.pop("id")
print("After removing id:", student)

for key, value in student.items():
    print(key, ":", value)
