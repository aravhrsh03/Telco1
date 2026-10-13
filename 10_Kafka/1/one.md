# Apache Kafka - Corporate Technical Documentation

**Date:** 30/07/2026

---

# Keywords

* Kafka
* Apache Kafka
* Distributed Event Streaming Platform
* Event Streaming
* Message Broker
* Producer
* Consumer
* Broker
* Topic
* Partition
* ZooKeeper
* KRaft
* KafkaProducer
* KafkaConsumer
* kafka-python
* bootstrap_servers
* value_serializer
* value_deserializer
* key_serializer
* acks
* retries
* batch_size
* linger_ms
* compression_type
* client_id
* max_request_size
* auto_offset_reset
* ETL Pipeline
* Log Aggregation
* Real-Time Analytics
* Event-Driven Applications
* Python Kafka Client

---

# Tags / Abbreviations Reference

| Tag   | Meaning              |
| ----- | -------------------- |
| LIB   | Library              |
| USA   | Usage (example code) |
| PAR   | Parameters           |
| SYN   | Syntax               |
| WHY   | Why this is used     |
| EXA   | Example              |
| MET   | Methods              |
| CAT   | Cannot have it       |
| ALI   | Alias                |
| RES   | Expected Result      |
| OPT   | Optional             |
| ANE   | Another Example      |
| FUN   | Functions used       |
| DAM   | Data Members         |
| TYS   | Types                |
| VER   | Python Version       |
| USC   | Use Cases            |
| [COM] | CLI Command          |
| [INS] | Install this library |
| [STE] | Steps                |

---

# KAFKA (Apache Kafka)

## Definition

Apache Kafka is a distributed event streaming platform.

* It stores streams of data (events/messages) in the form of logs.
* It preserves the order of messages within a partition (first in, first out).
* It acts as a message broker between producers and consumers.
* It is designed to handle high-throughput, real-time data processing.
* Originally developed in Java, but supports clients in Python, Java, Go, C#, and many other languages.
* Data is stored durably and can be replayed by consumers.
* Commonly used for ETL pipelines, log aggregation, event-driven applications, and real-time analytics.

---

# Quick Flow

```
Producer → Kafka Topic → Consumer
```

---

# Kafka Components

| Component | Description                                                  |
| --------- | ------------------------------------------------------------ |
| Producer  | Sends messages (data) to Kafka.                              |
| Broker    | Kafka server that stores and manages messages.               |
| Topic     | A category/channel where messages are stored.                |
| Consumer  | Reads messages from a topic.                                 |
| ZooKeeper | (Old) Managed Kafka brokers and cluster coordination.        |
| KRaft     | (New) Kafka's built-in metadata manager; replaces ZooKeeper. |

---

# Kafka Python

## LIB

```
kafka-python
```

---

# INS

## Install Kafka Python Library

```bash
pip install kafka-python
```

---

# Producer

## WHY

Producer is responsible for sending messages/data to Kafka.

It writes data into a Kafka Topic.

---

# USA

## producer.py

```python
from kafka import KafkaProducer
import json

# Create Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

# Data/message to send
message = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Send message to Kafka topic
producer.send(
    "user_topic",
    value=message
)

# Ensure message is sent
producer.flush()

print("Message sent successfully!")
```

---

# PAR

## KafkaProducer Parameters

### bootstrap_servers

* Kafka broker address where the producer sends messages.
* Example:

```
localhost:9092
```

---

### value_serializer

* Converts Python data into bytes before sending to Kafka.

---

### key_serializer

* Converts message key into bytes before sending.
* Used for message partitioning.

---

### acks

* Controls producer confirmation level.

Values:

| Value | Description                  |
| ----- | ---------------------------- |
| 0     | No waiting for confirmation. |
| 1     | Leader confirmation.         |
| all   | All replicas confirmation.   |

---

### retries

* Number of retry attempts if message sending fails.

---

### batch_size

* Size of messages grouped together before sending.

---

### linger_ms

* Wait time to collect messages before sending a batch.

---

### compression_type

* Compresses messages to reduce network usage.

Examples:

```
gzip
snappy
lz4
```

---

### client_id

* Name/identifier of the producer client.

---

### max_request_size

* Maximum size of a message request allowed.

---

# Consumer

## WHY

Consumer reads messages from Kafka topics.

It continuously listens for incoming messages from Kafka.

---

# USA

## Consumer.py

```python
from kafka import KafkaConsumer
import json

# Create Kafka Consumer
consumer = KafkaConsumer(
    "user_topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# Read messages
for message in consumer:
    print("Received:", message.value)
```

---

# PAR

## KafkaConsumer Parameters

### KafkaConsumer

* Creates a consumer to read Kafka messages.

---

### "user_topic"

* Topic name to consume from.

---

### bootstrap_servers

* Kafka broker address.

Example:

```
localhost:9092
```

---

### auto_offset_reset

* Defines where to start reading messages.

Values:

| Value    | Description                           |
| -------- | ------------------------------------- |
| earliest | Read old messages from the beginning. |
| latest   | Read only new messages.               |

---

### value_deserializer

* Converts Kafka bytes back into Python data.

---

### for message in consumer

* Continuously listens for new messages.

---

# Kafka Producer and Consumer Flow

```
Python Producer
        |
        |
        v
Kafka Topic
        |
        |
        v
Python Consumer
```

---

# Summary

Apache Kafka provides a distributed, durable, and high-throughput platform for handling real-time event streams.

Using the `kafka-python` library:

* `KafkaProducer` sends messages to Kafka topics.
* `KafkaConsumer` reads messages from Kafka topics.
* Serializers convert Python objects into Kafka-compatible bytes.
* Deserializers convert Kafka bytes back into Python objects.
