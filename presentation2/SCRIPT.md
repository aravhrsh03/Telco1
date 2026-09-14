# Recording Script — "Network Operations & Predictive Intelligence"

Word-for-word narration, slide by slide, for the 17-slide deck built by
`build_deck.py` (`Network_Operations_Predictive_Intelligence.pptx`). Every
slide number below is verified against that script's own build order — not
assumed from `PITCH_DECK.md`, which currently numbers slides 12 onward one
lower than the real deck (it merges the Anomaly Detection slide and the AI
Assistant demo into a single "Slide 12"; in the actual `.pptx` they are two
separate slides, 12 and 13). If you update `PITCH_DECK.md`, carry this
numbering forward — this script is the source of truth for what is actually
in the deck.

**Target total runtime: ~10–12 minutes.** Two segments are marked **LIVE
DEMO** — they are the actual product; everything else is framing around them.

---

## The story this script is telling, in one paragraph

A NOC team has three unmet needs: context for a raw number, a trust signal
for the data itself, and an explanation instead of a five-tool manual
investigation. The platform is built around one boundary that meets all
three — data says what happened, ML says whether it's unusual, and the AI
layer says what it means and what to check next, and no layer ever does
another layer's job. Slides 1–2 prove that boundary works before a single
slide of explanation. Slides 3–4 name the boundary. Slides 5–13 walk it
feature by feature, front door to AI layer, in the same order data actually
flows through the system. Slides 14–17 step back, prove the rigor, recap the
scale, and close on the same line the deck opened with. Nothing in this
script should ever feel like a list of features — it should feel like one
system, explained in the order it was built.

---

## How to deliver this — 4 rules

1. **Lead with outcomes, not implementation.** Don't say "I used a
   distributed processing engine" — say "this scales to every day of data
   with the exact same logic," *then* mention what runs it. The audience
   remembers what the system does for them, not the library names.
2. **Never apologize for a number.** The model's 70.6% accuracy, the
   current pipeline health, the honest 19.5% precision figure — present
   these as evidence of rigor, not weaknesses to rush past. A viewer trusts
   the pitch *more*, not less, when you own the honest numbers with a
   straight face and explain why they're the right numbers.
3. **The two live-demo segments are the actual product.** Everything else
   is framing around them. If you only rehearse two things, rehearse the
   Slide 2 hook and the Slide 13 AI-assistant demo — in that order of
   priority.
4. **Every "why it matters" answers a question the audience is already
   silently asking.** If a line doesn't answer "so what?", cut it. This
   script is written that way on purpose — use the same discipline if you
   improvise.

---

## Before you hit record — checklist

- [ ] **Start the API** — `cd Phase4 && uvicorn app.main:app --reload` —
      confirm `http://localhost:8000/docs` loads.
- [ ] **Start the dashboard** — `cd Phase5/noc-dashboard && npm run dev` —
      confirm `http://localhost:5173` loads.
- [ ] **Open these ahead of time** so you never wait on-screen mid-take:
  1. Browser tab — the NOC dashboard (`localhost:5173`)
  2. Browser tab — the API docs (`localhost:8000/docs`)
  3. A terminal / Claude Code window in this repo, ready for the live
     AI-assistant demo
  4. This deck, in a readable view (Presenter View if you can — the speaker
     notes on every slide mirror this script)
- [ ] **Check `GET /pipeline/status` once before recording.** Either
      outcome is usable — pick your line:
  - `healthy: true` → present it straightforwardly: "the pipeline is
    healthy right now."
  - `healthy: false` → don't hide this. Frame it as the product working as
    designed (see Slide 13 notes below) — a system that admits its own
    limits instead of papering over them is a *stronger* pitch, not a
    weaker one.
- [ ] **Pick one `grid_id`** (e.g. `4821`) and reuse it everywhere — the
      hook, the drill-downs, the AI explanation — so the numbers stay
      consistent across the whole recording.
- [ ] Rehearse the Slide 2 hook and the Slide 13 demo at least twice each,
      out loud, with the actual dashboard open — not just read silently.
- [ ] Silence notifications; full-screen the browser/terminal before each
      demo; close any tab that isn't one of the four above.

---

## Slide 1 — Title
**~15 sec · Standard**

