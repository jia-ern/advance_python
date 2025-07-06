# Programming paradigm
- ways of organizing programs
- approach to solve the problem using some programming language 
- method to solve a problem using tools and techniques that are available to us following some approach

## Type of paradigms
- Procedural oriented
- Functional oriented
- Object-oriented

## Procedural oriented
- series of computational steps are divided modules which means that the code is grouped in functions 
- code is serially executed step by step
- combines the serial code to instruct a computer with each step to perform a certain task. 
- Use Cases:
  - helps in the modularity of code and modularization is usually done by the functional implementation. 
  - helps in an easy organization related items without difficulty and so each file acts as a container. 
- Advantages
  - General-purpose programming
  - Code reusability
  - Portable source code
- Disadvantages
  - Data protection
  - Not suitable for real-world objects
  - Harder to write

```python
# Procedural way of finding sum of a list 

mylist = [10, 20, 30, 40]

# modularization is done by functional approach
def sum_the_list(mylist):
    res = 0
    for val in mylist:
        res += val
    return res

print(sum_the_list(mylist))
```

## Functional oriented
- a paradigm in which everything is bind in pure mathematical functions style. 
- aka. declarative paradigms: uses declarations overstatements. 
- uses the mathematical function and treats every statement as functional expression as an expression is executed to produce a value. 
- Lambda functions or Recursion are basic approaches used for its implementation. 
- mainly focus on "what to solve" rather than "how to solve". 
- to treat functions as values and pass them as an argument make the code more readable & understandable. 
- Advantages
  - Simple to understand 
  - Making debugging and testing easier 
  - Enhances the comprehension and readability of the code
- Disadvantages 
  - Low performance
  - Writing programs is a daunting task
  - Low readability of the code

```python
# Functional way of finding sum of a list 
import functools

mylist = [11, 22, 33, 44]

# Recursive Functional approach
def sum_the_list(mylist):
    
    if len(mylist) == 1:
        return mylist[0]
    else:
        return mylist[0] + sum_the_list(mylist[1:])

print(functools.reduce(lambda x, y: x + y, mylist))
```

## Object-oriented
- objects are the key element of paradigms. 
- Objects = instance of a class that contains both data members & method functions. 
- Each object has 2 properties
  - attributes
  - behaviours / methods
- relates data members & methods functions that support encapsulation and with the help of the concept of an inheritance
- Advantages
  - Relation with Real world entities
  - Code reusability
  - Abstraction or data hiding
- Disadvantages
  - Data protection
  - Not suitable for all types of problems
  - Slow Speed
- EG: features:
  - Inheritance
  - Encapsulation
  - Abstraction

```python
class Emp:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print("Hello, % s. You are % s old." % (self.name, self.age))

# Objects of class Emp has been made here        
Emps = [Emp("John", 43),
    Emp("Hilbert", 16),
    Emp("Alice", 30)]

# Objects of class Emp has been used here
for emp in Emps:
    emp.info()
```

## Procedural vs Functional Programming
| Aspect | Procedural Programming | Functional Programming |
| :-- | :-- | :-- |
| Focus | Focuses on procedures (step-by-step execution). | Focuses on functions (composition and immutability). |
| State | Uses mutable state and shared variables. | Avoids mutable state; prefers immutability and pure functions. |
| Side Effects | Side effects are common (e.g., modifying global variables). | Almost no side effects (functions are "pure"). |
| Control Flow | Uses loops and conditionals to control execution. | Uses recursion and function composition instead of loops. |
| Reusability | Functions often depend on global state, making reusability harder. | Highly reusable and modular functions due to lack of dependence on external state. |
| Concurrency | Difficult due to shared mutable state, requiring locks or synchronization. | Easier, as lack of mutable state avoids race conditions. |
| Example Languages | C, Pascal, Fortran, BASIC. | Haskell, Lisp, Clojure, F#. |


## OOPs Concepts in Python
- Class in Python
- Objects in Python 
- Polymorphism in Python 
- Encapsulation in Python 
- Inheritance in Python 
- Data Abstraction in Python

### Class
- a collection of objects
- a template / blueprint for creating objects
- every object belong to some class

#### Built-in class function
- getattr(dog1, 'name')
- setattr(dog1, 'name', 'modified_name')
- delattr(dog1, 'name')

#### Built-in class attributes
-  key features that enable developers to provide important information about classes and their models
- EG:
  - __dict__: dictionary containing class namespace
  - __doc__: class documentation string
  - __name__: class name
  - __module__: module name in which class is defined
  - __bases__: list of base classes

