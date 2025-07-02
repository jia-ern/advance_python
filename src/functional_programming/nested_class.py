# Nested class
# aka. inner class
# class declared inisde another class

# Benefits of Nested Classes
# Encapsulation: Inner classes can help to hide implementation details from external code.
# Organization: Groups related logic inside a single conceptual object.
# Clarity: Highlights tight coupling between classes, making dependencies explicit.
# Locality: Keeps code that is closely related in one place, improving readability.

# Drawbacks of Using Nested Classes
# Reduced Reusability: Nested classes cannot be accessed directly unless done explicitly via the outer class.
# Can Cause Confusion: Deeply nested classes or long chains of dependencies may make code harder to follow.
# Harder Testing: If you need to test nested classes individually, it can complicate unit testing.


# ============ 1. To Group Helper Functionality ============
# When an inner class logically belongs to the functionality of the outer class and is meant to provide helpers
# can make it a nested class.

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

    def add_employee(self, name, position):
        self.employees.append(self.Employee(name, position))

    def show_employees(self):
        print(f"Department: {self.name}")
        for employee in self.employees:
            print(f"- {employee.name}, {employee.position}")

# Usage
department = Department("HR")
department.add_employee("Alice", "Manager")
department.add_employee("Bob", "Recruiter")
department.show_employees()


print("=====================================================")
# ============ 2. When an Inner Class Should Not Be Exposed Globally ============
# If a class is only relevant to its enclosing class and is unlikely to be used elsewhere,
# can define it as a nested class.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = self.Engine()

    class Engine:
        def __init__(self):
            self.horsepower = 200
            self.type = "Inline-4"

    def show_details(self):
        print(f"Car: {self.make} {self.model}, Engine: {self.engine.horsepower}HP, {self.engine.type}")

car = Car("Toyota", "Corolla")
car.show_details()


print("=====================================================")
# ============ 3. Encapsulation and Information Hiding ============
class Database:
    def __init__(self):
        self._cursor = self._Cursor()

    class _Cursor:
        def execute(self, query):
            print(f"Executing query: {query}")

    def run_query(self, query):
        self._cursor.execute(query)

db = Database()
db.run_query("SELECT * FROM users")


print("=====================================================")
# ============ 4. To Define Hierarchical Relationships ============
class University:
    def __init__(self, name):
        self.name = name

    class Department:
        def __init__(self, name):
            self.name = name
            self.students = []

        class Student:
            def __init__(self, name, id):
                self.name = name
                self.id = id

        def add_student(self, name, id):
            self.students.append(self.Student(name, id))

        def show_students(self):
            print(f"Department: {self.name}")
            for student in self.students:
                print(f"- {student.name}, ID: {student.id}")

# Usage
cs = University.Department("Computer Science")
cs.add_student("Alice", "1001")
cs.add_student("Bob", "1002")
cs.show_students()
