# Day 8: Tuples, packing, and unpacking

coordinates = (10, 20)
print(coordinates)
print(coordinates[0])
print("Count:", (1, 2, 2, 3).count(2))
print("Index:", (10, 20, 30).index(20))

# A single-element tuple requires a trailing comma.
single_item = (5,)
print(single_item, type(single_item))

# Tuple packing and unpacking
data = 10, 20, 30
a, b, c = data
print(a, b, c)

# Tuples are immutable: direct item assignment is not allowed.
# coordinates[0] = 100  # Uncomment to see TypeError.
