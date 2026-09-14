# ML & Claude Deep Dive — Phase 6 (Machine Learning) and Phase 7 (Claude Layer)

This document explains, in depth, everything that was built in **Phase 6 (ML)**
and **Phase 7 (Claude)** of the Network Operations & Predictive Intelligence
platform: what each script does, the exact formulas/rules it enforces, why it
was built that way, and how the two phases connect to each other and to the
rest of the platform (Phases 1-5).

It assumes the reader has *not* read the code yet — every section explains the
"what" and the "why", not just the file name.

---

## 0. Where Phase 6 and Phase 7 sit in the platform

```
Phase 1  Local Python profiling / rule-based alerting (NP3) on one daily file
Phase 2  PySpark pipeline: clean -> aggregate country-codes to (grid, hour) -> GeoJSON enrich
Phase 3  Data Engineering: Airflow DAG, storage zones, star schema, pipeline-status record
Phase 4  FastAPI service (API1-API6) over the warehouse
Phase 5  React (Vite) NOC dashboard incl. Milan grid map
Phase 6  MACHINE LEARNING: engineered features -> risk classifier -> anomaly baseline -> batch scoring
Phase 7  CLAUDE: the reasoning / engineering-assistance layer on top of all of it
```

The project's own mental model (from the root `CLAUDE.md`):

> Data and Spark answer *what happened*. ML answers *is this unusual or
> risky*. Claude answers *what does the evidence mean, what should I inspect
> next, and how can we safely evolve the software* — over curated evidence
> only.

Two rules from `CLAUDE.md` apply to **both** phases and show up everywhere
below, so they are worth stating once up front:

1. **Activity values are proportional activity measures, not counts or MB.**
   Never converted into call/SMS counts or megabytes, in ML output, API
   strings, or anything Claude says.
2. **"High activity" is never "congestion".** There is no capacity/utilization
   data anywhere in the platform. The model and Claude may only ever say
   "high activity relative to baseline".

---

# PART A — Phase 6: Machine Learning

Phase 6 lives under `Phase6/`. It has one job: turn the Phase 2/3 hourly
warehouse (`hourly_grid_summary`) into an **operational attention signal** —
never a diagnosis, never a confirmed fault, never "congestion".

```
Phase6/
  ml/
    paths.py              shared, env-driven paths for every ML artifact
    features.py           ML2 — feature engineering (pandas + PySpark dual impl.)
    train.py               ML3 — label creation + chronological train/test + training
    evaluate.py             ML3 evaluation — metrics, confusion matrix, NP3 comparison
    anomaly_baseline.py     ML4 — hour-of-day historical baseline + anomaly scoring
    batch_score.py           ML6 — score every grid, persist outputs, print summary
    tests/                   leakage, model-training, anomaly-baseline, batch-score tests
  models/
    risk_classifier.joblib   the trained, persisted model bundle
  docs/
    ml_def.md                 the one-page problem statement
    ml2_feature_definitions.md  full spec + manual verification of the 6 features
    ml3_risk_classifier.md       full training/evaluation report with real numbers
```

## A.0 — The problem statement (`docs/ml_def.md`)

- **Objective:** predict whether a grid will experience unusually high
  activity during the *next* hour.
- **Prediction unit:** one grid, one future hourly interval (`t+1`).
- **Features:** computed only from the trailing window ending at `t` — never
  from `t+1` or later.
- **Target:** `HIGH_ACTIVITY_RISK` — whether `total_activity` at `t+1`
  exceeds a threshold relative to the grid's own recent baseline.
- **Business action:** predictions flag *locations to investigate*. They do
  **not** confirm congestion, degradation or a fault.
- **Non-goals:** the model never predicts congestion, capacity, throughput,
  latency or packet loss — that data does not exist in this platform.
- **Leakage prevention:** features only ever see `<= t`; the label only ever
  comes from `t+1`. This single rule is enforced in three independent places
  (feature engineering, label construction, and an automated test) — see A.1
  and A.7.

## A.1 — ML2: Feature Engineering (`ml/features.py`)

### What it produces

Six engineered features per `(grid_id, feature_timestamp)`, where
`feature_timestamp = t`. All are computed from a **trailing window ending at
`t`, inclusive** — nothing after `t` is ever read.

| # | Feature | Window | Formula | Meaning |
|---|---|---|---|---|
| 1 | `avg_activity` | 24h `[t-23, t]` | mean of `total_activity` | the grid's recent baseline activity level |
| 2 | `activity_growth` | two 12h halves of `[t-23, t]` | `(recent_12h_mean − prior_12h_mean) / prior_12h_mean` | is activity accelerating or decelerating over the last half-day vs. the half-day before it |
| 3 | `active_hours` | 24h `[t-23, t]` | count of hours where `total_activity > 0` | persistence/uptime of activity, 0–24 |
| 4 | `peak_ratio` | 24h `[t-23, t]` | `max(total_activity) / avg_activity` | burstiness — how far the single busiest hour is above the grid's own average |
| 5 | `variability` | 24h `[t-23, t]` | `stddev(total_activity) / avg_activity` (coefficient of variation) | normalized volatility, comparable across small and large grids |
| 6 | `internet_share` | 24h `[t-23, t]` | `sum(internet_activity) / sum(total_activity)` | what fraction of composite activity is data vs. voice/SMS |

