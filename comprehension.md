# What is a comprehension
- a way of writing compact code in python.

## Type of comprehension
- list
- set
- dict

## List comprehension
- Syntax 1: [expression for var in list]
- Syntax 2: [expression for var in iterable if condition1]
- Syntax 3: [expression for var in iterable if condition1 else condition2]
- Syntax 4: [expression if condition1 else expression for var in iterable]
- Syntax 5: [expression for var in iterable1 for j in iterable2]
- if-elif-else in List Comprehension: [expression for var in iterable if condition1]

## Dict comprehension
- Syntax: {key: value for (key, value) in iterable}
- EG: {num:num**2 for num in range(1, 5)}
- Output: {1:1,2:4,3:9,4:16,5:25}

## Set comprehension
- Syntax: {expression for var in iterable}

