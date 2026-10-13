# Telecom Domain Projects - Backend API Requirements

## Project 1: Customer Self-Care Portal ⭐⭐⭐⭐⭐

### Overview

Customer portal to manage mobile accounts, SIMs, and recharge activities.

### Roles

* Customer
* Admin

### Security

* Register & Login
* JWT Authentication
* Password Hashing
* Role-Based Authorization

### Business Rules

**Customer**

* Register only once with a unique mobile number.
* Maximum 5 active SIMs per customer.
* Recharge amount must be ≥ ₹10.
* Cannot recharge inactive SIMs.
* Can view only personal recharge history.

**Admin**

* Activate / Deactivate SIMs.
* View all customers.
* Suspend customers.

### APIs

```
POST   /register
POST   /login

POST   /sim
GET    /sim

POST   /recharge
GET    /recharge/history

PUT    /admin/activate-sim
PUT    /admin/deactivate-sim

GET    /admin/customers
```

---

# Project 2: Broadband Installation Management ⭐⭐⭐⭐⭐

### Overview

Customers request broadband installation. Engineers complete installations after manager approval.

### Roles

* Customer
* Engineer
* Manager

### Business Rules

**Customer**

* Cannot create duplicate installation requests for same address.
* Maximum 3 pending requests.

**Engineer**

* Can update only assigned installations.

**Manager**

* Assign engineers.
* Approve requests.
* Reject requests.

### APIs

```
POST /register
POST /login

POST /installation
GET  /installation

PUT /installation/assign
PUT /installation/complete
PUT /installation/approve
```

---

# Project 3: Telecom Complaint Management ⭐⭐⭐⭐

### Roles

* Customer
* Support Engineer
* Admin

### Business Rules

**Customer**

* Cannot raise duplicate complaints within 24 hours.

**Support Engineer**

* Resolve only assigned complaints.

**Admin**

* Assign complaints.
* Escalate complaints.
* Close complaints.

### APIs

```
POST /complaint

GET  /complaints

PUT  /assign
PUT  /resolve
PUT  /close
```

---

# Project 4: Recharge & Wallet System ⭐⭐⭐⭐⭐

### Overview

Customers maintain wallet balance and recharge using wallet funds.

### Business Rules

* Wallet balance cannot be negative.
* Recharge amount cannot exceed wallet balance.
* Recharge plan must exist.
* Recharge extends validity.
* Expired SIM cannot recharge.

### APIs

```
POST /wallet/add
GET  /wallet

POST /recharge
GET  /transactions
```

---

# Project 5: Employee Leave Management ⭐⭐⭐⭐⭐

### Roles

* Employee
* Manager
* HR

### Business Rules

**Employee**

* Maximum 20 leave days/year.
* Cannot apply leave for past dates.

**Manager**

* Approve or reject leave.

**HR**

* View all leave requests.

### APIs

```
POST /login

POST /leave
GET  /leave

PUT /approve
PUT /reject
```

---

# Project 6: SIM Inventory Management ⭐⭐⭐⭐⭐

### Overview

Warehouse manages SIM stock and retailer requests.

### Roles

* Warehouse Admin
* Retailer

### Business Rules

* Cannot issue SIMs beyond available stock.
* Retailer limit: 100 SIMs/day.
* Stock updates automatically.

### APIs

```
POST /login

POST /issue
POST /receive

GET /stock
GET /transactions
```

---

# Project 7: Postpaid Billing System ⭐⭐⭐⭐⭐

### Business Rules

* Monthly bill generation.
* Payment updates bill status.
* Late payment penalty: ₹100.
* Services blocked after 60 days unpaid.

### APIs

```
POST /generate-bill

POST /pay-bill

GET /bill
GET /bill/history
```

---

# Project 8: Network Outage Management ⭐⭐⭐⭐⭐

### Roles

* Network Engineer
* Admin

### Business Rules

* Engineers update only assigned outages.
* Customers can view outage status.
* Admin verifies and closes outages.

### APIs

```
POST   /outage
PUT    /outage
GET    /outage
DELETE /outage
```

---

# Project 9: Family Plan Management ⭐⭐⭐⭐⭐

### Business Rules

* One primary account holder.
* Maximum 5 family members.
* Only primary user manages members.
* All members share the same data plan.

### APIs

```
POST   /family

POST   /family/add-member

DELETE /family/member

GET    /family
```

---

# Project 10: Telecom Loyalty Rewards ⭐⭐⭐⭐⭐

### Business Rules

Recharge Rewards:

| Recharge Amount | Points |
| --------------- | ------ |
| > ₹500          | 50     |
| > ₹1000         | 120    |

Rules:

* Minimum 200 points required for redemption.
* Cannot redeem more points than available balance.

### APIs

```
POST /reward/recharge

GET  /reward/points

POST /reward/redeem
```

---

# Common Technical Features

## Authentication

* JWT Token Security
* BCrypt Password Encryption
* Role-Based Access Control

## Backend Capabilities

* REST API Architecture
* Validation & Exception Handling
* Database Persistence
* Transaction Management
* Audit Logging

## Recommended Stack

```
Backend   : Spring Boot
Security  : Spring Security + JWT
Database  : MySQL / PostgreSQL
ORM       : Hibernate / JPA
Testing   : JUnit + Mockito
Docs      : Swagger / OpenAPI
```

---

# Project Collection Summary

| Project                   | Domain                    | Complexity |
| ------------------------- | ------------------------- | ---------- |
| Customer Self-Care Portal | Mobile Account Management | ⭐⭐⭐⭐⭐      |
| Broadband Installation    | Service Provisioning      | ⭐⭐⭐⭐⭐      |
| Complaint Management      | Customer Support          | ⭐⭐⭐⭐       |
| Wallet Recharge           | Payment System            | ⭐⭐⭐⭐⭐      |
| Leave Management          | HR System                 | ⭐⭐⭐⭐⭐      |
| SIM Inventory             | Stock Management          | ⭐⭐⭐⭐⭐      |
| Postpaid Billing          | Billing System            | ⭐⭐⭐⭐⭐      |
| Network Outage            | Operations Management     | ⭐⭐⭐⭐⭐      |
| Family Plan               | Account Management        | ⭐⭐⭐⭐⭐      |
| Loyalty Rewards           | Reward Platform           | ⭐⭐⭐⭐⭐      |

```
```
