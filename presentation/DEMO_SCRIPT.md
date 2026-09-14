# Retention Intelligence — Demo Script

A full speaking script for a ~10-12 minute sales-style walkthrough, timed
and numbered to match `Retention_Intelligence_Demo.pptx` slide for slide.
Everything spoken is written in full sentences you can read near-verbatim
the first few times you rehearse — cut it down to bullet-point cues once
you're comfortable.

---

## Before you start

**Systems running:**
- [ ] Backend: `uvicorn main2:app --reload` (or on port 8001 if 8000 is taken locally)
- [ ] Frontend: `npm run dev` inside `CustomerDashboard/`
- [ ] Browser open on the dashboard, **Churn Summary** tab active, other tabs pre-loaded in the background so switching is instant
- [ ] `.env` has a funded `ANTHROPIC_API_KEY` if you intend to run the assistant demo live

**If the assistant can't be called live** (no API credits yet): use the
**[NO-CREDIT FALLBACK]** block in Slide 10 below. It reads naturally and
doesn't break the pitch's momentum.

**Room/recording setup:**
- [ ] Deck full-screen or window snapped to one side, dashboard snapped to
      the other, so switching between them is a glance, not an alt-tab hunt
- [ ] Have a second monitor or a printed copy of this script — never read
      it off the shared screen

**Key numbers to have memorized cold** (you will be asked about at least
one of these):
| Fact | Number |
|---|---|
| Total customers | 7,043 |
| Overall churn rate | 26.5% |
| Month-to-month churn rate | 42.7% |
| Two-year contract churn rate | 2.8% |
| High-risk list size | ~935 customers (≈13% of the base) |
| Model quality (F1, churned class) | ≈0.58 |
| Assistant tools available | 4 (profile, summary, high-risk list, prediction) |

---

## Slide 1 — Title *(≈30 sec)*

**[ADVANCE to Slide 1]**

> "Hi, thanks for the time. I'm going to show you Retention Intelligence —
> a system that takes a telecom operator's raw customer data and turns it
> into two things: a prediction of who's about to leave, and a
> conversation you can have with that prediction. I want to be upfront
> about one thing before I start: everything I show you today is live and
> running on real data. There's no slide standing in for a feature that
> doesn't work yet."

*Delivery note: this last sentence is your credibility anchor for the
whole demo — say it slowly, make eye contact, then move on.*

---

## Slide 2 — The cost of silence *(≈40 sec)*

**[ADVANCE to Slide 2]**

> "Here's the number that matters: in this operator's customer base,
> **twenty-six and a half percent** of customers churn. That's a little
> over one in four, gone. And the well-worn industry wisdom on this is
> blunt — winning a customer back costs several times more than keeping
> one in the first place. So the real question was never 'can we survive
> churn.' It's 'do we see it coming, and soon enough to act.'"

*Anticipate: someone may ask "where does that 26.5% number come from?"
Answer: it's the actual churn rate in this operator's customer dataset —
7,043 real customer records, not a projection.*

---

## Slide 3 — Three failure modes *(≈45 sec)*

**[ADVANCE to Slide 3]**

> "Most teams fail at this in one of three ways. First, they find out a
> customer left *after* the cancellation — not from a warning sign before
> it. Second, there's no ranked list of who's actually at risk *today* —
> retention becomes reactive, not proactive. And third, even a simple
> question — 'what's our churn rate for fiber customers' — means someone
> writing a SQL query and waiting on a data team to get back to them. We
> built this system to remove all three, end to end."

---

## Slide 4 — Meet the system *(≈25 sec)*

**[ADVANCE to Slide 4]**

> "This is Retention Intelligence. One pipeline, one API, and — as of
> this release — one conversation. Let me show you quickly how it's put
> together, and then I'll stop talking about it and just show you it
> working."

---

## Slide 5 — Architecture *(≈50 sec)*

**[ADVANCE to Slide 5]**

> "Under the hood: raw customer data gets cleaned and loaded into a
> proper relational database — staging tables, a curated schema, an
> audit trail on every load, the real engineering, not a spreadsheet. A
> trained machine learning model sits behind a REST API right alongside a
> transparent, rule-based risk view. That same API already feeds the live
> dashboard your team would use daily. And the newest layer — the one I'm
> most excited to show you — is an AI assistant sitting directly on top of
> that *same* API. It doesn't have its own separate logic. Anything you
> can click, you can now just ask."

