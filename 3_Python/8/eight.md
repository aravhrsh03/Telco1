# Python OOP Concepts, Dunder Methods, Iterators, Abstraction, SOLID Principles & Design Patterns

## Keywords

Python, Object-Oriented Programming, OOP, Inheritance, Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, Hybrid Inheritance, Method Resolution Order (MRO), Method Overriding, Polymorphism, Duck Typing, Dunder Methods, Magic Methods, Special Methods, Object Creation, Attribute Access, Comparison Operators, Arithmetic Operators, Container Methods, Iterator, Iteration, __getitem__, Abstraction, Abstract Class, Abstract Method, ABC Module, SOLID Principles, Single Responsibility Principle, Open Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle, Builder Pattern, Creational Design Pattern, Strategy Pattern, Behavioral Design Pattern, Observer Pattern, Adapter Pattern, Structural Design Pattern.

## Original Keywords / Tags From Notes

- [SYN]
- [USA]
- [RES]
- [WHY]
- [RUNTIME]
- [EXA]
- [ADV]
- [CAT]
- [VER]
- [MET]
- [PAR]
- [ANE]
- [WORKING]
- [TYS]
- [LIB]
- [FUN]
- [USC]
- [COMPONENTS]

---

# Date

14/07/2026

---

# Instance / Inheritance

Instance is having the behaviour of the parent class or the class which we are going to inherit.

Types of inheritance:

- Single
- Multiple
- Multilevel
- Hybrid
- Hierarchical

---

# Single Inheritance

Single inheritance contains one parent class and one child class.

## Syntax

```python
class <parent-class>:
    <methods>

class <child-class>(<parent-class>):
    <methods>
````

---

# Multilevel Inheritance

Multilevel inheritance follows a chain structure:

First → Second → Third

## Syntax

```python
class first:
    <methods>

class second(first):
    <methods>

class third(second):
    <methods>
```

---

# Multiple Inheritance

Multiple inheritance allows one child class to inherit from multiple parent classes.

Structure:

Third inherits from First and Second.

## Syntax

```python
class first:
    <methods>

class second:
    <methods>

class third(first, second):
    <methods>
```

## Method Resolution Order (MRO)

Search method using MRO (Method Resolution Order).

### Note

MRO is nothing but searching the method in the current class first, then following the order of classes available in the declaration during inheritance.

---

# Method Overriding

Method overriding occurs when parent and inherited child classes contain methods with the same name.

## Example

```python
class A:
    def sound(self):
        print("Music...")


class B(A):
    def sound(self):
        super().sound()
        print("thunder...")


b1 = B()
b1.sound()
```

## Note

Constructors are invoked using a bottom-up approach.

Example:

Parent → Child1 → Child2

The constructor checking order is:

Child2 → Child1 → Parent

---

# Polymorphism

Polymorphism means one interface having multiple forms.

Types:

* Compile-time polymorphism

  * Not available in Python because Python uses an interpreter.
* Runtime polymorphism

  * Available in Python because method behavior is decided during runtime.

---

# Duck Typing

Duck typing is a concept where an object is accepted based on its behavior (methods/attributes), not based on its class or type.

## Runtime

Runtime concept.

## Why

* Focuses on behavior, not type.
* No need for `isinstance()`.
* Makes code flexible and reusable.

## Example

```python
class Duck:
    def quack(self):
        print("Quack!")


class Person:
    def quack(self):
        print("I'm quacking like a duck!")


def make_it_quack(obj):
    obj.quack()


