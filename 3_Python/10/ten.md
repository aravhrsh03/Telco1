# Python Task, Process, Thread, GIL & Multiprocessing

## Keywords

Python, Task, Process, Thread, Multithreading, Multiprocessing, Parallel Execution, Concurrency, CPU Core, Memory Management, GIL, Global Interpreter Lock, CPython, Process Management, multiprocessing Module, Process, Pool, Queue, Pipe, Lock, Semaphore, Event, Condition, Value, Array, Manager, Synchronization.

## Original Keywords / Tags From Notes

- [EXA]
- [WHY]
- [CONS]
- [LIB]
- [USA]
- [ANE]
- [Notes]
- [Process]
- [Pool]
- [Queue]
- [Pipe]
- [Lock]
- [Semaphore]
- [Event]
- [Condition]
- [Value]
- [Array]
- [Manager]

---

# Date

16/07/2026

---

# Task

A task is a unit of work.

## Characteristics

- Higher-level concept.
- Represents a job or activity to be completed.
- Can contain multiple processes.

---

# Process

A process is a program that is currently running.

It is an active instance of a program.

## Characteristics

- Has its own memory and resources.
- Can contain multiple threads.
- Managed by the operating system.

## Separate Resources

Each process has separate:

- Memory.
- GIL (Global Interpreter Lock).
- CPU cores.
- Python interpreter.

---

# Thread

A thread is a smaller execution unit inside a process.

## Characteristics

- Smaller unit under a process.
- Smallest unit of execution.
- Performs a specific task inside a process.
- Shares memory and resources of the process.
- Multiple threads can run simultaneously.

---

# Example

- Browsing in Chrome → Task

    - Chrome application running → Process

        - Loading webpage → Thread

        - Handling user input → Thread

        - Playing video → Thread

---

# GIL (Global Interpreter Lock)

GIL is a lock in CPython that allows only one thread to execute Python bytecode at a time.

## Purpose

- Prevents multiple threads from modifying Python objects simultaneously.
- Avoids memory conflicts.
- Provides safe memory management.

## Why

- Memory Management.
- Reference management.
- Prevent corruption in tasks and memory.

## Working

Threads can run concurrently by switching between tasks, but CPU-bound Python code does not achieve true parallel execution on multiple CPU cores.

## Cons

- Slower because it directly connects with CPU execution.

## Note

Threads execute one by one in CPython due to the GIL.

---

# Process

A process is an independent execution unit with separate memory.

## Characteristics

- Runs tasks in parallel using multiple CPU cores.
- Avoids Python GIL limitations.

## Library

```python
multiprocessing
````

---

# Process Example

```python
from multiprocessing import Process


def worker():
    print("Hello from worker process")


if __name__ == "__main__":

    P = Process(target=worker)

    P.start()   # starts process

    P.join()    # waits for process completion
```

---

# Multiple Process Example

```python
from multiprocessing import Process
import time
import os


def worker(name):

    for i in range(3):
        print(f"{name} : {i}")
        time.sleep(1)

    print("Hello from worker process", os.getpid())


if __name__ == "__main__":

    P = Process(target=worker, args=("process-1",))

    P2 = Process(target=worker, args=("process-2",))

    P.start()

    P2.start()

    P.join()

    P2.join()

    print("Main process finished")
```

---

# Multiprocessing (Python)

Multiprocessing runs multiple processes independently to achieve parallel execution.

## Characteristics

* Runs multiple processes separately.
* Bypasses Python GIL.
* Uses multiple CPU cores.

---

# Multiprocessing Components

## Process

Creates a new independent process.

### Usage

* Used to run a function in parallel.

---

# Pool

Pool creates a group of worker processes.

## Purpose

* Automatically distributes tasks among workers.

## Example

```python
from multiprocessing import Pool


def square(num):
    return num * num


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5]

    with Pool(processes=2) as pool:

        result = pool.map(square, nums)

    print(result)
```

---

# Queue

Queue allows safe data sharing between processes.

## Characteristics

* Follows FIFO (First In First Out) communication.
* Provides process-safe communication.

## Example

```python
from multiprocessing import Process, Queue


def worker(q):

    for i in range(1, 6):

        q.put(i)


if __name__ == "__main__":

    q = Queue()

    p = Process(target=worker, args=(q,))

    p.start()

    p.join()


    while not q.empty():

        print(q.get())
```

---

# Pipe

Pipe creates a communication channel between two processes.

## Purpose

* Used for direct sending and receiving data between processes.

---

# Lock

Lock allows only one process to access shared data at a time.

## Purpose

* Prevents race conditions.
* Provides synchronization.

---

# Semaphore

Semaphore controls how many processes can access a resource simultaneously.

## Purpose

* Limits resource usage.
* Controls concurrent access.

---

# Event

Event sends a signal between processes.

## Purpose

* Used to notify a process that something happened.

---

# Condition

Condition allows processes to wait until a specific condition is met.

## Purpose

* Used for advanced process synchronization.

---

# Value

Value creates a shared single variable between processes.

## Purpose

* Used for sharing numbers or simple data.

---

# Array

Array creates a shared memory array between processes.

## Purpose

* Used for sharing multiple values.

---

# Manager

Manager provides shared objects between processes.

## Supported Shared Objects

* List.
* Dictionary.
* Other data structures.