### Zero-division / edge-case handling

No feature may ever produce `NaN`, `Infinity` or `-Infinity`. The rules:

| Condition | Feature | Result |
|---|---|---|
| `avg_activity == 0` | `peak_ratio` | `0.0` |
| `avg_activity == 0` | `variability` | `0.0` |
| `sum(total_activity) == 0` | `internet_share` | `0.0` |
| prior 12h mean `== 0` and recent 12h mean `== 0` | `activity_growth` | `0.0` |
| prior 12h mean `== 0` and recent 12h mean `> 0` | `activity_growth` | `1.0` (activity emerging from nothing) |
| less than 24h of history available | all | computed on the partial window that does exist (`min_periods=1`) |

### Two implementations, same math

`engineer_network_features()` dispatches to one of two backends depending on
the input type:

- **`_engineer_features_pandas`** — vectorized with `groupby().rolling()`
  windows per `grid_id`. Used for local/small runs and by the tests.
- **`_engineer_features_spark`** — the same six formulas expressed as
  PySpark `Window` functions (`rowsBetween(-23, 0)` for the 24h window,
  `rowsBetween(-11, 0)` / `rowsBetween(-23, -12)` for the growth halves).
  Used for the full warehouse-scale run, matching the project rule that
  large-scale computation stays in Spark.

Both paths are checked against each other and against manual arithmetic — see
A.7 for the real numbers.

### Output

`save_feature_table()` persists:
- **Parquet** (`data/analytics/network_feature_table/network_features.parquet`)
  — the full historical feature table (every grid, every hour it was computed
  for). In the actual run this is **1,679,994 rows**.
- **CSV** (`outputs/network_feature_table.csv`) — only the *latest* row per
  grid (one snapshot per grid, **10,000 rows** for the Milan grid), tagged
  `data_quality_status = "PASSED"`. This is the file the API and the
  `/network-health` check read for a fast, current snapshot.

## A.2 — ML3: Risk Classifier Training (`ml/train.py`)

### Step 1 — building the labeled dataset (`prepare_labeled_dataset`)

The target is created by joining each feature row (at `t`) to the *future*
`total_activity` at `t+1` (via a per-grid `shift(-1)` on the raw hourly
table):

```
HIGH_ACTIVITY_RISK = 1  if  future_total_activity(t+1) >= 1.5 * avg_activity(t)
                        AND future_total_activity(t+1) > 5.0
HIGH_ACTIVITY_RISK = 0  otherwise
```

The `> 5.0` floor exists so that a grid going from "almost nothing" to
"slightly more than nothing" (a large *relative* jump on a near-zero base)
doesn't get flagged as risk. The first 24 hours of the dataset (the "burn-in"
period) are dropped because their trailing windows are necessarily partial.

### Step 2 — chronological train/test split (`chronological_train_test_split`)

This is **not** a random split. All timestamps are sorted; the earliest 80%
become the training set and the latest 20% become the test set — this
mirrors how the model would actually be deployed (train on the past, evaluate
on the future). The function asserts `train_latest_timestamp < test_earliest_timestamp`
and raises if that is ever violated — a second, independent leakage guard on
top of the feature-window rule in A.1.

### Step 3 — training (`train_risk_model`)

- **Algorithm:** `LogisticRegression(class_weight="balanced", random_state=42, max_iter=1000)`
  — chosen for interpretability (see coefficients below), not raw accuracy.
- **Scaling:** `StandardScaler` fit **only on the training set**, then applied
  (never re-fit) to the test set and to every later scoring call. Fitting on
  test data would itself be a leakage bug; the code structurally prevents it
  by scoping the `fit_transform` call to `X_train` only.
- **`class_weight="balanced"`** compensates for the fact that "high activity
  risk" is a minority class (~10-12% positive rate) — without it, a trivial
  always-predict-negative model would score ~90% accuracy while catching zero
  real events.

### Step 4 — persistence (`save_model_artifacts`)

A single `joblib` bundle containing `{model, scaler, feature_names,
coefficients, split_info, model_type, random_state}` is written to
`Phase6/models/risk_classifier.joblib` (and copied to
`outputs/risk_classifier.joblib`). Every downstream consumer (API5's
`/network/predict-risk`, `batch_score.py`, `network_health.py`) loads this one
bundle — there is exactly one source of truth for "the model".

## A.3 — ML3 Evaluation (`ml/evaluate.py`)

Loads the persisted bundle, re-derives the same chronological test set, and
reports:

1. **Standard metrics** — accuracy, precision, recall, confusion matrix,
   compared against the test set's own base rate (so "70% accuracy" can be
   judged against "90.6% accuracy is what an always-negative predictor would
   get").
