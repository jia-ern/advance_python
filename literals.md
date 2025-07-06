# Types of Literals in Python

This document highlights the key types of literals in Python, their descriptions, examples, and whether they are mutable or immutable.

---

| **Type of Literal**       | **Description**                                                                    | **Example**                                                       | **Mutable/Immutable** |
|---------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------|
| **Integer Literals**       | Whole numbers (without decimals).                                                  | `a = 77`                                                        | Immutable             |
| **Float Literals**         | Numbers with a decimal point.                                                      | `b = 3.144`                                                     | Immutable             |
| **Complex Literals**       | Numbers with real and imaginary parts.                                             | `c = 7 + 5j`                                                    | Immutable             |
| **String Literals**        | Stores text. Can use single, double, or triple quotes.                              | `greeting = "Bonjour"`<br>`story = """Once upon a time..."""`    | Immutable             |
| **Boolean Literals**       | Represents True (1) or False (0).                                                  | `a = (1 == True)  # True`<br>`b = (1 == False)  # False`         | Immutable             |
| **Boolean as Numbers**     | Boolean values can act as numbers (1 or 0).                                        | `c = True + 3  # 4`<br>`d = False + 7  # 7`                      | Immutable             |
| **List Literals**          | Stores multiple values; can be changed.                                            | `Rank = ["First", "Second", "Third"]`                           | Mutable               |
| **Tuple Literals**         | Like a list but cannot be changed.                                                 | `colors = ("Red", "Blue", "Green")`                             | Immutable             |
| **Dictionary Literals**    | Stores key-value pairs.                                                            | `Class = {"Jai": 10, "Anaya": 12}`                              | Mutable               |
| **Set Literals**           | Stores unique values, unordered.                                                   | `unique_num = {1, 2, 3}`                                        | Mutable               |
| **Special Literals**       | Represents "nothing" or "empty."                                                   | `water_remain = None`                                           | Immutable             |

---

## **Key Notes**
- **Immutable**: The value of the literal cannot be changed after its creation.
- **Mutable**: The value of the literal can be modified after its creation.

---

## **Examples Explained**
### **Integer Literals**
```python
a = 77  # An integer literal example
print(type(a))  # Output: <class 'int'>