make_it_quack(Duck())
make_it_quack(Person())
```

## Result

```
Quack!
I'm quacking like a duck!
```

## Examples

* Any object with a `.read()` method can be treated like a file.
* Any object with a `.write()` method can be used for writing.

## Advantages

* Flexible
* Less coupling
* Easy to extend

## Catch

Missing required method/attribute raises `AttributeError`.

## Version

Available in all Python versions.

---

# Dunder Methods (Magic / Special Methods)

Dunder methods are built-in methods that define how objects behave in Python.

---

## Object Creation

| Method       | Description                                   |
| ------------ | --------------------------------------------- |
| `__new__()`  | Creates a new object.                         |
| `__init__()` | Initializes the object.                       |
| `__del__()`  | Destructor called before object is destroyed. |

---

## String Representation

| Method         | Description                          |
| -------------- | ------------------------------------ |
| `__str__()`    | User-friendly string representation. |
| `__repr__()`   | Official string representation.      |
| `__format__()` | Used by `format(obj)`.               |
| `__bytes__()`  | Used by `bytes(obj)`.                |

---

## Attribute Access

| Method               | Description                            |
| -------------------- | -------------------------------------- |
| `__getattr__()`      | Called when an attribute is not found. |
| `__getattribute__()` | Called for every attribute access.     |
| `__setattr__()`      | Assigns an attribute.                  |
| `__delattr__()`      | Deletes an attribute.                  |
| `__dir__()`          | Used by `dir(obj)`.                    |

---

## Comparison

| Method     | Operator |
| ---------- | -------- |
| `__eq__()` | `==`     |
| `__ne__()` | `!=`     |
| `__lt__()` | `<`      |
| `__le__()` | `<=`     |
| `__gt__()` | `>`      |
| `__ge__()` | `>=`     |

---

## Arithmetic

| Method           | Operator |
| ---------------- | -------- |
| `__add__()`      | `+`      |
| `__sub__()`      | `-`      |
| `__mul__()`      | `*`      |
| `__truediv__()`  | `/`      |
| `__floordiv__()` | `//`     |
| `__mod__()`      | `%`      |
| `__pow__()`      | `**`     |
| `__neg__()`      | `-obj`   |

---

## Container

| Method           | Description        |
| ---------------- | ------------------ |
| `__len__()`      | `len(obj)`         |
| `__getitem__()`  | `obj[key]`         |
| `__setitem__()`  | `obj[key] = value` |
| `__delitem__()`  | `del obj[key]`     |
| `__contains__()` | `in`               |

---

## Iterator

| Method       | Description |
| ------------ | ----------- |
| `__iter__()` | `iter(obj)` |
| `__next__()` | `next(obj)` |

---

## Callable

| Method       | Description                         |
| ------------ | ----------------------------------- |
| `__call__()` | Makes object callable using `obj()` |

---

## Context Manager

| Method        | Description          |
| ------------- | -------------------- |
| `__enter__()` | with statement entry |
| `__exit__()`  | with statement exit  |

---

## Type Conversion

| Method          | Description    |
| --------------- | -------------- |
| `__int__()`     | `int(obj)`     |
| `__float__()`   | `float(obj)`   |
| `__bool__()`    | `bool(obj)`    |
| `__complex__()` | `complex(obj)` |

---

## Copy

| Method           | Description          |
| ---------------- | -------------------- |
| `__copy__()`     | `copy.copy(obj)`     |
| `__deepcopy__()` | `copy.deepcopy(obj)` |

---

## Example

```python
class Demo:
    def __str__(self):
        return "Hello"


d = Demo()
print(d)
```

## Result

```
Hello
```

## Version

Available in all Python versions.

---

# **getitem**()

`__getitem__()` is a special dunder method used to access an object using the indexing operator `[]`.

## Runtime

Runtime concept.

## Why

* Makes custom objects behave like lists, tuples, or dictionaries.
* Supports indexing and slicing.

## Syntax

```python
def __getitem__(self, key):
    pass
```

## Parameters

* key = Index, slice, or dictionary key passed inside `[]`.

## Example

```python
class Student:
    def __init__(self):
        self.marks = [90, 85, 78]

    def __getitem__(self, index):
        return self.marks[index]


s = Student()

print(s[0])
print(s[2])
```

## Result

```
90
78
```

## Another Example

```python
class Square:
    def __getitem__(self, n):
        return n ** 2


s = Square()

print(s[5])
```

## Result

```
25
```

---

# Iterator

Iterator is an object that allows traversal through elements one by one using `__iter__()` and `__next__()`.

## Runtime

Runtime concept.

## Why

* Makes custom objects work with `for` loops.
* Controls how values are generated one at a time.

## Methods

| Method       | Description                  |
| ------------ | ---------------------------- |
| `__iter__()` | Returns the iterator object. |
| `__next__()` | Returns the next value.      |

## Example

```python
class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            value = self.start
            self.start += 1
            return value
        else:
            raise StopIteration


counter = Counter(1, 5)

for i in counter:
    print(i)
```

## Result

```
1
2
3
4
5
```

