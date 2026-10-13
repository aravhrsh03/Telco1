# Python Notes

## 📌 Keywords Covered
- Python
- Dynamic Typing
- Scripted Language
- Interpreted Language
- Single Thread
- Object Identity
- `id()`
- Rebinding
- Variable References
- Extended Unpacking
- LEGB Rule
- Scope Resolution
- Bytes Data Type
- Shallow Copy
- Deep Copy
- `copy.copy()`
- List Slicing
- Slice Assignment
- Memory Management

---

## 🏷️ Tags & Keywords Used in Notes
- LIB = Library
- USA = Usage
- PAR = Parameters
- SYN = Syntax
- WHY = Why this is used
- EXA = Example
- MET = Methods
- CAT = Cannot have it
- ALI = Alias
- RES = Expected Result
- OPT = Optional
- ANE = Another Example
- FUN = Functions Used
- DAM = Data Members
- TYS = Types
- VER = Python Version
- USC = Use Cases

---

## Date

**07/07/2026**

---

# Python

## Definition

Python is a **high-level, dynamically typed, interpreted, and general-purpose programming language**. It emphasizes readability and supports multiple programming paradigms such as procedural, object-oriented, and functional programming.

---

## Characteristics

- Dynamic Typed
- Scripted Language
- Interpreted Language
- Single-threaded execution by default (one Python thread executes bytecode at a time in the standard CPython interpreter due to the Global Interpreter Lock (GIL))
- Created for **ABC language's successor** and general-purpose programming.

> **Correction**
>
> **"Satellite transaction (Created for)"** appears to be incorrect or incomplete. Python was created by **Guido van Rossum** as a successor to the **ABC programming language**, not specifically for satellite transactions.

---

# Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| **LIB** | Library |
| **USA** | Usage (Example Code) |
| **PAR** | Parameters |
| **SYN** | Syntax |
| **WHY** | Why this is used |
| **EXA** | Example |
| **MET** | Methods |
| **CAT** | Cannot Have It |
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

# Object Identity

## `id()`

### Definition

Returns the **Object Identity (Memory Identity)** of an object.

### Syntax

```python
id(object)
```

### Example

```python
num = 10
print(id(num))
```

### Result

- Displays the unique memory identity of the object.

---

# Rebinding

## Definition

Rebinding occurs when a variable that references one object is assigned to another object.

```python
num = 1
num = "string"
```

### Note

- This is **not overriding**.
- The variable now points to a completely different object.
- Therefore, the result of `id(num)` changes.

---

# Variable Reference

## Definition

- Every variable in Python is a **reference** to an object.
- Variables do not directly store values.
- They store references to objects in memory.

---

# Extended Unpacking

## Definition

Extended unpacking allows collecting multiple values into a single variable using `*`.

### Example

```python
f, *d, e = [1, 2, 3, 4]
```

### Result

```python
f = 1
d = [2, 3]
e = 4
```

---

# LEGB Rule

## Definition

Python searches for variables using the **LEGB** rule.

| Scope | Meaning |
|--------|---------|
| **L** | Local |
| **E** | Enclosing |
| **G** | Global |
| **B** | Built-in |

### Search Order

```text
Local
   ↓
Enclosing
   ↓
Global
   ↓
Built-in
```

---

# Bytes Data Type

## Definition

The `bytes` data type represents immutable sequences of bytes.

### Common Use Cases

- Audio data
- Image data
- Network packets
- Binary files

---

# Copying Objects

## Shallow Copy

### Definition

- Creates a new outer container.
- Inner mutable objects are still shared between copies.

```python
import copy

a = [1, 2, [1, 3]]
b = copy.copy(a)
```

### Characteristics

- Outer list is copied.
- Inner nested list points to the same reference.

---

## Deep Copy

### Definition

Creates a completely independent copy of the object, including all nested objects.

```python
import copy

b = copy.deepcopy(a)
```

### Characteristics

- New outer container.
- New nested objects.
- No shared references.

---

## `copy.copy()`

### Definition

Performs a **shallow copy**.

### Behavior

- Outer container is copied.
- Inner mutable objects remain shared.

---

# List Slice Assignment

## Update Slice

### Syntax

```python
<list-name>[start:end] = [value]
```

### Definition

Replaces the elements in the specified slice with the given values.

> **Correction**
>
> It does **not** update "all occurrences." It replaces the elements within the specified slice (`start:end`).

### Example

```python
nums = [1, 2, 3, 4]

nums[1:3] = [10, 20]
```

### Result

```python
[1, 10, 20, 4]
```

---

## Slice Assignment with Step

### Syntax

```python
<list-name>[start:end:step] = [value] * (total-step-count)
```

### Definition

Assigns values only to the positions selected by the specified step.

The number of assigned values **must match** the number of selected positions.

### Example

```python
nums = [1, 2, 3, 4, 5, 6]

nums[::2] = [10, 20, 30]
```

### Result

```python
[10, 2, 20, 4, 30, 6]
```

---

# Summary

| Topic | Key Point |
|--------|-----------|
| Dynamic Typing | Variable type determined at runtime |
| Scripted | Executed as scripts without compilation to machine code |
| Interpreted | Code executed by the Python interpreter |
| Single Thread | Executes one thread of Python bytecode at a time (CPython) |
| `id()` | Returns object memory identity |
| Rebinding | Variable points to a new object |
| Variable | Stores object references |
| Extended Unpacking | Collects remaining values using `*` |
| LEGB | Variable lookup order |
| Bytes | Used for binary data |
| Shallow Copy | Shares nested references |
| Deep Copy | Completely independent copy |
| `copy.copy()` | Performs shallow copy |
| Slice Assignment | Replaces elements in a specified slice |
| Slice Assignment with Step | Updates only stepped positions |