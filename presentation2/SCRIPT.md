# Recording Script — "Network Operations & Predictive Intelligence"

Word-for-word narration to follow while recording, mapped slide-by-slide to
`PITCH_DECK.md`. Target total runtime: **~9–11 minutes**.

---

## How to deliver this — 3 rules

1. **Lead with outcomes, not implementation.** Don't say "I used a distributed
   processing engine" — say "this scales to every day of data with the exact
   same logic," *then* mention what runs it.
2. **Never apologize for a number.** The model's 70.6% accuracy, the current
   pipeline health, the honest precision figure — present these as evidence of
   rigor, not weaknesses to rush past. A viewer trusts the pitch more, not
   less, when you own the honest numbers with a straight face.
3. **The two live-demo segments are the actual product.** Everything else is
   framing around them. If you only rehearse two things, rehearse the Slide 2
   hook and the Slide 12 AI-assistant demo.

---

## Before you hit record — checklist

- [ ] **Start the API** — `cd Phase4 && uvicorn app.main:app --reload` — confirm `http://localhost:8000/docs` loads.
- [ ] **Start the dashboard** — `cd Phase5/noc-dashboard && npm run dev` — confirm `http://localhost:5173` loads.
- [ ] **Open these ahead of time** so you never wait on-screen mid-take:
  1. Browser tab — the NOC dashboard (`localhost:5173`)
  2. Browser tab — the API docs (`localhost:8000/docs`)
  3. A terminal / Claude Code window in this repo, ready for the live AI-assistant demo
  4. This deck, in a readable view
- [ ] **Check `GET /pipeline/status` once before recording.** Either outcome is
      usable — pick your line:
  - `healthy: true` → present it straightforwardly: "the pipeline is healthy right now."
  - `healthy: false` → don't hide this. Frame it as the product working as
    designed (see Slide 12 notes below) — a system that admits its own limits
    instead of papering over them is a *stronger* pitch, not a weaker one.
- [ ] **Pick one `grid_id`** (e.g. `4821`) and reuse it everywhere — the hook,
      the full demo, the AI explanation — so the numbers stay consistent.
- [ ] Rehearse the Slide 2 hook at least twice.
- [ ] Silence notifications; full-screen the browser/terminal before each demo.

---

## Slide 1 — Title
**~15 sec**

**SAY:**
> "Hi, I'm [Your Name]. This is Network Operations and Predictive
> Intelligence — a platform that doesn't just show you the network, it tells
> you what's happening, whether it's normal, and what to check next. Let me
> show you, before I explain how it works."

**SHOW:** Title slide only.

---

## Slide 2 — THE HOOK (live demo, 60–90 sec) ⭐ most important segment
**~75 sec**

Don't explain anything yet — just show it.

**SAY (before switching):**
> "This is the live dashboard, and this is the live AI layer on top of it. No
> slides for the next minute — just watch."

**SHOW — switch to the dashboard at `localhost:5173`:**
1. Open **Hotspots & Milan Map**.
2. Point at the map: *"That's a real 10,000-cell grid over Milan, ranked by
   real activity, right now."*
3. Click the **top-ranked hotspot** polygon.
4. **SAY:** *"Now let's ask what that actually means."*

**SHOW — switch to Claude Code / your assistant window:**
5. Ask: *"Explain grid [your chosen id] right now."*
6. Let the four-part answer render. Don't summarize it — let it speak for
   itself for a few seconds.

**SAY (cutting back to the deck):**
> "That explanation didn't come from a script. Every number in it was pulled
> live from the exact platform you just saw. Now let me walk you through it,
> feature by feature."

**SHOW:** Return to Slide 3.

> **If you'd rather not risk a live call failing on camera:** pre-run this
> exact sequence once, screen-record it, and cut that clip in here instead of
> going fully live. What matters is that it looks and *is* real, not that
> it's unedited.

---

## Slide 3 — The Problem
**~25 sec**

**SAY:**
> "Here's why that matters. Every NOC deals with the same problem: raw
> numbers everywhere, but no easy way to know if a number is actually normal.
> A dashboard can show you a spike — it can't tell you whether you can even
> trust the data behind it, and it can't tell you what to do about it."

