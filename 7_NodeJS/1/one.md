# JavaScript & Node.js Fundamentals

> **Date:** 22/07/2026

---

# 📌 Keywords

- JavaScript
- Node.js
- Runtime Environment
- Browser JavaScript Engine
- V8 Engine
- Machine Code
- Frontend
- Backend
- Single Threaded
- Event Loop
- REPL
- npm
- npx
- npm audit
- npm init
- package.json
- Dependencies
- Tilde (~)
- Caret (^)
- Semantic Versioning
- process Object
- Buffer
- CommonJS
- ES Modules (ESM)
- ES5
- ES6
- module.exports
- require()
- export
- import
- Named Export
- Default Export
- File Handling
- fs
- fs/promises
- Promise
- async/await
- try/catch
- HTTP Module
- createServer()
- request
- response
- Headers
- HTTP Status Codes
- JSON Response
- CORS

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
- ES5
- ES6

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
| VER | Python Version *(Original Note)* |
| USC | Use Cases |

> **Note:** Although **VER** is mentioned as **Python Version** in the abbreviations, in these notes it is being used for **Version Information** (e.g., ES5, ES6). The meaning has been interpreted based on context.

---

# JavaScript

JavaScript is a **high-level**, **interpreted/scripting**, and **programming language**.

## Features

- Used for **Frontend Development** (Browser).
- Used for **Backend Development** (Node.js).
- Backend JavaScript runs using **Node.js**.
- Works in all modern browsers:
  - Chrome
  - Edge
  - Firefox
  - Brave
  - Safari
- Browsers already contain a JavaScript engine.
- JavaScript can be executed directly inside the Browser Console.
- Browser JavaScript does **not** require Node.js.
- Node.js allows JavaScript to execute **outside the browser**.
- JavaScript follows a **Single-Threaded Execution Model**, meaning the main JavaScript execution thread processes one task at a time. Asynchronous operations are handled using the Event Loop.

---

# Execution Flow

## Browser

```
JavaScript
      ↓
Browser JavaScript Engine (Example: V8)
      ↓
Machine Code
```

## Backend

```
JavaScript
      ↓
Node.js Runtime
      ↓
V8 Engine
      ↓
Machine Code
```

---

# Node.js

Node.js is a **JavaScript Runtime Environment** used to execute JavaScript outside the browser.

## Features

- Runtime environment for JavaScript.
- Uses Google's **V8 Engine**.
- Enables backend development.
- Supports file handling.
- Supports networking.
- Supports server-side programming.

---

## npm

Node Package Manager.

Used to:

- Install packages
- Manage dependencies
- Create projects
- Install libraries like:
  - axios
  - express
  - mongoose
  - etc.

---

## npx

Runs npm packages **temporarily** without installing them globally.

---

## npm audit

Checks installed dependencies for known security vulnerabilities.

---

# REPL

**REPL** stands for:

```
Read
Evaluate
Print
Loop
```

It is an interactive environment where JavaScript code can be executed line by line.

---

# Event Loop

The Event Loop is responsible for handling **asynchronous operations** in Node.js.

Examples:

- File Handling
- Network Requests
- Timers
- Event Handling

---

# npm init

Creates a **package.json** file.

The package.json stores:

- Project Name
- Version
- Dependencies
- Scripts
- Metadata

## Usage

```
npm init
```

Asks configuration questions.

---

### Automatic Initialization

```
npm init -y
```

Creates package.json using default values.

---

### Memory Tip

```
npm init
=
Initialize a Node.js Project
```

---

# Tilde (~) and Caret (^)

## Tilde (~)

Allows only **Patch Updates**.

Example:

```
~1.2.3
```

Allowed

```
1.2.4
1.2.9
```

Not Allowed

```
1.3.0
2.0.0
```

Used mainly for **bug-fix releases**.

---

## Caret (^)

Allows

- Minor Updates
- Patch Updates

Keeps Major Version Fixed.

Example

```
^1.2.3
```

Allowed

```
1.2.4
1.3.0
1.9.9
```

Not Allowed

```
2.0.0
```

Used for:

- New Features
- Bug Fixes

---

## Memory

```
~
=
Patch Only

^

=
Minor + Patch
```

---

# process Object

The **process** object is a built-in Node.js global object.

It provides information and control over the currently running Node.js process.

---

## [MET]

### process.pid

Returns current Process ID.

```javascript
console.log(process.pid);
```

---

### process.cwd()

Returns Current Working Directory.

```javascript
console.log(process.cwd());
```

---

### process.version

Returns current Node.js Version.

```javascript
console.log(process.version);
```

---

### process.platform

Returns Operating System Platform.

```javascript
console.log(process.platform);
```

---

### process.argv

Returns Command Line Arguments.

```javascript
console.log(process.argv);
```

---

### process.env

Returns Environment Variables.

```javascript
console.log(process.env);
```

---

### process.exit()

Stops the Node.js Process.

```javascript
process.exit();
```

---

### process.memoryUsage()

Returns memory usage information.

```javascript
console.log(process.memoryUsage());
```

---

### process.uptime()

Returns process running time.

```javascript
console.log(process.uptime());
```

---

### Memory

```
process
=
Information + Control
of current Node.js Program
```

---

# Buffer

Buffer stores and manipulates **Binary Data** directly in memory.

Used while working with:

- Files
- Images
- Videos
- Network Packets
- Streams

Buffers are useful because binary data cannot always be represented as normal text.

---

# Modules

---

# ES5 Export (CommonJS)

Exports values using CommonJS Module System.

## [SYN]

```javascript
module.exports = <value>;
```

## [USA]

