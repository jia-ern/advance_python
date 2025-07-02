# 5! = 5*4*3*2*1 = 120

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# ================  Direct Recursion ================

def decrement(n):
    print(n)
    if n == 0:
        return
    return decrement(n-1)

decrement(10)

# ================  Direct Recursion ================
print("===========================")
def decrement(n):
    if n <= 0:
        return
    print(n, end = " ")
    decrement1(n-1)

def decrement1(n):
    print(n, end=" ")
    decrement(n-1)

decrement1(10)

# ================  Fibonacci Recursion ================
print("\n===========================")

def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return (fibonacci(n-2)+fibonacci(n-1))

print(fibonacci(10))

# ================  Modify global ================

x = 10

def add():
    global x
    x = x + 20
    return x

print(x)
print(add())
print(x)