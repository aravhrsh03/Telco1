# Python Practice Problems (40 Questions)

A collection of Python interview and coding practice problems covering arrays, strings, dictionaries, sets, functions, generators, decorators, and mixed data structure problems.

---

# Arrays / Lists

## 1. Two Sum (Medium)

**Problem**

Given a list of integers, return the indices of two numbers that add up to the target.

**Input**

```python
nums = [2, 7, 11, 15]
target = 9
```

**Output**

```python
[0, 1]
```

---

## 2. Product of Array Except Self (Hard)

**Problem**

Return an array where each element is the product of every other element.

**Constraint**

- Do **not** use division.

**Input**

```python
[1, 2, 3, 4]
```

**Output**

```python
[24, 12, 8, 6]
```

---

## 3. Rotate Array

**Input**

```python
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
```

**Output**

```python
[5, 6, 7, 1, 2, 3, 4]
```

---

## 4. Move Zeros

**Input**

```python
[0, 1, 0, 3, 12]
```

**Output**

```python
[1, 3, 12, 0, 0]
```

---

## 5. Longest Consecutive Sequence

**Input**

```python
[100, 4, 200, 1, 3, 2]
```

**Output**

```python
4
```

**Explanation**

The longest consecutive sequence is:

```text
1, 2, 3, 4
```

---

# Strings (Using Lists & Loops)

## 6. Group Anagrams

**Input**

```python
["eat", "tea", "tan", "ate", "nat", "bat"]
```

**Output**

```python
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
```

---

## 7. Longest Substring Without Repeating Characters

**Input**

```python
"abcabcbb"
```

**Output**

```python
3
```

---

## 8. First Non-Repeating Character

**Input**

```python
"aabbccddef"
```

**Output**

```python
"e"
```

---

## 9. Valid Parentheses

**Input**

```python
"{[()]}"
```

**Output**

```python
True
```

---

## 10. Compress String

**Input**

```text
aaabbcccc
```

**Output**

```text
a3b2c4
```

---

# Dictionary

## 11. Frequency Sort

Sort numbers based on frequency (highest frequency first).

**Input**

```python
[4, 4, 1, 2, 2, 2, 3]
```

**Output**

```python
[2, 2, 2, 4, 4, 1, 3]
```

---

## 12. Top K Frequent Elements

**Input**

```python
nums = [1, 1, 1, 2, 2, 3]
k = 2
```

**Output**

```python
[1, 2]
```

---

## 13. Find Duplicate Files

Given folders and filenames:

```python
{
    "A": ["a.txt", "b.txt"],
    "B": ["x.txt", "y.txt"],
    "C": ["b.txt", "z.txt"]
}
```

Find duplicate filenames.

---

## 14. Merge Dictionaries (Deep Merge)

Merge nested dictionaries recursively.

**Input**

```python
d1 = {
    "a": {
        "x": 1
    }
}

d2 = {
    "a": {
        "y": 2
    }
}
```

**Output**

```python
{
    "a": {
        "x": 1,
        "y": 2
    }
}
```

---

# Sets

## 15. Common Set Operations (Without Built-in Methods)

Given

```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
```

Implement **without using built-in set methods**:

- Intersection
- Difference
- Symmetric Difference
- Union

---

## 16. Sudoku Validator

Using sets, verify whether Sudoku rows contain duplicates.

---

## 17. Missing Number

Numbers from **1 to 100** are present except one.

Find the missing number using sets.

---

# Functions

## 18. Implement `map()`

Create your own version:

```python
my_map(function, iterable)
```

Do not use Python's built-in `map()`.

---

## 19. Implement `filter()`

Create your own implementation without using `filter()`.

---

## 20. Implement `reduce()`

Create your own implementation without importing `functools`.

---

# Lambda Functions

## 21. Sort Employees

```python
employees = [
    ("John", 50000),
    ("Alex", 90000),
    ("David", 70000)
]
```

Sort by:

- Salary
- Name
- Length of name

---

## 22. Nested Sorting

```python
[
    ("John", 25, 60000),
    ("Alex", 20, 90000),
    ("David", 25, 70000)
]
```

Sort by:

1. Age
2. Salary (descending)
3. Name

---

# Generators

## 23. Prime Number Generator

Generate prime numbers forever.

Example output:

```text
2
3
5
7
11
13
17
...
```

---

## 24. Fibonacci Generator

Generate Fibonacci numbers forever.

Example output:

```text
0
1
1
2
3
5
8
13
...
```

---

## 25. File Reader Generator

Read a large text file **line by line** using `yield`.

---

# Decorators

## 26. Retry Decorator

Create a decorator that retries a function up to **5 times** before failing.

---

## 27. Cache Decorator

Create a decorator that stores previous function results (memoization).

---

## 28. Access Control Decorator

Create an `@admin` decorator so that only admin users can execute the function.

---

## 29. Execution Timer

Create a decorator that prints the execution time of a function.

---

## 30. Function Logger

Create a decorator that logs:

- Function arguments
- Return value
- Execution time
- Exceptions

---

# Mixed Problems

## 31. Flatten Nested List

**Input**

```python
[1, [2, [3, [4]], 5], 6]
```

**Output**

```python
[1, 2, 3, 4, 5, 6]
```

---

## 32. Deep Dictionary Flatten

**Input**

```python
{
    "a": {
        "b": {
            "c": 10
        }
    }
}
```

**Output**

```python
{
    "a.b.c": 10
}
```

---

## 33. Matrix Transpose

**Input**

```python
[
    [1, 2, 3],
    [4, 5, 6]
]
```

**Output**

```python
[
    [1, 4],
    [2, 5],
    [3, 6]
]
```

---

## 34. Spiral Matrix

Print the matrix

```text
1 2 3
4 5 6
7 8 9
```

in spiral order:

```text
1 2 3 6 9 8 7 4 5
```

---

## 35. Rotate Matrix 90°

**Input**

```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Output**

```python
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

---

## 36. Pascal Triangle

Generate the first **n** rows of Pascal's Triangle.

---

## 37. Merge Intervals

**Input**

```python
[[1, 3], [2, 6], [8, 10], [15, 18]]
```

**Output**

```python
[[1, 6], [8, 10], [15, 18]]
```

---

## 38. Interval Intersection

**Input**

```python
A = [[1, 5], [10, 14]]
B = [[2, 6], [8, 10]]
```

Find all interval intersections.

---

## 39. LRU Cache Simulation

Implement an LRU Cache using only:

- List
- Dictionary

Do not use external libraries.

---

## 40. Mini Database

Implement the following operations using only **lists** and **dictionaries**:

- `insert()`
- `update()`
- `delete()`
- `search()`
- `sort()`

---