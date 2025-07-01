import functools

nums = [1, 2, 3, 4, 5]
total = 0

def sum_nums(num1, num2):
    return num1 + num2

reduced_value = functools.reduce(sum_nums, nums)

print(reduced_value)