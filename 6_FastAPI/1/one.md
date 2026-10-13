# FastAPI, HTTP & Pydantic Notes

**Date:** 20/07/2026

---

# 📌 Keywords

- HTTP
- URL
- HTTP Components
- HTTP Methods
- HTTP Status Codes
- FastAPI
- Backend Framework
- Python
- Uvicorn
- REST API
- CRUD
- GET
- POST
- PUT
- PATCH
- DELETE
- Path Parameters
- Query Parameters
- Body Parameters
- Pydantic
- BaseModel
- Strong Typing
- Response Model
- Async Client
- httpx
- Async Programming
- API Development
- Request
- Response
- Validation

---

# 🏷 Tags / Custom Keywords Used

## Abbreviations

| Tag | Meaning |
|------|----------|
| LIB | Library |
| USA | Usage (Example Code) |
| PAR | Parameters |
| SYN | Syntax |
| WHY | Why this is used |
| EXA | Example |
| MET | Methods |
| CAT | Cannot Have It |
| ALI | Alias |
| RES | Expected Result |
| OPT | Optional |
| ANE | Another Example |
| FUN | Functions Used |
| DAM | Data Members |
| TYS | Types |
| VER | Python Version |
| USC | Use Cases |

### Custom Tags

| Tag | Meaning |
|------|----------|
| [COM] | CLI Command |
| [INS] | Install Library |
| [RUN] | Run Command |

---

# HTTP

## Definition

HTTP (**HyperText Transfer Protocol**) is an application-layer protocol used for communication between clients and servers over the internet.

---

## Components

- URL
- Methods
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
- Status Codes
    - 1xx
    - 2xx
    - 3xx
    - 4xx
    - 5xx

---

## URL

**Definition**

A **Uniform Resource Locator (URL)** is the address used to access a resource on a web server.

**Example**

```
https://example.com/users/1
```

---

## HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Retrieve data |
| POST | Create new data |
| PUT | Completely replace an existing resource |
| PATCH | Partially update an existing resource |
| DELETE | Remove a resource |

---

## HTTP Status Codes

| Code | Meaning |
|------|----------|
| 1xx | Informational Responses |
| 2xx | Success Responses |
| 3xx | Redirection Messages |
| 4xx | Client Errors |
| 5xx | Server Errors |

---

# FastAPI

## Definition

FastAPI is a modern, high-performance Python backend framework used for building REST APIs.

It automatically supports:

- Type Validation
- Interactive API Documentation
- Async Programming
- High Performance
- Pydantic Integration

---

## [INS]

Install FastAPI

```bash
pip install "fastapi[standard]"
```

Install Uvicorn

```bash
pip install uvicorn
```

---

## [USA]

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

emp = []

@app.get("/")
def home():
    return {"message": "Hello"}

# Get all employees
@app.get("/emp")
def get_data():
    return emp

@app.post("/emp")
def add_data(data: dict):
    emp.append(data)
    return {
        "message": "Employee added successfully",
        "data": data
    }

# Complete replacement of an employee record
@app.put("/emp")
def update_emp(id: int, emp1: dict):
    for index, employee in enumerate(emp):
        if employee.get("id") == id:
            emp[index] = emp1
            return {
                "message": "Employee updated successfully",
                "data": emp1
            }

@app.delete("/emp")
def delete_emp(id: int):
    for index, employee in enumerate(emp):
        if employee.get("id") == id:
            deleted_emp = emp.pop(index)
            return {
                "message": "Employee deleted successfully",
                "data": deleted_emp
            }

@app.get("/emp/{id}")
def get_employee(id: int):
    for employee in emp:
        if employee.get("id") == id:
            return employee

    raise HTTPException(status_code=404, detail="Employee not found")
