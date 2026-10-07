# Prodapt AI Operations Center — Presentation Kit

A multi-agent AI system for a (fictional) telecom provider. One chat box takes a
plain-English customer/staff inquiry; a **LangGraph supervisor** routes it to
specialist agents (**LlamaIndex** RAG + semantic SQL, **Google ADK** A2A
microservices, **CrewAI** reply writer) and a **Streamlit** UI shows the answer
plus a full agent execution trace.

Source code lives in the project repo: <https://github.com/aravhrsh03/rag-capstone>.
This folder is the *presentation material* for it.

| File | Use it for |
|---|---|
| `PRESENTATION_SCRIPT.md` | Word-for-word talk track + demo clicks, ~10 min |
| `RUN_STEPS.md` | Exact steps to start the app before presenting |
| `HOW_IT_WORKS.md` | Deep architecture / code walkthrough (read once, reference during Q&A) |
| `QA_CHEATSHEET.md` | Likely questions with short answers |

## Order to use them
1. Follow `RUN_STEPS.md` 15 minutes before you present.
2. Read `PRESENTATION_SCRIPT.md` top to bottom; rehearse once with the live app.
3. Skim `QA_CHEATSHEET.md` before questions.
