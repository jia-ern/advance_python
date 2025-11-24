

print("fib_normal")
def fib_normal(n):
    print(f'Calculate Fibonacci of {n}')
    if n < 2:
        return 1
    return fib_normal(n-2) + fib_normal(n-1)

fib_normal(5)

# ==================================================================================================================
print("===========================================================")
print("fib_with_cache")
# lru_cache
# to cache the result of a function.
# When you pass same argument to the function, function just gets the result from the cache instead of recalculating it.

from functools import lru_cache

@lru_cache
def fib_with_cache(n):
    print(f'Calculate the Fibonacci of {n}')
    if n < 2:
        return 1
    return fib_with_cache(n-2) + fib_with_cache(n-1)

fib_with_cache(5)

# ==================================================================================================================
print("===========================================================")
print("fib_with_sequence")
from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)

    @staticmethod
    @lru_cache(2**16)
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n-2) + Fibonacci.fib(n-1)

fibonacci = Fibonacci(6)

print('Accessing Fibonacci sequence using []:')
print(fibonacci[0])
print(fibonacci[1])
print(fibonacci[2])

print('Accessing Fibonacci sequence using for loop:')
for f in fibonacci:
    print(f)