```

> **Note**
>
> The original notes imported `HTTPException` but did not use it. Returning a `404 Not Found` exception when an employee does not exist is the standard FastAPI practice.

---

## [RUN]

```bash
python -m uvicorn <file-name>:app --reload
```

Example

```bash
python -m uvicorn main:app --reload
```

---

# HTTP Request Parameters

---

## 1. Path Parameter

### Definition

A Path Parameter is part of the URL path and is used to identify a specific resource.

### [SYN]

```
https://<link>/<route-name>/{parameter}
```

### [EXA]

```
https://api.example.com/users/101
```

### Explanation

Used to identify a specific resource.

Example:

User ID = **101**

---

### Example Code

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

### Request

```
GET /users/101
```

---

## 2. Query Parameter

### Definition

A Query Parameter is appended after `?` in the URL and is generally used for filtering, searching, sorting, or pagination.

### [SYN]

```
https://<link>/<route-name>?<key>=<value>
```

### [EXA]

```
https://api.example.com/users?active=true
```

### Explanation

Used to filter or customize the returned result.

---

### Example Code

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users(active: bool):
    return {"active": active}
```

### Request

```
GET /users?active=true
```

---

## 3. Body Parameter

### Definition

A Body Parameter is data sent inside the HTTP request body.

It is mainly used with:

- POST
- PUT
- PATCH

---

### [SYN]

```
POST/PUT/PATCH https://<link>/<route-name>
```

### Request Body

```json
{
    "name": "Alice",
    "age": 25
}
```

---

### Example Code

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user
```

> **Correction**
>
> The original notes returned `User`, which is the class itself. The correct implementation is `return user`, which returns the validated request data.

### Request

```
POST /users
```

Body

```json
{
    "name": "Alice",
    "age": 25
}
```

---

# Pydantic

## Definition

Pydantic is a Python library used for **data validation**, **serialization**, and **strong typing**.

FastAPI uses Pydantic internally to validate incoming request data.

---

## WHY

- Strong Typing
- Automatic Validation
- Automatic Type Conversion
- Cleaner API Code
- Better Error Messages

---

## [USA]

```python
from pydantic import BaseModel

class Employee(BaseModel):
    id: int
    name: str
    age: int

emp = []

@app.post("/employee")
def add_employee(data: Employee):
    emp.append(data)
    return data
```

> **Note**
>
> The class name has been changed from `employee` to `Employee` to follow Python naming conventions. The functionality remains the same.

---

# Response Model (FastAPI)

## Definition

A **Response Model** is a Pydantic model that defines and validates the structure of the API response before it is sent to the client.

---

## WHY

- Hides sensitive information
- Validates output
- Automatically generates documentation
- Maintains consistent API responses

---

## [SYN]

```python
@app.get("/users/{id}", response_model=UserResponse)
```

---

## Example

### Request

```
GET /users/1
```

Returned by API

```json
{
    "id": 1,
    "name": "Alice",
    "password": "secret"
}
```

Response Sent

```json
{
    "id": 1,
    "name": "Alice"
}
```

---

### Note

Any field that is **not** included inside the `response_model` is automatically removed before sending the response.

Example:

```
password
```

will not be returned if it is not part of the response model.

---

# Async Client (FastAPI)

## Definition

An **Async Client** is used to perform **non-blocking HTTP requests**, allowing multiple operations to execute concurrently without blocking the application.

FastAPI commonly uses the **httpx** library for asynchronous HTTP requests.

---

## WHY

- Better Performance
- Concurrent Requests
- Non-blocking I/O
- Faster API Communication

---

## Example

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get(
        "https://api.example.com/users"
    )
```

---

## Note

`AsyncClient` improves performance during I/O-bound operations because the application can continue processing other requests while waiting for the HTTP response.

---

# Summary

## HTTP

- URL
- HTTP Methods
- HTTP Status Codes

---

## FastAPI

- Backend Framework
- REST API Development
- CRUD Operations
- Request Validation
- Response Validation

---

## Parameters

- Path Parameter
- Query Parameter
- Body Parameter

---

## Pydantic

- BaseModel
- Strong Typing
- Data Validation

---

## Response Model

- Output Validation
- Hide Sensitive Data
- Automatic Filtering

---

## Async Client

- httpx.AsyncClient
- Non-blocking Requests
- Concurrent Execution
- Improved Performance