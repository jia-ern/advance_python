print("================================================")
print("Changing Case")
# upper():
s = "hello world"
print("Original: ", s)
print("upper: ", s.upper())

# lower():
# Converts all characters in the string to lowercase.
print("lower: ", s.lower())

# capitalize():
# Capitalizes the first character of the string and makes the rest lowercase.
print("capitalize: ", s.capitalize())

# title():
# Capitalizes the first letter of each word in the string.
print("title: ", s.title())

# swapcase():
# Swap the cases of all characters in a string
print("swapcase: ", s.swapcase())


# Replacing Substrings
print("================================================")
print("Replacing Substrings")
s1 = "I love Python"
s2 = s1.replace("Python", "programming")
print(s2)

# Trimming Whitespace
print("================================================")
print("Trimming Whitespace")
s = "   Hello World!   "
print(s.strip())

# Concatenating Strings
print("================================================")
print("Concatenating Strings")
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

# Slicing Strings
print("================================================")
print("Slicing Strings")
s = "Hello, Python!"
print(s[0:5])   # Output: "Hello" (characters from index 0 to 4)
print(s[7:])    # Output: "Python!" (characters from index 7 to the end)
print(s[:5])    # Output: "Hello" (characters from the start to index 4)
print(s[::2])   # Output: "Hoo yhn" (every second character)

# Checking for Substrings
print("================================================")
print("Checking for Substrings")
s = "Python is fun"
print("Python" in s)

# Formatting Strings
print("================================================")
s = "Geek"
print(f"name - {s}")