**Why this slide is here:** it makes one promise — this system tells you
*what's happening, whether it's normal, and what to check next* — and then
the very next slide proves it live, before any explanation. Say the promise
plainly; don't oversell it, the demo does that work.

**SAY:**
> "Hi, I'm [Your Name]. This is Network Operations and Predictive
> Intelligence — a platform that doesn't just show you the network, it
> tells you what's happening, whether it's normal, and what to check next.
> Let me show you, before I explain how it works."

**SHOW:** Title slide only. Hold for a beat before cutting to the dashboard.

---

## Slide 2 — THE HOOK (live demo) ⭐ most important segment
**~75 sec · LIVE DEMO**

**Why this slide is here:** everything you're about to explain for the next
ten minutes, this slide proves works, unscripted, in under ninety seconds.
It buys credibility for every claim that follows — the audience has already
seen the AI layer produce a real, grounded answer before you've said a
single sentence about how it works.

**SAY (before switching away from the deck):**
> "This is the live dashboard, and this is the live AI layer on top of it.
> No slides for the next minute — just watch."

**SHOW — switch to the dashboard at `localhost:5173`:**
1. Open **Hotspots & Milan Map**.
2. Point at the map: *"That's a real 10,000-cell grid over Milan, ranked by
   real activity, right now."*
3. Click the **top-ranked hotspot** polygon.
4. **SAY:** *"Now let's ask what that actually means."*

**SHOW — switch to Claude Code / your assistant window:**
5. Ask: *"Explain grid [your chosen id] right now."*
6. Let the four-part answer render. Don't summarize it — let it speak for
   itself for a few seconds. Silence here is doing work; don't talk over
   the answer appearing on screen.

**SAY (cutting back to the deck):**
> "That explanation didn't come from a script. Every number in it was
> pulled live from the exact platform you just saw. Now let me walk you
> through it, feature by feature."

**SHOW:** Return to Slide 3.

**Delivery note:** if you'd rather not risk a live call failing on camera,
pre-run this exact sequence once, screen-record it, and cut that clip in
here instead of going fully live. What matters is that it *looks and is*
real, not that it's unedited — but never fabricate an answer if the live
call fails; re-record instead.

---

## Slide 3 — The Problem
**~25 sec · Standard**

**Why this slide is here:** it names the three gaps the whole rest of the
pitch closes, one by one — so every later feature slide has an obvious
answer to "why does this exist?" without you needing to restate it.

**SAY:**
> "Here's why that matters. Every NOC deals with the same problem: raw
> numbers everywhere, but no easy way to know if a number is actually
> normal. A dashboard can show you a spike — it can't tell you whether you
> can even trust the data behind it, and it can't tell you what to do about
> it."

**SHOW:** Problem slide — let the three bullets land one at a time if your
clicker/animation supports it; otherwise read them in order, evenly paced.

---

## Slide 4 — The Promise
**~25 sec · Standard**

**Why this slide is here:** this is the one design idea the entire product
hangs on. Every feature slide after this either implements or protects this
boundary — say it slowly enough that it's memorable, because you will refer
back to it on Slides 13 and 17.

**SAY:**
> "So the whole product is built around one boundary. Data and processing
> tell you what happened. Machine learning tells you if it's unusual or
> risky. And the AI layer tells you what it means and what to check next.
> No layer does another layer's job. That discipline is what you just
> watched work."

**SHOW:** The three-layer table. Read the closing quote slowly, with a
short pause before "And the AI layer tells you what it means" — that's the
sentence the rest of the deck is proving.

---

## Slide 5 — Feature 1: Trusted Ingestion
**~30 sec · Standard**

**Why this slide is here:** it's the front door, chronologically the first
thing that happens to any data, and it sets up the "nothing enters the
system unaccounted for" standard that every later trust claim depends on.

**SAY:**
> "Let's go feature by feature, starting at the very front door. Every file
> that comes in is validated before it touches anything downstream —
> schema check, minimum quality, sane values. Anything bad is quarantined
> with a named reason, never silently dropped, and never silently processed
> either. That matters because a bad file corrupting the analytics layer is
> the most expensive kind of failure there is — the kind that doesn't
> announce itself."