## Working

For:

```python
for i in counter:
```

Internally:

```python
iter(counter) -> counter.__iter__()

next(counter) -> counter.__next__()
```

When `__next__()` raises `StopIteration`, the for loop stops.

## Another Example

```python
print(next(counter))
```

Result:

```
1
```

```python
print(next(counter))
```

Result:

```
2
```

## Version

Available in all Python versions.

---

# Abstraction

Abstraction hides implementation details and exposes only essential features to the user.

## Runtime

Runtime concept.

## Why

* Hides unnecessary details.
* Improves security and maintainability.
* Focuses on "what to do" instead of "how to do it".

## Types

* Abstract Class
* Abstract Method

## Library

`abc` (Abstract Base Class)

## Functions

* `ABC`
* `@abstractmethod`

## Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Bark")


d = Dog()
d.sound()
```

## Result

```
Bark
```

## Catch

* Cannot create an object of an abstract class.
* A child class must implement all abstract methods, otherwise it also becomes abstract.

## Version

Available in all Python versions using the `abc` module.

---

# SOLID Principles

SOLID principles are five design principles used in Object-Oriented Programming to create maintainable, flexible, and scalable software.

## Usage

* Scalable
* Easy evaluation

## Principles

## 1. S - Single Responsibility Principle (SRP)

* A class should have only one reason to change.
* One class = one responsibility.

## 2. O - Open/Closed Principle (OCP)

* Software entities should be open for extension but closed for modification.
* Add new behavior without changing existing code.

## 3. L - Liskov Substitution Principle (LSP)

* Child classes should be replaceable with parent classes without breaking the program.
* Subclass must behave like its superclass.

## 4. I - Interface Segregation Principle (ISP)

* A class should not be forced to implement methods it does not use.
* Prefer small, specific interfaces.

## 5. D - Dependency Inversion Principle (DIP)

* High-level modules should depend on abstractions, not concrete implementations.
* High-level classes should not directly depend on low-level classes.
* Depend on interfaces, not details.

---

# Builder Pattern

Builder pattern is a creational design pattern used to construct complex objects step by step.

## Why

* Avoids large constructors with many parameters.
* Creates objects in a flexible way.
* Separates object creation logic from the final object.

## Type

Creational Design Pattern.

## Components

* Builder → Defines steps to create an object.
* Concrete Builder → Implements object creation steps.
* Director → Controls the building process.
* Product → Final object being created.

---

# Strategy Pattern

Strategy pattern is a behavioral design pattern that allows selecting an algorithm or behavior at runtime without changing client code.

## Why

* Avoids large if-else conditions.
* Allows different behaviors to be swapped easily.
* Follows Open/Closed Principle.

## Type

Behavioral Design Pattern.

## Components

* Strategy → Defines common behavior/interface.
* Concrete Strategy → Implements different algorithms.
* Context → Uses a strategy object.

---

# Observer Pattern

Observer pattern is a behavioral design pattern where one object (Subject) notifies multiple dependent objects (Observers) automatically when its state changes.

## Why

* Creates loose coupling between objects.
* Automatically updates dependent objects.
* Useful for event-based systems.

## Type

Behavioral Design Pattern.

## Components

* Subject → Maintains state and observers.
* Observer → Receives updates.
* notify() → Sends updates to all observers.

## Advantages

* Loose coupling.
* Easy to add/remove observers.
* Supports event-driven programming.

## Usage

* YouTube subscribers getting notifications.
* Stock price alerts.
* GUI button click events.
* Weather updates.

---

# Adapter Pattern

Adapter pattern is a structural design pattern that allows incompatible classes to work together by converting one interface into another expected interface.

## Why

* Makes existing code reusable.
* Connects classes with incompatible interfaces.
* Avoids modifying existing classes.

## Type

Structural Design Pattern.

## Components

* Target → Interface expected by the client.
* Adapter → Converts the interface.
* Adaptee → Existing class with incompatible interface.
* Client → Uses the Target interface.

## Advantages

* Reuses existing classes.
* Reduces code changes.
* Improves compatibility.

## Examples

* USB-C adapter for old USB devices.
* Payment gateway adapters.
* API response format conversion.

## Catch

Too many adapters can make the design complex.

## Version

Commonly used in Object-Oriented Design.
