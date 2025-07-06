# @property decorator
# a built-in decorator in Python
# helpful in defining the properties effortlessly without manually calling the inbuilt function property().
# to return the property attributes of a class from the stated getter, setter and deleter as parameters.

# Python program to illustrate the use of
# @property decorator
print("========================================")
print("with @property")
class Portal:
    def __init__(self):
        self.__name = ''

    # @property decorator makes the name method behave like an attribute (p.name)
    # instead of requiring a method call (p.name())
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @name.deleter
    def name(self):
        del self.__name

p = Portal();

# Setting name
p.name = 'GeeksforGeeks'
print(p.name)

# Deletes name
del p.name

# As name is deleted above this will throw an error
# print(p.name)

# ==============================================
# without @property
print("========================================")
print("without @property")
class Portal:
    def __init__(self):
        self.__name = ''

    def get_name(self):
        return self.__name

    def set_name(self, val):
        self.__name = val

p = Portal();
p.set_name('GeeksforGeeks')
print(p.get_name())
