# Network Operations & Predictive Intelligence
### The Pitch Deck (feature by feature)

*Companion to `SCRIPT.md` — this file is the deck content; `SCRIPT.md` is what
you say and click while recording it.*

---

## Slide 1 — Title

**Network Operations & Predictive Intelligence**
*A live NOC platform that doesn't just show you the network — it tells you
what's happening, whether it's normal, and what to check next.*

---

## Slide 2 — The Problem

Every Network Operations team deals with the same three gaps:

- **Raw numbers, no context.** A dashboard can show a spike. It can't tell you
  whether that spike is normal for that cell at that hour, or genuinely unusual.
- **No trust signal.** If the underlying data pipeline had a bad run today, most
  dashboards show yesterday's numbers anyway — with total confidence, and no
  warning.
- **Investigation is manual.** An engineer has to open five tools, pull history,
  check a model score, and write up what it means — every single time, for
  every flagged cell.

**What a NOC team actually needs:** a system that separates *what happened*
from *is this unusual* from *what does it mean* — and never blurs the three.

---

## Slide 3 — The Promise

That separation is the whole design:

| Layer | Answers | Never does |
|---|---|---|
| **Data + processing** | *What happened?* | Interpretation |
| **Machine learning** | *Is this unusual or risky?* | Investigation, or claiming a confirmed fault |
| **AI assistant** | *What does the evidence mean? What next?* | The analytics stack's job; touching raw data |

> "Data tells you what happened. Machine learning tells you if it's unusual.
> The AI layer tells you what it means and what to check next — and it never
> does another layer's job."

That discipline is what makes every feature below both trustworthy and safe
to keep changing.

---

## Slide 4 — Feature 1: Trusted Ingestion

**What it does:** Every incoming daily activity file is validated *before* it
can touch anything downstream — schema check, minimum-quality check (no
malformed timestamps, no out-of-range grid IDs, no negative activity, no
duplicate files). Anything that fails is **quarantined with a named reason**,
never silently dropped and never silently processed.

**Why it matters:** A bad file corrupting the analytics layer is the single
most expensive kind of failure — because it doesn't announce itself. This
feature exists so it can't happen quietly.

**The proof point:** every file, good or bad, gets an audit row — filename,
status, row count, reason, timestamp. Nothing enters the system unaccounted for.

---

## Slide 5 — Feature 2: One Governed Pipeline, One Trust Signal

**What it does:** Ingested files are cleaned and aggregated at real scale
(distributed processing, not a single-machine script), loaded into a proper
analytics warehouse, and checked by **15 automated quality gates** after every
run — grain correctness, row-count consistency, geographic sanity, cross-layer
agreement. **Any single gate failing fails the whole run.**

That produces one machine-readable artifact everything else depends on: a
**pipeline status record** — "is the data behind this dashboard trustworthy,
right now?" It's not a log line; it's a first-class output the API, the
dashboard, and the AI assistant all read before saying anything.

**The proof point:** the platform has processed **1.68 million grid-hour
records** end to end, guarded the whole way by those 15 gates.

---

## Slide 6 — Feature 3: Live Network Summary

**What it does:** One glance answers "how's the network right now" — total
activity, how many grid cells are active, the peak hour, and the top cell for
the current reporting window.

**Why it matters:** This is the front door. It's the first thing an operator
sees, and it always shows the *data's own current time* (not the viewer's
clock) — critical for a system where "now" is a defined concept (`AS_OF`), not
just whatever the browser says.

---

## Slide 7 — Feature 4: Grid Explorer

**What it does:** Pick any one of the **10,000 geographic grid cells** covering
Milan and pull its hourly activity — SMS, call, and internet activity,
individually and combined — on demand.

**Why it matters:** Every summary and every alert eventually leads an operator
to ask "wait, show me *that specific cell*." This is that drill-down, and it's
just a thin, fast consumer of the same stable API everything else uses.

---

## Slide 8 — Feature 5: Hotspot Ranking + the Milan Map

**What it does:** Ranks grid cells by current activity and renders the
highlighted cells on a real, interactive map of Milan's 100×100 grid.

**Why it matters — and this is the detail worth dwelling on:** each cell in the
underlying map data carries *two* possible identifiers, and the wrong one
would silently draw every hotspot on its *neighbor's* square — full apparent
coverage, no error, no warning. This platform joins on the **correct**
identifier (`properties.cellId`, never the raw array index) and proves it: any
highlighted cell's centerpoint can be pulled independently and checked against
where it should actually sit. That's the difference between a map that *looks*
right and a map that *is* right.

---

## Slide 9 — Feature 6: Rule-Based Alerts

