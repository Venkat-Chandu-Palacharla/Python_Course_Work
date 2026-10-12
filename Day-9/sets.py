# Day 9: Sets

numbers = {1, 2, 2, 3}
print("Duplicates removed:", numbers)

numbers.add(4)
numbers.discard(2)
print("After add/discard:", numbers)

left = {1, 2, 3}
right = {3, 4, 5}
print("Union:", left | right)
print("Intersection:", left & right)
print("Difference:", left - right)
print("Symmetric difference:", left ^ right)
print("Membership:", 3 in left)

# Use set() for an empty set; {} creates an empty dictionary.
empty_set = set()
print(empty_set)
