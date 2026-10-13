# Python Notes

## 📌 Keywords Covered
- `zip_longest()`
- `reversed()`
- `sorted()`
- `for` Loop
- `else` with `for`
- `any()`
- `all()`
- `itertools.count()`
- `itertools.cycle()`
- `itertools.islice()`
- `match` Statement
- Structural Pattern Matching
- Functions
- Positional-Only Arguments (`/`)
- Keyword-Only Arguments (`*`)
- Variable-Length Arguments (`*args`)
- Keyword Variable-Length Arguments (`**kwargs`)
- Lambda Function
- Anonymous Function
- Generator
- `yield`
- Decorator
- Function Wrapping

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

## 🏷️ Tags & Keywords Used in Notes

- LIB
- USA
- PAR
- SYN
- WHY
- EXA
- MET
- ALI
- NOTE
- ANE
- OPT

---

## Date

**09/07/2026**

---

# `zip_longest()`

## Definition

Combines multiple iterables into pairs like `zip()`, but continues until the **longest iterable** is exhausted.

Missing values are replaced using the specified `fillvalue`.

### LIB

```python
itertools
```

### SYN

```python
<collection_type>(
    zip_longest(
        iterable1,
        iterable2,
        fillvalue=<value>
    )
)
```

### PAR

| Parameter | Description |
|-----------|-------------|
| `fillvalue` | Value used when one iterable has no corresponding element |

### USA

```python
from itertools import zip_longest

s1 = {"a", "b"}
s2 = {10, 11}

print(
    list(
        zip_longest(
            s1,
            s2,
            fillvalue="NA"
        )
    )
)
```

### NOTE

Solves the limitation of `zip()` by preserving extra values from the longer iterable.

---

# `reversed()`

## Definition

Returns a reverse iterator over the given iterable.

### SYN

```python
reversed(<iterable>)
```

### USA

```python
nums = [1, 2, 3]

print(list(reversed(nums)))
```

### RES

```python
[3, 2, 1]
```

---

# `sorted()`

## Definition

Returns a **new sorted list** from any iterable.

### SYN

```python
sorted(iterable)
```

### PAR

| Parameter | Description |
|-----------|-------------|
| `reverse` | `True` for descending order |

### USA

```python
nums = [4, 2, 1]

print(sorted(nums))
```

```python
print(sorted(nums, reverse=True))
```

---

# `for` Loop

## Definition

Iterates over an iterable.

### USA

```python
for value in iterable:
    print(value)
else:
    print("Completed")
```

### NOTE

- `else` executes when the loop completes normally.
- `else` does **not** execute if the loop exits using `break`.
- The loop variable remains accessible inside the `else` block.

> **Correction**
>
> A `for` loop iterates over an iterable. It is **not limited to `(start, stop, step)`**. Those values are commonly supplied using `range(start, stop, step)`.

---

# `any()`

## Definition

Returns:

- `True` if **at least one** element is truthy.
- Otherwise `False`.

### USA

```python
any([False, False, True])
```

### RES

```python
True
```

---

# `all()`

## Definition

Returns:

- `True` if **every** element is truthy.
- Otherwise `False`.

### USA

```python
all([True, True, True])
```

### RES

```python
True
```

---

# `count()`

## Definition

Creates an infinite counter.

### LIB

```python
itertools
```

### SYN

```python
count(start=0, step=1)
```

### USA

```python
from itertools import count

for i in count(1):
    print(i)

    if i == 5:
        break
```

---

# `cycle()`

## Definition

Repeats an iterable infinitely.

### LIB

```python
itertools
```

### SYN

```python
cycle(iterable)
```

### USA

```python
from itertools import cycle

for x in cycle("ABC"):
    print(x)

    if x == "C":
        break
```

### ANE

```python
from itertools import cycle

colors = cycle(
    ["RED", "GREEN", "BLUE"]
)

for _ in range(7):
    print(next(colors))
```

---

# `islice()`

## Definition

Returns selected items from an iterator without consuming everything.

Frequently used with `cycle()` to limit infinite iterators.

### LIB

```python
itertools
```

### SYN

```python
islice(iterable, stop)
```

or

```python
islice(iterable, start, stop, step)
```

### USA

```python
from itertools import cycle, islice

for x in islice(
    cycle("ABC"),
    10
):
    print(x)
```

