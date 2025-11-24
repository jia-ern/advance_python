class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # compare two objects by their values.
    def __eq__(self, other):
        return self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

    def __lt__(self, other):
        return self.age < other.age

    # __str__ method returns a string representation of an object that is human-readable
    def __str__(self):
        return f'Person({self.first_name},{self.last_name},{self.age})'

    # __repr__ method returns a string representation of an object that is machine-readable
    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

john = Person('John', 'Doe', 25)
jane = Person('Jane', 'Doe', 25)
older = Person('Jane', 'Doe', 27)
younger = Person('Jane', 'Doe', 21)

print(john == jane)
print(john < older)
print(john > younger)

print("__str__: ", john)
print("__repr__: ", repr(john))