**SHOW:** Feature 1 slide, emphasizing the "PROOF POINT" callout — every
file, good or bad, gets an audit row.

---

## Slide 6 — Feature 2: One Governed Pipeline, One Trust Signal
**~35 sec · Standard**

**Why this slide is here:** this is the slide that introduces the pipeline
status record — the single artifact Slide 13's AI demo depends on, and the
concept you'll return to explicitly if that demo shows an unhealthy
pipeline. Land this one clearly; it pays off twice more later.

**SAY:**
> "After ingestion, the data is processed at real scale and loaded into an
> analytics warehouse. Then fifteen automated quality gates check the
> output — any single failure fails the whole run. That produces one
> artifact everything else depends on: a pipeline status record. It's not a
> log line — it's a machine-readable trust signal that the API, the
> dashboard, and the AI assistant all check before they say anything. This
> platform has processed one point six eight million grid-hour records end
> to end, guarded the whole way by those fifteen gates."

**SHOW:** Feature 2 slide, emphasize the trust-signal callout and the
1.68M-record proof point.

---

## Slide 7 — Feature 3: Live Network Summary
**~20 sec · Standard**

**Why this slide is here:** it's the first thing an operator's eyes actually
land on, so it earns a short, punchy slide rather than a long explanation —
the interesting idea (the data's own clock, not the browser's) is one
sentence, not three.

**SAY:**
> "That's what feeds the front page of the dashboard — total activity, how
> many cells are active, the peak hour, the top cell, all for right now.
> Notice it shows the data's own current time, not the viewer's clock —
> that matters more than it sounds like it should."

**SHOW:** Feature 3 slide. Optionally flash back to the live Overview page
for a few seconds if you have it open in a second tab.

---

## Slide 8 — Feature 4: Grid Explorer
**~25 sec · Standard**

**Why this slide is here:** every operator's next instinct after a summary
is "show me one specific cell" — this slide exists to satisfy that instinct
and to demonstrate the API is stable enough that a drill-down page is just
a thin, fast consumer of it.

**SAY:**
> "Next, drill-down. Pick any one of the ten thousand grid cells and pull
> its hourly activity — SMS, call, internet, and combined — on demand.
> Every summary and every alert eventually leads someone to ask 'show me
> that one cell,' and this is that."

**SHOW:** Switch to Grid Explorer live if you have it open, and type your
chosen `grid_id`. If staying in slides, just present Feature 4.

---

## Slide 9 — Feature 5: Hotspot Ranking + the Milan Map
**~35 sec · Standard**

**Why this slide is here:** this is the technical depth moment of the
pitch — the audience already saw the map work in the hook, so this slide's
job is to prove *why* it's trustworthy, not just that it renders. This is
the single best "we did the hard part right" beat in the whole deck.

**SAY:**
> "You already saw the map in the opening hook — here's the detail worth
> dwelling on. Each cell in the underlying map data carries two possible
> identifiers, and using the wrong one would silently draw every hotspot on
> its neighbor's square — full apparent coverage, no error, no warning
> anywhere. This platform joins on the correct one, and proves it: any
> highlighted cell's real center point can be pulled independently and
> checked against where it should sit. That's the difference between a map
> that looks right and a map that is right."

**SHOW:** Feature 5 slide, or revisit the live map briefly to re-anchor the
audience in what they saw during the hook.

---

## Slide 10 — Feature 6: Rule-Based Alerts
**~25 sec · Standard**

**Why this slide is here:** it deliberately comes *before* the ML slides —
the audience should understand there's a transparent, explainable layer
doing real work before any model is involved, so the ML slides that follow
read as an addition to a solid foundation, not a replacement for one.

**SAY:**
> "Before any machine learning gets involved, there's a transparent first
> layer: each cell's current activity compared to its own recent baseline,
> three plain rules, every alert carrying a human-readable reason. No black
> box — an operator can read exactly why an alert fired."

**SHOW:** Feature 6 slide.

---

## Slide 11 — Feature 7: Predictive Risk Scoring
**~45 sec · Standard — deliver the honest number with confidence, not apology**

**Why this slide is here:** this is the credibility test of the whole
pitch. Most audiences expect a vendor to lead with the highest number they
can find; this slide leads with a number that looks *worse* on its face and
explains exactly why that's the right number. Deliver it like you're proud
of it, because you should be — a naively "better" number here would be the
actual red flag.

