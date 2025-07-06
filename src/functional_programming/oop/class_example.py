class Dog:
    """This is a class for Dogs"""
    species = "Canine"  # Class attribute

    # __init__ method:
    # constructor, auto called when a new object is created. initializes the attributes of the class.
    # self:
    # represents the current instance of the class.
    # ensures that when you call __init__, it operates on the specific object being created or manipulated
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

dog1 = Dog("Buddy", 3)  # Create an instance of Dog
dog2 = Dog("Charlie", 5)  # Create another instance of Dog

print(dog1.name, dog1.age, dog1.species)  # Access instance and class attributes
print(dog2.name, dog2.age, dog2.species)  # Access instance and class attributes
print(Dog.species)  # Access class attribute directly

# Modify instance variables
dog1.name = "Max"
print("Modified name:", dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print("Modified species:", dog1.species)  # (Updated class variable)
print(dog2.species)


# Built-in class function
print("=======================================")
print("Built-in class function: ")
print(getattr(dog1, 'name'))
setattr(dog1, 'name', 'modified_name')
print("Modified dog1:", dog1.__dict__)
delattr(dog1, 'name')
print("Deleted name of dog1:", dog1.__dict__)
print("hasattr dog1 name: ", hasattr(dog1, 'name'))


# Built-in class attribute
print("=======================================")
print("Built-in class attribute: ")
print(Dog.__doc__)
print(Dog.__name__)
print(Dog.__module__)
print(Dog.__bases__)
print(Dog.__dict__)


# __new__ Method vs __init__ method
# creating a new instance of a class. It allocates memory and returns the new object.
# Rarely overridden but useful for customizing object creation and especially in singleton or immutable objects.
print("================================================")
print("Non_Singleton: __new__ vs __init__ method")
class Non_Singleton:
    def __init__(self, value):
        print("__init__ called")
        self.value = value
        print(self.value)

obj1= Non_Singleton(42)
obj2 = Non_Singleton(43)


print("================================================")
print("Singleton: __new__ vs __init__ method")
class Singleton:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.value = args[0]  # if this was done in __init__ both would be 43 because __init__ still runs
        return cls.instance

a = Singleton(42); b = Singleton(43)
print(a is b)
print(a.value); print(b.value)


print("================================================")
print("__init_subclass__ method: ")
class Parent:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs) # Call base implementation
        print(f"Initializing subclass: {cls.__name__}")
        if not hasattr(cls, "required_method"):
                raise TypeError(f"{cls.__name__} must define 'required_method'.")

class ValidChild(Parent):
    def required_method(self):
        pass

# class InvalidChild(Parent):  # Raises TypeError
#     pass


print("================================================")
print("Metaclass method: ")
class Meta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Initializing subclass: {cls.__name__}")
        # Modify the class during its creation
        if "my_method" not in class_dict:
            raise TypeError(f"{name} must define 'my_method' method")
        return super().__new__(cls, name, bases, class_dict)

# Using the metaclass
class Base(metaclass=Meta):
    def my_method(self):  # This must be defined; otherwise, TypeError is raised
        pass

class ValidChild(Base):
    def my_method(self):  # Satisfies the metaclass condition
        print("Valid method implementation.")

# class InvalidChild(Base):  # Raises TypeError because `my_method` is missing
#     pass


print("================================================")
print("Dynamic attributes: ")
class GFG:
    employee = True

# Driver Code
e1 = GFG()
e2 = GFG()

e1.employee = False
e2.name = "Nikhil"

print(e1.employee)
print(e2.employee)
print(e2.name)

# this will raise an error as name is a dynamic attribute created only for the e2 object
# AttributeError: 'GFG' object has no attribute 'name'
# print(e1.name)
