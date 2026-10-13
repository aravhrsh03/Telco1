# Network API Development Tasks

## Overview

This document contains a set of intermediate and advanced networking API development tasks.  
Each task requires creating a REST API endpoint that simulates telecom, router, switch, and network monitoring operations.

---

# Level 1 - Intermediate APIs

---

## 1. SIM Activation API

### Objective
Create an API to activate a SIM card for a customer with a selected plan.

### Endpoint

```

POST /activate

````

### Request Body

```json
{
  "sim_number": "9876543210",
  "customer": "John",
  "plan": "Unlimited"
}
````

### Expected Response

```json
{
  "message": "SIM Activated Successfully",
  "status": "Active"
}
```

---

## 2. Recharge API

### Objective

Create an API to recharge a mobile number with a selected amount.

### Endpoint

```
POST /recharge
```

### Request Body

```json
{
  "mobile": "9876543210",
  "amount": 299
}
```

### Expected Response

```json
{
  "mobile": "9876543210",
  "plan": "28 Days",
  "status": "Recharge Successful"
}
```

---

## 3. Signal Strength Check API

### Objective

Retrieve the signal strength and quality of a network tower.

### Endpoint

```
GET /signal?tower=Tower101
```

### Expected Response

```json
{
  "tower": "Tower101",
  "signal": "-72 dBm",
  "quality": "Good"
}
```

---

## 4. Router Login API

### Objective

Authenticate and connect to a network router.

### Endpoint

```
POST /router/login
```

### Request Body

```json
{
  "ip": "192.168.1.1",
  "username": "admin",
  "password": "admin123"
}
```

### Expected Response

```json
{
  "status": "Connected"
}
```

---

## 5. Network Device Inventory API

### Objective

Display all available network devices and their status.

### Endpoint

```
GET /devices
```

### Expected Response

```json
[
  {
    "hostname": "R1",
    "ip": "10.10.10.1",
    "status": "UP"
  },
  {
    "hostname": "SW1",
    "ip": "10.10.10.2",
    "status": "DOWN"
  }
]
```

---

## 6. Ping API

### Objective

Check whether an IP address is reachable and measure latency.

### Endpoint

```
GET /ping?ip=8.8.8.8
```

### Expected Response

```json
{
  "ip": "8.8.8.8",
  "status": "Reachable",
  "latency": "18 ms"
}
```

---

## 7. IP Validation API

### Objective

Validate whether an IP address format is correct.

### Endpoint

```
GET /validate?ip=192.168.1.100
```

### Expected Response

```json
{
  "ip": "192.168.1.100",
  "valid": true
}
```

---

## 8. VLAN Configuration API

### Objective

Create a VLAN configuration in a network switch.

### Endpoint

```
POST /vlan
```

### Request Body

```json
{
  "vlan_id": 20,
  "name": "HR"
}
```

### Expected Response

```json
{
  "message": "VLAN Created"
}
```

---

## 9. Interface Status API

### Objective

Retrieve network interface status and speed.

### Endpoint

```
GET /interface?name=Gig0/1
```

### Expected Response

```json
{
  "interface": "Gig0/1",
  "status": "UP",
  "speed": "1 Gbps"
}
```

---

## 10. MAC Address Lookup API

### Objective

Identify device vendor and type using a MAC address.

### Endpoint

```
GET /mac?address=AA:BB:CC:DD:EE:FF
```

### Expected Response

```json
{
  "vendor": "Cisco",
  "type": "Switch"
}
```

---

# Level 2 - Advanced APIs

---

## 11. Multiple Router Configuration API

### Objective

Configure multiple routers simultaneously and return success/failure count.

### Endpoint

```
POST /configure
```

### Request Body

```json
{
  "routers": [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3"
  ]
}
```

### Expected Response

```json
{
  "configured": 3,
  "failed": 0
}
```

---

## 12. Router Configuration Backup API

### Objective

Create a backup file of router configuration.

### Endpoint

```
POST /backup
```

### Request Body

```json
{
  "hostname": "R1"
}
```

### Expected Response

```json
{
  "status": "Backup Completed",
  "file": "R1.cfg"
}
```

---

## 13. Interface Utilization API

### Objective

Monitor transmit and receive bandwidth usage.

### Endpoint

```
GET /utilization?interface=Gig0/1
```

### Expected Response

```json
{
  "tx": "45%",
  "rx": "38%"
}
```

---

## 14. OSPF Neighbor Status API

### Objective

Retrieve OSPF neighbor connection states.

### Endpoint

```
GET /ospf
```

### Expected Response

```json
[
  {
    "neighbor": "10.10.10.2",
    "state": "FULL"
  },
  {
    "neighbor": "10.10.10.3",
    "state": "FULL"
  }
]
```

---

## 15. CPU Monitoring API

### Objective

Monitor router CPU utilization.

### Endpoint

```
GET /cpu
```

### Expected Response

```json
{
  "hostname": "R1",
  "cpu": "32%"
}
```

---

## 16. Memory Usage API

### Objective

Retrieve device memory statistics.

### Endpoint

```
GET /memory
```

### Expected Response

```json
{
  "used": "2 GB",
  "free": "6 GB"
}
```

---

## 17. Bandwidth Calculator API

### Objective

Calculate required bandwidth based on users and speed requirements.

### Endpoint

```
GET /bandwidth?users=250&speed=20
```

### Expected Response

```json
{
  "required_bandwidth": "5000 Mbps"
}
```

---

## 18. DHCP Lease API

### Objective

Retrieve DHCP lease information for an IP address.

### Endpoint

```
GET /lease?ip=192.168.1.20
```

### Expected Response

```json
{
  "hostname": "Laptop01",
  "lease_time": "12 Hours"
}
```

---

## 19. RESTCONF Device Details API

### Objective

Retrieve network device information using RESTCONF.

### Endpoint

```
GET /restconf/device
```

### Expected Response

```json
{
  "hostname": "CSR1000v",
  "version": "17.09",
  "serial": "FTX123456"
}
```

---

## 20. Network Health Dashboard API

### Objective

Provide a summary of overall network health.

### Endpoint

```
GET /dashboard
```

### Expected Response

```json
{
  "routers": 15,
  "switches": 32,
  "firewalls": 4,
  "up_devices": 49,
  "down_devices": 2
}
```

---

# Completion Criteria

A successful implementation should:

* Follow REST API standards
* Accept JSON request payloads where required
* Return proper HTTP status codes
* Validate input parameters
* Provide meaningful API responses
* Simulate real-world telecom and network management operations
