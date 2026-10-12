# Day 8: Lists and common operations

numbers = [10, 20, 30, 20]
print("Original:", numbers)
print("First:", numbers[0])
print("Last:", numbers[-1])
print("Slice:", numbers[1:3])

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)  # removes first matching value
last_item = numbers.pop()
print("After changes:", numbers)
print("Popped:", last_item)
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

numbers.sort()
print("Sorted:", numbers)
print("Length:", len(numbers))

nested = [[1, 2], [3, 4]]
print(nested[0])
print(nested[1][1])
