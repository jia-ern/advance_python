# iterator
# an object that holds a sequence of values
# provide sequential traversal through a collection of items, eg: lists, tuples  dictionaries
# implement 2 methods:
# __iter__() : returns the iterator object itself, making iterators iterable as well
# __next__()

# Iterables
# objects that can return an iterator.

s = "GFG"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))


# Creating an iterator
print("=========================================")
print("Creating an iterator")
class EvenNumbers:
    def __iter__(self):
        self.n = 2  # Start from the first even number
        return self

    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next even number
        return x

# Create an instance of EvenNumbers
even = EvenNumbers()
it = iter(even)

# Print the first five even numbers
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


print("=========================================")
print("StopIteration Exception")
li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break