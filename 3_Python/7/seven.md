# Python Notes

## 📌 Keywords Covered
- OOPS
- Object-Oriented Programming
- Class
- Object
- Constructor
- Default Constructor
- Instance Variable
- Static Variable
- Class Variable
- Nested Class
- `__repr__()`
- Dataclass
- Pydantic
- Singleton Class
- Enum Class
- Frozen Class
- Factory Class
- Proxy Class
- Metaclass
- Instance Method
- Class Method
- Static Method
- `@property`
- Getter
- Setter
- Encapsulation
- Object Creation
- Runtime
- Compile Time

---

## 🏷️ Python Abbreviations (Always Available)

| Abbreviation | Meaning |
|--------------|---------|
| **LIB** | Library |
| **USA** | Usage (Example Code) |
| **PAR** | Parameters |
| **SYN** | Syntax |
| **WHY** | Why this is used |
| **EXA** | Example |
| **MET** | Methods |
| **CAT** | Cannot Have It / Limitations |
| **ALI** | Alias |
| **RES** | Expected Result |
| **OPT** | Optional |
| **ANE** | Another Example |
| **FUN** | Functions Used |
| **DAM** | Data Members |
| **TYS** | Types |
| **VER** | Python Version |
| **USC** | Use Cases |

---

## 🏷️ Tags & Keywords Used in Notes

- USA
- NOTE
- SYN
- RES
- TYS
- VER
- ALI
- EXA
- ANE
- LIB
- Default
- Parameterized
- Copy

---

## Date

**13/07/2026**

---

# OOPS (Object-Oriented Programming)

## Definition

OOPS (Object-Oriented Programming System) is a programming approach based on:

- Classes
- Objects
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## Programming Language Types

### 4 PL (Programming Language Types)

## Functional Programming Language (FPL)

- Logic is mainly represented as functions.
- Follows a **Top-Down** approach.

---

## Structural Programming Language (SPL)

- Focuses on structured programming using:
  - Loops
  - Conditions
  - Functions

---

## Procedural Programming Language

- Program is divided into procedures/functions.
- Follows a **Bottom-Up** approach.

---

## Object-Oriented Programming Language

- Program is organized around objects and classes.

---

# Class

## Definition

A class is a **template/blueprint for creating objects**.

---

## SYN

```python
class <class-name>:

    def __init__(self, <parameters>):
        self.<parameter> = <parameter>

    def <method-name>(self, <parameters>):
        <statements>
```

---

## Constructor

### Definition

`__init__()` initializes object attributes.

If no constructor is defined, Python provides a default constructor behavior.

---

## USA

```python
class emp:

    def display(self):
        print(self.name)


e = emp()

e.name = "Madhan"

e.display()
```

### RES

```text
Madhan
```

### NOTE

If `name` is not assigned:

```python
e.display()
```

Result:

```text
AttributeError
```

---

# Static Variable / Class Variable

## Definition

A static variable is shared among all objects of a class.

In Python, it is commonly called a **class variable**.

---

## USA

```python
class emp:

    company = "Prodapt"

    def display(self):
        print(self.company)
        print(self.emp)


e = emp()

e.emp = "madhan"

e.display()
```

### RES

```text
Prodapt
madhan
```

---

## Updating Static Variable

### Update for All Objects

```python
<class-name>.<static-variable> = <value>
```

Example:

```python
emp.company = "ABC"
```

---

### Update for Specific Object

```python
<class-object>.<static-variable> = <value>
```

Example:

```python
e.company = "XYZ"
```

This creates/updates an instance attribute for that object only.

---

# Nested Class

## Definition

A class defined inside another class.

---

## SYN

```python
class Outer:

    class Inner:

        def method(self):
            <statement>


variable = Outer.Inner()
```

### NOTE

Inner class objects are created using the outer class reference.

---

# `__repr__()`

## Definition

`__repr__()` is a special class method used to provide the official string representation of an object.

### Trigger

Called automatically when:

```python
print(object)
```

or

```python
repr(object)
```

is used.

---

## USA

```python
class Demo:

    def __repr__(self):
        return "Demo Object"


d = Demo()

print(d)
```

### RES

```text
Demo Object
```

---

# Dataclass

## Definition

A dataclass automatically creates:

- Data members
- Constructor
- `__repr__`
- Comparison methods

---

## ALI

```text
Pydantic Model (Conceptually)
```

---

## LIB

```python
dataclasses
```

---

## VER

```text
Python 3.7+
```

---

## USA

```python
from dataclasses import dataclass


@dataclass
class emp:

    id: int
    name: str


e1 = emp(
    101,
    "Flemming"
)
```

### NOTE

No need to manually define `__repr__()`.

---

# Singleton Class

## Definition

A Singleton class allows only **one object instance** to be created.

---

## USA

```python
class Single:

    _instance = None

    def __new__(cls):

        if cls._instance is None:

            cls._instance = super().__new__(cls)

        return cls._instance


o1 = Single()

o2 = Single()
```

