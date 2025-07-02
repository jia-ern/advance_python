# Closure
# allows a function to remember & access variables from its lexical scope, even when function is executed outside that scope.
# closely related to nested functions
# commonly used in functional programming, event handling and callbacks.

# ===========================  1. Maintain State Without Using a Class ===========================
def make_counter():
    count = 0  # Enclosed variable

    def increment():
        nonlocal count  # Access and modify outer variable
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())  # Output: 1
print(counter())  # Output: 2
print(counter())  # Output: 3

# ===========================  2. Function Factories ===========================
def multiplier_factory(factor):
    def multiplier(number):
        return number * factor  # Retains access to `factor`
    return multiplier

double = multiplier_factory(2)
triple = multiplier_factory(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

# =========================== 3. Data Hiding and Encapsulation ===========================
# There is no direct way to access secret from outside the closure, because:
# The variable secret exists only inside the create_secret function’s scope, and is not returned directly.
def create_secret(secret):
    def reveal_secret():
        return f"The secret is: {secret}"  # Encapsulates `secret`
    return reveal_secret

my_secret = create_secret("Closures are cool!")
print(my_secret())  # Output: "The secret is: Closures are cool!"

# ===========================  4. Callback Functions ===========================
def on_event(name):
    event_message = f"Event triggered for {name}"

    def callback():
        print(event_message)  # Access outer variable
    return callback

button_click = on_event("Button")
button_click()  # Output: Event triggered for Button

# ===========================  5. Reducing Dependency on Global Variables ===========================
def create_logger():
    log = []  # Maintain state

    def logger(message):
        log.append(message)    # Retains access to the `log` variable
        print(f"Log updated: {log}")
    return logger

my_logger = create_logger()
my_logger("Start process")    # Output: Log updated: ['Start process']
my_logger("Process completed") # Output: Log updated: ['Start process', 'Process completed']

#=====================================================

def fun1(x):
    # This is the outer function that takes an argument 'x'
    def fun2(y):
        # This is the inner function that takes an argument 'y'
        return x + y  # 'x' is captured from the outer function

    return fun2  # Returning the inner function as a closure


# Create a closure by calling outer_function
closure = fun1(10)

# Now, we can use the closure, which "remembers" the value of 'x' as 10
print(closure(5))