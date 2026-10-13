# SCENARIO 2: Handling Long-Running ML Operations in FastAPI & React

> **The Challenge:** Your React frontend triggers a FastAPI endpoint to score thousands of transactions using a machine learning model. Because the entire pipeline (data loading, feature engineering, and inference) takes **40 to 60 seconds**, the UI appears frozen, leading to poor user experience and potential request timeouts.

---

## 🏗️ Architectural Design Solutions

To keep the user informed and prevent HTTP timeouts during heavy ML workloads, choose one of the following production-ready patterns:

### Option A: Asynchronous Task Queue with WebSockets / Polling (Recommended for Heavy Batch Jobs)

Best for operations exceeding 30 seconds, ensuring fault tolerance and background processing.

#### **1. Backend (FastAPI + Celery + Redis):**
* The API endpoint accepts the batch request, instantly spawns a background worker task, and returns a `task_id` with a `202 Accepted` status code.
* The background worker updates task progress (e.g., percentage completed or chunks processed) in Redis as it iterates through the batches.


#### **2. Frontend (React):**
* **Polling:** The React client periodically queries a status endpoint (`/tasks/{task_id}`) every few seconds to fetch the latest progress.
* **WebSockets:** Alternatively, establish a WebSocket connection for real-time, bi-directional progress updates pushed directly from the server.
* Display a dynamic **progress bar** and granular status messages (e.g., *"Engineering features: 45% complete"*).



### Option B: Streaming Responses (Server-Sent Events / SSE)

Best for continuous, step-by-step feedback where you want to stream results as soon as chunks are processed.

#### **1. Backend (FastAPI `StreamingResponse`):**
* Use FastAPI's `StreamingResponse` combined with generators (`yield`) to stream data chunks back to the client using Server-Sent Events (SSE).
* Process records in smaller batches (e.g., 500 records at a time), yielding progress updates or partial scoring results incrementally.


* **2. Frontend (React):**
* Consume the stream using the native `EventSource` API or standard `fetch` with readable streams to render results live as they arrive.



---

## 🚀 Implementation Blueprint (Task Queue + WebSockets Approach)

```
[React Frontend] --(1. POST /score)--> [FastAPI] --(2. Spawn Task)--> [Celery Worker]
       ^                                                                      |
       |---(3. WebSocket / Poll Progress)--- [Redis State Store] <------------|

```

* **Timeout Prevention:** HTTP connections are closed immediately with a `202` response, completely bypassing gateway/load balancer timeouts (like Nginx 504 errors).
* **User Experience (UX):** Replaces the "frozen screen" anxiety with an active progress bar, estimated time remaining (ETA), and a cancel option if needed.
* **Scalability:** Heavy ML workloads run asynchronously on worker nodes, keeping the FastAPI web server responsive to other incoming API requests.

---
---

# SCENARIO 2 (Continued): Handling WebSockets & State in Scaled FastAPI Deployments

> **The Challenge:** When scaling horizontally with a load balancer (`fastapi1`, `fastapi2`, etc.), you hit a distributed systems hurdle: **The client's WebSocket connection might land on `fastapi1`, while the background ML worker updates state or broadcasts messages through `fastapi2`.**

---

## ⚡ The Solution: Decoupled State & Redis Pub/Sub

To make your architecture stateless and robust across multiple server instances, you must decouple WebSocket connections from task execution using **Redis Pub/Sub** as a message broker.

### How It Works:

1. **Centralized State:** The ML worker updates its progress directly in **Redis** (the single source of truth), completely independent of which FastAPI instance triggered it.
2. **Pub/Sub Broadcasting:** When the worker updates progress, it publishes the event to a Redis channel (e.g., `task_progress:{task_id}`).
3. **Any Instance Can Relay:** Whichever FastAPI instance (`fastapi1` or `fastapi2`) currently holds the client's open WebSocket connection is subscribed to that Redis channel. It instantly catches the message and forwards it down to the React frontend.

---

## 🛠️ Architectural Blueprint

```
[React Frontend] 
       │ (WebSocket connection - lands on FastAPI 2)
       ▼
  [FastAPI 2] ◄──(Subscribed)──┐
                                │
[Redis Pub/Sub & State Store] ──┘
       ▲
       │ (Publishes progress updates)
[Celery Worker (Runs ML Job)]

```

---

## 🚀 Alternative Scaling Strategies

### **1. Sticky Sessions (Session Affinity):**
* Configure your load balancer (e.g., Nginx, AWS ALB) to use sticky sessions based on cookies or IP addresses.
* *Drawdown:* Less resilient if a backend instance crashes mid-job; Redis Pub/Sub remains the cleaner, cloud-native standard.


### **2. Fallback to Polling for Simplicity:**
* If managing a WebSocket cluster feels too complex for your current scale, use **HTTP Polling** instead. Because state is stored centrally in Redis, the React frontend can query `/tasks/{task_id}` via the load balancer, and *any* FastAPI instance can instantly return the correct progress.