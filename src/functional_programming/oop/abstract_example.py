"""
This module provides an overview of abstract classes and methods in Python using the `abc` module.

It includes functions for:
- Defining an abstract class with abstract and concrete methods.

Example usage:
>>> from abstract_example import Dog, Labrador, Beagle
>>> labrador = Labrador("Buddy")
>>> labrador.display_name()
Dog's Name: Buddy
>>> labrador.sound()
Labrador Woof!
"""

from abc import ABC, abstractmethod


class Dog(ABC):  # Abstract Class
    """
    Dog is an abstract class that represents a generic dog.

    This class provides an abstract method `sound` that must be implemented by any subclass,
    as well as a concrete method `display_name` to display the dog's name.

    Attributes:
        name (str): The name associated with the instance of Dog.
    """
    def __init__(self, name):
        self._name = name # Protected Attribute

    @abstractmethod
    def sound(self):  # Abstract Method
        """An abstract method that must be implemented by subclasses to define the dog's sound."""
        raise NotImplementedError

    def display_name(self):  # Concrete Method
        """An concrete method that displays the dog's name."""
        print(f"Dog's Name: {self._name}")


class Labrador(Dog):  # Partial Abstraction
    """
    Labrador is a subclass of Dog that represents a specific breed.

    This class overrides the abstract method `sound` to provide a specific implementation.

    Attributes: None
    """
    def sound(self):
        print("Labrador Woof!")


class Beagle(Dog):  # Partial Abstraction
    """
    Beagle is a subclass of Dog that represents a specific breed.

    This class overrides the abstract method `sound` to provide a specific implementation.

    Attributes: None
    """
    def sound(self):
        print("Beagle Bark!")


dogs = [Labrador("Buddy"), Beagle("Charlie")]
for dog in dogs:
    dog.display_name()  # Calls concrete method
    dog.sound()  # Calls implemented abstract method

# Output:
# Dog's Name: Buddy
# Labrador Woof!
# Dog's Name: Charlie
# Beagle Bark!