**What it does:** A transparent, explainable first layer of detection — each
cell's current activity is compared against its own recent baseline, and three
plain rules fire when activity is materially high, materially low, or spiking
sharply versus the previous hour. Every alert carries a human-readable reason.

**Why it matters:** No black box. An operator (or an auditor) can read the rule
and the number and understand *exactly* why an alert fired — before any machine
learning is involved at all.

---

## Slide 10 — Feature 7: Predictive Risk Scoring

**What it does:** A live machine-learning model estimates the probability that
a grid cell is about to see an activity surge in the **next** hour, from six
engineered features describing its trailing 24-hour behavior — how active,
how peaky, how erratic, how fast-growing, how internet-heavy.

**Why it's built honestly, not just impressively:** the model predicts the
*next* hour using only *past* data — never the same window it's being scored
on — and it's evaluated on a strictly time-ordered split (train on the past,
test on a later, genuinely unseen period). That discipline is what makes the
score real instead of a number that looks good on a slide and means nothing in
production.

**The honest number:** ~70.6% test accuracy — deliberately *lower* than the
~90% you'd get by predicting "nothing's wrong" every time, because it's tuned
to actually catch real surges (recall ≈ 68%) rather than stay quiet. It's an
**attention filter for a human**, not an automatic trigger — and a
suspiciously *higher* number here would actually be a red flag, not a win (see
Slide 12).

---

## Slide 11 — Feature 8: Anomaly Detection

**What it does:** A second, independent signal — not "is this predicted to
surge," but "is this unusual for *this specific cell at this specific hour of
day*, based on its own history." A cell that's normally quiet at 3am gets
judged against its own 3am baseline, not a network-wide average.

**Why it matters:** Three signals — the transparent rule, the predictive
model, and this historical-anomaly check — see three different things. When
they **agree**, an operator has high confidence fast. When they **disagree**,
that disagreement is surfaced as information, not smoothed away — because
that's exactly the case that deserves a closer look.

---

## Slide 12 — Feature 9: The AI Assistant

**What it does:** Ask it, in plain language, to explain a grid cell or the
network's current situation. It checks the pipeline's trust signal **first**,
then pulls current activity, history, the model's risk score, the anomaly
signal, and the cell's real location — all through defined tool calls into the
exact same API everything else uses — and returns a structured answer:

- **SEVERITY** — how urgent
- **EVIDENCE** — every number, traced to a real tool call
- **INTERPRETATION** — clearly marked as inference, not fact
- **NEXT CHECKS** — what a human should look at next

**Why it matters:** It never sees raw data, never invents a number, and never
asserts a network situation as fact without first checking whether the
underlying data can even be trusted. If the pipeline is unhealthy, it says so
instead of answering anyway.

---

## Slide 13 — Why You Can Trust Every Number On Screen

- The core grain rule — one row per grid cell per hour — is enforced **in
  code, in three separate places**, including the warehouse's own primary key.
- The risk model trains on a strictly time-ordered split; it never sees the
  future.
- The vocabulary is deliberately strict: this system never claims
  **"congestion"**, because there is no capacity or throughput data anywhere in
  it — only proportional **activity** measures.
- The pipeline has been tested against deliberately injected failures — a
  missing file, a duplicate, a malformed timestamp, negative values, a schema
  change — and each one produces a distinguishable, honest status.

---

## Slide 14 — The Scale, Recap

| | |
|---|---|
| Grid cells modeled | **10,000** (a 100×100 grid over Milan) |
| Analytics records processed | **~1.68 million** grid-hours |
| Quality gates per run | **15**, any single failure fails the run |
| Stable API surface | **6 endpoints** — summary, grid detail, hotspots/alerts, features, risk prediction, pipeline status |
| ML features per prediction | **6**, computed only from the trailing 24 hours |
| Independent detection signals | **3** — rule alert, predictive risk score, anomaly score |

---

## Slide 15 — Where This Goes Next

- Wire the ML risk scores directly into the hotspot ranking view.
- Replace the remaining hardcoded alert thresholds with the full rule engine.
- Expose the platform's tools over a standard protocol (MCP) so any AI surface
  can investigate a grid the same, grounded way.
- Keep accumulating history — the anomaly baseline gets sharper with every
  additional day of data.
- Point ingestion at a real live feed — the architecture doesn't change, only
  the source.

---

## Slide 16 — Close

*"Data tells you what happened. Machine learning tells you if it's unusual.
The AI layer tells you what it means and what to check next — without ever
doing the analytics stack's job."*

**Network Operations & Predictive Intelligence** — thank you.