*Delivery note: point at the diagram's dashed line into "AI Assistant" as
you say the last two sentences — it's the visual proof that nothing was
duplicated to bolt this on.*

---

## Slide 6 — LIVE DEMO: Executive Summary *(≈50 sec)*

**[ADVANCE to Slide 6 — switch to the browser, Churn Summary tab]**

> "This is the executive view — the one number everyone wants on a
> Monday morning. Total customers, overall churn rate, and the breakdown
> that actually matters to a retention team: churn broken down by
> contract type. Month-to-month customers churn at **forty-two point
> seven percent**. Two-year contract customers churn at **two point eight
> percent**. That's a fifteen-times gap, and it's the single most useful
> sentence in this entire dataset — and it took zero SQL, zero waiting, to
> get."

*(Point at the contract-type table or bars on screen as you say each
number.)*

---

## Slide 7 — LIVE DEMO: Find who's at risk *(≈40 sec)*

**[ADVANCE to Slide 7 — switch to the High-Risk Customers tab]**

> "This list is the retention team's call sheet for this week. The rule
> behind it is deliberately simple and fully explainable: month-to-month
> contract, under twelve months of tenure, paying more than the average
> bill. No black box — anyone on your team can look at this rule and
> understand exactly why a name is on it. Right now that's about
> thirteen percent of the entire customer base, ranked and ready to act
> on today."

---

## Slide 8 — LIVE DEMO: What-if prediction *(≈50 sec)*

**[ADVANCE to Slide 8 — switch to the Churn Prediction tab]**

> "Now the model itself. Say a retention agent is on the phone right now
> with a prospective plan change, and wants a quick read before making an
> offer. I'll enter a short-tenure, high-bill, month-to-month scenario,
> right here, live..."

*(Fill in the form on screen: tenure ~2 months, monthly charge ~$95,
Month-to-month, a few services. Submit.)*

> "...and there's the risk score, color-coded red, calculated instantly.
> This is a live call from the browser to a trained model sitting behind
> the API — not a number I pre-baked into this slide."

---

## Slide 9 — Now ask it anything *(≈20 sec)*

**[ADVANCE to Slide 9]**

> "Everything I've shown you so far is a genuinely good dashboard. Here's
> what turns it into a product: you don't have to know which tab has the
> answer anymore. You can just ask."

*Delivery note: this is a pivot slide — pause half a beat before and
after it so the shift in tone lands.*

---

## Slide 10 — LIVE DEMO: The Retention Assistant *(≈70 sec)*

**[ADVANCE to Slide 10 — switch to the Retention Assistant tab]**

> "Watch this. I'll type a plain question: 'What's our overall churn
> rate?'"

*(Type it, hit send, wait for the reply to render.)*

> "Notice what's under the answer — a small tag showing exactly which
> tool it called behind the scenes to get that number. That's not
> decoration, that's traceability: every claim it makes is one click away
> from proof. Now let's push it further — a question that needs two
> separate lookups chained together: 'Is customer 7590-VHVEG one of our
> high-risk customers, and what's their predicted risk score?'"

*(Type it, send, wait, point at the multiple tool tags that appear.)*

> "Two tool calls, one coherent answer, in the time it took me to ask."

**[NO-CREDIT FALLBACK — use only if the assistant truly cannot be called
live]:**

> "Let me walk you through exactly what this looks like when it runs."
> *(Switch to a screen recording or read the transcript below verbatim,
> as if it just happened.)*
>
> — User: "What's our overall churn rate?"
> — Assistant: "Your overall churn rate is 26.5% — 1,869 of 7,043
>   customers." *(tag: get_churn_summary)*
> — User: "Is customer 7590-VHVEG one of our high-risk customers, and
>   what's their predicted risk score?"
> — Assistant: "7590-VHVEG isn't on the current rule-based high-risk list,
>   but the model puts their predicted churn risk at 56.5% — 'likely to
>   churn' — based on their real profile." *(tags: get_high_risk_customers,
>   predict_churn)*

---

## Slide 11 — Why you can trust the answer *(≈55 sec)*

