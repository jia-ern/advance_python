# Deep Copy and Shallow Copy in Python

# Deep copy in Python
# creates a new compound object before inserting copies of the items found in the original into it in a recursive manner.
# 1. construct a new collection object
# 2. recursively populate it with copies of the child objects found in the original.
# Any changes made to a copy of the object do not reflect in the original object.

import copy

a = [[1, 2, 3], [4, 5, 6]]

# Creating a deep copy of the nested list 'a'
b = copy.deepcopy(a)

# Modifying an element in the deep-copied list
b[0][0] = 99
print("b deep copy: ", b)
print("a: ", a)


# Shallow copy in Python
# creates a new object but retains references to the objects contained within the original.
# only copies the top-level structure without duplicating nested elements.
# Changes made to a copy of an object do reflect in the original object.
# In python, this is implemented using the "copy.copy()" function.

a = [[1, 2, 3], [4, 5, 6]]

# Creating a shallow copy of the nested list 'original'
b = copy.copy(a)

# Modifying an element in the shallow-copied list
b[0][0] = 99

# Printing the original and shallow-copied lists
print("b shallow copy: ", b)
print("a: ", a)
