# Recording Script — "Retention Intelligence"

Word-for-word narration to follow while recording, mapped slide-by-slide to
`Retention_Intelligence_Demo.pptx` (built by `build_deck.py`). Target total
runtime: **~8–10 minutes**.

---

## How to deliver this — 3 rules

1. **Lead with outcomes, not implementation.** Don't say "we one-hot encode
   categorical features" — say "it tells you how risky a customer is,"
   *then* mention how, if asked.
2. **Never apologize for a number.** The model's F1 ≈ 0.57–0.58, the honest
   before/after risk-score flip, the fact a real bug was found in your own
   code — present these as evidence of rigor, not weaknesses to rush past.
   Finding and fixing a real defect with Claude, in front of the audience,
   is a *stronger* pitch than pretending nothing was ever wrong.
3. **The two live-demo segments are the actual product.** Everything else
   is framing around them. If you only rehearse two things, rehearse the
   Slide 2 hook and the Slide 12 Retention Assistant demo.

---

## Before you hit record — checklist

- [ ] **Start the API** — `cd D:\telecom_churn\Telecom-Churn-project && uvicorn main2:app --reload --port 8000` (check `main2.py` / `.env` for the exact port you've configured).
- [ ] **Start the dashboard** — `cd CustomerDashboard && npm run dev`.
- [ ] **Confirm `ANTHROPIC_API_KEY` is set** (`.env`) — the Retention Assistant tab calls the real Claude API live.
- [ ] **Open these ahead of time** so you never wait on-screen mid-take:
  1. Browser tab — the Customer Dashboard (Vite dev URL)
  2. Browser tab — the API docs (`/docs`)
  3. This deck, in a readable view
- [ ] **Pick two customer IDs and reuse them everywhere**: `7590-VHVEG` (the
      hook, and the CL1 before/after story) and `9237-HQITU` / `3668-QPYBK`
      (the second live demo) — these are real rows in
      `customer_ml_features.csv`, not placeholders.
- [ ] Rehearse the Slide 2 hook and the Slide 12 demo at least twice each.
- [ ] Silence notifications; full-screen the browser before each demo.

---

## Slide 1 — Title
**~15 sec**

**SAY:**
> "Hi, I'm [Your Name]. This is Retention Intelligence — a platform that
> doesn't just tell you a customer might leave, it explains why, backs
> that with a real model, and lets your team ask it anything in plain
> language. Let me show you, before I explain how it works."

**SHOW:** Title slide only.

---

## Slide 2 — THE HOOK (live demo, 60–90 sec) ⭐ most important segment
**~75 sec**

Don't explain anything yet — just show it.

**SAY (before switching):**
> "This is the live dashboard, and this is the live AI layer on top of it.
> No slides for the next minute — just watch."

**SHOW — switch to the dashboard:**
1. Open **High-Risk Customers**.
2. Point at the ranked list: *"Every one of these is a real customer,
   flagged by a fully explainable rule — month-to-month, under a year with
   us, paying above average."*
3. Switch to the **Retention Assistant** tab.
4. Ask: *"Is customer 7590-VHVEG one of our high-risk customers, and
   what's their predicted risk score?"*
5. Let the answer render, and point at the line showing which tools
   produced it. Don't summarize — let it speak for itself for a few
   seconds.

**SAY (cutting back to the deck):**
> "That answer didn't come from a script. Every number in it was pulled
> live, through a real tool call, from the exact platform you just saw.
> Now let me walk you through it, feature by feature."

**SHOW:** Return to Slide 3.

> **If you'd rather not risk a live call failing on camera:** pre-run this
> exact sequence once, screen-record it, and cut that clip in here instead
> of going fully live.

---

## Slide 3 — The Problem
**~25 sec**

**SAY:**
> "Here's why that matters. Every retention team deals with the same
> problem: a customer cancels, and only then does anyone look back and see
> the warning signs. A rule-based list can flag risk — it can't explain
> it, and it definitely can't answer 'why', or 'what if we offered them a
> different contract'."

**SHOW:** Problem slide.

---

## Slide 4 — The Promise
**~25 sec**

**SAY:**
> "So the whole product is built around one boundary. The database and
> pipeline hold what's actually true about a customer. The model estimates
> how risky they are. And the AI layer turns that into a plain-language
> answer — grounded in a real tool call every time, never a guess. That
> discipline is what you just watched work."

**SHOW:** The three-layer table. Read the closing quote slowly.

---

## Slide 5 — Feature 1: A Trusted Data Foundation
**~30 sec**

**SAY:**
> "Let's go feature by feature, starting at the foundation. One cleaning
> class fixes the dataset's real problems — once — and everything
> downstream imports it instead of re-implementing the fix. That's what
> lets a dashboard, a model, and an AI assistant all agree on the same
> customer: 7,043 of them, cleaned once, loaded into a typed schema."

**SHOW:** Feature 1 slide.

---

## Slide 6 — Feature 2: One Governed Pipeline
**~30 sec**

**SAY:**
> "That cleaning class feeds a real pipeline — seven stages, from
> ingestion through a scheduled daily brief, with a quality gate that has
> to pass and a PySpark cross-check proving the numbers hold on a
> completely different processing engine, not just in one notebook."

**SHOW:** Feature 2 slide.

---

## Slide 7 — Feature 3: Executive Churn Summary
**~20 sec**

**SAY:**
> "First stop on the dashboard: the executive summary. Total customers,
> churn rate, and the split by contract and service type — the number a
> manager actually opens the dashboard to see."

**SHOW — optionally flash back to the Churn Summary tab.**

---

## Slide 8 — Feature 4: Find Who's At Risk, Today
**~25 sec**

**SAY:**
> "Next, the ranked list retention teams actually work from — fully
> explainable, no model required to understand why someone's on it — plus
> instant lookup for any single customer by ID the moment a support call
> comes in."

**SHOW:** Feature 4 slide, or the High-Risk Customers / Customer Search tabs.

---

## Slide 9 — Feature 5: Predictive Risk Scoring — Audited and Fixed
**~50 sec — deliver the bug-and-fix story with confidence, not apology**

**SAY:**
> "Here's the number I actually want to talk about. We used Claude to
> audit our own inference code, and it found a real defect: the live
> prediction endpoint was only using four of the model's thirty-eight
> trained inputs — everything else silently defaulted to zero, for every
> customer, on every request. For one real customer, 7590-VHVEG, that bug
> produced 'unlikely to churn' at 45.8%. Fixed — using their real data —
> that same customer scores 56.5% and flips to 'likely to churn'. Same
> customer, opposite answer. That's the cost of the bug, and it's why we
> don't just say we fixed it — two git commits bracket the before and
> after, so it's auditable, not just claimed."

**SHOW:** Feature 5 slide with the three metric tiles.

---

## Slide 10 — Feature 6: The Retention Assistant
**~30 sec**

**SAY:**
> "And now the payoff — ask it anything. Four tools, wired directly into
> the same functions the dashboard already uses, so there's exactly one
> implementation of 'what's true about a customer', not two that could
> drift apart. Every answer shows its work, and it's built to refuse a
> question no tool can answer rather than invent a cause."

**SHOW:** Feature 6 slide.

---

## Slide 11 — Feature 7: Automation
**~25 sec**

**SAY:**
> "Two more places Claude works without anyone chatting with it at all: a
> daily brief that only ever sees aggregated risk deltas by segment, never
> a raw customer, and a code reviewer that runs automatically before any
> change reaches the shared repo."

**SHOW:** Feature 7 slide.

---

## Slide 12 — The Retention Assistant, Live (second live demo)
**~90 sec**

**SAY (before switching):**
> "Let's push it further than a lookup."

**SHOW — switch to the Retention Assistant tab:**
1. Ask: *"What's the overall churn rate, and how does customer
   9237-HQITU's predicted risk compare to that average?"*
2. Narrate as it runs: *"Watch — it calls the summary tool and the
   prediction tool, in the same turn, before it says a word."* Point at
   the tools-used line under the answer.
3. Ask a second, harder one: *"Customer 3668-QPYBK has a month-to-month
   contract. What would their churn risk look like on a two-year contract
   instead?"*

**SAY (returning to slides):**
> "Nothing here was invented — every number came from a real tool call
> into the platform you've been watching."

---

## Slide 13 — Why You Can Trust Every Answer
**~30 sec**

**SAY:**
> "A few things make this more than a demo. Every reply is checked against
> a fifteen-question evaluation set that specifically includes questions
> it should refuse to answer. Every tool argument is schema-validated
> before it touches the database. A secret-leakage guard runs on every
> outbound prompt in the system. And every conversation is written to a
> permanent audit log."

**SHOW:** Trust slide.

---

## Slide 14 — The Scale, Recap
**~20 sec**

**SAY:**
> "So, the numbers behind everything you just watched: seven thousand and
> forty-three customers, four live AI tools with no duplicated logic, a
> fifteen-question evaluation harness, and an honest F1 score on the class
> that actually matters — not raw accuracy, which a lazy model could win
> for free."

**SHOW:** Scale table.

---

## Slide 15 — Where This Goes Next
**~20 sec**

**SAY:**
> "And this isn't a finished, static thing. Next: put the pipeline DAG on
> a real scheduler, add per-customer authorization, and run the full
> two-model evaluation to lock in a production model choice with real
> numbers instead of a documented default."

**SHOW:** Roadmap bullets.

---

## Slide 16 — Close
**~15 sec**

**SAY:**
> "That's Retention Intelligence — the database tells you what's true, the
> model tells you how risky, and the AI layer tells you what to do about
> it, grounded in a real tool call every time. Thanks for watching — happy
> to answer questions."

**SHOW:** Closing slide. Hold for a beat before cutting.

---

## Timing summary

| Segment | Approx. time |
|---|---|
| Slide 1 (title) | ~15 sec |
| **Slide 2 (the hook — live demo)** | **~75 sec** |
| Slides 3–4 (problem, promise) | ~50 sec |
| Slides 5–11 (features 1–7) | ~3.5 min |
| **Slide 12 (Retention Assistant — second live demo)** | **~90 sec** |
| Slides 13–16 (rigor, recap, roadmap, close) | ~1.5 min |
| **Total** | **~8–10 min** |

If you need a shorter cut, keep only slides **1, 2 (hook), 4, 5, 9, 12
(demo), 16** — that alone tells the whole story, demo-first, in about
4–5 minutes.