```javascript
function add(a, b) {
    return a + b;
}

module.exports = add;
```

---

# ES5 Import

Imports modules using require().

## [SYN]

```javascript
require(<module-path>);
```

## [USA]

```javascript
const add = require("./math");

add(2,3);
```

---

# ES5 Multiple Export

## [SYN]

```javascript
module.exports = {
    add,
    subtract
}
```

---

# ES6 Export

Exports values using ES Modules.

## [TYS]

1. Named Export
2. Default Export

---

# ES6 Named Export

Exports multiple named values.

## [SYN]

```javascript
export { value };
```

## [USA]

```javascript
export function add(a,b){
    return a+b;
}
```

---

# ES6 Named Import

Imports using exported name.

## [SYN]

```javascript
import { add } from "./math.js";
```

---

# ES6 Default Export

Exports one primary value.

## [SYN]

```javascript
export default value;
```

## [USA]

```javascript
export default function add(a,b){
    return a+b;
}
```

---

# ES6 Default Import

Imports default export without curly braces.

## [SYN]

```javascript
import add from "./math.js";
```

---

# CommonJS vs ES Modules

## ES5

Export

```javascript
module.exports
```

Import

```javascript
require()
```

---

## ES6

Export

```javascript
export
```

Import

```javascript
import
```

---

## WHY

- ES5 → Older Node.js Module System (CommonJS)
- ES6 → Modern JavaScript Module System (ESM)

---

## VER

- ES5 → CommonJS
- ES6 → ES Modules (ESM)

---

# File Handling

Used to:

- Create Files
- Read Files
- Update Files
- Delete Files

---

## [LIB]

```
fs
```

Node.js File System Module.

```
fs/promises
```

Promise-based File System Module.

---

## fs/promises

Provides Promise-based file handling methods.

### [USA]

```javascript
import fs from "fs/promises";
```

---

## writeFile()

Creates or overwrites a file.

### [SYN]

```javascript
fs.writeFile(fileName, data)
```

### [USA]

```javascript
fs.writeFile("f1.txt","new file created")
.then(()=>{
    console.log("file created...");
})
.catch((err)=>{
    console.log(err);
});
```

---

# Promise Methods

## .then()

Runs after Promise resolves successfully.

## .catch()

Runs when Promise rejects.

### [SYN]

```javascript
promise
.then(successFunction)
.catch(errorFunction);
```

---

# async/await

### [USA]

```javascript
async function createFile(){

    await fs.writeFile("f1.txt","new file created");

    console.log("file created...");
}

createFile();
```

---

# try/catch

Handles errors in async functions.

```javascript
async function createFile(){

    try{

        await fs.writeFile("f1.txt","new file created");

        console.log("file created...");

    }

    catch(err){

        console.log(err);

    }

}
```

---

# Common fs Methods

## [MET]

| Method | Purpose |
|---------|----------|
| writeFile() | Create/Write File |
| readFile() | Read File |
| appendFile() | Append Content |
| rename() | Rename File |
| unlink() | Delete File |
| mkdir() | Create Folder |
| access() | Check File Existence/Permissions |

---

## WHY

`fs/promises` performs non-blocking file operations using Promises, making asynchronous code cleaner and easier to manage.

---

## Memory

```
.then()
=
Success

.catch()
=
Error

await
=
Wait for Promise Result
```

---

# HTTP Module

Creates HTTP Servers and handles Client Requests.

---

## [LIB]

```
http
```

Built-in Node.js Module.

---

## [USA]

```javascript
import http from "http";

const server = http.createServer((request,response)=>{

    response.write("Welcome to node js server");

    response.end();

});

server.listen(3000);

console.log("server working");
```

---

# createServer()

## [SYN]

```javascript
http.createServer((request,response)=>{

    // response

});
```

---

# request

Contains Client Request Information.

## [DAM]

```
request.url
```

Requested URL Path.

```
request.method
```

HTTP Method.

```
request.headers
```

Request Headers.

---

# response

Sends data back to client.

## [FUN]

### response.write()

Writes response data.

### response.end()

Ends the response.

---

# response.setHeader()

Sets HTTP Response Headers.

## [SYN]

```javascript
response.setHeader(headerName,value);
```

## [USA]

```javascript
response.setHeader("Content-Type","text/html");
```

---

# Common Headers

## Content-Type

Defines response data type.

Examples

```
text/html
application/json
```

---

## Access-Control-Allow-Origin

Allows Cross-Origin Resource Sharing (CORS) requests.

---

## Cache-Control

Controls browser caching behavior.

---

# response.writeHead()

Sets HTTP Status Code and Headers together.

## [SYN]

```javascript
response.writeHead(statusCode,{
    headers
});
```

## [USA]

```javascript
response.writeHead(200,{
    "Content-Type":"application/json"
});
```

---

# HTTP Status Codes

| Code | Meaning |
|------|----------|
| 200 | Success (OK) |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# Request Methods

## GET

Retrieve Data.

---

## POST

Send/Create Data.

---

## PUT

Update Existing Data.

---

## DELETE

Delete Data.

---

# server.listen()

Starts the HTTP Server.

## [SYN]

```javascript
server.listen(portNumber);
```

## [USA]

```javascript
server.listen(3000);
```

---

# JSON Response

## [USA]

```javascript
response.setHeader("Content-Type","application/json");

response.end(JSON.stringify({

    message:"Hello"

}));
```

---

## WHY

The built-in HTTP module allows developers to create web servers and handle HTTP requests without using external frameworks such as Express.

---

## Memory

```
createServer()
=
Create Server

request
=
Client Data

response
=
Server Data

setHeader()
=
Add Response Headers

listen()
=
Start Server
```