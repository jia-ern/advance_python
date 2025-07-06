print("===================================")
print("Using * for merging lists")
a = [1, 2, 3]
b = [4, 5, 6]

# Use the unpacking operator * to merge the two lists into one
c = [*a, *b]
print(c)

print("===================================")
print("Using * with a generator expression")
n = [1, 2, 3, 4, 5]

# Use map() with a lambda function to square each element.
s = [*map(lambda x: x**2, n)]
print(s)