2. **Suspicious-accuracy check** — if accuracy exceeds 95%, the script
   flags it for manual leakage investigation rather than treating it as a win
   (a model that looks *too* good on this kind of temporal problem usually
   has a leak). In the actual run this did **not** trigger (accuracy was
   70.57%) — see the real numbers in A.7.
3. **Interpretability** — the logistic regression coefficients, printed with
   a plain-English direction (`Increases Risk (+)` / `Decreases Risk (-)`).
4. **NP3 rule-based comparison** — the model's predictions are compared
   against a rule reproduced from Phase 1's `AlertGenerator` (fires when
   `future_total_activity >= 2.0 * avg_activity`, floor `5.0`) across all four
   quadrants: agree-positive, ML-only, NP3-only, agree-negative. This is the
   evidence behind Claude's later "ML vs NP3" reasoning in `/network-health`.
5. **Three required, written observations** — proactive lead time over the
   rule, high overlap on severe spikes, and an explicit statement of the
   precision/recall trade-off and what it means operationally (use the model
   as a *prioritization filter*, not an automated dispatch trigger).

## A.4 — ML4: Anomaly Baseline (`ml/anomaly_baseline.py`)

This is a second, independent signal alongside the classifier — a simple,
transparent statistical baseline rather than a trained model.

- **`build_hourly_baseline`** computes the **median** `total_activity` for
  every `(grid_id, hour_of_day)` pair across the *entire* historical dataset.
  This captures each grid's own daily rhythm (e.g. grid 42 quiet at 3am, busy
  at 9am) as a fixed lookup table.
- It explicitly reuses `compute_baseline()` from **`Phase1/src/baseline.py`**
  — the same function that powers the original NP3 rule-based alert generator
  from Phase 1 — but with a different bucketing key: NP3 buckets by `grid_id`
  alone, within a single day, leave-one-out; ML4 buckets by
  `(grid_id, hour_of_day)` across the whole accumulated history as a fixed
  table. **One baseline implementation, two configurations** — this was a
  deliberate design choice to avoid maintaining two divergent "what is
  normal" definitions.
- **`score_anomaly`** compares one observation against its baseline:
  `anomaly_ratio = current_activity / baseline_activity`;
  `is_anomalous = anomaly_ratio >= 1.5` (the same 1.5x threshold used in the
  ML3 label definition, so the two signals are conceptually aligned). If no
  baseline exists for that `(grid, hour)` pair, the observation is scored as
  **non-anomalous** rather than flagged — a sparse-data grid is not assumed to
  be misbehaving.
- **`score_anomaly_batch`** is the vectorized version used by ML6. It uses
  `avg_activity` (the 24h trailing mean from the feature table) as the
  "current activity" proxy, rather than a single raw reading, so the anomaly
  score stays coherent with the same quantity the ML3 label is built from.

## A.5 — ML6: Batch Scoring (`ml/batch_score.py`)

The production entry point — designed to be called by the Phase 3
orchestrator (`de7_orchest.py`) as the final pipeline step. For every grid:

