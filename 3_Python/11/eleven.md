# Python Multithreading, CPU Bound Processing & Regular Expression (Regex)

## Keywords

Python, Multithreading, Threading, Thread, Main Thread, Daemon Thread, Non-Daemon Thread, ThreadPool, CPU Bound, Compute Bound, Processing Bound, GIL, Global Interpreter Lock, Multiprocessing, Process, Parallel Execution, Process Management, Process Methods, Process ID, Regular Expression, Regex, re Module, Pattern Matching, Text Search, Text Extraction, Text Replacement, Regex Patterns, Character Sets, Quantifiers, Symbols, Validation.

## Original Keywords / Tags From Notes

- [LIB]
- [USA]
- [MET]
- [WHY]
- [EXA]
- [PAR]
- [SYN]
- [FUN]
- [DAM]
- [ALI]
- [RES]
- [OPT]
- [CAT]
- [ANE]
- [TYS]
- [VER]
- [USC]

---

# Date

17/07/2026

---

# Multithreading

Multithreading is a technique where multiple threads execute within the same process.

## Characteristics

- Same memory is shared between n number of threads.
- Threads share:
    - Same file.
    - Same GIL.
    - Same variables.
- Threads are lightweight execution units inside a process.

## Library

```python
threading
````

---

# Thread Example

```python
import threading


def worker():
    print("Working thread..")


t = threading.Thread(target=worker)

t.start()

t.join()
```

---

# Thread Methods

## join()

`join()` is not mandatory.

### Purpose

* Without `join()`, the thread will not join with the main thread.
* Used to wait for the current thread to complete execution before remaining code runs.

---

# CPU Bound

CPU-bound tasks are tasks where the CPU performs most of the work.

## Characteristics

* Heavy calculations.
* Uses CPU continuously instead of waiting.
* Performance depends on CPU speed.
* Uses multiple CPU cores for better performance.
* In Python, multithreading does not improve CPU-bound tasks because of GIL.
* Best solution is multiprocessing using separate processes.

---

# Why Use Multiprocessing for CPU Bound Tasks

* To perform heavy calculations faster.
* To use multiple CPU cores.
* To avoid GIL limitations.
* To improve execution speed of CPU-intensive programs.

---

# Examples of CPU Bound Tasks

* Prime number calculation.
* Matrix multiplication.
* Image processing.
* Video rendering.
* Machine Learning training.
* Password hashing.
* Scientific calculations.
* Data compression.

---

# Multiprocessing Library

```python
multiprocessing
```

---

# CPU Bound Multiprocessing Example

```python
from multiprocessing import Process


def worker():

    total = 0

    for i in range(10000000):
        total += i

    print("Calculation Finished")


p = Process(target=worker)

p.start()

p.join()
```

---

# Process Parameters

```python
Process(
    target=function_name,
    args=(arg1, arg2),
    name="ProcessName",
    daemon=False
)
```

---

# Process Syntax

```python
from multiprocessing import Process


p = Process(
    target=function_name,
    args=(arguments,)
)

p.start()

p.join()
```

---

# Process Methods

## start()

* Starts the process.
* Executes the target function.

---

## join()

* Not mandatory.
* Without this, the main program continues executing.
* Used to wait until the current process finishes.

---

## is_alive()

* Returns `True` if the process is running.
* Returns `False` if the process has finished.

---

## terminate()

* Stops the process immediately.

---

## close()

* Releases process resources.
* Used in some multiprocessing objects.

---

# Process Functions

| Function      | Description                       |
| ------------- | --------------------------------- |
| `Process()`   | Creates a new process             |
| `start()`     | Starts execution                  |
| `join()`      | Waits for process completion      |
| `is_alive()`  | Checks whether process is running |
| `terminate()` | Stops the process                 |

---

# Process Data Members

## p.pid

* Returns Process ID.

## p.name

* Returns process name.

## p.daemon

* Returns daemon status.

---

# Aliases of CPU Bound

* CPU Intensive Task.
* Compute Bound.
* Processing Bound.

---

# Result

* Heavy calculations execute faster.
* Multiple CPU cores work together.
* Better performance for CPU-intensive programs.
* Main process waits when `join()` is used.

---

# Optional Process Parameters

## args

* Optional.
* Passes arguments to the function.

## name

* Optional.
* Gives a custom process name.

## daemon

* Optional.
* Runs process in background.

---

# Catch

* Cannot efficiently use multithreading for CPU-bound tasks in Python.
* Cannot achieve true parallel execution using threads because of GIL.
* Not suitable for waiting tasks like file reading or downloading.

---

# Another Multiprocessing Example

```python
from multiprocessing import Process


