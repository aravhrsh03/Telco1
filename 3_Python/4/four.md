# Python Notes

## 📌 Keywords Covered
- Recursion
- Recursive Function
- Base Condition
- Indirect Recursion
- Mutual Recursion
- Tail Recursion
- Head Recursion
- Tree Recursion
- Nested Recursion
- Linear Recursion
- Binary Recursion
- N-ary Recursion
- Graph Traversal
- DFS
- Fibonacci
- Factorial
- McCarthy 91 Function
- Backtracking
- Divide and Conquer
- Binary Tree

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
- WHY
- SYN
- PAR
- RES
- EXA
- ANE
- CAT
- NOTE

---

## Date

**10/07/2026**

---

# Recursion

## Definition

**Recursion** is a programming technique in which a function **calls itself** to solve a problem by breaking it into smaller subproblems.

Every recursive function should contain:

- **Base Condition** (Stopping condition)
- **Recursive Call**

---

# Types of Recursion

## 1. Indirect Recursion (Mutual Recursion)

### Definition

Two or more functions recursively call each other.

### ALI

- Mutual Recursion

### USA

```python
def even(n):
    if n == 0:
        return True
    return odd(n - 1)


def odd(n):
    if n == 0:
        return False
    return even(n - 1)


print(even(10))
print(odd(7))
```

### RES

```text
True
True
```

> **Correction**
>
> The original code contained:
>
> ```python
> if n == 0":
> ```
>
> which has been corrected to:
>
> ```python
> if n == 0:
> ```

---

## 2. Tail Recursion

### Definition

The recursive call is the **last executable statement** in the function.

### WHY

- Easier to optimize in languages that support **Tail Call Optimization (TCO)**.

### NOTE

Python **does not perform Tail Call Optimization (TCO)**.

The reason is **not because Python uses the heap**. Python intentionally keeps every recursive call on the call stack to preserve complete stack traces for debugging.

### USA

```python
def show(n):
    if n == 0:
        return

    print(n)

    show(n - 1)


show(5)
```

### RES

```text
5
4
3
2
1
```

---

## 3. Head Recursion

### Definition

The recursive call happens **immediately after the base condition**, before any remaining work.

### USA

```python
def show(n):
    if n == 0:
        return

    show(n - 1)

    print(n)


show(5)
```

### RES

```text
1
2
3
4
5
```

---

## 4. Tree Recursion

### Definition

A function makes **multiple recursive calls**, producing a tree-like execution.

### WHY

Used in:

- Fibonacci
- Binary Trees
- Backtracking

### USA

```python
def fib(num):
    if num <= 1:
        return num

    return fib(num - 1) + fib(num - 2)


print(fib(5))
```

### RES

```text
5
```

---

## 5. Nested Recursion

### Definition

A recursive call is passed as an argument to another recursive call.

### WHY

Used when:

- The next recursive computation depends on the result of another recursive call.
- Common in theoretical recursion problems.

### SYN

```python
def func(n):

    if base_condition:
        return value

    return func(func(n - 1))
```

### USA

```python
def nested(n):

    if n > 100:
        return n - 10

    return nested(
        nested(n + 11)
    )


print(nested(95))
```

### RES

```text
91
```

### EXA

- McCarthy 91 Function

---

## 6. Linear Recursion

### Definition

Each recursive call creates **exactly one** recursive call.

### WHY

Used for:

- Number traversal
- String traversal
- Linked List traversal
- Factorial

### SYN

```python
def func(n):

    if base_condition:
        return

    func(n - 1)
```

### USA

```python
def show(n):

    if n == 0:
        return

    print(n)

    show(n - 1)


show(5)
```

### RES

```text
5
4
3
2
1
```

### ANE

```python
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


print(factorial(5))
```

### RES

```text
120
```

---

## 7. Binary Recursion

### Definition

Each recursive call generates **two recursive calls**.

### WHY

Commonly used in:

- Divide and Conquer
- Fibonacci
- Binary Tree Traversal
- Backtracking

### SYN

```python
def func(n):

    if base_condition:
        return

    func(n - 1)
    func(n - 2)
```

### USA

```python
def fib(n):

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(fib(5))
```

### RES

```text
5
```

### EXA

- Fibonacci
- Binary Tree Traversal

### CAT

Repeated recursive calls make this approach inefficient.

Time Complexity for Fibonacci:

```text
O(2ⁿ)
```

---

## 8. N-ary Recursion

### Definition

Each recursive call generates **N recursive calls**, where **N > 2**.

### ALI

- N Array Recursion

> **Correction**
>
> The standard term is **N-ary Recursion**, although your note refers to it as **N Array Recursion**.

### WHY

Used for:

- Graph Traversal
- N-ary Trees
- Game Trees
- Combinations
- Permutations
- Backtracking

### PAR

Depends on the **branching factor (N)**.

### SYN

```python
def func(node):

    for child in children:
        func(child)
```

### USA

```python
graph = {
    "A": ["B", "C", "D"],
    "B": [],
    "C": [],
    "D": []
}


def dfs(node):

    print(node)

    for child in graph[node]:
        dfs(child)


dfs("A")
```

### RES

```text
A
B
C
D
```

### ANE

```python
def print_paths(level):

    if level == 0:
        return

    for _ in range(3):
        print_paths(level - 1)


print_paths(2)
```

### EXA

- DFS on N-ary Trees
- Graph Traversal
- Game Search
- Backtracking with Multiple Choices

### CAT

Can become computationally expensive because the number of recursive calls grows exponentially with the branching factor.

---

# Comparison of Recursion Types

| Recursion Type | Recursive Calls per Function | Common Use Cases |
|----------------|------------------------------|------------------|
| **Indirect (Mutual)** | One (through another function) | Even/Odd checking |
| **Tail** | One (last statement) | Countdown, Iterative-style recursion |
| **Head** | One (before processing) | Reverse processing |
| **Tree** | Multiple | Fibonacci, Trees |
| **Nested** | Recursive call inside another recursive call | McCarthy 91 Function |
| **Linear** | One | Factorial, Linked Lists |
| **Binary** | Two | Fibonacci, Binary Trees |
| **N-ary** | N (>2) | Graphs, DFS, Backtracking |

---

# Summary

- **Recursion** solves problems by repeatedly calling the same function.
- Every recursive function should have a **base condition** to prevent infinite recursion.
- **Tail** and **Head** recursion differ in where the recursive call occurs.
- **Tree**, **Binary**, and **N-ary** recursion create multiple recursive branches.
- **Nested** recursion uses the result of one recursive call as the input to another.
- **Linear** recursion makes exactly one recursive call per function invocation.
- Python supports all these recursion styles but **does not optimize Tail Recursion (no Tail Call Optimization)**.