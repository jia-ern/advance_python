print("fib_normal")
def fib_normal(n):
    print(f'Calculate Fibonacci of {n}')
    if n < 2:
        return 1
    return fib_normal(n-2) + fib_normal(n-1)

# ==================================================================================================================
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