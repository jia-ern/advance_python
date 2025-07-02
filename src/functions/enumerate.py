# enumerate() function
# adds a counter to each item in a list or other iterable.
# turns the iterable into something we can loop through, where each item comes with its number (starting from 0 by default).
# We can also turn it into a list of (number, item) pairs using list().

a = ["Geeks", "for", "Geeks"]

enum_obj = enumerate(a)
print(type(enum_obj))

# Iterating list using enumerate to get both index and element
for i, name in enum_obj:
    print(f"Index {i}: {name}")

# Converting to a list of tuples
print(list(enumerate(a)))

# start with index 1
print(list(enumerate(a, 1)))