# Telecom System Design Patterns - Practice Questions

This document contains design pattern problems based on a telecom system.

Patterns covered:

1. Strategy Pattern
2. Factory Pattern
3. Singleton Pattern
4. Builder Pattern
5. Observer Pattern
6. Repository Pattern
7. Proxy Pattern
8. Decorator Pattern
9. Adapter Pattern
10. Facade Pattern
11. Command Pattern
12. Dependency Injection
13. Factory + Strategy Combination

---

# Question 1: SMS Notification System (Strategy Pattern)

## Problem

A telecom company sends notifications through different channels:

- SMS
- Email
- WhatsApp

Design the system so that the notification method can be changed without modifying existing code.

## Expected Classes

- `Notification`
- `SMSNotification`
- `EmailNotification`
- `WhatsAppNotification`
- `NotificationService`

## Test Cases

```python
service = NotificationService(SMSNotification())
service.send("Recharge Successful")
````

Expected:

```
SMS: Recharge Successful
```

---

```python
service.strategy = EmailNotification()
service.send("Bill Generated")
```

Expected:

```
Email: Bill Generated
```

---

```python
service.strategy = WhatsAppNotification()
service.send("Plan Expiring")
```

Expected:

```
WhatsApp: Plan Expiring
```

---

# Question 2: Recharge Plan Factory (Factory Pattern)

## Problem

Create recharge plans using a factory.

Available plans:

* Prepaid
* Postpaid
* Broadband

## Test Cases

```python
plan = PlanFactory.create("prepaid")
plan.activate()
```

Expected:

```
Prepaid Plan Activated
```

---

```python
plan = PlanFactory.create("broadband")
plan.activate()
```

Expected:

```
Broadband Activated
```

---

```python
PlanFactory.create("unknown")
```

Expected:

```
ValueError
```

---

# Question 3: Telecom Logger (Singleton Pattern)

## Problem

Every tower writes logs.

Only one logger object should exist.

## Test Cases

```python
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)
```

Expected:

```
True
```

---

# Question 4: SIM Activation (Builder Pattern)

## Problem

SIM activation includes optional services.

Available services:

* Voice
* Data
* SMS
* International Roaming

## Test Case

```python
sim = (
    SIMBuilder()
    .voice()
    .data()
    .sms()
    .build()
)

sim.show()
```

Expected:

```
Voice : Yes
Data : Yes
SMS : Yes
Roaming : No
```

---

# Question 5: Tower Alert System (Observer Pattern)

## Problem

Whenever a tower goes down, notify:

* Network Team
* Maintenance Team
* Operations Team

## Test Case

```python
tower.down()
```

Expected:

```
Network Team notified
Maintenance Team notified
Operations Team notified
```

---

# Question 6: Call Routing (Strategy Pattern)

## Problem

Calls can be routed using:

* VoLTE
* 4G
* 5G
* WiFi Calling

## Test Cases

```python
router = Router(VoLTE())

router.route()
```

Expected:

```
Routing through VoLTE
```

---

```python
router.strategy = FiveG()

router.route()
```

Expected:

```
Routing through 5G
```

---

# Question 7: Tower Database (Repository Pattern)

## Problem

Store tower information.

## Test Cases

```python
repo.save(Tower("Tower1"))
repo.save(Tower("Tower2"))

repo.get_all()
```

Expected:

```
Tower1
Tower2
```

---

# Question 8: Customer Authentication (Proxy Pattern)

## Problem

Only authenticated customers can:

* Recharge
* Change Plan
* View Bill

## Test Cases

```python
customer = Proxy(True)

customer.view_bill()
```

Expected:

```
Bill Displayed
```

---

```python
customer = Proxy(False)

customer.view_bill()
```

Expected:

```
Access Denied
```

---

# Question 9: Recharge Logging (Decorator Pattern)

## Problem

Every recharge should be logged.

## Test Case

```python
recharge(399)
```

Expected:

```
Logging Started
Recharge Successful : 399
Logging Finished
```

---

# Question 10: Telecom API Adapter Pattern

## Problem

Old billing system returns XML.

New application expects JSON.

Create an adapter.

## Test Case

```python
adapter.get_bill()
```

Expected:

```json
{
    "customer": "John",
    "amount": 499
}
```

---

# Question 11: Tower Configuration (Facade Pattern)

## Problem

Starting a telecom tower requires:

* Power On
* Load Firmware
* Initialize Radio
* Connect to Core Network

Hide all internal steps.

## Test Case

```python
tower.start()
```

Expected:

```
Power On
Firmware Loaded
Radio Initialized
Connected
Tower Ready
```

---

# Question 12: Customer Complaint System (Command Pattern)

## Problem

Customer raises complaints.

Operations team executes them later.

## Test Case

```python
queue.execute()
```

Expected:

```
Complaint Resolved
```

---

# Question 13: Billing Service (Dependency Injection)

## Problem

Bills can be sent using:

* Email
* SMS
* WhatsApp

Inject the sender.

## Test Case

```python
Billing(SMS()).send_bill()
```

Expected:

```
Bill Sent via SMS
```

---

# Question 14: Network Monitoring System

## Problem

Whenever CPU usage exceeds 90%,
notify engineers.

## Test Cases

```python
monitor.cpu = 95
```

Expected:

```
Engineer notified
```

---

```python
monitor.cpu = 50
```

Expected:

```
No notification
```

---

# Question 15: AI Chatbot for Telecom

## Pattern Used

* Factory Pattern
* Strategy Pattern

## Problem

Customer asks:

* Recharge
* Bill
* Network Issue

Use Factory to create the correct handler and Strategy to process the request.

## Test Cases

```python
chatbot.handle("bill")
```

Expected:

```
Showing Current Bill
```

---

```python
chatbot.handle("network")
```

Expected:

```
Troubleshooting Network
```

---

# Summary of Design Patterns

| Question            | Pattern              |
| ------------------- | -------------------- |
| Notification System | Strategy             |
| Recharge Plans      | Factory              |
| Logger              | Singleton            |
| SIM Activation      | Builder              |
| Tower Alert         | Observer             |
| Call Routing        | Strategy             |
| Tower Database      | Repository           |
| Authentication      | Proxy                |
| Recharge Logging    | Decorator            |
| Billing Adapter     | Adapter              |
| Tower Startup       | Facade               |
| Complaint System    | Command              |
| Billing Sender      | Dependency Injection |
| Network Monitoring  | Observer             |
| AI Chatbot          | Factory + Strategy   |