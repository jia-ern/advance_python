print("=========================================")
print("Single, Multilevel, Multiple Inheritance")
# Single Inheritance
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

print("Single Inheritance: ")
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

print("Multilevel Inheritance: ")
guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

print("Multiple Inheritance: ")
retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()


print("=========================================")
print("Super for Single, Inheritance")
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent's constructor first
        self.age = age

parent = Parent("Alice")
child = Child("Bob", 12)

print("Parent:", parent.name)
print("Child:", child.name, child.age)


print("=========================================")
print("Super for Multilevel Inheritance")
class Grandparent:
    def __init__(self, name):
        self.name = name

class Parent(Grandparent):
    def __init__(self, name, age):
        super().__init__(name)  # Call grandparent's constructor
        self.age = age

class Child(Parent):
    def __init__(self, name, age, hobby):
        super().__init__(name, age)  # Call parent's constructor
        self.hobby = hobby

child = Child("Charlie", 8, "reading")
print("Child:", child.name, child.age, child.hobby)


print("=========================================")
print("Super for Multiple Inheritance")
class Base1:
    def __init__(self, x):
        self.x = x

class Base2:
    def __init__(self, y):
        self.y = y

class Derived(Base1, Base2):
    def __init__(self, x, y, z):
        super().__init__(x)  # Call first base class constructor
        # Call second base class constructor explicitly
        Base2.__init__(self, y)
        self.z = z

derived = Derived(1, 2, 3)
print("Derived:", derived.x, derived.y, derived.z)
