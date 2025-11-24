# Monkey patching
# dynamically modify or extend existing code at runtime without changing the original code.

# 1. identify target that can be a module, class, method, or function you want to patch.
# 2. create your patch by writing code to add, modify, or replace existing logic.
# 3. apply the patch by using an assignment to apply it to the target. The patch will overwrite or extend the existing behavior.

# Use case:
# 1. Quick fix: EG: third-party library has an urgent bug that you cannot wait for official release.
# can use monkey patching to apply quick fixes while waiting for a proper solution.

# add_speech() function
# adds the speak() method by adding a speak attribute to the class & assigning a lambda expression & returning class.
# lambda expression accepts a message and displays it to the console.
def add_speech(cls):
    cls.speak = lambda self, message: print(message)
    return cls

class Robot:
    def __init__(self, name):
        self.name = name

@add_speech
class RobotDecorator:
    def __init__(self, name):
        self.name = name

# a decorator
Robot = add_speech(Robot)

robot = Robot('Optimus Prime')
robot.speak('Hi')

robot_decorator = RobotDecorator('Optimus Prime Decorator')
robot_decorator.speak('Hi')