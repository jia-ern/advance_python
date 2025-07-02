# Exceptions
- an event which occurs during the execution of program that disrupts normal flow of program
- can be handled using exception
- Exception handling allows to respond to the error, instead of crashing the running program
- dangerous
  - lead to sudden termination of program
  - data loss
  - corrupt data files
  - block application
- EG: ZeroDivisionError, TypeError

try:
    #code containing suspicious code

except [ExceptionName]:
    # code to handle exception

else:
    # code to execute if no exception

finally:
    # always execute

## Catching Exceptions
- can handle errors more efficiently 
- by specifying the types of exceptions we expect. 
- This can make code both safer and easier to debug.

## Raise an Exception
- raise an exception in Python 
- using the raise keyword followed by an instance of the exception class that we want to trigger. 
- can choose from built-in exceptions / define own custom exceptions by inheriting from Python's built-in Exception class.

## Exception type
# Python Exceptions

Python provides a variety of built-in exception classes that are used to indicate errors or unusual program behavior during execution.

---

## **Base Exceptions**

| **Exception Name**  | **Description**                                       |
|----------------------|-------------------------------------------------------|
| `BaseException`      | The base class for all built-in exceptions.           |
| `Exception`          | The base class for all non-exit exceptions.          |

---

## **Arithmetic Exceptions**

| **Exception Name**       | **Description**                                                  |
|---------------------------|------------------------------------------------------------------|
| `ArithmeticError`         | Base class for all errors related to arithmetic operations.     |
| `ZeroDivisionError`       | Raised when a division or modulo operation is performed with zero as the divisor. |
| `OverflowError`           | Raised when a numerical operation exceeds the maximum limit of a data type. |
| `FloatingPointError`      | Raised when a floating-point operation fails.                  |

---

## **Assertion and Attribute Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `AssertionError`          | Raised when an **assert statement** fails.            |
| `AttributeError`          | Raised when an attribute reference or assignment fails. |

---

## **Index and Key Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `IndexError`             | Raised when a sequence subscript is out of range.     |
| `KeyError`               | Raised when a dictionary key is not found.            |

---

## **Memory and Name Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `MemoryError`            | Raised when an operation runs out of memory.          |
| `NameError`              | Raised when a local or global name is not found.      |

---

## **System and Type Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `OSError`                | Raised when a system-related operation (like file I/O) fails. |
| `TypeError`              | Raised when an operation or function is applied to an object of inappropriate type. |

---

## **Value Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `ValueError`             | Raised when a function receives an argument of the right type but inappropriate value. |

---

## **Import Exceptions**

| **Exception Name**       | **Description**                                        |
|---------------------------|-------------------------------------------------------|
| `ImportError`            | Raised when an import statement has issues.           |
| `ModuleNotFoundError`    | Raised when a module cannot be found.                  |

# Python Exception Hierarchy

This is the entire Python exception hierarchy, showing how built-in exceptions are structured and how they inherit from each other.

---

## **BaseException**
The base class for all built-in exceptions.

- **BaseExceptionGroup**
- **GeneratorExit**
- **KeyboardInterrupt**
- **SystemExit**
- **Exception**
  - **ArithmeticError**
    - **FloatingPointError**
    - **OverflowError**
    - **ZeroDivisionError**
  - **AssertionError**
  - **AttributeError**
  - **BufferError**
  - **EOFError**
  - **ExceptionGroup** (*inherits from BaseExceptionGroup*)
  - **ImportError**
    - **ModuleNotFoundError**
  - **LookupError**
    - **IndexError**
    - **KeyError**
  - **MemoryError**
  - **NameError**
    - **UnboundLocalError**
  - **OSError**
    - **BlockingIOError**
    - **ChildProcessError**
    - **ConnectionError**
      - **BrokenPipeError**
      - **ConnectionAbortedError**
      - **ConnectionRefusedError**
      - **ConnectionResetError**
    - **FileExistsError**
    - **FileNotFoundError**
    - **InterruptedError**
    - **IsADirectoryError**
    - **NotADirectoryError**
    - **PermissionError**
    - **ProcessLookupError**
    - **TimeoutError**
  - **ReferenceError**
  - **RuntimeError**
    - **NotImplementedError**
    - **PythonFinalizationError**
    - **RecursionError**
  - **StopAsyncIteration**
  - **StopIteration**
  - **SyntaxError**
    - **IndentationError**
      - **TabError**
  - **SystemError**
  - **TypeError**
  - **ValueError**
    - **UnicodeError**
      - **UnicodeDecodeError**
      - **UnicodeEncodeError**
      - **UnicodeTranslateError**
  - **Warning**
    - **BytesWarning**
    - **DeprecationWarning**
    - **EncodingWarning**
    - **FutureWarning**
    - **ImportWarning**
    - **PendingDeprecationWarning**
    - **ResourceWarning**
    - **RuntimeWarning**
    - **SyntaxWarning**
    - **UnicodeWarning**
    - **UserWarning**

# Error
- serious issues that a program should not try to handle. 
- problems in the code's logic or configuration 
- need to be fixed by the programmer. 
- EG: syntax errors, memory errors.
- errors cannot be handled

## Syntax Error
- a coding mistake that prevents the code from running
