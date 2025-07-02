# creating a list of objects involves storing instances of a class in a list
# which allows for easy access, modification and iteration

# ====================== 1. Using list comprehension ======================
print("=====================================================")
print("1. Using list comprehension")
class Geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# create list of objects
a = [Geeks(name, roll) for name, roll in [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]]

for obj in a:
    print(obj.name, obj.roll, sep=' ')


# ====================== 2. Using map() ======================
print("=====================================================")
print("2. Using map()")
class Geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# create list of objects
a = list(map(lambda x: Geeks(x[0], x[1]), [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]))


for obj in a:
    print(obj.name, obj.roll, sep=' ')


# ====================== 3. Using extend() ======================
print("=====================================================")
print("3. Using extend()")
class Geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# create list of objects
a = []
a.extend([Geeks('Akash', 2), Geeks('Deependra', 40), Geeks('Reaper', 44), Geeks('Veer', 67)])

for obj in a:
    print(obj.name, obj.roll, sep=' ')


# ====================== 4. for loop ======================
print("=====================================================")
print("4. for loop")

class Geeks:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

# create list of objects
a = []
for data in [('Akash', 2), ('Deependra', 40), ('Reaper', 44), ('Veer', 67)]:
    a.append(Geeks(data[0], data[1]))

for obj in a:
    print(obj.name, obj.roll, sep=' ')

