# Network Proj 2 — Run Guide

How to run the **Network Operations & Predictive Intelligence** platform end
to end, from a cold start to the AI (Claude) layer answering questions,
grounded in real tool calls.

This mirrors what's set up and verified on the build machine. If you're on a
different machine, the *order* of steps stays the same — only installed
versions and paths might differ.

---

## 0. What you need installed

| Component | Version used | Needed for |
|---|---|---|
| Python | 3.10 or 3.11 | everything |
| JDK | 11 or 17 | Spark |
| PySpark | matched to the JDK | the processing pipeline |
| MySQL | 8.x | the analytics warehouse |
| Node.js / npm | any recent LTS | the dashboard (optional) |
| An Anthropic API key with credit | — | the AI (Claude) layer |

Smoke test once, from the repo root:
```powershell
python --version
java -version
python -c "import pyspark; print(pyspark.__version__)"
python Phase3\config.py          # prints every resolved path/setting
```

---

## 1. Start MySQL

Make sure the MySQL server is running and reachable (default assumed:
`localhost:3306`, user `root`). `Phase3/warehouse/de6_load_mysql.py` creates
the database, tables and indexes automatically — nothing to set up by hand
unless you want to inspect the schema first (`Phase3/warehouse/de6_schema.sql`).

---

## 2. Run the data pipeline (Phase 3)

This ingests the raw daily activity files, runs the Spark processing job,
loads the warehouse, and runs **15 automated quality gates**. It writes
`Phase3/status/pipeline_status.json` — the trust signal every later layer
(API, dashboard, Claude) checks before saying anything.

```powershell
cd D:\main_project1

python Phase3\run_pipeline.py --dry-run     # see the resolved plan, runs nothing
python Phase3\run_pipeline.py               # the full run — expect ~8-12 minutes

Get-Content Phase3\status\pipeline_status.json
```

**Before moving on, confirm the run actually succeeded:**
```powershell
python -c "import json; d=json.load(open('Phase3/status/pipeline_status.json')); print(d['status'], d['as_of'], d['metrics']['rows_published'])"
```
You want `SUCCESS`, a real `as_of` timestamp, and a non-zero `rows_published`.
If it's unhealthy, everything downstream still runs — but the AI layer will
(correctly) refuse to assert anything as fact and will say the data can't be
trusted. That's expected behavior, not a bug, but you probably want a clean
run for a normal walkthrough.

Useful partial runs while iterating:
```powershell
python Phase3\run_pipeline.py --skip-spark      # reuse the existing analytics layer (~2 min)
python Phase3\run_pipeline.py --ingest-only     # just validate/route incoming files
```

---

## 3. Start the API (Phase 4)

```powershell
cd D:\main_project1\Phase4
python -m uvicorn app.main:app --reload --port 8000
```

Leave this running in its own terminal. Confirm it's up:
`http://localhost:8000/docs`

This is the **only** thing the dashboard and Claude are allowed to read from —
neither one touches the warehouse or raw files directly.

---

## 4. (Optional) Start the dashboard (Phase 5)

```powershell
cd D:\main_project1\Phase5\noc-dashboard
npm install        # first time only
npm run dev
```

`http://localhost:5173` — not required for the Claude layer, but this is
where you'd actually *see* the Milan hotspot map, the summary KPIs, and the
predictive-risk page.

---

## 5. The ML model (Phase 6)

Nothing to run here on a normal pass — the risk classifier is already trained
and saved at `Phase6/models/risk_classifier.joblib`, and the API loads it
automatically at startup. You'd only re-run training
(`Phase6/ml/train.py`) after loading new data through the pipeline.

---

## 6. Set up the AI layer (Phase 7)

```powershell
cd D:\main_project1\Phase7
pip install -r requirements.txt
```

`Phase7/.env` needs:
```
ANTHROPIC_API_KEY=sk-ant-...
NETWORK_API_BASE_URL=http://localhost:8000
```
(Copy `Phase7/.env.example` to `Phase7/.env` if it doesn't exist yet, then
fill in the key. The API key needs an Anthropic account with an active credit
balance — a `400 "credit balance is too low"` error means the key is valid
but the account needs billing set up at
`https://console.anthropic.com/settings/billing`.)

Quick connectivity check:
```powershell
python -c "from claude_client import get_client, pick_model, text_of; c=get_client(); m=c.messages.create(model=pick_model('fast'), max_tokens=20, messages=[{'role':'user','content':'Reply with: OK'}]); print(text_of(m))"
```

---

## 7. Run the Claude labs

All from `D:\main_project1\Phase7`, with the API from step 3 still running:

```powershell
python c1_insight_generator.py --grid 4821
python c2_noc_assistant.py --ask "Which areas need attention right now?"
python c3_incident_investigation.py --grid 4821
python agents\noc_investigator.py --grid 4821
```

Or, from Claude Code at the repo root (`D:\main_project1`), the packaged
slash commands:
```
/check-pipeline
/explain-grid 4821
/network-health 4821
/investigate-grid 4821
```

---

## The order that matters

```
MySQL running
   │
Phase 3 pipeline  →  writes pipeline_status.json (the trust signal)
   │
Phase 4 API  (uvicorn on :8000)
   │
   ├── Phase 5 dashboard (optional, :5173)
   │
   └── Phase 7 Claude layer  (needs Phase 7/.env + a funded API key)
```

Everything in Phase 7 depends on the API being up; the API depends on the
warehouse the pipeline loaded. Skip a step and you'll see either
`Connection refused` (API isn't running) or a 404 for a grid (the warehouse
hasn't been loaded, or that grid ID doesn't exist).

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'Phase3'` | run from `D:\main_project1`, not from inside `Phase3\` |
| No files detected during ingestion | the glob requires `-mi-` in the filename |
| MySQL `Access denied` | set `TELECOM_DB_USER` / `TELECOM_DB_PASSWORD` env vars |
| Spark `HADOOP_HOME unset` | set `HADOOP_HOME` to a dir containing `bin\winutils.exe` |
| A quality gate failed | read `quality_checks[]` in `pipeline_status.json` — every gate has a `note` explaining what it catches |
| `ANTHROPIC_API_KEY is not set` | create `Phase7/.env` from `Phase7/.env.example` |
| `400 credit balance is too low` | the key is valid; fund the Anthropic account, then retry |
| `GET /network/... Connection refused` | start the Phase 4 API on port 8000 (step 3) |
| `APIError ... 404` for a grid | use a `grid_id` that actually exists in the warehouse (1–10000, and the pipeline must have loaded data first) |
| Slash commands don't appear in Claude Code | run Claude Code from the repo root `D:\main_project1`, not from inside `Phase7\` |

Full detail: `Phase3/docs/RUNBOOK.md` and `Phase7/README.md` in the project repo.
