# Presentation Script (~10 minutes)

Text in **bold quotes** is what to say. `[CLICK]` / `[SHOW]` are actions.
The demo queries below match the project's five verified scenarios.

---

## 1. The problem (1 min)
**"Prodapt is a telecom provider. Today, answering one customer inquiry means a
human checks up to four separate systems — policy documents, an outage database,
live network dashboards and the billing system — then hand-writes a reply. It's
slow and error-prone."**

**"I built an AI Operations Center: one chat box, and a team of AI specialists
that fetch the real facts and write one accurate reply."**

## 2. The architecture in one picture (2 min)
[SHOW] the diagram in `HOW_IT_WORKS.md` section 3 (the mermaid diagram renders on GitHub).

**"There are five pieces, each chosen for a reason:"**
1. **"LangGraph is the brain — a supervisor. An LLM reads the question, decides which specialist to call next, and loops until done."**
2. **"LlamaIndex does retrieval only: PolicyRAG answers from six policy documents using a vector index; NetworkAnalytics turns English into SQL over the outage database."**
3. **"Google ADK runs Network Diagnostics and Billing as separate microservices on ports 8001 and 8002, talking over the A2A protocol — because in real life the NOC and Billing are different teams who deploy independently."**
4. **"CrewAI is the last step — a Communications Specialist drafts the reply and a Quality Reviewer checks it."**
5. **"Streamlit is the UI, with a live execution trace so you can see every decision."**

**"Two rules are enforced in code, not left to the LLM: the CrewAI writer always runs last, and there's a six-hop cap so the loop can never run forever."**

## 3. Live demo (5 min)
[SHOW] Streamlit, sidebar all green. **"These status lights are live health checks — database, vector index, both ADK services."**

### Demo A — Document RAG (30s)
Type: `What is Prodapt's roaming policy for Western Europe?`
**"The supervisor routes to PolicyRAG, which retrieves from the roaming policy — Travel Pass $10/day, Business $5/day, Enterprise included — then CrewAI polishes it."**
[CLICK] expand **Agent Execution Trace**: 2 steps (PolicyRAG → CustomerCommsCrew).

### Demo B — Text-to-SQL (30s)
Type: `Which region had the most CRITICAL network outages?`
**"This goes to NetworkAnalytics. LlamaIndex picks the right table by meaning, writes the SQL, runs it. Answer: Midwest, 6 critical outages."**

### Demo C — Agent-to-agent diagnosis (45s)
Type: `My 5G keeps dropping in Austin near tower TX-512. Please diagnose.`
**"Now the supervisor calls the Network Diagnostics service over A2A. It reads the latest sample for tower TX-512 — operational, 3.8% packet loss, open incident INC-8841 — and the reply tells the customer a known issue is being worked."**

### Demo D — The business rule (1.5 min) — main demo
Type: `Customer CUST-10002 was charged twice for Unlimited Plus. Investigate and apply credit.`
**"The Billing agent finds the duplicate $65.99 charge. Policy says credits up to $50 auto-apply; above that they need approval. So it records the credit as PENDING_APPROVAL and the balance stays $131.98."**
**"Notice the final reply says 'submitted for approval', not 'applied'. The Quality Reviewer is specifically told to catch that mistake."**
[SHOW] the trace.

### Demo E — Multi-agent chain (1 min)
Type: `We had a 6-hour outage in the Midwest. Am I eligible for an SLA credit and what does policy say?`
**"Two specialists this time: NetworkAnalytics finds the outage, PolicyRAG applies the SLA formula — $22.50 Business, $62.25 Enterprise pending, Consumer not eligible — and CrewAI merges both into one answer."**

## 4. What makes it trustworthy (1 min)
- **"No in-memory data — every tool re-reads SQLite on each call."**
- **"Answers come from tool calls and documents, not model memory."**
- **"Failure is graceful — if an ADK service is down, the graph returns the exact command to start it instead of crashing."**
- **"There's a pytest suite across every layer, and all five scenarios were run live end to end."**
- **"Testing caught a real bug: an Anthropic SDK version mismatch was silently turning RAG answers into 'Empty Response'. It's fixed by a version pin and documented."**

## 5. Close (30s)
**"One question in, a sourced and reviewed reply out, with every agent step visible. Each part — RAG, diagnostics, billing — can be swapped or deployed independently, and one setting, LLM_PROVIDER, switches the whole stack between Claude and OpenAI. Thank you — happy to take questions."**

---

## Timing cheat
| Section | Min |
|---|---|
| Problem | 1 |
| Architecture | 2 |
| Demo A–E | 5 |
| Trust | 1 |
| Close + buffer | 1 |

## If the live demo fails
Don't debug on stage. Say **"Let me show the verified results"** and read the
expected outcomes from the demo steps above (they match the project README's
Verification section).
