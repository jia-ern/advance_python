# Partial Function
# allow us to fix a certain number of arguments of a function & generate a new func

from functools import partial

print("======================================================")
# =============== 1. Simplifying Function Calls ===============
# Partial functions are great for repeated use cases where a function is often called with the same arguments.

def add(a, b):
    return a + b

# Pre-fill one argument (`a=10`)
add_ten = partial(add, 10)

# Call the new function with only the remaining arguments
print(add_ten(5))  # Output: 15
print(add_ten(20)) # Output: 30


print("======================================================")
# =============== 2. Working With Functions That Have Many Arguments ===============
# General-purpose function
def open_file(filename, mode="r", encoding=None):
    return open(file=filename, mode=mode, encoding=encoding)

# Create a partial function for reading text files
read_text_file = partial(open_file, mode="r", encoding="utf-8")

file = read_text_file("example.txt")
print(file.read())
file.close()


print("======================================================")
# =============== 3. Using Partial Functions in Event Handling ===============
def on_click(button_name, user_action):
    print(f"{button_name} clicked with action {user_action}")

# Pre-fill button name
save_button_handler = partial(on_click, "Save Button")

# Call handler with dynamic user action
save_button_handler("Save Progress") # Output: Save Button clicked with action Save Progress
save_button_handler("Submit Form")   # Output: Save Button clicked with action Submit Form


print("======================================================")
# =============== 4. Making Functions Compatible With APIs That Expect Fewer Arguments ===============
def multiply(a, b):
    return a * b

# Pre-fill one argument (`a=2`)
double = partial(multiply, 2)

numbers = [1, 2, 3, 4]
result = map(double, numbers)  # `double(n)` will be called for each `n`
print(list(result))  # Output: [2, 4, 6, 8]


print("======================================================")
# =============== 5. Configuring Functions for Higher-Order Usage ===============
def format_text(text, prefix, suffix):
    return f"{prefix}{text}{suffix}"

# Pre-fill prefix and suffix
html_formatter = partial(format_text, prefix="<p>", suffix="</p>")
markdown_formatter = partial(format_text, prefix="**", suffix="**")

print(html_formatter("Hello World"))     # Output: <p>Hello World</p>
print(markdown_formatter("Hello World")) # Output: **Hello World**


print("======================================================")
# =============== 6. Improving Code Reusability ===============
def file_operation(filename, mode, encoding, content):
    with open(filename, mode, encoding=encoding) as file:
        if mode == "w":
            file.write(content)
        elif mode == "r":
            return file.read()

# Create reusable partial functions
write_file = partial(file_operation, mode="w", encoding="utf-8")
read_file = partial(file_operation, mode="r", encoding="utf-8")

write_file("example.txt", content="Partial functions are cool!")
print(read_file("example.txt")) # Output: Partial functions are cool!
