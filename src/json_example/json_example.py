import json

# Parse JSON String - Convert from JSON to Python object
print("=========================================")
print("Parse JSON String")

# JSON string
emp = '{"id":"09", "name": "Nitin", "department":"Finance"}'
print("This is JSON", type(emp))

# Convert string to Python dict
d = json.loads(emp)
print("Converted to Python", type(d))
print(d)


# Convert from Python object to JSON
print("=========================================")
print("Convert from Python object to JSON")
# Python dict
d = {'id': '09', 'name': 'Nitin', 'department': 'Finance'}
print("This is Python", type(d))

# Convert Python dict to JSON
obj = json.dumps(d, indent=4)
print("Converted to JSON", type(obj))
print(obj)


# Writing JSON to a file in Python
print("=========================================")
print("Writing JSON to a file in Python")
dictionary = {
    "emp_details": [
        {
            "name": "sathiyajith",
            "rollno": 56,
            "cgpa": 8.6,
            "phonenumber": "9976770500"
        }
    ]
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)


# Python read JSON file
print("=========================================")
print("Python read JSON file")
f = open('sample.json', )

data = json.load(f)

for i in data['emp_details']:
    print(i)
    print(i["name"], i["rollno"])

f.close()

# Updating a JSON string
print("=========================================")
print("Updating a JSON string")
x = '{ "organization":"GeeksForGeeks","city":"Noida","country":"India"}'

# python object to be appended
y = {"pin":110096}

z = json.loads(x)
z.update(y)
print(json.dumps(z))

# Updating a JSON file
print("=========================================")
print("Updating a JSON file")
def write_json(new_data, filename='sample.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        json.dump(file_data, file, indent=4)

y = {"emp_name": "Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
     }

write_json(y)


# Convert class object to JSON in Python
print("=========================================")
print("Convert class object to JSON in Python")
# ========== Method 1: Using json.dumps() with __dict__ ==========
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
res = json.dumps(p1.__dict__)
print(res)

# ========== Method 2: Using dataclasses with asdict() ==========
from dataclasses import dataclass, asdict

@dataclass
class Person:
    name: str
    age: int

p1 = Person("Alice", 30)
res = json.dumps(asdict(p1))  # Convert to dictionary and then JSON
print(res)

# ========== Method 3: Using __json__ method ==========
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __json__(self):
        return {'name': self.name, 'age': self.age}

p1 = Person("Alice", 30)
res = json.dumps(p1, default=lambda o: o.__json__() if hasattr(o, '__json__') else None)
print(res)

