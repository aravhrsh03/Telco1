# Python Unit Testing - unittest, PyTest, Fixtures & Testing Utilities

## Keywords

Python, Unit Testing, Testing Framework, unittest, PyTest, Assertions, Test Cases, Test Functions, Test Classes, Test Execution, Test Commands, Fixtures, pytest.fixture, Markers, Exception Testing, TempPath, Capsys, MonkeyPatch, Mocking, Automation Testing, API Testing, Django Testing, Flask Testing, Data Validation.

## Original Keywords / Tags From Notes

- [LIB]
- [USA]
- [PAR]
- [SYN]
- [WHY]
- [EXA]
- [MET]
- [CAT]
- [ALI]
- [RES]
- [OPT]
- [ANE]
- [FUN]
- [DAM]
- [TYS]
- [VER]
- [USC]
- [RUN]
- [FLAGS]

---

# Abbreviation

| Keyword | Meaning |
|---|---|
| LIB | Library |
| USA | Usage (Example Code) |
| PAR | Parameters |
| SYN | Syntax |
| WHY | Why this is used |
| EXA | Example |
| MET | Methods |
| CAT | Cannot have it |
| ALI | Alias |
| RES | Expected Result |
| OPT | Optional |
| ANE | Another Example |
| FUN | Functions Used |
| DAM | Data Members |
| TYS | Types |
| VER | Python Version |
| USC | Use Cases |

---

# Date

17/07

---

# unittest

`unittest` is a built-in Python testing framework used for creating and running unit tests.

---

# unittest Naming Rules

## File

File name should start with `test`.

### Example

```text
test_sample.py
````

### Rule

* Strictly lowercase `test`.

---

## Function

Function name should start with `test`.

### Example

```python
test_add()
```

### Rule

* Strictly lowercase `test`.

---

## Class

Class should start with the word `Test`.

### Example

```python
class TestCals
```

---

# Example Application File

## func.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

---

# unittest Test File

## test_sample.py

## Library

```python
unittest
```

## Example

```python
import unittest

from func import add


class Testcals(unittest.TestCase):

    def test_add(self):

        self.assertEqual(add(3, 3), 3)

        # Syntax:
        # assertEqual(<function>, <expected-result>)


    def test_subtract(self):

        self.assertEqual(subtract(10, 5), 5)


    def test_multiply(self):

        self.assertEqual(multiply(2, 3), 4)


    def test_divide(self):

        self.assertEqual(divide(3, 3), 3)


if __name__ == "__main__":

    unittest.main()
```

---

# unittest Run Commands

## Run Specific Function

```bash
python -m unittest -v <file_name>.<class>.<function>
```

## Run Specific Class

```bash
python -m unittest -v <file_name>.<class>
```

## Run Complete File

```bash
python -m unittest -v <file_name>
```

---

# unittest Methods

| Method                | Description                 |
| --------------------- | --------------------------- |
| `assertEqual()`       | Checks equality             |
| `assertNotEqual()`    | Checks inequality           |
| `assertTrue()`        | Checks True condition       |
| `assertFalse()`       | Checks False condition      |
| `assertIsNone()`      | Checks None value           |
| `assertIn()`          | Checks item exists          |
| `assertNotIn()`       | Checks item does not exist  |
| `assertRaises()`      | Checks exception raising    |
| `assertIsInstance()`  | Checks object type          |
| `assertAlmostEqual()` | Checks approximate equality |

---

# PyTest

PyTest is a Python testing framework used for simple and scalable testing.

---

# PyTest Naming Rules

## File

File name should start with:

```text
test_
```

Example:

```text
test_sample.py
```

---

## Function

Function name should start with:

```text
test_
```

Example:

```python
test_add()
```

---

## Class

Class name should start with:

```text
Test
```

Example:

```python
class TestCalc:
```

## Note

* No need to inherit `unittest.TestCase`.

---

# PyTest Example

## func.py

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b
```

---

# test_sample.py

## Library

```python
pytest
```

## Example

