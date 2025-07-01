# What is a function
- an object
- an organized block of reusable code
- can be called any number of times
- contains a set of instructions which perform specific tasks.

## Type of functions
- Build-in
- Eg: len()
- User defined

# Scope
- region of the code where an identifier can be accessed

## Identifier
- a name using which we can identify a particular object.

### Type of Identifier
- Local
- Global
- Non-local
- Built-in

## Nested function
- a function defined inside another function

## Parameters
- variable for holding actual values
- present in function definition

## Arguments:
- values provided at function call


### Type of Arguments
- Positional arguments
- Keyword arguments
- Default arguments
- Variable length arguments

#### Positional arguments
`def display(name, age):
    print(f"name is {name} and age is {age}")`

#### Keyword arguments
`def display(name, age):
    print(f"name is {name} and age is {age}")`
`display(name='Jake', age=3)`

#### Default arguments
`def display(name, age=3):
    print(f"name is {name} and age is {age}")`
`display(name='Jake')`

#### Variable length positional arguments
`def display(*name):
    print(f"name is {name}")`
`display('Jake', 'Ali', 'Abu')`

#### Variable length keyword arguments
`def display(**nums):
    return sum(nums.values())
`print(display(n1=10,n2=20,n3=30))`

# Lambda function
- syntax: lambda arg_list: expression/python statement
- used as parameters for functions that accepts functions as parameters
- mostly used in high order functions
- useful for small expression and less code required
- useful when we use filter(), map(), reduce()

# First class objects
- instance of some class
- can be stored in data structures
- can be assigned to var
- can perform operations on these obj
- can be passed as arguments to functions
- can be returned as value from function

# Returning Functions from Other Functions
- allows you to dynamically generate functions at runtime that are tailored to specific use cases or configurations.
- to build highly customizable code where the behavior of the returned function is based on configuration or parameters passed to the outer function.
- foundation of decorators, allowing you to wrap another function dynamically while adding additional behavior.
- Currying

# High Order function
- function which operated on other function
  - contains other functions as param
  - returns a function as output
