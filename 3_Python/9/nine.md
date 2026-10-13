# Python Exception Handling, Exception Chaining, Logging & Traceback

## Keywords

Python, Exception Handling, Error Handling, Errors, Exceptions, Try Except, Else Block, Finally Block, Exception Tree, BaseException, Built-in Exceptions, raise, assert, User Defined Exception, Custom Exception, Exception Chaining, Implicit Chaining, Explicit Chaining, Suppressed Chaining, Python Logging, logging Module, Debugging, Log Levels, Traceback, traceback Module, Exception Tracking.

## Original Keywords / Tags From Notes

- [SYN]
- [WHY]
- [TYS]
- [USA]
- [RES]
- [EXA]
- [VER]
- [LIB]
- [MET]
- [Note]

---

# Date

15/07/2026

---

# Exception Handling

Exception handling is a mechanism used to handle runtime errors and prevent the program from stopping unexpectedly.

## Error

- Unknown error that stops the program.

## Exception

- Predicting expected errors and preventing them before stopping the program.

## Testing

- Checking or validating whether we match the scenario with client requirements.

---

# Exception Handling Syntax

```python
try:
    <statements>

except:
    <statements>

else:
    # Executes when no error occurs
    <statements>

finally:
    # Optional
    # Executes for both try and except
    <statements>
````

---

# Exception Tree

```
BaseException
│
├── BaseExceptionGroup
│   └── ExceptionGroup
│
├── GeneratorExit
│
├── KeyboardInterrupt
│
├── SystemExit
│
└── Exception
    │
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    │
    ├── AssertionError
    │
    ├── AttributeError
    │
    ├── BufferError
    │
    ├── EOFError
    │
    ├── ImportError
    │   └── ModuleNotFoundError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── MemoryError
    │
    ├── NameError
    │   └── UnboundLocalError
    │
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   │
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   └── TimeoutError
    │
    ├── ReferenceError
    │
    ├── RuntimeError
    │   ├── NotImplementedError
    │   └── RecursionError
    │
    ├── StopAsyncIteration
    │
    ├── StopIteration
    │
    ├── SyntaxError
    │   ├── IndentationError
    │   │   └── TabError
    │   └── Other SyntaxError cases
    │
    ├── TypeError
    │
    ├── ValueError
    │   ├── UnicodeError
    │   │   ├── UnicodeDecodeError
    │   │   ├── UnicodeEncodeError
    │   │   └── UnicodeTranslateError
    │   │
    │   └── Other ValueError cases
    │
    ├── Warning
    │   ├── BytesWarning
    │   ├── DeprecationWarning
    │   ├── EncodingWarning
    │   ├── FutureWarning
    │   ├── ImportWarning
    │   ├── PendingDeprecationWarning
    │   ├── ResourceWarning
    │   ├── RuntimeWarning
    │   ├── SyntaxWarning
    │   ├── UnicodeWarning
    │   └── UserWarning
    │
    └── ExceptionGroup (Python 3.11+)
```

---

# raise Keyword

`raise` is used to immediately raise an error or exception.

## Usage

* Protection.
* Creating custom exceptions.

---

# assert Keyword

`assert` is used to check a condition.

## Usage

* Used for debugging and testing.

## Syntax

```python
assert condition, message
```

## Working

Condition True:

* Continue normally.

Condition False:

* Creates `AssertionError`.
* Attaches message.
* Raises exception.

## Note

Python accepts nested `try` blocks.

---

# User Defined Exception

User-defined exceptions are used for creating custom exceptions.

## Syntax

```python
class <custom-exception>(Exception):
    <statements>


try:
    <statements>

    <condition/assertion>
        raise <custom-exception>

except:
    <statements>
```

## Note

`try/except` block is optional as we raise when we want it.

---

# Custom Exception With Rules

## Example

```python
class SalaryError(Exception):

    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return f"Invalid Salary: {self.salary}"


try:
    salary = 5000

    if salary < 10000:
        raise SalaryError(salary)

except SalaryError as e:
    print(e)
```

## Note

`IndexError` and `IndexOutOfBound` are the same concept.

---

# Chaining Exceptions

Exception chaining is used to raise a new exception while keeping the original exception (root cause).

## Why

* Keeps the original error.
* Makes debugging easier.
* Adds more information to exceptions.

## Types

1. Implicit
2. Explicit
3. Suppressed

---

# Implicit Exception Chaining

## Syntax

```python
raise NewError()
```

## Example

```python
try:
    int("abc")

except ValueError:
    raise RuntimeError("Failed")
```

## Result

Original + New exception.

---

# Explicit Exception Chaining

## Syntax

```python
raise NewError() from e
```

## Example

```python
try:
    int("abc")

except ValueError as e:
    raise RuntimeError("Failed") from e
```

## Result

Original exception is shown as the direct cause.

---

# Suppressed Exception Chaining

## Syntax

```python
raise NewError() from None
```

## Example

```python
try:
    int("abc")

except ValueError:
    raise RuntimeError("Failed") from None
```

## Result

Only the new exception is shown.

---

# Examples

```
FileNotFoundError
        ↓
ConfigError


TimeoutError
        ↓
APIError
```

## Version

Python 3.x

---

# Python Logging

Python logging is used to record program events, errors, warnings, and debugging information.

## Library

```python
import logging
```

## Why

* Tracks program execution.
* Helps debug errors.
* Stores logs in console or file.
* Better than using `print()`.

---

# Logging Levels

* DEBUG
* INFO
* WARNING
* ERROR
* CRITICAL

---

# Syntax

```python
logging.basicConfig(level=logging.INFO)

logging.info("Message")
```

---

# Logging Methods

```python
logging.debug()

logging.info()

logging.warning()

logging.error()

logging.critical()

logging.exception()
```

---

# Logging Example

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program Started")
logging.warning("Low Battery")
logging.error("File Not Found")
```

## Result

```
INFO:root:Program Started

WARNING:root:Low Battery

ERROR:root:File Not Found
```

---

# Log To File

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application Started")
```

---

# Log Exception

```python
import logging

try:
    10 / 0

except ZeroDivisionError:
    logging.exception("Division Error")
```

## Result

* Logs appear in console or file.
* Errors are easier to trace.
* Exception traceback is recorded.

## Examples

* Application logs.
* Error tracking.
* Debugging.
* Server logs.

---

# Traceback

Traceback shows the sequence of function calls that caused an exception.

## Library

```python
import traceback
```

## Why

* Finds the error location.
* Shows full exception details.
* Useful for debugging.

---

# Traceback Methods

| Method                    | Description                         |
| ------------------------- | ----------------------------------- |
| `traceback.print_exc()`   | Prints current exception traceback. |
| `traceback.format_exc()`  | Returns traceback as a string.      |
| `traceback.print_stack()` | Prints current stack trace.         |

---

# Traceback Example

```python
import traceback

try:
    10 / 0

except:
    traceback.print_exc()
```

## Result

Displays the complete exception traceback.

## Version

Python 3.x

