# Network Operations & Predictive Intelligence — Sales Presentation Kit

This folder is everything you need to record a "selling the product" walkthrough
video of the platform: a slide-by-slide pitch deck, a word-for-word recording
script, and a Q&A cheat sheet for questions afterward.

It is written feature-by-feature — each capability of the product gets its own
slide and its own script section, so you (or anyone else) can present the
platform as a product, not as a class assignment.

## Contents

| File | Use it for |
|---|---|
| `PITCH_DECK.md` | The deck itself — 15 slides in Markdown. Read it top to bottom to see the full pitch, or open it side-by-side while recording. Renders cleanly on GitHub. |
| `SCRIPT.md` | The full narration, slide by slide: what to say, what to click, how long each part should take (~9–11 min total). This is the file to actually follow while recording. |
| `QA_CHEATSHEET.md` | Likely questions a reviewer/buyer will ask afterward, with a 2–4 sentence answer for each. |

## Quick start

1. Skim `PITCH_DECK.md` once so the flow is in your head.
2. Open `SCRIPT.md`, read the **"Before you hit record"** checklist, and start
   the API + dashboard as instructed.
3. Record following `SCRIPT.md` slide by slide. Two sections are marked
   **LIVE DEMO** — those are the actual product; everything else is framing
   around them.
4. Skim `QA_CHEATSHEET.md` before taking questions live.

## What this product is, in one line

A telecom Network Operations platform that ingests raw mobile-network activity,
turns it into a governed, trustworthy analytics layer, scores it for risk and
anomalies with machine learning, serves all of it through a stable API and a
live dashboard, and puts an AI assistant on top that explains what the evidence
means — grounded only in real tool calls, never invented.

## A note on accuracy

Every number in this kit (10,000 grid cells, 1.68M analytics rows, the model's
70.6% test accuracy, the 15 quality gates, etc.) is pulled from this
project's own `PROJECT_WALKTHROUGH.md` and `PROJECT_DEEP_DIVE.md` at the repo
root — not invented for the pitch. If you re-run the pipeline or retrain the
model, treat these as a snapshot and re-check the current figures before
quoting them live (the platform's own trust signal — `/pipeline/status` — is
exactly the mechanism built for that check; use it).

This kit also follows the project's own vocabulary rules throughout: activity
values are described as **proportional activity measures**, never as message
counts or megabytes; high activity is described as a **hotspot** or an
**attention signal**, never as "congestion"; a risk or anomaly score is
described as a **signal**, never a confirmed fault.
