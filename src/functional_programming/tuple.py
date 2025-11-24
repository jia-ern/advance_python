from collections import namedtuple


# namedtuple
# Lightweight data containers.
# a function that returns a new named tuple class.
# a class factory.
# No methods.
# USe case: Pure Data Representations / Performance-Critical Applications

Point2D = namedtuple('Point2D',['x','y'])
point = Point2D(100, 200)

# unpacking
x, y = point
print(f'({x}, {y})')  # (100, 200)

# indexing
x = point[0]
y = point[1]
print(f'({x}, {y})')  # (100, 200)

# iterating

for coordinate in point:
    print(coordinate)

print(Point2D._fields)

