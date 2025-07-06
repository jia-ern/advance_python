#Enums
# a set of symbolic names bound to unique values
# centralize the definition of name values -> easier to upgrade / extend the set of values as per our requirements

# Access Enum:
# By value:- In this method, the value of enum member is passed.
# By name:- In this method, the name of the enum member is passed.

from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))
