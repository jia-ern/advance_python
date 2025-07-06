import pickle

# Pickling
print("================================================")
print("Pickling")
person = {
    "name": "Alice",
    "age": 30,
    "gender": "female"
}
# Pickle the object to a binary file
with open("person.pickle","wb") as file:
    pickle.dump(person, file)

print("Pickling completed")

# unpickling
print("================================================")
print("Unpickling")

with open('person.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)