**SAY:**
> "Now the machine learning. A live model estimates the probability that a
> cell is about to see an activity surge in the next hour, from six
> features describing its trailing twenty-four hours. And here's the
> number I actually want to talk about: seventy point six percent test
> accuracy — on paper, that's worse than just predicting 'nothing's wrong'
> every time, which would score about ninety percent. That's deliberate.
> It's tuned to actually catch real surges — about two out of every three —
> at the cost of some false alarms, which makes it an attention filter for
> a human, not an automatic trigger. And if this number had come back above
> ninety-five percent, that wouldn't be a win — it would mean the model was
> seeing its own answer, and I'd have gone back to fix it."

**SHOW:** Feature 7 slide with the three metric tiles (70.6% / 68% / 19.5%).
If time allows, switch to the live Predictive Risk page and submit your
chosen grid — *"a real inference, not a canned demo value."*

**Delivery note:** don't rush the last sentence about the 95% red flag —
it's the line that turns an "honest confession" into a demonstration of
rigor. Let it land.

---

## Slide 12 — Feature 8: Anomaly Detection
**~30 sec · Standard**

**Why this slide is here:** this introduces the *third* independent signal
and sets up the payoff line about agreement and disagreement — which you'll
echo again on Slide 14. It is deliberately its own slide, separate from the
AI assistant demo that follows immediately after, because it's a distinct
technical idea (a second ML-adjacent signal) that deserves its own beat
before the live demo raises the energy again.

**SAY:**
> "One more signal sits alongside the risk score: an anomaly baseline that
> asks 'is this unusual for this cell at this hour of day,' based on its
> own history — not a network-wide average. A cell that's normally quiet at
> 3am is judged against its own 3am baseline, not against what a busy
> daytime cell looks like. Now — three independent signals: a transparent
> rule, a predictive score, and this historical-anomaly check. When they
> agree, that's high confidence, fast. When they disagree, that's
> information surfaced to a human, not smoothed away."

**SHOW:** Feature 8 slide.

**Delivery note:** end on "not smoothed away" with a small pause — it's the
transition line into the live AI demo, where you're about to show exactly
that reconciliation happening in real time.

---

## Slide 13 — Feature 9: THE AI ASSISTANT (live demo) ⭐ second-most important segment
**~90–120 sec · LIVE DEMO**

**Why this slide is here:** this is the payoff for every feature slide that
came before it. Every signal you just explained — the trust record, the
rule alert, the risk score, the anomaly score, the location — gets pulled
together here, live, into one grounded answer. If the audience remembers
one thing from this pitch, it should be watching this happen in real time.

**SAY (before switching away from the deck):**
> "Let's put the AI layer in the room with all of it."

**SHOW — switch to Claude Code / your assistant window:**

- **If `/pipeline/status` is healthy**, ask something new:
  > "What's the network situation for the last hour?"

  Narrate as it runs: *"Watch — pipeline status first, then the summary,
  then hotspots, before it says a word."* When it answers, point to the
  four sections as they render: **"Severity, evidence traced to real
  calls, interpretation clearly marked as inference, and next checks for a
  human."**

- **If `/pipeline/status` is currently unhealthy**, ask the same question
  and narrate the more interesting outcome:
  > "Watch what happens when the pipeline itself isn't healthy."

  When it reports the data can't be fully trusted rather than answering
  anyway: *"That's not a failure — that's the product working exactly as
  designed. It won't assert anything as fact until the trust signal says
  it can."*

**SAY (returning to slides):**
> "Nothing you've seen in this video was invented — every number came from
> a real tool call into the platform you've been watching."

**Delivery note:** this is the slide the whole script is called "the hook"
and "the payoff" for — spend your rehearsal time here, not on the calmer
feature slides. If pipeline status flips between healthy and unhealthy
between rehearsal and recording, both branches above are fully scripted;
pick whichever is true right before you hit record and don't force the
other.

---

## Slide 14 — Why You Can Trust Every Number
**~30 sec · Standard**

**Why this slide is here:** the demo already earned trust experientially;
this slide earns it *explicitly*, for the part of the audience that wants
to know the discipline behind what they just watched, not just that it
worked once on camera.

