# Python Notes

## 📌 Keywords Covered
- Python
- `reduce()`
- `enumerate()`
- `iter()`
- `next()`
- Iterator
- One-Hot Encoding
- `namedtuple`
- Set
- FrozenSet
- Nested FrozenSet
- Set Operations
- Combinations
- `itertools`
- `zip()`
- `hash()`
- Dictionary (`dict`)
- Hashable
- Unhashable
- Functional Programming
- Collections Module
- Functools Module

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
- CAT
- ALI
- RES
- OPT
- NOTE

---

## Date

**08/07/2026**

---

# `reduce()`

## Definition

`reduce()` applies a function cumulatively to the elements of an iterable and reduces them to a **single value**.

### LIB

```python
functools
```

### SYN

```python
reduce(<callback-function>, iterable[, initializer])
```

> **Correction**
>
> `initializer` is **optional**, so the correct syntax is:
>
> ```python
> reduce(function, iterable[, initializer])
> ```

### USA

```python
from functools import reduce

numbers = [10, 20, 30, 40]

res = reduce(lambda x, y: x if x > y else y, numbers)

print(res)
```

### RES

```python
40
```

---

# `enumerate()`

## Definition

Returns an **enumerate object (iterator)** containing pairs of:

```text
(index, current_value)
```

### PAR

| Parameter | Description |
|-----------|-------------|
| `start` | Starting index (Default = `0`) |

### USA

```python
for ind, val in enumerate("MNC", start=3):
    print(ind, val)
```

### RES

```text
3 M
4 N
5 C
```

---

# `iter()`

## Definition

Creates an **iterator object** from an iterable.

### SYN

```python
iterator = iter(<iterable>)
```

### USA

```python
nums = [1, 2, 3]

it = iter(nums)
```

---

# `next()`

## Definition

Returns the next value from an iterator.

### SYN

```python
next(<iterator>)
```

### PAR

| Parameter | Description |
|-----------|-------------|
| `default` | Value returned when the iterator is exhausted |

### USA

```python
next(iterator, "Completed")
```

### WHY

If the iterator reaches the end:

- Returns the default value (if provided).
- Otherwise raises `StopIteration`.

> **Correction**
>
> The iterator starts **before the first element**, not at index `-1`.

---

# One-Hot Encoding

## Definition

Represents categorical values using **0s and 1s**.

### EXA

```text
Apple  = [1, 0, 0]
Orange = [0, 1, 0]
Mango  = [0, 0, 1]
```

### WHY

- Matching category → `1`
- Non-matching category → `0`

Used in Machine Learning models.

---

# `namedtuple`

## Definition

Creates lightweight immutable objects similar to:

- Struct (C/C++)
- Data Class
- Pydantic BaseModel (conceptually, but without validation)

### LIB

```python
collections
```

### PAR

| Parameter | Description |
|-----------|-------------|
| Tuple Name | Name of the new tuple type |
| Variable Names | Field names |

### SYN

```python
namedtuple(<tuple-name>, [field_names])
```

### USA

```python
from collections import namedtuple

Student = namedtuple(
    "Student",
    ["name", "id", "marks"]
)

s = Student("Steve Jobs", 111, 100)

print(s.name)
```

### RES

```text
Steve Jobs
```

---

# Set

## Definition

An unordered collection containing **unique values**.

### CAT

- List
- Set

These cannot be stored directly as set elements because they are **unhashable**.

---

## MET

### `remove()`

Removes the value.

If unavailable:

- Raises `KeyError`

---

### `discard()`

Removes the value.

If unavailable:

- No error is raised.

---

### `pop()`

Removes and returns an **arbitrary** element.

> **Correction**
>
> It is **not truly random**. It removes an arbitrary element.

---

### `union()`

Combines multiple sets.

### ALI

```python
|
```

---

### `intersection()`

Returns common values.

### ALI

```python
&
```

---

