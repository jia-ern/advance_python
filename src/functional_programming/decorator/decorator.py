# Decorator
# functions which takes other functions as input, add additional functionalities and returns it
# a callable python obj which modifies other functions / oop

# =========== 1. A simple decorator function ===========
print("=================================================")
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper adds functionality before the original function.")
        original_function()
        print("Wrapper adds functionality after the original function.")
    return wrapper_function

# Target Function
def say_hello():
    print("Hello!")

# Manually applying the decorator
decorated_function = decorator_function(say_hello)
decorated_function()

# =========== 2. Decorator Syntax sugar @ ===========
print("=================================================")
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper adds functionality before the original function.")
        original_function()
        print("Wrapper adds functionality after the original function.")
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

# =========== 3. Use case 1: Logging ===========
print("=================================================")
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} executed successfully")
        return result
    return wrapper

@logging_decorator
def add(a, b):
    return a + b

print(add(5, 3))
# Output:
# Calling function: add
# Function add executed successfully
# 8

# =========== 4. Use case 2: Input Validation ===========
print("=================================================")
def validate_inputs(func):
    def wrapper(a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both inputs must be integers")
        return func(a, b)
    return wrapper

@validate_inputs
def multiply(a, b):
    return a * b

print(multiply(4, 5))  # Output: 20
# print(multiply("4", 5))  # Raises ValueError: Both inputs must be integers

# =========== 5. Use case 3: Authorization ===========
print("=================================================")
def authorize(func):
    def wrapper(user):
        if user != "admin":
            raise PermissionError("Unauthorized user")
        return func(user)
    return wrapper

@authorize
def access_dashboard(user):
    return f"Welcome, {user}!"

print(access_dashboard("admin"))  # Output: Welcome, admin!
# print(access_dashboard("guest"))  # Raises PermissionError: Unauthorized user

# =========== 6. Use case 4: Tracking Execution Time ===========
print("=================================================")
import time

def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_execution
def slow_function():
    time.sleep(2)
    print("Slow function executed!")

slow_function()
# Output:
# Slow function executed!
# slow_function took 2.0000 seconds

# =========== 7. Use case 5: Automatically Apply Behavior to Classes ===========
print("=================================================")
def add_greeting(cls):
    class ModifiedClass(cls):
        def greet(self):
            return f"Hello, {self.name}!"
    return ModifiedClass

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
print(person.greet())  # Output: Hello, Alice!

# =========== 8. Use case 6: Chaining Multiple Decorators ===========
# Applied bottom-to-top; greet -> decorator_two -> decorator_one
# When multiple decorators are applied to a function, they are executed in the reverse order of their appearance.
print("=================================================")

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()
# Output:
# Decorator One
# Decorator Two
# Hello!

# =========== 9. Handling Decorated Functions (functools.wraps) ===========
# When a decorator wraps a function, details like the function's name, docstring, signature are replaced by those of the wrapper function.
# To preserve the original function's metadata, use functools.wraps.
print("=================================================")

from functools import wraps

def decorator_function(func):
    @wraps(func)  # Preserve original metadata
    def wrapper(*args, **kwargs):
        print("Wrapper adds functionality")
        return func(*args, **kwargs)
    return wrapper

@decorator_function
def say_hello():
    """This function prints hello."""
    print("Hello!")

print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)   # Output: This function prints hello.

# =========== 10. Parameterized Decorators ===========
print("=================================================")
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
# Output:
# Hello!
# Hello!
# Hello!
