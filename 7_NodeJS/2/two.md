# HTTP Module – Multiple Requests, Swagger, Express & MySQL

> **Date:** 23/07/2026

---

# 📌 Keywords

- HTTP Module
- URL Routing
- Route Matching
- request.url
- request.method
- HTTP Methods
- Route Order
- Default Route
- HTTP Status Code
- HTML Response
- JSON Response
- Express.js
- Swagger
- Swagger UI
- swagger-jsdoc
- swagger-ui-express
- Middleware
- app.use()
- app.get()
- app.post()
- app.put()
- app.delete()
- req
- res
- app.listen()
- Express + MySQL
- mysql2
- Database Connection
- createConnection()
- connect()
- query()
- SQL
- CRUD APIs
- REST APIs
- REST Services
- Authentication
- Student Management
- Inventory System

---

# 🏷️ Tags / Identifiers Used

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
- ANE
- FUN
- DAM
- TYS
- VER
- USC
- INS
- MEMORY

---

# 📖 Abbreviations

| Tag | Meaning |
|------|---------|
| LIB | Library |
| USA | Usage (Example Code) |
| PAR | Parameters |
| SYN | Syntax |
| WHY | Why this is Used |
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
| VER | Version |
| USC | Use Cases |
| INS | Installation |

---

# HTTP Module – Multiple Requests

HTTP servers can respond differently based on the **requested URL (route)** and **HTTP method**.

---

# URL Routing

Routes incoming client requests to different responses based on the requested URL.

## [SYN]

```javascript
if (request.url === "<path>") {
    <response>
}
else {
    <response>
}
```

---

## Multiple URLs

### [USA]

```javascript
if (request.url === "/") {

    response.end("Home");

}
else if (request.url === "/about") {

    response.end("About");

}
else if (request.url === "/contact") {

    response.end("Contact");

}
else {

    response.writeHead(404);

    response.end("Not Found");

}
```

---

# URL + HTTP Method

Routes can be matched using both the **URL** and the **HTTP Method**.

## [SYN]

```javascript
if (
    request.url === "<path>" &&
    request.method === "<method>"
) {

    <response>

}
```

---

## [EXA]

```javascript
if (
    request.url === "/users" &&
    request.method === "GET"
) {

    response.end("Users");

}
```

---

# Returning HTML Pages

## [USA]

```javascript
if (request.url === "/") {

    response.setHeader(
        "Content-Type",
        "text/html"
    );

    response.end(`
        <h1>Home</h1>
        <p>Welcome</p>
    `);

}
```

---

# Returning JSON for Different URLs

## [USA]

```javascript
if (request.url === "/user") {

    response.setHeader(
        "Content-Type",
        "application/json"
    );

    response.end(
        JSON.stringify({

            id: 1,

            name: "John"

        })
    );

}
```

---

# request.url

Contains the URL path requested by the client.

## [DAM]

```javascript
request.url
```

## [RES]

```
/
/about
/contact
/users
```

---

# request.method

Contains the HTTP method used in the request.

## [DAM]

```javascript
request.method
```

## [RES]

```
GET
POST
PUT
PATCH
DELETE
```

---

# Route Order

The **first matching route** is executed.

Routes should be written from **most specific** to **least specific**, with the default route placed last.

---

# Default Route

Handles requests that do not match any defined route.

## [USA]

```javascript
else {

    response.writeHead(404);

    response.end("Not Found");

}
```

---

# Common Routes

| Route | Purpose |
|--------|----------|
| / | Home |
| /about | About Page |
| /contact | Contact Page |
| /users | User Resource |
| /login | Login |
| /register | Register |

---

## WHY

A single HTTP server can handle multiple URLs and HTTP methods using routing logic.

---

## USC

- Website Pages
- REST APIs
- Authentication
- CRUD Operations

---

## MEMORY

```
url
=
Route

method
=
Action

if
=
Match

end()
=
Send Response

404
=
No Matching Route
```

---

# Swagger & Express

---

# Swagger

Swagger is an **API documentation and testing tool** based on the **OpenAPI Specification (OAS)**.

It provides an interactive web interface for exploring and testing REST APIs.

---

## WHY

- Generate API documentation automatically.
- Test APIs directly from the browser.
- Improve API readability for developers.

---

## INS

```bash
npm install express

npm install swagger-ui-express

npm install swagger-jsdoc
```

---

# Express

Express is a lightweight **Web Framework** built on top of Node.js' HTTP module.

It simplifies:

- Routing
- Middleware
- Request Handling
- Response Handling

---

## WHY

Reduces boilerplate code and simplifies backend development.

---

## LIB

```javascript
import express from "express";
```

---

# Create Express Application

## [USA]

```javascript
const app = express();
```

---

# app.use()

Registers middleware.

Middleware executes before reaching the final route handler.

---

## [SYN]

```javascript
app.use(path, middleware);
```

---

## [EXA]

```javascript
app.use(express.json());
```

> **Note:** `express.json()` is built-in middleware used to parse incoming JSON request bodies.

---

# Swagger Route

## [USA]

```javascript
app.use(

    "/api-docs",

    swaggerUi.serve,

    swaggerUi.setup(swaggerSpec)

);
```

