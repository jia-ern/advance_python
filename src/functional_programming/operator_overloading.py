# Operator Overloading
# giving extended meaning beyond their predefined operational meaning.
# same built-in operator or function shows different behavior for objects of different classes

# EG: operator + is used to add two integers as well as join two strings and merge two lists.
# achievable because '+' operator is overloaded by int oop and str oop.
print(1 + 2)

# concatenate two strings
print("Hello "+"World")

# Product two numbers
print(3 * 4)

# Repeat the String
print("Hello"*4)


print("=======================================================")
# 1. ================ overload function ================
# Python Program illustrate how
# to overload an binary + operator
# And how it actually works

class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2))
print(A.__add__(ob3,ob4))
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

# special function "__add__( )"
# when the objects ob1 and ob2 are coded as "ob1 + ob2",
# special function is automatically called as ob1.__add__(ob2)
# means that ob1 calls the __add__( ) function with ob2 as an Argument
# means A .__add__(ob1, ob2).
# When the Binary operator is overloaded, the object before operator calls respective func with object after operator as parameter.
