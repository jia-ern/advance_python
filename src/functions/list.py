a = [10, 20, 30, 40, 50]

print("First element: ", a[0])
print("Last element: ", a[-1])

# ============== Creating List with Repeated Elements ==============
# Create a list [0, 0, 0, 0, 0, 0, 0]
b = [0] * 7
print("Repeated Elements: ", b)

# ============== Adding element into list ==============
# Initialize an empty list
a = []

# Adding 10 to end of list
print("Adding element into list:")
print("Original:", a)
a.append(10)
print("After append(10):", a)

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a)

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)


# ============== Updating Elements into List ==============
a = [10, 20, 30, 40, 50]
# Change the second element
a[1] = 25
print(a)