**SAY:**
> "A few things make this more than a demo. The one-row-per-cell-per-hour
> rule is enforced in code, in three separate places, including the
> database's own primary key. The risk model trains on a strictly
> time-ordered split so it never sees the future. The vocabulary is
> deliberately strict — this system never claims 'congestion,' because
> there's no capacity data anywhere in it. And the pipeline has actually
> been tested against injected failures, and each one produces a
> distinguishable, honest status."

**SHOW:** Feature/trust slide with the four bullets.

---

## Slide 15 — The Scale, Recap
**~20 sec · Standard**

**Why this slide is here:** a short, numbers-only breath before the close —
it exists to leave the audience with something concrete and memorable, not
to introduce anything new. Deliver it briskly.

**SAY:**
> "So, the numbers behind everything you just watched: ten thousand grid
> cells, one point six eight million analytics records, fifteen automated
> quality gates, six stable API endpoints, six engineered features, and
> three independent signals working together."

**SHOW:** The two rows of metric tiles.

---

## Slide 16 — Where This Goes Next
**~20 sec · Standard**

**Why this slide is here:** it signals this is a living system, not a
finished demo, and it gives a natural bridge into questions — every bullet
here is a plausible thing a reviewer asks about next, so you've pre-empted
it.

**SAY:**
> "And this isn't a finished, static thing. Next: wiring the ML risk scores
> directly into the hotspot view, replacing the remaining hardcoded
> thresholds with the full rule engine, exposing these tools over a
> standard protocol so any AI surface can investigate a cell the same way,
> and simply accumulating more history so the anomaly baseline keeps
> getting sharper."

**SHOW:** Roadmap bullets.

---

## Slide 17 — Close
**~15 sec · Standard**

**Why this slide is here:** it closes on the exact same design boundary
named in Slide 4 — the audience should recognize the line and feel that
everything in between was proof of it, not a departure from it.

**SAY:**
> "That's Network Operations and Predictive Intelligence — data tells you
> what happened, machine learning tells you if it's unusual, and the AI
> layer tells you what it means and what to check next, without ever doing
> the analytics stack's job. Thanks for watching — happy to answer
> questions."

**SHOW:** Closing slide. Hold for a beat before cutting — don't rush off
the last frame.

---

## Timing summary

| Segment | Slides | Approx. time |
|---|---|---|
| Title | 1 | ~15 sec |
| **The hook — live demo** | **2** | **~75 sec** |
| Problem, Promise | 3–4 | ~50 sec |
| Features 1–6 (ingestion → alerts) | 5–10 | ~2.9 min |
| Feature 7 (predictive risk) | 11 | ~45 sec |
| Feature 8 (anomaly detection) | 12 | ~30 sec |
| **Feature 9 — the AI assistant, live demo** | **13** | **~1.5–2 min** |
| Trust, scale, roadmap | 14–16 | ~70 sec |
| Close | 17 | ~15 sec |
| **Total** | **1–17** | **~10–12 min** |

If you need a shorter cut, keep only slides **1, 2 (hook), 4, 9, 11, 13
(demo), 17** — that alone tells the whole story, demo-first, in about
4–5 minutes.

---

## Common pitfalls to avoid

- **Don't summarize the live demos instead of letting them run.** The
  silence while the AI assistant's answer renders is doing more
  persuasive work than any line of narration could. Let it breathe.
- **Don't hedge the 70.6% accuracy number.** Say it once, clearly, and
  move straight to why it's the right number. Hedging reads as doubt about
  your own work; a single clear explanation reads as rigor.
- **Don't skip Slide 9's join-key detail to save time.** It is the single
  most concrete piece of evidence in the whole deck that this platform was
  built carefully, not just assembled to look good — cut runtime elsewhere
  first.
- **Don't over-narrate the pipeline-status branch on Slide 13.** Whichever
  branch is true (healthy or unhealthy) when you record, deliver it
  straight — both are pre-scripted as strengths, not as an apology.
- **Don't let Slide 16 turn into a feature-request list read flatly.**
  Keep the pace of Slide 4's promise — these are the next proofs of the
  same design boundary, not a disconnected wish list.
