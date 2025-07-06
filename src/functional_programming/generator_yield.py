# A generator function
# returns an iterator object.
# use yield to produce a series of results over time.
# Note: return: to send back a single value

print("yield: ")
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Yields the current value of count
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)

# VS return
print("========================================================")
print("return: ")
def sum_up_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total  # Returns the final result and exits the function

result = sum_up_to(5)
print(result)


# Python Generator Expression
print("========================================================")
print("Python Generator Expression: ")
sq = (x*x for x in range(1, 6))
for i in sq:
    print(i)