```python
from func import *


def test_add():

    assert add(2, 3) == 5


def test_subtract():

    assert subtract(10, 5) == 5


def test_multiply():

    assert multiply(2, 3) == 6


def test_divide():

    assert divide(10, 2) == 5
```

---

# PyTest Assertion Syntax

```python
assert <function> == <expected_result>
```

## Example

```python
assert add(2, 3) == 5
```

---

# PyTest Run Commands

## Run All Tests

```bash
pytest
```

## Run With Details

```bash
pytest -v
```

## Run Specific File

```bash
pytest test_sample.py
```

## Run Specific Function

```bash
pytest test_sample.py::test_add
```

## Run Specific Class

```bash
pytest test_sample.py::TestCalc
```

---

# PyTest Methods

```python
assert a == b

assert a != b

assert a > b

assert a < b

assert True

assert False

pytest.raises()
```

---

# Exception Testing

## Example

```python
import pytest

from func import divide


def test_divide_by_zero():

    with pytest.raises(ZeroDivisionError):

        divide(5, 0)
```

---

# Fixtures

Fixtures are used to reuse common setup code.

## Characteristics

* Runs before test function.
* Avoids duplicate code.
* Created using `@pytest.fixture`.

---

# Fixture Library

```python
import pytest
```

---

# Fixture Example

```python
import pytest


@pytest.fixture
def data():

    return [1, 2, 3]


def test_length(data):

    assert len(data) == 3
```

---

# Why Fixtures

* Reuse setup code.
* Cleaner tests.
* Reduce code duplication.

---

# Fixture Syntax

```python
@pytest.fixture
def fixture_name():

    return value


def test_name(fixture_name):

    assert ...
```

---

# Fixture Use Cases

* Database connection.
* Test data.
* File setup.
* Object creation.

---

# Fixture Remember

```text
@pytest.fixture
        ↓
Create Fixture
        ↓
Pass as Function Argument
        ↓
Use in Test
```

---

# Built-in PyTest Fixtures

* TempPath
* Capsys
* MonkeyPatch

---

# TempPath

TempPath provides a temporary directory for testing files.

---

# Capsys

Capsys is used to capture and show output.

## Example

```python
def greet():

    print("something")


def test_greet(capsys):

    greet()

    captured = capsys.readouterr()

    assert captured.out == "Welcome to pytest"
```

## Note

```text
something != Welcome to pytest
```

---

# MonkeyPatch

MonkeyPatch is used to temporarily modify objects during testing.

---

# Example

## app.py

```python
def get_data():

    return "database"
```

---

## sample.py

```python
def fake_data():

    return "Mock Data"


def test_mock(monkeypatch):

    monkeypatch.setattr(app, "get_data", fake_data)

    assert app.get_data() == "Mock Data"
```

## Working

* `get_data()` from `app.py` is temporarily changed to `fake_data()`.
* Test checks the modified behavior.

---

# PyTest Markers

Markers are used to group tests.

## Example

```python
import pytest


@pytest.mark.slow
def test_add():

    assert add(2, 3) == 5
```

---

# Run Marker

```bash
pytest -m slow
```

---

# Parameters

## PyTest Assertions

```python
assert <condition>
```

## Exception Testing

```python
with pytest.raises(Exception):
```

---

# Use Cases

* Unit Testing.
* API Testing.
* Django Testing.
* Flask Testing.
* Automation Testing.
* Data Validation.

---

# Version

Python 3.x

---

# Installation

```bash
pip install pytest
```

---

# Quick Difference

## unittest

```python
self.assertEqual(add(2,3),5)
```

## pytest

```python
assert add(2,3) == 5
```

---

# Remember

```text
File      → test_*.py

Function  → test_*

Class     → Test*

Command   → pytest -v

Assertion → assert

Exception → pytest.raises()

Setup     → @pytest.fixture
```

---

# Additional Run Command

```bash
python -m pytest <file-name>.py
```

---

# Flags

## -s

Used to show output.

Example:

```bash
pytest -s
```