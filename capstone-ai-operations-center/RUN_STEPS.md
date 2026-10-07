# Run Steps (do this before presenting)

Requires Python 3.10+ and an `ANTHROPIC_API_KEY`. All commands run from the
project root (`capstone-project/`).

## One-time setup
```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env            # macOS/Linux: cp .env.example .env
# edit .env -> set ANTHROPIC_API_KEY=...
```
(`LLM_PROVIDER=openai` + `OPENAI_API_KEY` switches the whole stack to OpenAI.)

## Every time — 3 terminals (activate the venv in each)
```bash
# Once, resets demo data
python init_db.py                                   # expect: network_towers: 10 rows

# Terminal 1 - Network Diagnostics ADK service, port 8001
python adk-services/network_diagnostics/agent.py

# Terminal 2 - Billing Resolution ADK service, port 8002
python adk-services/billing_resolution/agent.py

# Terminal 3 - UI
streamlit run ui/app.py                             # opens http://localhost:8501
```

## Pre-flight checklist
- [ ] http://localhost:8001/.well-known/agent-card.json loads
- [ ] http://localhost:8002/.well-known/agent-card.json loads
- [ ] Streamlit sidebar shows Database / Vector index / both ADK services all green
- [ ] Ran scenario 1 once already so the vector index is built (first run is slow)
- [ ] Re-ran `python init_db.py` right before the demo (scenario 4 writes a credit row)

## Optional: prove it works with tests
```bash
pip install -r requirements-dev.txt
pytest
```

## If something breaks
| Symptom | Fix |
|---|---|
| Sidebar: Database not found | `python init_db.py` |
| ADK service "Not running" | start it in its own terminal; check ports 8001/8002 are free |
| API-key errors | key in `.env` matches `LLM_PROVIDER`; restart after saving |
| Stale policy answers | delete `data/vector_index/` and re-ask a policy question |
