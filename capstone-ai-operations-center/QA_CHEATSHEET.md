# Q&A Cheat Sheet

**Why five frameworks?** Each fits one job: LangGraph = routing loop, LlamaIndex = retrieval, ADK/A2A = independently deployable services, CrewAI = draft + review writing, Streamlit = fast UI.

**How does the supervisor decide?** An LLM with structured output (`RouteDecision`) picks one of six workers. Three code rules override it: no FINISH before CustomerCommsCrew, no repeating CustomerCommsCrew, no re-running a worker already used. Maximum 6 worker hops.

**What stops hallucination?** Facts come from tools and documents (SQLite, vector index). The reviewer agent checks the draft against those findings.

**What is A2A?** Google's Agent-to-Agent protocol. Each ADK service publishes an "agent card" at `/.well-known/agent-card.json`; LangGraph calls it through `RemoteA2aAgent` over HTTP.

**Why a $50 limit?** It is the billing policy: up to $50 → APPLIED (balance reduced); over $50 → PENDING_APPROVAL (balance unchanged). The balance never goes below zero.

**How does text-to-SQL pick the right table?** Each table has a human-written description; they are embedded in an `ObjectIndex`; the question is matched semantically, then the LLM writes the SQL. Billing tables are deliberately not exposed to it.

**Why is the first policy query slow?** It builds the vector index once (local HuggingFace embeddings) and persists it to `data/vector_index/`.

**Can it use another LLM?** Yes — `LLM_PROVIDER=openai` in `.env`; the ADK agents can use Gemini via `ADK_MODEL`.

**What if a service is down?** The node returns a message with the command to start it; the graph doesn't crash.

**How was it tested?** A pytest suite (config, DB, tools, state, remote client, graph, RAG error paths, crew fallback) plus all 5 spec scenarios run live.

**Limitations / next steps?** Credit approval is not a built workflow (credits stay PENDING_APPROVAL); the data is synthetic. See `DEPENDENCIES_AND_NEXT_STEPS.md` in the code repo.