**SHOW:** Problem slide.

---

## Slide 4 — The Promise
**~25 sec**

**SAY:**
> "So the whole product is built around one boundary. Data and processing
> tell you what happened. Machine learning tells you if it's unusual or
> risky. And the AI layer tells you what it means and what to check next. No
> layer does another layer's job. That discipline is what you just watched
> work."

**SHOW:** The three-layer table. Read the closing quote slowly.

---

## Slide 5 — Feature 1: Trusted Ingestion
**~30 sec**

**SAY:**
> "Let's go feature by feature, starting at the very front door. Every file
> that comes in is validated before it touches anything downstream — schema,
> minimum quality, sane values. Anything bad is quarantined with a named
> reason, never silently dropped, and never silently processed either. That
> matters because a bad file corrupting the analytics layer is the most
> expensive kind of failure there is — the kind that doesn't announce
> itself."

**SHOW:** Feature 1 slide.

---

## Slide 6 — Feature 2: One Governed Pipeline, One Trust Signal
**~35 sec**

**SAY:**
> "After ingestion, the data is processed at real scale and loaded into an
> analytics warehouse. Then fifteen automated quality gates check the output
> — any single failure fails the whole run. That produces one artifact
> everything else depends on: a pipeline status record. It's not a log
> line — it's a machine-readable trust signal that the API, the dashboard,
> and the AI assistant all check before they say anything. This platform has
> processed one point six eight million grid-hour records end to end, guarded
> the whole way by those fifteen gates."

**SHOW:** Feature 2 slide, emphasize the trust-signal callout.

---

## Slide 7 — Feature 3: Live Network Summary
**~20 sec**

**SAY:**
> "That's what feeds the front page of the dashboard — total activity, how
> many cells are active, the peak hour, the top cell, all for right now.
> Notice it shows the *data's* current time, not the viewer's clock — that
> matters more than it sounds like it should."

**SHOW — optionally flash back to the Overview page for a few seconds.**

---

## Slide 8 — Feature 4: Grid Explorer
**~25 sec**

**SAY:**
> "Next, drill-down. Pick any one of the ten thousand grid cells and pull its
> hourly activity — SMS, call, internet, and combined — on demand. Every
> summary and every alert eventually leads someone to ask 'show me that one
> cell,' and this is that."

**SHOW — switch to Grid Explorer, type your chosen grid_id.**

---

## Slide 9 — Feature 5: Hotspot Ranking + the Milan Map
**~35 sec**

**SAY:**
> "You already saw the map in the opening hook — here's the detail worth
> dwelling on. Each cell in the underlying map data carries two possible
> identifiers, and using the wrong one would silently draw every hotspot on
> its *neighbor's* square — full apparent coverage, no error, no warning
> anywhere. This platform joins on the correct one, and proves it: any
> highlighted cell's real center point can be pulled independently and
> checked against where it should sit. That's the difference between a map
> that looks right and a map that is right."

**SHOW:** Feature 5 slide, or revisit the map briefly.

---

## Slide 10 — Feature 6: Rule-Based Alerts
**~25 sec**

**SAY:**
> "Before any machine learning gets involved, there's a transparent first
> layer: each cell's current activity compared to its own recent baseline,
> three plain rules, every alert carrying a human-readable reason. No black
> box — an operator can read exactly why an alert fired."

**SHOW:** Feature 6 slide.

---

## Slide 11 — Feature 7: Predictive Risk Scoring
**~45 sec — deliver the honest number with confidence, not apology**

**SAY:**
> "Now the machine learning. A live model estimates the probability that a
> cell is about to see an activity surge in the *next* hour, from six
> features describing its trailing twenty-four hours. And here's the number I
> actually want to talk about: seventy point six percent test accuracy — on
> paper, that's *worse* than just predicting 'nothing's wrong' every time,
> which would score about ninety percent. That's deliberate. It's tuned to
> actually catch real surges — about two out of every three — at the cost of
> some false alarms, which makes it an attention filter for a human, not an
> automatic trigger. And if this number had come back above ninety-five
> percent, that wouldn't be a win — it would mean the model was seeing its own
> answer, and I'd have gone back to fix it."

