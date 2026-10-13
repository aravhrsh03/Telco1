# SCENARIO 3: Wrong Use of HTTP Methods

> **The Challenge:** A developer builds endpoints that completely ignore standard HTTP verb semantics (e.g., `GET /delete_customer/123`, `POST /get_customer`, `GET /update_customer`). While code execution might technically succeed, this anti-pattern breaks web standards and system behaviors.

---

## ⚠️ Problems Created by This Approach

### **1. Broken Caching & Idempotency:**
* `GET` requests are designed to be safe, cacheable, and side-effect free. Using `GET` to delete or update state violates browser, CDN, and proxy caching mechanisms, risking unintended data mutations or stale caches.


### **2. Security & Compliance Risks:**
* `POST` endpoints are often used to transmit sensitive data (like passwords or profile updates) in the request body. Moving sensitive queries or parameters into URL paths (as in `GET /delete_customer/123`) exposes them in server access logs, browser history, and proxy logs.


### **3. Developer Confusion & Poor Maintainability:**
* API consumers expect RESTful predictability. Non-standard routes require constant documentation lookup, increasing integration errors and onboarding time.


### **4. Tooling Incompatibility:**
* Automated documentation tools (like Swagger/OpenAPI), API gateways, and security scanners rely on correct HTTP methods to enforce policies, rate limits, and access controls.



---

## 🛠️ Proper REST Redesign

To fix this, align the actions with resource-oriented URIs and standard HTTP methods:

| Incorrect Endpoint | Proper REST Endpoint | HTTP Method | Description |
| --- | --- | --- | --- |
| `GET /delete_customer/123` | `/customers/123` | `DELETE` | Removes customer resource 123 |
| `POST /get_customer` | `/customers/123` | `GET` | Retrieves details for customer 123 (use query params for filters if fetching lists) |
| `GET /update_customer` | `/customers/123` | `PUT` or `PATCH` | Replaces (`PUT`) or partially updates (`PATCH`) customer 123 |

---

## 🚀 Best Practices for the Redesigned API

* **Use Nouns, Not Verbs:** Resource paths should represent entities (e.g., `/customers`) rather than actions (e.g., `/get_customer`). Let the HTTP verb (`GET`, `POST`, `PUT`, `DELETE`) dictate the action.
* **Proper Status Codes:** Pair the methods with appropriate HTTP status codes:
* `200 OK` for successful fetches and updates.
* `201 Created` for resource creation.
* `204 No Content` for successful deletions.