1. Load the **latest** feature snapshot per grid (from ML2's output).
2. Load the trained ML3 model bundle.
3. Apply the *training* scaler (`.transform`, never `.fit`) and
   `predict_proba` to get a `risk_score` in `[0, 1]`.
4. Map probability to an operator-facing level:
   `>= 0.60` → `HIGH`, `>= 0.35` → `MEDIUM`, else `LOW`.
5. Build the ML4 hourly baseline from history and score every grid's anomaly
   ratio against it (`score_anomaly_batch`).
6. Persist both signals together to `outputs/batch_risk_scores.parquet` /
   `.csv`, with a `scored_at` timestamp and `model_version` (traced back to
   the split timestamp the model was trained on).
7. Print an operational summary (counts of HIGH/MEDIUM/LOW, anomalous count)
   ending with an explicit reminder:

   > These scores are operational ATTENTION SIGNALS... This is NOT a
   > confirmed fault or congestion event.

This CSV/Parquet pair is what `Phase7/checks/network_health.py` reads to show
the "anomaly" signal alongside the live rule alert and live classifier call.

## A.6 — Shared paths (`ml/paths.py`)

Every artifact path (`HOURLY_GRID_SUMMARY`, `FEATURE_TABLE_*`,
`MODEL_BUNDLE_PATH`, `BATCH_RISK_SCORES_*`, `RISK_PREDICTIONS_*`) has a
sensible default derived from the project root, overridable through an
environment variable (e.g. `TELECOM_MODEL_BUNDLE_PATH`). This mirrors the
same pattern in `Phase3/config.py`, so the ML pipeline still runs if the repo
is moved or run in CI from a different root.

## A.7 — The real numbers (from `Phase6/docs/ml2_feature_definitions.md` and `ml3_risk_classifier.md`)

**Feature table:** 1,679,994 rows in the full parquet history; 10,000 rows
(one per grid) in the latest-snapshot CSV. Manual verification for grid 1 at
`2013-11-07 17:30:00` matched the pipeline output exactly to 4 decimal places
for all six features (e.g. `avg_activity = 68.7011`, `peak_ratio = 1.8345`,
`variability = 0.3835`).

**Chronological split:**

| Split | Range | Rows | Positive base rate |
|---|---|---|---|
| Train (80%) | 2013-11-01 18:30 → 2013-11-06 11:30 | 1,139,995 | 12.29% |
| Test (20%) | 2013-11-06 12:30 → 2013-11-07 16:30 | 289,999 | 9.41% |

**Feature coefficients (direction of risk):**

| Feature | Coefficient | Direction |
|---|---|---|
| `variability` | +0.5820 | strongest risk driver — volatile grids precede surges |
| `peak_ratio` | +0.2428 | bursty grids are more likely to spike again |
| `activity_growth` | −0.1902 | mean-reversion — a grid that already surged tends to cool down next |
| `internet_share` | −0.0472 | data-heavy grids are slightly more stable |
| `avg_activity` | −0.0014 | ~neutral — risk is scale-adjusted, not absolute-volume driven |
| `active_hours` | ~0.0000 | neutral — nearly constant across active urban cells |

**Test-set metrics:** accuracy 70.57% (vs. 90.59% for an always-negative
predictor — accuracy alone is misleading here), recall 68.29%, precision
19.54%. Confusion matrix: TN 186,023 / FP 76,693 / FN 8,652 / TP 18,631.

**ML vs. NP3 (2.0x rule) on the test set:** of the 2,670 real NP3-rule
alerts, the classifier agreed on 2,424 (90.8%) and missed 246. It additionally
flagged 92,900 intervals the rule missed — moderate surges (1.5x-1.9x) that
the fixed 2.0x threshold is structurally blind to. The documented conclusion:
**the model is a prioritization/attention filter, not an automated dispatch
trigger** — its 19.5% precision means roughly 4 in 5 HIGH flags will not turn
into a confirmed severe event, so a human still decides what to act on.

## A.8 — What Phase 6 deliberately does *not* do

- It never asserts congestion, capacity or a confirmed fault — only a risk
  probability and an anomaly ratio.
- It never trains or scores on data after `t` for a prediction about `t`
  (enforced structurally in features.py, and independently in the
  chronological split assertion, and independently again in
  `Phase7/checks/leakage_check.py` and the ML2/leakage test suite).
- It never converts `total_activity`/`internet_activity` into call counts,
  SMS counts or megabytes anywhere in its output.

---

# PART B — Phase 7: Claude Layer

Phase 7 lives under `Phase7/` (with companion `.claude/` config at the repo
root). It is organized as 16 labs, **C1 through C16**, each demonstrating one
capability of Claude/Claude Code applied to this specific platform. The
constant, non-negotiable architecture rule for all of them:

> Claude sees **curated evidence only** — 10-20 records, API responses, ML
> outputs, pipeline status. Never raw rows. Large-scale computation stays in
> Spark/SQL.

## B.0 — Core plumbing (used by almost every lab)

| File | Role |
|---|---|
| `config.py` | reads `Phase7/.env` (no external dependency — hand-rolled parser), exposes `API_BASE_URL`, `ANTHROPIC_API_KEY`, and the three model-tier ids |
| `api_client.py` | **thin** HTTP wrappers over Phase 4's API1-API6. Explicitly forbidden from containing business logic — "if a wrapper ever needs a calculation, the endpoint is missing and belongs in the API, not here." |
| `claude_client.py` | `get_client()` (Anthropic SDK client), `pick_model(tier)` mapping `fast`/`default`/`deep` to model ids, `text_of(message)` helper |
| `evidence.py` | builds the **curated evidence package** for one grid; composes ML4/ML6 scoring by calling API4 (features) then API5 (`predict-risk`) — this is the only place that turns raw feature values into a `risk_score`/`risk_level`/`direction` triple for Claude to read |
| `tools.py` | the tool schema list + `dispatch()` used by every tool-calling lab (C2, C14); every tool name maps 1:1 onto a real API endpoint |

### Model tiers (`docs/C1_model_selection.md`)

| Tier | Model | Use for |
|---|---|---|
| `fast` | `claude-haiku-4-5-20251001` | high-volume, low-stakes, unambiguous checks (bulk `/explain-grid`, routine `/check-pipeline`) |
| `default` | `claude-sonnet-5` | the everyday NOC assistant — C1, C2, C7 commands, single-grid explain/review |
| `deep` | `claude-opus-5` | multi-source investigation, signal disagreement, unhealthy-pipeline reasoning — C3, C9 combine step, C14 with a degraded pipeline, C15 CI review |

Rule of thumb (C16): spend model capability on *judgement under uncertainty*,
not on *finding data in a haystack* — fix the context design first, then pick
the model tier.

## B.1 — C1: Network Insight Generator (`c1_insight_generator.py`)

Turns one curated grid-evidence package (built by `evidence.py`) into an
explanation in **exactly four sections**, every time:

```
SEVERITY       NORMAL / ATTENTION / HIGH  (or INSUFFICIENT EVIDENCE)
EVIDENCE       only numbers present in the package, quoted
INTERPRETATION what this MIGHT mean — explicitly marked as inference
NEXT CHECKS    what a human engineer should look at next
```

Enforced rules (in the system prompt): never assert congestion; never invent
a number not in the evidence; if the evidence is insufficient, say so
explicitly instead of guessing; if `pipeline_status` is missing/unhealthy,
let that constrain the severity. The `--drop <field>` flag removes an
evidence key before sending (e.g. `--drop anomaly`) specifically to prove the
model degrades to "INSUFFICIENT EVIDENCE" rather than filling the gap with an
assumption — this is graded as an acceptance criterion.

## B.2 — C2: Tool-Using NOC Assistant (`c2_noc_assistant.py`)

A natural-language assistant that **must** call a real tool for every factual
claim (`get_network_summary`, `get_grid_activity`, `get_hotspots`,
`get_alerts`, `get_grid_features`, `get_anomaly_score`, `get_grid_location`,
`get_pipeline_status`) rather than answer from memory. Implements the
standard Anthropic tool-use loop: send messages + tool schemas → if
`stop_reason == "tool_use"`, dispatch each tool call, feed results back as
`tool_result` blocks → repeat until the model produces a final text answer.
Every tool call is appended to a `tool_log`, printed at the end as the
**TOOL-CALL LOG** — the grading contract is that every number in the answer
should trace to a line in that log. If a tool call fails (e.g. the API is
down), `dispatch()` returns `{"error": ...}` instead of raising, so the
assistant can name the failed tool and narrow its conclusion instead of
inventing a value.

## B.3 — C3: Long-Context Incident Investigation (`c3_incident_investigation.py`)

A deliberate **context-engineering experiment**: the same investigation
question is run twice against the same grid —

- **`CURATED`** — the same small evidence package as C1/evidence.py.
- **`DUMP-EVERYTHING`** — the anti-pattern: every raw activity point
  unsummarized, plus all 200 network-wide alerts, plus everything else that
  can be pulled — deliberately verbose, to make the contrast visible.

Both are sent through the same three-section prompt (`CURRENT EVIDENCE` /
`HISTORICAL EVIDENCE` / `UNCERTAINTY`), and the script prints the approximate
context size in characters for each so the difference is measurable, not just
asserted. `--unhealthy-pipeline` flips `pipeline_status.healthy` to `False`
and injects a simulated "rejected rows" reason, to prove the `UNCERTAINTY`
section changes materially when the trust signal degrades.

## B.4 — C4: Introducing Claude Code to the repo

No script — this is the governance layer: the root `CLAUDE.md` (the
non-negotiable rules quoted in Part 0) plus `docs/C4_REPO_MAP.md` (the
directory-by-directory responsibility map and the landing→dashboard data-flow
diagram) and `docs/C4_MISSING_TESTS.md`. The stated acceptance test: ask
Claude Code *"is grid 4821 congested?"* — the correct behavior is to correct
the framing, not answer the question as posed, because rule 4 (no capacity
data exists) makes the question itself invalid.

## B.5 — C5: Plan Mode

No script — a workflow deliverable (`docs/C5_PLAN_sharpest_activity_increase.md`):
use Claude Code's Plan Mode to draft an implementation plan for a real feature
("sharpest activity increase"), revise at least one element, then execute and
verify against the real tests.

## B.6 — C6: Permissions & Security Model

`docs/C6_permission_policy.md` classifies every category of operation into
**allow / ask / deny**, then `docs/C6_settings.local.sample.json` is the
concrete Claude Code settings file to copy into `.claude/settings.local.json`.

| Class | Examples | Why |
|---|---|---|
| **allow** | read source, run tests, lint, `git status`/`diff`/`log`, edit application code (`Phase2/spark`, `Phase4/app`, `Phase6/ml`, `Phase7`) | read-only or safety-netted by tests/review |
| **ask** | `pip install`, edit Airflow DAGs/pipeline config, edit API response models, `git commit`/`push`, DB migrations | silent supply-chain drift, production-DAG breakage, or contract breakage should never happen unseen |
| **deny** | read `.env`/`*.pem`/`secrets/**`, `rm`/`rmdir`, write/edit under `data/raw/` or `data/landing/`, destructive SQL (`psql`, `dropdb`) | credential exposure, irreversible loss, or breaking the immutable raw-data reproducibility anchor |

This is deliberately **learner-owned** — Claude was not allowed to write
`.claude/settings.local.json` itself; it could only explain the tradeoffs.

## B.7 — C7: Slash Commands (`.claude/commands/*.md` → `Phase7/checks/*.py`)

Five commands, each a thin prompt wrapper around a Python backend that only
*gathers and prints* — interpretation is left to Claude in the command prompt,
not baked into the script:

| Command | Backend | What it prints |
|---|---|---|
| `/check-pipeline` | `checks/check_pipeline.py` | `/pipeline/status` health summary |
| `/explain-grid <id>` | `checks/explain_grid.py` | activity, features, anomaly score, location → four-section explanation |
| `/network-health <id>` | `checks/network_health.py` | the `(grid_id, timestamp)` grain duplicate check **plus** all three signals side by side (rule alert, classifier, anomaly score) |
| `/review-anomaly <id>` | shares evidence assembly with explain-grid | four-section review focused on whether the anomaly is real/actionable |
| `/test-api` | runs the Phase 4 pytest suite | pass/fail summary |
| `/investigate-grid <id>` | fans out to the C9 subagents | the combined multi-specialist report |

`network_health.py` is worth detailing because it's the one script that
brings ML and rule-based signals together mechanically (Claude then reasons
over the printed JSON): it runs `grain_check.check_grain()` (see B.11), then
for one grid separately calls `/network/alerts` (rule alert), calls
`/network/grid/{id}/features` → `/network/predict-risk` (the live classifier
call), and reads the latest row for that grid out of
`outputs/batch_risk_scores.csv` (the ML6 anomaly signal) — printing all three
as one JSON block plus a compact summary object. It exits non-zero if the
grain check fails, which is the C7 acceptance criterion.

## B.8 — C8: Skills (`.claude/skills/*/SKILL.md`)

Skills package domain rules into a description-triggered file so they don't
need to be re-prompted every time. Three exist:

- **`network-anomaly-analysis`** — activates on "why is this grid flagged /
  what does this score mean / is this unusual". Requires five evidence items
  before answering (current activity, baseline excluding the current
  interval, anomaly score + direction, firing rule alerts, pipeline status);
  refuses to produce a severity if any are missing. Enforces the same
  four-section format as C1 and the same terminology rules (no "congestion",
  no unit conversion, "grid" ≠ "cell tower").
- **`pipeline-troubleshooting`** — activates on data-trust questions ("can I
  trust this data / why did a run fail / is the analytics layer stale").
- **`telecom-data-quality`** — activates when *reviewing a code change* to
  the Spark pipeline, feature code, warehouse schema or an API response, for
  grain / leakage / geographic-join / API-contract / terminology risk.

The documented before/after test: ask "Grid 4821 has a high activity number
this hour. Is it congested?" with the skill enabled vs. the folder renamed to
disable it — with the skill, the answer rejects "congested" and asks for
missing evidence instead of guessing a severity.

## B.9 — C9: Subagents & Orchestration (`.claude/agents/*.md`)

Four narrowly-scoped specialist subagents, each with a **restricted tool set**
and a single question it is allowed to answer:

| Subagent | Tools | Answers only |
|---|---|---|
| `data-pipeline-agent` | Bash, Read, Grep | is the underlying data trustworthy right now? |
| `network-analysis-agent` | Bash, Read | is this grid's activity pattern unusual *for this grid*? |
| `ml-analysis-agent` | Bash, Read | what is the model saying and why? |
| `api-agent` | Bash, Read | are the services up and is the served data fresh? |

The `/investigate-grid <id>` command is the **supervisor**: it runs all four
in parallel and produces one combined report — `SEVERITY` (single verdict),
`EVIDENCE` (attributed per specialist), `DISAGREEMENT` (surfaced explicitly,
never averaged away), `UNCERTAINTY`, `NEXT CHECKS`. The hard rule: if
`data-pipeline-agent` says the data is not trustworthy, that **caps** the
combined severity no matter what the other three found — trust in the data is
load-bearing for every other conclusion.

**When *not* to orchestrate** (a documented, deliberate anti-pattern
discussion): a single agent beats the four-agent fan-out when the pipeline is
already known unhealthy (one status check settles it), the question is
genuinely single-perspective ("what's the anomaly score for grid X"), or
latency matters more than breadth.

## B.10 — C10: Hooks (`Phase7/hooks/*.py`, wired via `.claude/settings.json`)

Two event-driven hooks that run *automatically*, outside any prompt:

1. **`post_edit_tests.py`** (`PostToolUse`, matches `Edit|Write|MultiEdit`) —
   after any edit under a Spark/ML path (`Phase2/spark`, `Phase2/src`,
   `Phase6/ml`, `Phase7/checks`), it automatically runs `grain_check.py` and
   `leakage_check.py`. These are described as "the two failures that are
   silent and expensive" — they never wait for CI. A failure exits code `2`
   so Claude sees it immediately; every run (pass or fail) is appended to
   `Phase7/logs/hook_outcomes.log`.
2. **`pre_pipeline_guard.py`** (`PreToolUse`, same matcher) — before any edit
   to an Airflow DAG or pipeline config path (`Phase3/dags`,
   `Phase3/pipeline`, `Phase3/config.py`, `de*_orchest.py`,
   `telecom_pipeline_dag.py`), it returns a permission decision of `"ask"`
   with an explicit reason, forcing a human confirmation before a change that
   could break a scheduled production run — logged either way.

The documented **hooks vs. CI** split: hooks are for the tight feedback loop
on the two or three failures you cannot afford to discover late (grain
duplication, feature leakage, pipeline-config confirmation); everything else
(full test suite, coverage, security scans, deploy gating) belongs in CI.

## B.11 — C11: Checkpoints & Safe Rollback (`Phase7/experiments/compare_thresholds.py`)

A worked experiment in reversibility: before changing the real ML4 anomaly
threshold, `compare_thresholds.py` **re-applies** candidate thresholds to the
*existing* batch scores (no retraining, no pipeline re-run) and prints a
before/after table — alert volume, distinct grids flagged, NP3 rule
agreement, and top-20 attention-list churn — so the operational impact can be
*predicted* before the real change is made. The documented procedure: commit
a checkpoint → preview with the script → make the real change → re-run batch
scoring → compare on the same metrics → roll back via `git reset --hard`
if the change added false positives without new signal (the worked example:
halving the threshold from 1.50 to 1.18 roughly doubled alert volume
2,961→5,922 with zero change to the top-20 list — i.e., pure noise, a
rollback candidate).

## B.12 — C12: MCP Server (`Phase7/mcp/network_mcp_server.py`)

A `FastMCP`-based server exposing the same API1-API6 endpoints as MCP tools
(`network_summary`, `grid_activity`, `grid_features`, `grid_location`,
`hotspots`, `alerts`, `pipeline_status`) so Claude Code (or any other MCP
client) can call them directly, without going through `tools.py`'s
Anthropic-SDK-specific dispatch. Same hard rule as `api_client.py`: **no
business logic** — every tool is one HTTP call returning the endpoint's JSON
verbatim. It does add input validation as a security boundary (`_grid`
rejects non-positive or absurdly large ids, `_limit` clamps to `[1, 100]`,
`_as_of` requires an ISO-date-shaped string) and never lets an exception
propagate into the MCP transport — everything funnels through `_safe()` into
a structured `{"error": ...}` result instead.

## B.13 — C13: Plugin (`Phase7/plugin/`)

Packages the whole team standard — commands, skills, subagents, hooks, the
MCP registration and a reference copy of `CLAUDE.md` — into an installable
Claude Code plugin (`network-engineering`) with a local marketplace, so
engineers don't have to hand-recreate the setup. `.claude/` and
`Phase7/hooks/` remain the **canonical, editable** sources; `build_plugin.py`
assembles the plugin bundle from them (never the other way around).
Versioning is semver on rule-weight: patch = wording fixes, minor = new
command/skill/agent, major = a `CLAUDE.md` rule change or a breaking hook
behavior change — and the rules in `CLAUDE.md` only change by team decision,
never silently inside a plugin version bump.

## B.14 — C14: Headless NOC Investigation Agent (`Phase7/agents/noc_investigator.py`)

A fully headless (no interactive input) agent: input a `grid_id`, output a
structured JSON brief:

```json
{
  "severity": "NORMAL | ATTENTION | HIGH | INSUFFICIENT EVIDENCE",
  "evidence": [ {"claim": "...", "value": "...", "source_tool": "..."} ],
  "uncertainty": "what is unknown or untrustworthy",
  "recommended_checks": ["...", "..."]
}
```

Two rules are enforced by the **harness** (the Python script), not merely
requested of the model, which is the point of the lab:

1. **`pipeline_status` is always called first** — by the script itself,
   before the model even starts its tool loop — and its result is injected
   directly into the first user message. If it comes back unhealthy (or is
   forced unhealthy with `--unhealthy-pipeline`), the model is told to cap
   severity at `ATTENTION` and record why in `uncertainty`.
2. **Graceful degradation, never estimation.** `--disable-tool <name>` makes
   that tool return `{"error": ...}` for the run. The agent still completes
   and returns a brief; it names the missing source in `uncertainty` instead
   of substituting a guess. `_parse_brief()` also hardens the harness side:
   if the model's final output isn't valid JSON, the script itself constructs
   a fallback `INSUFFICIENT EVIDENCE` brief rather than crashing or fabricating
   one.

Every evidence item is required to carry a `source_tool`, and the full
tool-call log is attached under `_meta.tools_called` for grading/audit.

## B.15 — C15: Headless CI Engineering Review (`c15_ci_review.py`)

Reviews a git diff against `CLAUDE.md` and reports risk — **advisory only**:
the script has no tools, cannot edit, cannot merge, cannot deploy. It gathers
the diff (`git diff <base>...HEAD`, falling back to unstaged/staged diff),
the full text of `CLAUDE.md`, and (optionally) already-captured test output,
and asks Claude to assess exactly six categories, each `OK`/`RISK`/`N/A`:

1. **data-grain** — could this reintroduce duplicate `(grid_id, timestamp)` rows?
2. **leakage** — could a feature see data after its own `feature_timestamp`?
3. **geographic join** — if this touches a map join, is it on `properties.cellId`?
4. **API contract** — is any response-shape change non-additive?
5. **terminology** — any new string asserting congestion or converting units?
6. **missing tests** — what test should exist for this change but doesn't?

The report always ends with the literal line *"This review is advisory.
Approval, merge and deployment remain with a human."* — a hard human boundary
baked into the prompt, not left to the model's discretion. The recommended
run order is: run the real pytest suite first and capture its output, *then*
run this review in addition — never as a substitute.

## B.16 — C16: Context, Cost & Usage Optimization (`context_lab/compare_designs.py`)

A measured (not hand-waved) comparison of two context designs for the same
question — *"Which grids need operational attention right now, and why?"*:

| | Design A — raw rows, all grids, current window | Design B — top-20 curated evidence |
|---|---|---|
| records | ~10,000 rows (one hourly window of `hourly_grid_summary`) | 20 |
| context size | ~2,570,000 characters | ~3,000-6,000 characters |
| est. input tokens | **~642,000** | ~1,000-1,500 |
| relative cost | **~450x** | 1x (baseline) |
| includes pipeline status? | no | yes |

Design A is not just expensive — it is described as **untrustworthy**,
because it omits `/pipeline/status` entirely and pushes aggregation work
(finding the grids that matter inside 10,000 raw rows) onto the model instead
of onto Spark, which is exactly the architecture the project rules forbid.
This measured ratio is the empirical backing for the platform-wide rule:
*never send raw rows; summarize history; always include pipeline status;
drop any field that wouldn't change the answer.*

---

# PART C — How the two phases connect

- **`Phase7/evidence.py::anomaly_score()`** is the literal bridge: it calls
  API4 (`get_grid_features`, which serves the ML2 feature table) and then
  API5 (`predict_risk`, which runs the persisted ML3 model), and returns a
  small `{risk_score, risk_level, model_version, direction}` object — this
  is the *only* place Phase 7 composes an ML result, and it does no
  thresholding of its own.
- **`Phase7/checks/network_health.py`** reads ML6's `outputs/batch_risk_scores.csv`
  directly (as the "anomaly" signal) alongside a live rule-alert check and a
  live classifier call, so all three of the platform's independent signals
  (Phase 1 rule, Phase 6 classifier, Phase 6 anomaly baseline) are visible to
  Claude in one place — Claude decides what a disagreement between them
  means; the script only gathers.
- **Both phases obey the same terminology contract.** ML6's own summary
  print statement ("NOT a confirmed fault or congestion event") and every
  Claude system prompt (C1, C2, C3, skills) state the identical rule in the
  identical words — this is not a coincidence, it is the single project rule
  in `CLAUDE.md` rule 4 propagated everywhere activity numbers are surfaced.
- **C11's threshold experiment** operates directly on ML4/ML6 output
  (`anomaly_ratio` in `batch_risk_scores`), and **C10's post-edit hook** runs
  ML6's own leakage/grain checks (`grain_check.py`, `leakage_check.py`)
  automatically the moment Phase 6 code changes — the Claude layer is wired
  to protect Phase 6's own non-negotiable rules (A.8) as code moves.

---

# Appendix — full file map

| Concern | File |
|---|---|
| ML feature engineering | `Phase6/ml/features.py` |
| ML label + training | `Phase6/ml/train.py` |
| ML evaluation | `Phase6/ml/evaluate.py` |
| ML anomaly baseline | `Phase6/ml/anomaly_baseline.py` |
| ML batch scoring | `Phase6/ml/batch_score.py` |
| ML artifact paths | `Phase6/ml/paths.py` |
| Trained model | `Phase6/models/risk_classifier.joblib` |
| ML docs (spec + real numbers) | `Phase6/docs/ml_def.md`, `ml2_feature_definitions.md`, `ml3_risk_classifier.md` |
| Claude config/wiring | `Phase7/config.py`, `Phase7/claude_client.py`, `Phase7/api_client.py` |
| Curated evidence builder | `Phase7/evidence.py` |
| Tool schemas + dispatch | `Phase7/tools.py` |
| C1 insight generator | `Phase7/c1_insight_generator.py` |
| C2 tool-using assistant | `Phase7/c2_noc_assistant.py` |
| C3 incident investigation | `Phase7/c3_incident_investigation.py` |
| C7 slash-command backends | `Phase7/checks/*.py` |
| C8 skills | `Phase7/.claude/skills/*/SKILL.md` (canonical: `.claude/skills/`) |
| C9 subagents | `.claude/agents/*.md` |
| C10 hooks | `Phase7/hooks/*.py` |
| C11 threshold experiment | `Phase7/experiments/compare_thresholds.py` |
| C12 MCP server | `Phase7/mcp/network_mcp_server.py` |
| C13 plugin | `Phase7/plugin/` |
| C14 headless investigation agent | `Phase7/agents/noc_investigator.py` |
| C15 CI review | `Phase7/c15_ci_review.py` |
| C16 context/cost lab | `Phase7/context_lab/compare_designs.py` |
| All C-lab docs (rationale, checklists, acceptance criteria) | `Phase7/docs/C*.md` |