---

# app.get()

Handles HTTP GET requests.

---

## [SYN]

```javascript
app.get(path, (req, res) => {

});
```

---

## [EXA]

```javascript
app.get("/students", (req, res) => {

    res.send("Students");

});
```

---

# app.post()

Handles HTTP POST requests.

---

# app.put()

Handles HTTP PUT requests.

---

# app.delete()

Handles HTTP DELETE requests.

---

# req

Represents the incoming client request.

---

## [DAM]

```javascript
req.params
```

Route Parameters.

---

```javascript
req.query
```

Query Parameters.

---

```javascript
req.body
```

Request Body.

---

```javascript
req.headers
```

HTTP Headers.

---

# res

Represents the outgoing server response.

---

## [FUN]

```javascript
res.send()
```

Send text or HTML response.

---

```javascript
res.json()
```

Send JSON response.

---

```javascript
res.status()
```

Set HTTP status code.

---

# app.listen()

Starts the Express server.

---

## [SYN]

```javascript
app.listen(port);
```

---

## [EXA]

```javascript
app.listen(3000);
```

---

# HTTP Method Mapping

| Method | Operation |
|----------|-----------|
| GET | Read Data |
| POST | Create Data |
| PUT | Update Data |
| DELETE | Remove Data |

---

## USC

- API Development
- REST Services
- Middleware
- Swagger Documentation

---

## MEMORY

```
express()
=
Create Application

app.use()
=
Middleware

app.get()
=
GET Route

app.post()
=
POST Route

app.put()
=
PUT Route

app.delete()
=
DELETE Route

req
=
Request Object

res
=
Response Object

listen()
=
Start Server
```

---

# Complete Swagger Example

## [ANE]

```javascript
// server.js

import express from "express";

import swaggerUi from "swagger-ui-express";

import swaggerJsdoc from "swagger-jsdoc";

const app = express();

// Swagger Configuration

const options = {

    definition: {

        openapi: "3.0.0",

        info: {

            title: "Student API",

            version: "1.0.0",

            description: "Student Management API"

        }

    },

    apis: ["./server.js"]

};

const swaggerSpec = swaggerJsdoc(options);

// Swagger Route

app.use(

    "/api-docs",

    swaggerUi.serve,

    swaggerUi.setup(swaggerSpec)

);

/**
 * @swagger
 * /students:
 *   get:
 *     summary: Get all students
 *     responses:
 *       200:
 *         description: Students fetched successfully
 */

app.get("/students", (req, res) => {

    res.json([

        {

            id: 1,

            name: "John"

        },

        {

            id: 2,

            name: "Alice"

        }

    ]);

});

// Start Server

app.listen(3000, () => {

    console.log("Server Running");

    console.log(
        "Swagger : http://localhost:3000/api-docs"
    );

});
```

---

# Express + MySQL

Connects an Express application with a MySQL database.

---

## WHY

Used to:

- Store Records
- Retrieve Records
- Update Records
- Delete Records

---

## INS

```bash
npm install mysql2
```

---

## LIB

```javascript
import mysql from "mysql2";
```

---

# Create Connection

## [SYN]

```javascript
mysql.createConnection({

    host,

    user,

    password,

    port,

    database

});
```

---

# db.js

## [USA]

```javascript
import mysql from "mysql2";

const db = mysql.createConnection({

    host: "localhost",

    user: "root",

    password: "root",

    port: 3306,

    database: "college"

});

export default db;
```

---

# Connection Object

## [DAM]

### host

MySQL Server Address.

---

### user

MySQL Username.

---

### password

MySQL Password.

---

### port

MySQL Server Port.

Default:

```
3306
```

---

### database

Database Name.

---

# Connect Database

## [SYN]

```javascript
db.connect((err) => {

});
```

---

## Connection Example

### [USA]

```javascript
db.connect((err) => {

    if (err) {

        console.log(err);

        return;

    }

    console.log("Database Connected");

});
```

---

# Execute SQL Query

## [SYN]

```javascript
db.query(sql, callback);
```

---

# Select Data

## [USA]

```javascript
db.query(

    "SELECT * FROM students",

    (err, result) => {

        if (err) {

            console.log(err);

            return;

        }

        console.log(result);

    }

);
```

---

# Insert Data

## [USA]

```javascript
db.query(

    "INSERT INTO students(name) VALUES('John')",

    (err, result) => {

        console.log(result);

    }

);
```

---

# Express + Database Example

## [USA]

```javascript
app.get("/students", (req, res) => {

    db.query(

        "SELECT * FROM students",

        (err, result) => {

            if (err) {

                return res.status(500).send(err);

            }

            res.json(result);

        }

    );

});
```

---

# Common Database Methods

| Method | Purpose |
|----------|----------|
| createConnection() | Create Database Connection |
| connect() | Connect to Database |
| query() | Execute SQL Query |

---

## USC

- Login System
- Student Management
- CRUD APIs
- Inventory Management System

---

## MEMORY

```
mysql2
=
MySQL Library

createConnection()
=
Create Connection

connect()
=
Connect Database

query()
=
Execute SQL

result
=
Query Output
```