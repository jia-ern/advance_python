# callable() function
# a built-in function
# to check if an object is callable in Python i.e., it can be called like a function.
# returns True if the object can be called and False if not.

print("==================================")
print("When Function is callable")
x = 10
print(callable(x))

def geeks(x):
    return (x)
y = geeks
print(callable(y))

# Python program to illustrate callable()
print("==================================")
print("When Object is callable")
class Geek:
    def __call__(self):
        print('Hello GeeksforGeeks')

print(callable(Geek))

GeekObject = Geek()
GeekObject()

# When Object is NOT callable
print("==================================")
print("When Object is NOT callable")
# Python program to illustrate callable()
class Geek:
  def testFunc(self):
    print('Hello GeeksforGeeks')

# Suggests that the Geek class is callable
print(callable(Geek))

GeekObject = Geek()
# The object will be created but returns an error on calling
# GeekObject()
