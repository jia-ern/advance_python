https://medium.com/@aoctut/python-attributes-682285d76f11

# 8 Handpicked Features Of Python — The Disguised Michigan

Type system [DIS]
1. Dynamically Typed: 
- Data types are changeable inside a piece of code.
2. Implicitly Typed: 
- Data types are automatically inferred.
3. Strongly Typed:
- Implicit, non-requested, conversion to an unrelated data type, i.e. numerical to and from textual is not allowed, e.g. in a comparison.

Interpreted
Python is interpreted, that is it acts as a interpreter of the program statements in the following way.
- It parses high-level language statements one by one.
- It stops if it finds an error and reports it and the containing statement.
- It translates each statement into a low-level language without creating an object or executable file.
- It directly executes each statement. This can take place in 1 of the following ways.
a. In an interactive shell, with immediate response per statement.
b. As a script, saved as a file and run as a whole program.

Multiparadigm
1. Imperative Paradigm
- mainly states the how rather than the what of execution

1.1 Plain imperative paradigm
The program contains >= 1 statements, that is instructions to Python.
The control flow consists of:
a. Sequences, that is ordered statements
b. Selections, that is if- elif- else blocks
c. Loops, that is repeatable blocks of statements, e.g. while, for.

2. Procedural Paradigm
It is an extension to the plain imperative paradigm.
The program contains >=1 functions.
A function contains >=1 statements and returns 0 / more values.

3. Object Oriented (OO) Paradigm
It is an extension to the procedural paradigm.
The program contains >=1 classes, where the following hold for a class.
a. It can act as a template to create-instantiate objects.
b. It allows object interaction.
c. It contains fields, resembling variables inside a class.
d. It contains methods, resembling functions inside a class.
e. It is connected with other classes with relationships,
e.g. hasa-composition, isa-inheritance.

```python
# plain imperative paradigm
# sequence
x = 1 # implicitly typed
x = "1" # dynamically typed
print("1")
print(x)

# selection
if x == 1: # strongly typed
 print("yes")
else:
 print("no")
# loop
# print all even numbers in the range 1–20
for i in range(2, 21, 2):
 print(i)

# procedural paradigm
def f(x):
 return x + 1
# the numerical 2 and 2.5, with implicit conversion, are accepted
# as function arguments, but the unrelated textual "2" is not
print(f(2.5))

# object oriented paradigm
class Human:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def say(self, msg):
  return self.name + "[" + str(self.age) + "]: " + msg + "\n"

omar = Human("omar", 30)
alex = Human("alex", 40)
hello_message = "Hello"
goodbye_message = "Goodbye"
print(omar.say(hello_message) + alex.say(hello_message) + omar.say(goodbye_message) + alex.say(goodbye_message))
```

4. Declarative Paradigm
States the what rather than the how of execution. The declarative paradigm can take the following forms.

5. Functional Paradigm
The program contains >= 1 functions.
A function appears as in the procedural paradigm but has the following differences.
a. It has a more abstract control flow.
b. It is usually applied on data collections,
e.g. lists, tuples.
The program 
- may contain comprehensions, following set-builder notation.
- may contain higher-order functions, e.g., filter, map, reduce.
- almost exclusively contains immutable variables avoiding the error-prone variable updating.
Pattern matching of same-name different-arguments functions mostly replaces selection.
Recursion replaces loops.

```python
# Lambda functions / Recursion
# Functional way of finding sum of a list 
import functools

mylist = [11, 22, 33, 44]

# Recursive Functional approach
def sum_the_list(mylist):
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + sum_the_list(mylist[1:])

# lambda function is used
print(functools.reduce(lambda x, y: x + y, mylist))
```

6. Logical Paradigm
The program contains >=1 predicates, where the following hold for a predicate.
a. It can be true or false.
b. It is defined with >=1 clauses, where the following hold for a clause.
- It is a logic expression.
- It is defined with 1 or more rules or facts.
- It belongs to the first-order or the higher-order logic.
c. It is usually applied on data collections.
There are immutable variables, pattern matching, and recursion as in the functional paradigm.

7. Event-Driven Paradigm
User / system initiated events define the control flow & the following hold.
It is usually combined with the imperative paradigm.
Events can take the following forms.
a. User actions.
b. Sensor inputs.
c. Messages from other programs.
There is an event detection loop.
- It usually includes a GUI.
- It includes a thread mechanism responding to events.
- It includes event handlers.

```python
import asyncio

async def foo():
    print("Foo")
    await asyncio.sleep(1)
    print("End Foo")

async def bar():
    print("Bar")
    await asyncio.sleep(2)
    print("End Bar")

loop = asyncio.get_event_loop()
task1 = loop.create_task(foo())
task2 = loop.create_task(bar())

loop.run_until_complete(asyncio.wait([task1, task2]))
```
