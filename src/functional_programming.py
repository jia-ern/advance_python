def function1(a, b) -> int: #function definition
    return a + b

print(function1(1, 1)) #function call 1

def function2():
    print(2+1)

a = function2
a()

# ========= default arguments on mutable datatypes =========
def add_item(name, employee_data=[]):
    employee_data.append(name)
    print("Updated employee list: ", employee_data)

add_item("Ali")
add_item("John")
add_item("Jake")

# Output:
# Updated employee list:  ['Ali']
# Updated employee list:  ['Ali', 'John']
# Updated employee list:  ['Ali', 'John', 'Jake']
# As list is mutable, it will update the default argument

# Fix
def add_item(name, employee_data=None):
    if not employee_data:
        employee_data = []
    employee_data.append(name)
    print("Updated employee list: ", employee_data)

add_item("Ali")
add_item("John")
add_item("Jake")

## ============ Variable length positional arguments must be in front of Variable length keyword arguments ===============
# def display(**nums, *num):
#     return sum(nums.values())
# print(display(n1=10,n2=20,n3=30,40,50))

# Output: SyntaxError: arguments cannot follow var-keyword argument

# Fix:
def display(*num, **nums):
    return sum(nums.values())
print(display(10,30,40,50,n2=20,n3=30))


# ========================== pass in function ==========================
def msg(name):
    return f"Hello, {name}!"

def fun1(fun2, name):
    return fun2(name)

# Passing the greet function as an argument
print(fun1(msg, "Bob"))

# ============== Returning Functions from Other Functions ==============
# 1. allows you to dynamically generate functions at runtime that are tailored to specific use cases or configurations.
def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

# Generate specific multiplier functions
double = multiplier(2)
triple = multiplier(3)

# Use the dynamically created functions
print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# 2. to build highly customizable code where the behavior of the returned function is based on configuration or parameters passed to the outer function.
def greeting(salutation):
    def greet(name):
        return f"{salutation}, {name}!"
    return greet

say_hello = greeting("Hello")
say_goodbye = greeting("Goodbye")

print(say_hello("John"))  # Output: "Hello, John!"
print(say_goodbye("John"))  # Output: "Goodbye, John!"

#3. foundation of decorators, allowing you to wrap another function dynamically while adding additional behavior.
# When to Use:
# When you want to modify or extend the behavior of a function without modifying its code directly.
# Common in logging, access control (authentication/authorization), or memoization.
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@logger  # Equivalent to `add = logger(add)`
def add(a, b):
    return a + b

print(add(3, 5))
# Output:
# Calling add with (3, 5) and {}
# Result: 8
# 8

# 4. Currying
# When to Use:
# When you're working on functional paradigms, such as currying, partial function application, or higher-order functions.
# To make functions reusable and composable.

def curried_add(a):
    return lambda b: a + b

add_5 = curried_add(5)
print(add_5(10))  # Output: 15

# ========= Storing Functions in Data Structures =========
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# Storing functions in a dictionary
d = {
    "add": add,
    "subtract": subtract
}

# Calling functions from the dictionary
print(d["add"](5, 3))
print(d["subtract"](5, 3))