**SHOW:** Feature 7 slide, then switch to Predictive Risk page and submit your
chosen grid — *"a real inference, not a canned demo value."*

---

## Slide 12 — Feature 8 & 9: Anomaly Detection + the AI Assistant (second live demo)
**~90–120 sec**

**SAY:**
> "One more signal sits alongside the risk score: an anomaly baseline that
> asks 'is this unusual for *this* cell at *this* hour of day,' based on its
> own history — not a network-wide average. Now — three independent signals:
> a transparent rule, a predictive score, and a historical anomaly check. When
> they agree, that's high confidence fast. When they disagree, that's
> information surfaced to a human, not smoothed away. Let's put the AI layer
> in the room with all of it."

**SHOW — switch to Claude Code:**

- **If `/pipeline/status` is healthy**, ask something new:
  > "What's the network situation for the last hour?"

  Narrate as it runs: *"Watch — pipeline status first, then the summary, then
  hotspots, before it says a word."* When it answers, point to the four
  sections: **"Severity, evidence traced to real calls, interpretation clearly
  marked as inference, and next checks for a human."**

- **If `/pipeline/status` is currently unhealthy**, ask the same question and
  narrate the more interesting outcome:
  > "Watch what happens when the pipeline itself isn't healthy."

  When it reports the data can't be fully trusted rather than answering
  anyway: *"That's not a failure — that's the product working exactly as
  designed. It won't assert anything as fact until the trust signal says it
  can."*

**SAY (returning to slides):**
> "Nothing you've seen in this video was invented — every number came from a
> real tool call into the platform you've been watching."

---

## Slide 13 — Why You Can Trust Every Number
**~30 sec**

**SAY:**
> "A few things make this more than a demo. The one-row-per-cell-per-hour
> rule is enforced in code, in three separate places, including the
> database's own primary key. The risk model trains on a strictly
> time-ordered split so it never sees the future. The vocabulary is
> deliberately strict — this system never claims 'congestion,' because
> there's no capacity data anywhere in it. And the pipeline has actually been
> tested against injected failures, and each one produces a distinguishable,
> honest status."

**SHOW:** Feature 13 slide.

---

## Slide 14 — The Scale, Recap
**~20 sec**

**SAY:**
> "So, the numbers behind everything you just watched: ten thousand grid
> cells, one point six eight million analytics records, fifteen automated
> quality gates, six stable API endpoints, six engineered features, and three
> independent signals working together."

**SHOW:** Scale table.

---

## Slide 15 — Where This Goes Next
**~20 sec**

**SAY:**
> "And this isn't a finished, static thing. Next: wiring the ML risk scores
> directly into the hotspot view, replacing the remaining hardcoded thresholds
> with the full rule engine, exposing these tools over a standard protocol so
> any AI surface can investigate a cell the same way, and simply accumulating
> more history so the anomaly baseline keeps getting sharper."

**SHOW:** Roadmap bullets.

---

## Slide 16 — Close
**~15 sec**

**SAY:**
> "That's Network Operations and Predictive Intelligence — data tells you
> what happened, machine learning tells you if it's unusual, and the AI layer
> tells you what it means and what to check next, without ever doing the
> analytics stack's job. Thanks for watching — happy to answer questions."

**SHOW:** Closing slide. Hold for a beat before cutting.

---

## Timing summary

| Segment | Approx. time |
|---|---|
| Slide 1 (title) | ~15 sec |
| **Slide 2 (the hook — live demo)** | **~75 sec** |
| Slides 3–4 (problem, promise) | ~50 sec |
| Slides 5–10 (features 1–6) | ~2.75 min |
| Slide 11 (predictive risk + demo) | ~45 sec |
| **Slide 12 (anomaly + second live demo)** | **~1.5–2 min** |
| Slides 13–16 (rigor, recap, roadmap, close) | ~1.5 min |
| **Total** | **~9–11 min** |

If you need a shorter cut, keep only slides **1, 2 (hook), 4, 9, 11, 12
(demo), 16** — that alone tells the whole story, demo-first, in about
4–5 minutes.
