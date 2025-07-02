# Simple Exception Handling Example
import sys

print("=============================================")
print("ZeroDivisionError Exception Handling")
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Can't be divided by zero!")

# Check which exception comes first
print("=============================================")
print("Check which exception comes first")
n = 10
try:
    res = n / 0  # This will raise a ZeroDivisionError
except Exception as var:
    print(sys.exc_info()[0]) # <class 'ZeroDivisionError'>
    print(sys.exc_info()[1]) # division by zero
    # or
    print(var.__class__)


# complete exception
print("=============================================")
print("Complete exception")
try:
    n = 0
    res = 100 / n
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print("Result is", res)
finally:
    print("Execution complete.")

# catch exception
print("=============================================")
print("Catch exception")
try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x
except ValueError:
    print("Not Valid!")
except ZeroDivisionError:
    print("Zero has no inverse!")


# raise exception
print("=============================================")
print("Raise exception")
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)


# User defined exception
print("=============================================")
print("User defined exception")

class FiveDivisionError(Exception):
    "this is exception class called when five division error happens"
    def __init__(self):
        print("cannot divide by five")
    pass

try:
    num = 14
    divider = 0
    if divider == 5:
        raise FiveDivisionError
    div=num/divider
    print("Division: ", div)
except (FiveDivisionError, ZeroDivisionError) as var:
    print(var)


# Excepthook
print("=============================================")
print("Excepthook")
def format_traceback(exc_type, exc_value, exc_traceback):
    print(exc_type)
    print(exc_value)
    print(exc_traceback)

sys.excepthook=format_traceback

def display():
    print(1+"hello")

display()