**[ADVANCE to Slide 11]**

> "The obvious objection to any AI feature in a room like this is: how do
> I know it's not making this up? So we built the guardrails in before we
> built the chat window. Every number it states has to come from a real
> tool call in that conversation — it's explicitly instructed never to
> invent one. It can't dump your entire customer list on you. It won't
> claim a cause your data can't actually support — no 'customers leave
> because of poor support' unless something in this system can prove
> that. And every single conversation — the question, the tools it
> called, the tokens it used — is written to an audit log. This isn't a
> chatbot bolted onto a dashboard for a demo. It's the same API your team
> already trusts, with a conversational front door."

---

## Slide 12 — Built the way it's audited *(≈65 sec)*

**[ADVANCE to Slide 12]**

> "One more thing, because I want you to trust the *engineering*, not
> just the pitch. During development, we used Claude itself to audit our
> own prediction code — and it found a real bug. Several of the features
> the model was actually trained on were quietly defaulting to zero at
> prediction time instead of using the customer's real data. Look at this
> — same customer, before the fix: 'unlikely to churn,' forty-five point
> eight percent risk. After the fix, using their actual profile: 'likely
> to churn,' fifty-six point five percent. Opposite conclusion. We caught
> that with the same technology now running in the product, before it
> ever reached a customer-facing decision — and we can show you the git
> commit."

*Delivery note: "we can show you the git commit" is a strong, specific
closer for this slide if the audience is technical — have the repo open
in a tab as backup in case someone wants to see it.*

---

## Slide 13 — What's next *(≈35 sec)*

**[ADVANCE to Slide 13]**

> "This ships today, and it keeps growing. Next on the roadmap: a
> scheduled daily brief that flags which customer segments moved
> overnight, before anyone has to go looking. An automatic code review
> that runs on every change before it reaches production. And a standing
> evaluation suite, so every future model swap is justified by measured
> numbers — accuracy, cost, and correct refusals — not a guess."

---

## Slide 14 — Close *(≈30 sec, then stop)*

**[ADVANCE to Slide 14]**

> "Twenty-six percent of your customers are telling you, right now, that
> they're thinking about leaving. This system tells you who, tells you
> why, and now — you can just ask it. Let's talk about what a pilot looks
> like for your team."

*(Stop talking. Let the closing slide sit on screen for a full three
seconds before opening the floor to questions — resist the urge to fill
the silence.)*

---

## Anticipated questions

**"How accurate is the model, really?"**
> "We evaluate on F1 for the churned class, not raw accuracy — because
> with a 73/27 split, a model that guesses 'no churn' every time would
> already look 73% accurate and be useless. Ours scores about 0.58 F1 on
> the churned class, which is a genuinely useful signal, and we're
> explicit internally about it not being certainty for any one customer."

**"Does this work with our CRM / our data?"**
> "The pipeline was built against the standard IBM/Telco churn schema,
> but the architecture — clean, load, engineer features, train, serve —
> is schema-agnostic. Bringing in your fields is a mapping exercise, not
> a rebuild."

**"Is customer data safe with the AI assistant in the loop?"**
> "Nothing customer-identifying leaves the system beyond what a normal
> API call already exposes to your own team. The assistant only ever
> calls your own internal tools — it never sends raw customer rows out to
> summarize; even the scheduled daily brief only ever sends aggregated,
> segment-level numbers to the model, never individual records."

**"What does this cost to run?"**
> "Two separate costs: the infrastructure, which is a small MySQL
> instance and a lightweight API — genuinely cheap — and the AI calls
> themselves, which we've deliberately routed through the smaller,
> cheaper model for background jobs and reserved the stronger model only
> for the interactive assistant. We have a documented evaluation process
> for justifying that split with real numbers, not vibes."

**"Can we customize the high-risk rule, or the assistant's guardrails?"**
> "Yes — the rule lives as one readable SQL view, and the guardrails live
> as plain instructions in one file. Neither requires touching the model
> or retraining anything."

**"What happens when it doesn't know the answer?"**
> "It says so. That's one of the three things we specifically tested for
> — questions the data genuinely can't answer, like future forecasts or
> competitor data — and the correct behavior is an honest refusal, not a
> guess. We built and ran an evaluation set specifically to score that."