#### Static method vs Class Method
| Aspect | Class Method | Static Method |
| :-- | :-- | :-- |
| First Parameter | Takes cls as the first parameter, representing the class itself. | Does not take any special first parameter. |
| Access to Class State | Can access or modify the class state (class variables). | Cannot access or modify the class state. |
| Relationship with Class | Closely tied to the class, often used for operations related to the class. | Independent of the class or instance, used for utility tasks. |
| Purpose | Used when the method needs to interact with the class itself or its state. | Utility-type methods that operate independently of class state. |
| Decorator Used | @classmethod | @staticmethod |
| Callable From | Callable both from the class and from instances. | Callable both from the class and from instances. |


#### Static method vs Instance Method
| Aspect | Static Method | Function Inside Class (Instance Method) |
| :-- | :-- | :-- |
| Decorator | Defined with @staticmethod. | No decorator. Defined as a regular method inside the class. |
| First Parameter | Does not require self or cls as the first parameter. | Requires self as the first parameter to refer to the instance. |
| Access to Instance Data | Cannot access or modify instance attributes (self). | Can access and modify instance attributes (self) tied to the object. |
| Access to Class State | Cannot access or modify class attributes (cls). | By default, cannot directly interact with class attributes unless explicitly called via the class. |
| Purpose | Utility-type method that is related to the class but operates independently. | Methods designed to operate on individual instances and their data. |
| Relationship to Class/Instance | Independent of both the instance and the class; does not need state. | Tied to an instance of the class and requires instance-specific context. |
| Callable From | Callable directly through the class or an instance. | Callable only on an instance, where self refers to that instance. |


## __new__ vs __init__ method
| Aspect | __new__ Method | __init__ Method |
| :-- | :-- | :-- |
| Purpose | Responsible for creating a new instance of the class. | Responsible for initializing the newly created object. |
| When It Is Called | Called before the object is created (allocates memory). | Called after the object is created (sets up instance state). |
| Return Value | Must explicitly return the newly created instance (usually via super().__new__(cls)). | Does not return anything (None by default). |
| First Argument | Takes cls (the class itself) as the first argument. | Takes self (the instance) as the first argument. |
| Usage | Used mainly when subclassing immutable objects (like str, int, tuple) or customizing object creation logic. | Commonly used to set or initialize object attributes. |
| Interactions | Determines if an object will even get created. Without a valid instance, __init__ may never be called. | Only works on objects that are successfully created by __new__. |
| Example Use Cases | - Singleton pattern - Immutable objects (e.g., custom str or tuple subclasses) - Metaprogramming | - Setting up instance variables (e.g., self.name, self.age) - General initialization logic |
| Default Implementation | The base implementation of __new__ is provided by the object class (usually sufficient unless overridden). | The base implementation does nothing if not explicitly overridden in the class. |


#### __init_subclass__ method
- enforcing constraint on subclass
- a special class method in Python that gets called automatically when a new subclass is created. 
- defined in the parent class and is used to configure, validate, or modify the creation of subclasses. 
- it allows a parent class to control or influence the behavior of its children upon subclass definition


#### Metaclass
- need fine-grained control over class creation or want to enforce certain patterns or behaviors across multiple classes
- Use case: Enforcing Coding Standards
  - Naming Convention Meta Class: must start with Upper case
  - DocstringMeta class enforces the presence of docstrings for all methods
  - Limiting the Number of Methods
  - Deprecating Methods
  - Applying the Singleton Design Pattern


#### Metaclass vs __init_subclass__
| Aspect | Metaclass | __init_subclass__ |
| :-- | :-- | :-- |
| Purpose | Customizes class creation (the creation of the class itself, not its instances). | Called when a subclass of a parent class is defined. Focuses on subclass customization. |
| Definition | Defined by setting the metaclass attribute of a class (class Base(metaclass=Meta):). | A method defined in the parent class (class Parent:). |
| Scope | Operates at the class level — it affects the creation of the class itself and all its descendants. | Operates at the subclass level — only works on immediate child classes of the parent class. |
| When It Is Triggered | Called during class creation (when the class object is being created). | Called during subclass definition (when a new subclass is derived from the parent class). |
| Custom Behavior | Can modify the entire class object (its methods, attributes, etc.) during its creation. | Allows validation, registration, or configuration of child classes but does not modify the class itself. |
| Complexity | More flexible but also more complex. Requires experience with custom metaclasses. | Easier to use than metaclasses and suitable for most subclass-related use cases. |
| Use Cases | - Frameworks<br>- Customizing class creation<br>- Advanced object model manipulation | - Validating or enforcing subclass behavior<br>- Automatically configuring subclasses |
| Inheritance Control | Can control and modify how all classes (and their children) in its hierarchy behave. | Limited to directly influencing the immediate subclasses of the parent class where it is defined. |
| Implementation | Requires the definition of a separate metaclass object (usually by inheriting type). | Defined as a method directly in the parent class. |
| Custom Syntax | Mostly involves overriding the __new__ or __init__ methods of the metaclass. | Override __init_subclass__ in the parent class. |


