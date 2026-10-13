# Python Notes

## 📌 Keywords Covered
- Strings
- Immutable Strings
- Character Array
- Escape Characters
- Line Continuation (`\`)
- `ord()`
- `chr()`
- Raw String (`r""`)
- String Formatting
- `%` Formatting
- f-Strings
- `str.format()`
- `is` Operator
- String Interning
- `str.maketrans()`
- `str.translate()`
- ASCII
- Character Mapping

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
- SYN
- RES
- ANE
- NOTE

---

## Date

**11/07/2026**

---

# Strings

## Definition

A **string** is an immutable sequence of Unicode characters used to represent textual data.

> **Note**
>
> Although strings can be accessed like arrays using indexing, Python **does not have a separate character (`char`) data type**. A single character is simply a string of length `1`.

---

## Characteristics

- Immutable
- Sequence of characters
- Supports indexing and slicing
- Accepts:
  - Single quotes (`'`)
  - Double quotes (`"`)
  - Triple quotes (`'''` or `"""`) for multi-line strings

---

## Escape Characters

| Escape Character | Meaning |
|------------------|---------|
| `\n` | New Line |
| `\t` | Horizontal Tab |
| `\r` | Carriage Return |
| `\\` | Backslash |
| `\"` | Double Quote |
| `\'` | Single Quote |

---

# Line Continuation (`\`)

## Definition

A backslash (`\`) at the end of a line continues the statement onto the next line.

Adjacent string literals are automatically concatenated.

### USA

```python
s = "Hello" \
    "World"

print(s)
```

### RES

```text
HelloWorld
```

> **Correction**
>
> This is **line continuation in Python**, not specifically an IDLE feature. It works in any Python environment.

---

# `ord()`

## Definition

Returns the Unicode code point (ASCII value for ASCII characters) of a character.

### SYN

```python
ord(character)
```

### USA

```python
print(ord("A"))
```

### RES

```text
65
```

---

# `chr()`

## Definition

Returns the character corresponding to the given Unicode code point.

### SYN

```python
chr(integer)
```

### USA

```python
print(chr(65))
```

### RES

```text
A
```

---

# Raw String (`r""`)

## Definition

A raw string treats backslashes (`\`) as literal characters instead of escape characters.

### WHY

Commonly used for:

- Windows file paths
- Regular Expressions

### USA

```python
path = r"C:\Users\Admin\Documents"

print(path)
```

---

# String Formatting

## Definition

Formats values into strings using different techniques.

---

## 1. `%` Formatting

### SYN

```python
"%<specifier>" % (values)
```

### USA

```python
name = "Madhan"
id = 1

print("%s id %d" % (name, id))
```

---

## 2. f-Strings

### SYN

```python
f"{variable}"
```

### USA

```python
name = "Madhan"

print(f"{name}")
```

---

## 3. `str.format()`

### SYN

```python
"{}".format(values)
```

### USA

```python
name = "Madhan"
id = 1

print("{} {}".format(name, id))
```

---

# `is` Operator

## Definition

Checks whether **two variables refer to the same object in memory** (object identity).

It does **not** compare values.

### USA

```python
a = "python"
b = "python"

print(a is b)
```

### RES

```text
True
```

### ANE

```python
a = "python"

b = "".join(["py", "thon"])

print(a is b)
```

### RES

```text
False
```

### NOTE

Python often **interns** identical string literals, meaning they may reference the same memory location.

> **Correction**
>
> The note "`join()` is a force interning method" is incorrect.
>
> `join()` actually creates a **new string object**, which is why `a is b` becomes `False`. It does **not** force string interning.

---

# `str.maketrans()`

## Definition

Creates a translation table that can be used with `str.translate()` for character replacement or deletion.

---

## SYN

### Replace Characters

```python
str.maketrans(
    "source",
    "target"
)
```

### Delete Characters

```python
str.maketrans(
    "",
    "",
    "characters"
)
```

### Dictionary Mapping

```python
str.maketrans({
    "old": "new"
})
```

---

## PAR

| Parameter | Description |
|-----------|-------------|
| First Argument | Characters to replace |
| Second Argument | Replacement characters |
| Third Argument | Characters to delete |

---

## USA

### Delete Characters

```python
table = str.maketrans(
    "",
    "",
    "aeiou"
)

print(
    "education".translate(table)
)
```

### RES

```text
dctn
```

---

## ANE

### Dictionary Mapping

```python
table = str.maketrans({
    "a": "@",
    "e": "3",
    "i": "1",
    "o": "0"
})

text = "education"

print(
    text.translate(table)
)
```

### RES

```text
3duc@t10n
```

---

## ANE

### Character-to-Character Mapping

```python
table = str.maketrans(
    "abc",
    "xyz"
)

text = "abc"

print(
    text.translate(table)
)
```

### RES

```text
xyz
```

---

# Summary

| Topic | Purpose |
|--------|---------|
| Strings | Immutable sequence of Unicode characters |
| Escape Characters | Represent special characters such as newline and tab |
| Line Continuation (`\`) | Continue a statement onto the next line |
| `ord()` | Convert character to Unicode code point |
| `chr()` | Convert Unicode code point to character |
| Raw String (`r""`) | Preserve backslashes literally |
| `%` Formatting | Old-style string formatting |
| f-Strings | Modern string interpolation |
| `str.format()` | Positional and named string formatting |
| `is` Operator | Compare object identity (memory reference) |
| `str.maketrans()` | Create character translation table |
| `str.translate()` | Apply translation table to a string |