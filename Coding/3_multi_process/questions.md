# AI Telecom Data Processing – Multiprocessing & Exception Handling Assignment

## Question 1: Call Drop Prediction

### Scenario
A telecom company has **1,000,000 call records**.

Use **multiprocessing** so that each process analyzes a chunk of records and predicts whether a call is likely to drop.

### Input

```python
call_records = [
    {"signal": -95, "latency": 250},
    {"signal": -70, "latency": 50},
    {"signal": -120, "latency": 500},
]
```

### Prediction Rules

- If **Signal < -100** → **Drop**
- If **Latency > 300** → **Drop**
- Otherwise → **Stable**

### Exception Handling

Handle the following exceptions gracefully:

- Missing `signal`
- Missing `latency`
- Invalid data type

### Expected Output

```text
Record 1 → Stable
Record 2 → Stable
Record 3 → Drop
```

---

# Question 2: Customer Churn Prediction

## Scenario

A telecom company wants to predict customer churn.

Use **multiprocessing**, where each process analyzes **10,000 customers**.

### Prediction Rules

Predict **Churn** if:

- Usage < 50 minutes
- AND Complaints > 3

Otherwise predict **No Churn**.

### Exception Handling

Handle:

- Missing usage
- Invalid complaint count
- Null customer ID

### Expected Output

```text
Customer 1001 → Churn
Customer 1002 → No Churn
```

---

# Question 3: Fraud Detection

## Scenario

A telecom company wants to detect suspicious recharge transactions.

The dataset contains **1,000,000 recharge transactions**.

Split the workload across all CPU cores using **multiprocessing**.

### Prediction Rule

Flag a transaction as **Fraud** if:

- Recharge amount > ₹5000
- AND multiple recharges occur within 5 minutes

Otherwise classify as **Normal**.

### Exception Handling

Handle:

- ValueError
- KeyError
- TypeError

### Expected Output

```text
Transaction 101 → Normal
Transaction 102 → Fraud
Transaction 103 → Normal
```

---

# Question 4: Telecom Chatbot Log Analyzer

## Scenario

An AI chatbot generated **5 million customer conversations**.

Analyze the logs using **multiprocessing**.

### Tasks

Count the number of conversations belonging to:

- Positive
- Negative
- Complaint
- Escalation

### Exception Handling

Handle:

- Corrupted log
- Missing conversation
- Empty text

### Expected Output

```text
Positive    : 210000
Negative    : 184500
Complaint   : 35000
Escalation  : 1200
```

---

# Question 5: Voice Quality Prediction

## Scenario

Each process analyzes **1000 voice samples**.

Predict the quality of each voice sample using the MOS (Mean Opinion Score).

### Prediction Rules

- MOS > 4 → Excellent
- MOS between 3 and 4 → Good
- MOS < 3 → Poor

### Exception Handling

Handle:

- Invalid audio
- Empty file
- Unsupported format

### Expected Output

```text
Sample 1 → Excellent
Sample 2 → Good
Sample 3 → Poor
```

---

# Question 6: AI Tower Traffic Prediction

## Scenario

Each telecom tower sends hourly traffic statistics.

Use **multiprocessing**, where **each process predicts traffic for one city**.

### Prediction Rules

- Users > 5000 → High
- Users between 2000 and 5000 → Medium
- Users < 2000 → Low

### Exception Handling

Handle:

- Missing traffic data
- Negative user count

### Expected Output

```text
Tower A → High
Tower B → Medium
Tower C → Low
```

---

# Question 7: Spam SMS Detection

## Scenario

An AI model classifies SMS messages as Spam or Not Spam.

Use **parallel processing**, where each process classifies a subset of messages.

### Input

```python
messages = [
    "Congratulations! Win ₹500000",
    "Your OTP is 234567",
    "Limited offer buy now"
]
```

### Prediction Labels

- Spam
- Not Spam

### Exception Handling

Handle:

- Empty message
- None
- Invalid encoding

### Expected Output

```text
Message 1 → Spam
Message 2 → Not Spam
Message 3 → Spam
```

---

# Question 8: Telecom Image Classification

## Scenario

Telecom engineers upload tower images.

Each process classifies **100 images**.

### Prediction Labels

- Healthy Tower
- Damaged Tower
- Cable Fault

### Exception Handling

Handle:

- File not found
- Corrupted image
- Unsupported format

### Expected Output

```text
Image 1 → Healthy Tower
Image 2 → Cable Fault
Image 3 → Damaged Tower
```

---

# Question 9: Telecom Complaint Prioritization

## Scenario

An AI system prioritizes customer complaints.

### Input

```python
complaints = [
    {"priority": 5, "issue": "No Signal"},
    {"priority": 2, "issue": "Recharge"},
    {"priority": 10, "issue": "Fiber Cut"}
]
```

### Prediction Rules

- Priority ≥ 8 → Critical
- Priority between 4 and 7 → Medium
- Priority < 4 → Low

### Exception Handling

Handle:

- Missing priority
- Negative priority
- Invalid issue

### Expected Output

```text
Complaint 1 → Medium
Complaint 2 → Low
Complaint 3 → Critical
```

---

# Question 10: AI Call Sentiment Analysis

## Scenario

Call center recordings have been converted into text transcripts.

Use **multiprocessing** to analyze **100,000 transcripts** by splitting the workload across CPU cores.

### Prediction Labels

- Happy
- Neutral
- Angry

### Exception Handling

Handle:

- Missing transcript
- Empty text
- UnicodeDecodeError

### Expected Output

```text
Transcript 1 → Happy
Transcript 2 → Neutral
Transcript 3 → Angry
```

---

# Mini Project: AI Telecom Data Processing

## Scenario

A telecom company receives **500,000 customer records every day**.

Each record contains:

```python
{
    "customer_id": 101,
    "usage": 250,
    "complaints": 2,
    "signal": -85
}
```

## Requirements

### 1. Multiprocessing

- Divide the records among all available CPU cores.
- Each process should analyze its assigned records.

### 2. Prediction Rules

Predict **High Risk** if **any** of the following conditions are true:

- Usage < 50
- Complaints > 3
- Signal < -100

Otherwise predict:

- Normal

### 3. Exception Handling

Skip invalid records without stopping the program.

Handle cases such as:

- Missing customer ID
- Missing usage
- Missing complaints
- Missing signal
- Invalid data types

### 4. Summary Report

Display the following statistics after processing:

```text
========= SUMMARY =========

Total Records : 500000
Processed     : 499850
Skipped       : 150
High Risk     : 12450
Normal        : 487400

Time Taken    : 8.2 seconds
```

---

# Learning Objectives

After completing this assignment, students should be able to:

- Use Python multiprocessing for CPU-intensive tasks.
- Divide large datasets among multiple processes.
- Apply AI-inspired rule-based predictions.
- Implement robust exception handling.
- Process millions of telecom records efficiently.
- Generate meaningful processing summaries and performance metrics.