## Types of Constructors
- Default Constructor
  - does not take any parameters other than self. It initializes the object with default attribute values.
```python
class Car:
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020
```
- Parameterized Constructor
  - accepts arguments to initialize the object's attributes with specific values.
```python
class Car:
    def __init__(self, make, model, year):
      
        #Initialize the Car with specific attributes.
        self.make = make
        self.model = model
        self.year = year
```

#### Packing Arguments
- *args 
- **kwargs

#### Unpacking Arguments
- allows values from an iterable (list, tuple, or dictionary) to be passed as separate arguments to a function.
```python
def addition(a, b, c):
    return a + b + c

num = (1, 5, 10)  
result = addition(*num) 
print("Sum:", result)
```

```python
def info(name, age, country):
    print(f"Name: {name}, Age: {age}, Country: {country}")

data = {"name": "geeks for geeks", "age": 30, "country": "India"}
info(**data)
```

#### *args (Non-Keyword Arguments)
- Packs multiple positional arguments into a tuple.
```python
def sample(*args):
    print("Packed arguments:", args)

sample(1, 2, 3, 4, "geeks for geeks")
```

#### **kwargs (Keyword Arguments)
- Packs multiple keyword arguments into a dictionary.
```python
def sample(**kwargs):
    print("Packed keyword arguments:", kwargs)

sample(name="Anaya", age=25, country="India")
```


## Dynamic attributes 
- for attributes that are defined at runtime, after creating the objects or instances.


## method vs function
| Aspect | Method | Function |
| :-- | :-- | :-- |
| Definition | A method is a function that is bound to an object (e.g., a class instance or class itself). | A function is a standalone block of code that performs a specific task. |
| Association | Belongs to an object or class. | Independent and not associated with any object or class. |
| Call Syntax | object.method(arguments) | function(arguments) |
| Arguments | Instance methods take self as the first parameter (or cls for class methods). | Functions only take explicitly passed arguments. |
| Type | Defined as part of a class (using def inside a class body). | Defined globally or locally (outside any class context). |
| Binding | Bound to an object (instance or class) and can access its attributes and methods. | Not bound to any object; operates independently. |
| Use Case | Operate on or with objects' data (e.g., accessing instance or class members). | Perform standalone tasks or computations independent of the object. |
| Decorator Usages | Can be enhanced with decorators like @staticmethod or @classmethod. | Can use any decorator, not specific to object-oriented programming. |
| Scope of Availability | Available only through the class or an instance of the class. | Can be called from anywhere (if it’s in scope or imported). |
| Key Use | To describe behavior or actions that objects can take. | To encapsulate reusable logic or functionality without dependency on any object. |
| Examples | Instance methods, class methods, and static methods in Python classes. | Regular functions (standalone) such as print() or user-defined global functions. |


### Python Inheritance
- allows a class (child class) to acquire properties & methods of another class (parent class). 
- supports hierarchical classification and promotes code reuse.
- Types of Inheritance:
  - Single Inheritance: A child class inherits from a single parent class.
  - Multiple Inheritance: A child class inherits from more than one parent class.
  - Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another class.
  - Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
  - Hybrid Inheritance: A combination of two or more types of inheritance.


### Python Polymorphism
- allows methods to have the same name 
- but behave differently based on the object's context. 
- can be achieved through method overriding / overloading.
- Types of Polymorphism
  - Compile-Time Polymorphism: 
    - determined during the compilation of the program. 
    - allows methods / operators with the same name to behave differently based on their input parameters or usage. 
    - referred to as method / operator overloading.
  - Run-Time Polymorphism: 
    - determined during the execution of the program. 
    - occurs when a subclass provides a specific implementation for a method already defined in its parent class
    - known as method overriding.


### Encapsulation
- bundling of data (attributes) & methods (functions) within a class
- restricting access to some components to control interactions.
- EG: A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.
- Types of Encapsulation:
  - Public Members: Accessible from anywhere.
  - Protected Members: Accessible within the class and its subclasses.
  - Private Members: Accessible only within the class.


### Data Abstraction 
- Abstraction hides internal implementation details while exposing only the necessary functionality. 
- helps focus on "what to do" rather than "how to do it."
- Types of Abstraction:
  - Partial Abstraction: Abstract class contains both abstract & concrete methods.
    - Abstract: 
      - @abstractmethod decorator
      - cannot be instantiated directly 
      - any subclass must implement this method to be instantiated.
    - Concrete:
      - methods that have full implementations in an abstract class
      - can be used directly
Concrete Subclass: Dog is a subclass of Animal that provides an implementation for the sound() method. This allows the Dog class to be instantiated and used.
  - Full Abstraction: Abstract class contains only abstract methods (like interfaces).
