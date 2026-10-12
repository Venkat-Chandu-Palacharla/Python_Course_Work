# Day 7: String basics and operations

str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # concatenation
print("Python! " * 3)      # repetition

text = "Python"
print(text[0])             # first character
print(text[-1])            # last character
print(text[0:3])           # slicing
print(text[:4])
print(text[2:])
print("Pyt" in text)
print("Java" not in text)

# Strings are immutable: methods return new strings.
message = "python course"
print(message.upper())
print(message.capitalize())
print(message.replace("python", "Python"))
print(len(message))
print(ord("A"))
print(chr(97))