### NOTE

Prints the first **10** values generated from the infinite cycle.

> **Correction**
>
> Import should be:
>
> ```python
> from itertools import cycle, islice
> ```
>
> not
>
> ```python
> from itertools import cycle.islice
> ```

---

# `match` Statement

## ALI

```text
switch
```

## Definition

Performs structural pattern matching (introduced in Python 3.10).

### SYN

```python
match expression:
    case pattern:
        ...
    case _:
        ...
```

### USA

```python
a = 1

match a:

    case 1:
        print(1)

    case _:
        print("Fail")
```

### NOTE

`case _` represents the default case.

> **Correction**
>
> `case` uses **patterns**, not arbitrary `if` conditions. Guard conditions can be added using `if` after a pattern (e.g., `case x if x > 0:`).

---

# Functions

## Definition

Functions are reusable blocks of code invoked by their function name.

---

## Notes

- A function can return multiple values (comma-separated), which are returned as a tuple.
- Python **does not support traditional function overloading** based solely on different parameter signatures. A later function definition with the same name replaces the earlier one.
- Function overriding is achieved in object-oriented programming through inheritance.

> **Correction**
>
> The note "Overloading is allowed, not overriding" is incorrect for standard Python function definitions. Multiple definitions with the same name overwrite previous ones.

---

# Positional-Only Arguments (`/`)

## Definition

Parameters before `/` can only be supplied positionally.

### SYN

```python
def func(a, b, /):
    ...
```

### USA

```python
def posi(a1, b1, /):
    print(a1, b1)

posi(1, 2)
```

### ANE

```python
def posi2(a1, b1, /, x, y):
    print(a1 + b1)

posi2(
    1,
    2,
    x=1,
    y=2
)
```

> **Correction**
>
> The original syntax missed a comma before `/` in the second example.

---

# Keyword-Only Arguments (`*`)

## Definition

Parameters after `*` must be passed using keyword arguments.

### USA

```python
def keyw(name, *, city):
    print(name, city)

keyw(
    "madhan",
    city="chennai"
)
```

---

# `*args`

## Definition

Accepts any number of positional arguments.

### USA

```python
def fun(*a):
    print(sum(a))

fun(1, 2, 3, 4)
```

---

# `**kwargs`

## Definition

Accepts any number of keyword arguments.

### USA

```python
def fun(**kwargs):
    print(kwargs)

fun(
    key1=1,
    key2=2
)
```

---

# Lambda Function

## Definition

Anonymous function stored in a variable or passed directly as an argument.

### SYN

```python
variable = lambda parameters: expression
```

### USA

```python
add = lambda x, y: x + y

print(add(8, 9))
```

---

# Generator

## Definition

Generates values one at a time using `yield` instead of returning all values at once.

Useful for streaming large datasets.

### SYN

```python
def func():
    yield value
```

### USA

```python
def numbers():

    for i in range(1, 10000):
        yield i

g = numbers()

print(next(g))
```

> **Correction**
>
> `next()` should receive the generator object:
>
> ```python
> next(g)
> ```
>
> not
>
> ```python
> next()
> ```

---

# Decorator

## Definition

A decorator is a function that wraps another function to extend or modify its behavior without changing the original function.

### USA

```python
def deco(func):

    def wrap():
        print("Before")

        func()

        print("After")

    return wrap


@deco
def outer():
    print("Outer")


outer()
```

### RES

```text
Before
Outer
After
```

---

# Summary

| Topic | Purpose |
|--------|---------|
| `zip_longest()` | Zip until the longest iterable ends |
| `reversed()` | Reverse iterator |
| `sorted()` | Return sorted list |
| `for...else` | Execute `else` if loop completes normally |
| `any()` | Check if at least one element is truthy |
| `all()` | Check if all elements are truthy |
| `count()` | Infinite numeric counter |
| `cycle()` | Infinite iterable repetition |
| `islice()` | Slice an iterator |
| `match` | Structural pattern matching |
| Functions | Reusable code blocks |
| `/` | Positional-only parameters |
| `*` | Keyword-only parameters |
| `*args` | Variable positional arguments |
| `**kwargs` | Variable keyword arguments |
| Lambda | Anonymous function |
| Generator | Lazy value generation using `yield` |
| Decorator | Wrap and extend function behavior |