def square():

    for i in range(5):
        print(i * i)


p = Process(target=square)

p.start()

p.join()
```

---

# Types of CPU Bound Processing

* Single CPU-bound task.
* Multi-process CPU-bound task.
* Parallel CPU-bound task.

---

# Version

* Python 2.6+ (multiprocessing introduced).
* Python 3.x (Recommended).

---

# Usage

* Scientific computing.
* Machine Learning.
* Artificial Intelligence.
* Image processing.
* Video rendering.
* Data analysis.
* Password encryption.
* Cryptography.
* Mathematical simulations.
* Large numerical computations.

---

# Easy Remember

```
CPU Bound
    ↓
Heavy Calculations
    ↓
Uses CPU Continuously
    ↓
Multithreading ❌ (GIL)
    ↓
Multiprocessing ✅
    ↓
Uses Multiple CPU Cores
    ↓
Faster Execution
```

---

# Types of Threads

## Main Thread

* Available in Python.
* Default thread that starts program execution.

---

## Non-Daemon Thread

* Alive until it completes execution.
* Main thread waits for this thread to complete.

---

## Daemon Thread

* Background thread.
* Runs in the background.
* Does not prevent program termination.

---

# ThreadPool

ThreadPool manages multiple threads and distributes tasks among them.

## Example

```python
from concurrent.futures import ThreadPoolExecutor


def square(x):
    return x * x


with ThreadPoolExecutor(max_workers=3) as executor:

    result = executor.map(square, [1, 2, 3, 4, 5])


print(list(result))
```

---

# Regular Expression (Regex)

Regular Expression is a pattern used to search, match, extract, and replace text.

## Library

Python library:

```python
re
```

---

# Regex Example

```python
import re


result = re.search(r"\d+", "Age 25")


print(result.group())
```

## Result

```
25
```

---

# Why Use Regex

* Data validation.
* Text searching.
* Data extraction.
* Text replacement.

---

# Basic Patterns

| Pattern | Description             |
| ------- | ----------------------- |
| `\d`    | Digit (0-9)             |
| `\D`    | Non-digit               |
| `\w`    | Word (a-z, A-Z, 0-9, _) |
| `\W`    | Non-word                |
| `\s`    | Space                   |
| `\S`    | Non-space               |
| `.`     | Any character           |

---

# Character Set

| Pattern  | Description    |
| -------- | -------------- |
| `[abc]`  | Match a/b/c    |
| `[a-z]`  | Lowercase      |
| `[A-Z]`  | Uppercase      |
| `[0-9]`  | Numbers        |
| `[^0-9]` | Except numbers |

---

# Quantifiers

| Symbol  | Description     |
| ------- | --------------- |
| `*`     | 0 or more       |
| `+`     | 1 or more       |
| `?`     | Optional        |
| `{n}`   | Exactly n times |
| `{n,m}` | Range           |

---

# Symbols

| Symbol | Description |    |
| ------ | ----------- | -- |
| `^`    | Start       |    |
| `$`    | End         |    |
| `      | `           | OR |
| `()`   | Group       |    |

---

# Regex Methods

## re.match()

* Matches from beginning.

## re.search()

* Finds first match.

## re.findall()

* Finds all matches.

## re.sub()

* Replaces text.

## re.split()

* Splits string.

---

# Regex Syntax

```python
re.method(pattern, string)
```

---

# Regex Examples

## Numbers

```python
re.findall(r"\d+", "A10 B20")
```

Output:

```python
['10', '20']
```

---

## Phone Validation

```python
r"^[0-9]{10}$"
```

---

## Email Validation

```python
r"^[\w.-]+@[\w.-]+.\w+$"
```

---

# Regex Parameters

## pattern

* Search rule.

## string

* Input text.

## replacement

* New value.

---

# Catch

* Not suitable for complex parsing.
* Large regex becomes difficult to maintain.

---

# Usage

* Email validation.
* Phone validation.
* Password checking.
* Data extraction.
* Log processing.

---

# Version

Python 3.x

---

# Remember

```
\d → Number

\w → Word

\s → Space

+ → One or more

* → Zero or more

? → Optional

^ → Start

$ → End
```