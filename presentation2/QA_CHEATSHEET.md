# Q&A Cheat Sheet — Network Operations & Predictive Intelligence

Likely questions after the pitch, with a 2–4 sentence answer for each. If you
get one you genuinely can't answer, say **"Good question — let me follow up on
that"** rather than guessing.

---

## Value & purpose

**What's the business value? Who uses this?**
A NOC engineer today has to scan thousands of cells to find where to look.
This gives them a ranked, evidence-backed shortlist, and the AI assistant
pre-assembles the investigation — current activity, history, the model's view,
and whether the data itself can be trusted. It turns "where do I even start"
into "here are the cells that matter and why."

**Is this production-ready?**
It's a complete, working reference implementation, end to end, on a public
benchmark dataset. The architecture, the data discipline, the API contracts,
and the AI guardrails are done. A live deployment needs a real data feed
connected — the design doesn't change.

**What would it take to run this on real network data?**
Point ingestion at the real feed, map the source schema to the canonical one,
point the warehouse at a real database, retrain the model on real history.
Everything above the ingestion layer is unchanged — that's the payoff of
building the API contracts first.

**Why build every layer instead of just the useful bit?**
Each layer closes a gap the previous one leaves open. Without the warehouse,
every query re-scans files. Without the trust signal, nothing downstream can
tell you when the data is bad. Without stable API contracts, every internal
change breaks the dashboard.

---

## Architecture

**Why process at scale for a small dataset?**
The volume today isn't the point — the same processing logic runs on months
or years of files with no rewrite. Building it this way now forces the
distributed-processing discipline you'd otherwise learn the hard way once it's
live.

**Why a separate warehouse instead of querying files directly?**
Indexed relational queries are far faster for the API, and the schema's
primary key physically enforces the one-row-per-cell-per-hour rule — the
database itself refuses a duplicate.

**Why an API layer at all?**
It's the stable contract between the platform and everything that consumes
it. It let the dashboard, the ML integration, and the AI assistant get built
in parallel, and it means internal changes don't break anything downstream.

**What happens if a component fails?**
The system is designed to fail safely: a processing failure leaves the last
good analytics layer untouched and marks the run failed. The API returns
clear errors. The AI assistant reports the gap and narrows its conclusion
instead of inventing an answer.

**Are you locked into one AI vendor?**
The AI layer is a thin wrapper over the platform's own API using a standard
tool-calling approach — the model is swappable. The entire data and ML stack
has zero dependency on any AI; it runs on its own.

---

## Data correctness

**How do you know the numbers are right?**
Fifteen automated quality gates run every pipeline run — grain, geography, row
counts, cross-layer consistency — and any one failing fails the whole run. The
single most important check — one row per cell per hour — is enforced in
three separate places, including the database's own primary key.

**What's "the grain" and why does it matter so much?**
The raw data splits each cell-hour by an extra dimension, so one cell-hour is
actually several rows until they're summed together. Skip that step and every
downstream number is inflated — proportionally, so nothing *looks* wrong.
It's the single most important rule in the project.

**The source data is from 2013 — is that a problem?**
Not for demonstrating the platform — it's a well-known public benchmark. The
platform defines its own concept of "now" from the data itself, so historical
data behaves exactly like a live feed would, and any hour can be replayed
reproducibly. Real data plugs into the same slots.

**How do you know the map is correct?**
Each cell in the source geometry has two possible identifiers, and using the
wrong one shifts every hotspot to its neighbor's square — with no error and
100% apparent coverage. The platform uses the verified one and proves it: any
highlighted cell's real center point can be checked independently.

---

## Machine learning

**Your model's accuracy (71%) is worse than doing nothing (91%). Why is that
okay?**
"Doing nothing" scores ~91% by never flagging anything — and catching zero
real surges. This model catches about 68% of them. It's deliberately tuned
that way: a filter that surfaces candidates for a human, not an automated
trigger. The cost is false alarms, which a quick review absorbs.

**Can't you just make it more accurate?**
Yes — raise the threshold and accuracy goes up, but recall goes down: more
real surges get missed. Where to set that trade-off is an operations cost
conversation, not a modeling fix.

**Why such a simple model?**
It's interpretable — every score can be traced to which feature drove it —
and on this problem, a more complex model wouldn't add value. The value is in
the problem framing and the features, not the algorithm.

**How do you know the model isn't cheating?**
It's evaluated on a strictly time-ordered split — trained on the earlier
period, tested on a later, genuinely unseen one — and precision, recall, and
the base rate are reported, not just accuracy. A near-perfect score on this
data would mean the model saw its own answer; it would trigger an
investigation, not applause.

**Why three different signals instead of one?**
They see different things: a transparent threshold on recent history, a
predictive score for the next hour, and a historical-deviation check. When
they agree, confidence is high. When they disagree, that disagreement is
surfaced to the operator, not hidden.

---

## The AI layer

**How do you stop the AI from making things up?**
It can only answer using values it fetched through defined tool calls into
the platform's own API — it has no access to raw data at all. It separates
observed facts from inference, and when evidence is missing it says so rather
than filling the gap.

**What if it gives a bad recommendation?**
It recommends what to check — it never takes action, and a human makes every
decision. It also runs under a permission policy that denies anything
destructive.

**Is data sent to an external AI provider?**
Only the curated evidence for one specific question — a handful of API
responses and scores, never raw data or the full warehouse. That's a
deliberate design choice for cost and privacy.

**Does this replace NOC engineers?**
No. It removes the grunt work — gathering evidence, checking whether the
pipeline is healthy, drafting a first-pass assessment — so an engineer spends
time on judgment instead of collection.

---

## Skeptical / challenge questions

**What's the weakest part of this?**
Honestly, the ML — a week of data is thin, so precision figures aren't fully
stable yet, and one of the six features currently carries no signal because
every cell looks the same on it. That's a data-quantity issue, not a design
flaw; it improves with more history.

**What's actually transferable beyond the demo dataset?**
All of it: the quarantine-on-ingest pattern, the grain discipline, the stable
API contracts, the machine-readable trust signal, the honest ML evaluation,
and the AI guardrails — the things that are painful to retrofit once a system
is already live.

**What's the ROI?**
Faster, more consistent incident triage — the engineer starts with evidence
instead of a blank screen — and a platform that's safe to keep evolving:
stable contracts, automated quality gates, and an AI layer that checks its own
evidence before it speaks, so changes don't silently break things.