### RES

```text
o1 and o2 point to the same instance
```

---

# Enum Class

## Definition

Enum defines a collection of named constant values that are:

- Unique
- Immutable

---

## USA

```python
from enum import Enum


class Color(Enum):

    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)

print(Color.RED.value)

print(Color.RED.name)
```

### RES

```text
Color.RED
1
RED
```

---

# Frozen Class

## Definition

A frozen class is an immutable dataclass created using:

```python
@dataclass(frozen=True)
```

After creation, attributes cannot be modified.

---

## USA

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:

    x: int
    y: int


p = Point(1, 2)

# p.x = 3
```

### RES

```text
FrozenInstanceError
```

---

# Factory Class

## Definition

A Factory class creates and returns objects without exposing the exact object creation logic.

### Execution Time

```text
Runtime
```

---

## USA

```python
class ShapeFactory:

    def create_shape(self, shape_type):

        if shape_type == "circle":

            return Circle()

        elif shape_type == "square":

            return Square()

        else:

            raise ValueError(
                "Unknown shape type"
            )


class Circle:

    def draw(self):

        print("Drawing a Circle")


class Square:

    def draw(self):

        print("Drawing a Square")


factory = ShapeFactory()

shape = factory.create_shape("circle")

shape.draw()
```

### RES

```text
Drawing a Circle
```

---

# Proxy Class

## Definition

A Proxy class controls access to another object by holding the original object internally.

---

## USA

```python
class Printer:

    def print_doc(self):

        print("printing")


class PrinterProxy:

    def __init__(self):

        self.printer = Printer()


    def print_doc(self):

        print("Permission Checked")

        self.printer.print_doc()


p = PrinterProxy()

p.print_doc()
```

### RES

```text
Permission Checked
printing
```

---

# Metaclass

## Definition

A metaclass is a class that defines how other classes are created and behave.

### Execution Time

```text
Compile Time
```

> **Correction**
>
> Python creates classes dynamically at runtime through metaclasses. They operate during class creation, not traditional compile time.

---

## USA

```python
class std(type):

    pass


class demo(metaclass=std):

    pass


print(type(demo))
```

---

## ANE

```python
class MyMeta(type):

    def __new__(cls, name, bases, attrs):

        def hello(self):

            print("Hello")


        attrs["hello"] = hello

        return super().__new__(
            cls,
            name,
            bases,
            attrs
        )


class Student(metaclass=MyMeta):

    pass


class Employee(metaclass=MyMeta):

    pass


s = Student()

e = Employee()

s.hello()
```

### RES

```text
Hello
```

---

# Method Types

## Instance Method

### Definition

Default method type inside classes.

### Characteristics

- First parameter is `self`.
- Accesses and modifies:
  - Instance attributes
  - Class attributes

---

## Class Method

### Definition

Declared using:

```python
@classmethod
```

### Characteristics

- First parameter is `cls`.
- Accesses and modifies class-level data.
- Cannot directly access instance-specific data.

---

## Static Method

### Definition

Declared using:

```python
@staticmethod
```

### Characteristics

- No `self`.
- No `cls`.
- Works like a normal function inside a class.

---

## EXA

```python
class Demo:

    class_var = "class level"


    def instance_method(self):

        return f"Instance method: {self.class_var}"


    @classmethod
    def class_method(cls):

        return f"Class method: {cls.class_var}"


    @staticmethod
    def static_method():

        return "Static method: no access to class/instance data"



obj = Demo()

print(obj.instance_method())

print(Demo.class_method())

print(Demo.static_method())
```

---

# Property Decorator

## Definition

Provides getter and setter behavior for class attributes.

---

## Getter

```python
@property
```

---

## Setter

```python
@<method-name>.setter
```

---

## NOTE

Python does not have truly private variables.

Using:

```python
__variable
```

invokes **name mangling**, which changes the internal name but does not provide complete security.

---

# Constructor Types

## Default Constructor

- No parameters except `self`.

---

## Parameterized Constructor

- Accepts values during object creation.

---

## Copy Constructor

- Creates a new object using another object's values.

> **Note**
>
> Python does not have a built-in copy constructor syntax like C++. Copying is generally done using:
>
> - `copy.copy()`
> - `copy.deepcopy()`

---

# Summary

| Concept | Purpose |
|--------|---------|
| Class | Blueprint for objects |
| Object | Instance of a class |
| Static/Class Variable | Shared data among objects |
| Nested Class | Class inside another class |
| `__repr__()` | Object representation |
| Dataclass | Automatic data class creation |
| Singleton | One object instance |
| Enum | Named constants |
| Frozen Class | Immutable dataclass |
| Factory Class | Object creation abstraction |
| Proxy Class | Access control wrapper |
| Metaclass | Controls class creation |
| Instance Method | Object-level operations |
| Class Method | Class-level operations |
| Static Method | Utility functions inside class |
| Property | Getter/setter management |