### `difference()`

Returns values present in Set-1 but not Set-2.

### ALI

```python
-
```

---

### `symmetric_difference()`

Returns values excluding common elements.

### ALI

```python
^
```

---

# FrozenSet

## Definition

Immutable version of a set.

### SYN

```python
fs = frozenset(set_object)
```

---

## MET

- `union()`
- `intersection()`
- `difference()`
- `symmetric_difference()`

---

# Nested FrozenSet

## Definition

A `frozenset` can contain other `frozenset` objects because they are hashable.

### RES

```python
frozenset({
    frozenset({...}),
    frozenset({...})
})
```

### USA

```python
f1 = frozenset({1, 2})

f2 = frozenset({3, 4})

fs = {f1, f2}
```

### SYN

```python
{
    <frozenset_object>,
    <frozenset_object>
}
```

### NOTE

Works for:

- `frozenset`

Does **not** work for:

- `set`

---

# Combinations

## Definition

Returns all possible combinations as tuples.

### LIB

```python
itertools
```

### SYN

```python
combinations(iterable, r)
```

> **Correction**
>
> The syntax is:
>
> ```python
> combinations(iterable, r)
> ```
>
> It does **not** take start index and end index.

### USA

```python
from itertools import combinations

power = [1, 2, 3]

for r in range(len(power) + 1):
    print(list(combinations(power, r)))
```

---

# Combine Two Sets

## Problem

```text
Error: unhashable type: 'set'
```

Occurs when trying to place a set inside another set.

### SYN

```python
result = {
    *set1,
    *set2
}
```

### NOTE

`*` unpacks all values.

### USA

```python
a = {1, 2, 3}

b = {3, 4}

c = {*a, *b}

print(c)
```

### RES

```python
{1, 2, 3, 4}
```

---

# `zip()`

## Definition

Combines multiple iterables into pairs (tuples).

### SYN

```python
collection_type(
    zip(iterable1, iterable2)
)
```

### USA

```python
s1 = {"a", "b"}

s2 = {10, 11}

print(list(zip(s1, s2)))
```

### NOTE

- Stops when the shortest iterable ends.
- Extra values are ignored.

---

# `hash()`

## Definition

Returns the hash value of a hashable object.

### SYN

```python
hash(value)
```

### USA

```python
hash("string")
```

### NOTE

Accepts:

- Integer
- Float
- String
- Tuple (if hashable)
- FrozenSet

Does **not** accept:

- List
- Set
- Dictionary

because they are **unhashable**.

---

# Dictionary (`dict`)

## Definition

Stores data as **key-value pairs**.

Keys must be **hashable**.

### NOTE

Keys **cannot** be:

- List
- Set
- Dictionary

because they are **unhashable**.

---

## MET

### `get()`

Returns the value for a key.

If the key is unavailable:

- Returns the fallback value.
- If no fallback is provided, returns `None`.

#### PAR

| Parameter | Description |
|-----------|-------------|
| `key` | Dictionary key |
| `default` *(OPT)* | Fallback value |

---

### `items()`

Returns:

```text
(key, value)
```

pairs.

---

### `keys()`

Returns all keys.

---

### `values()`

Returns all values.

---

# Summary

| Topic | Purpose |
|--------|---------|
| `reduce()` | Reduce iterable to a single value |
| `enumerate()` | Iterate with index |
| `iter()` | Create iterator |
| `next()` | Fetch next iterator value |
| One-Hot Encoding | Encode categories using 0s and 1s |
| `namedtuple` | Lightweight immutable object |
| Set | Unique unordered collection |
| FrozenSet | Immutable set |
| Nested FrozenSet | Store frozensets inside a set |
| `combinations()` | Generate all combinations |
| Set Unpacking (`*`) | Merge multiple sets |
| `zip()` | Pair multiple iterables |
| `hash()` | Generate hash value |
| Dictionary | Store hashable key-value pairs |