# Overloading is not supported in Python
# Python only recognizes the latest definition of the function

# Way to overcome
# ================ 1. Use variable arg ================
def add(datatype, *args):
    if datatype == 'int':
        res = 0
    elif datatype == 'str':
        res = ''

    for item in args:
        res += item

    print(res)

add('int', 5, 6)
add('str', 'Hello ', 'World')

print("================================================")
# ================ 2. Using Default Arguments (None as default value) ================
def add(a=None, b=None):
    if a is not None and b is None:
        print(a)
    else:
        print(a + b)

add(2, 3)
add(2)


print("================================================")
# ================ 3. Using Multiple Dispatch ================
from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)

@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)

product(2, 3)
product(2, 3, 2)
product(2.2, 3.4, 2.3)
