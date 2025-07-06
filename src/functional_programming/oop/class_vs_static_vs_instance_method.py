print("===============================================")
print("classmethod")

class Example:
    class_state = "Active"

    @classmethod
    def modify_class_state(cls):
        cls.class_state = "Modified"
        return cls.class_state

print(Example.modify_class_state())


print("===============================================")
print("staticmethod")
class Example:
    @staticmethod
    def utility_function(x, y):
        return x + y

print(Example.utility_function(5, 3))  # Output: 8


print("===============================================")
print("Instance method")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 25)
print(person.greet())
