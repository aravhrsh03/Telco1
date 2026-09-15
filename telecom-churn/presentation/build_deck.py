"""
Build the sales/pitch deck for the Telecom Churn project - "Retention
Intelligence", feature by feature. Same visual style and slide grammar as
D:\\main_project1\\presentation2\\build_deck.py (the Network Operations deck),
applied to this project's own content.

    python presentation/build_deck.py
    -> presentation/Retention_Intelligence_Demo.pptx

All slide text lives in the BUILD section at the bottom - edit there, then
re-run.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# --------------------------------------------------------------------------
# palette (matches D:\main_project1\presentation2\build_deck.py)
# --------------------------------------------------------------------------
NAVY = RGBColor(0x11, 0x2A, 0x43)
STEEL = RGBColor(0x2E, 0x6C, 0x8E)
AMBER = RGBColor(0xDD, 0x7A, 0x2E)
LIGHT = RGBColor(0xEE, 0xF2, 0xF5)
GRAYTX = RGBColor(0x53, 0x62, 0x6E)
DARKTX = RGBColor(0x1E, 0x28, 0x30)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RULE = RGBColor(0xDD, 0x7A, 0x2E)

FONT = "Segoe UI"
FONT_LIGHT = "Segoe UI Light"

EMU_W = Inches(13.333)
EMU_H = Inches(7.5)

prs = Presentation()
prs.slide_width = EMU_W
prs.slide_height = EMU_H
BLANK = prs.slide_layouts[6]


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _set(run, size, *, bold=False, color=DARKTX, font=FONT):
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def rect(slide, x, y, w, h, fill, line=None, line_w=None, shape=MSO_SHAPE.RECTANGLE):
    sp = slide.shapes.add_shape(shape, x, y, w, h)
    sp.fill.solid()
    sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = line_w or Pt(1)
    sp.shadow.inherit = False
    return sp


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    return tf


def add_notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def base_slide(title, kicker="", *, number=None):
    slide = prs.slides.add_slide(BLANK)
    rect(slide, 0, 0, EMU_W, Inches(1.12), NAVY)
    rect(slide, 0, Inches(1.12), EMU_W, Pt(3), RULE)
    tf = textbox(slide, Inches(0.6), Inches(0.14), Inches(12.1), Inches(0.9),
                 anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    if kicker:
        r = p.add_run(); _set(r, 12, bold=True, color=AMBER, font=FONT)
        r.text = kicker.upper() + "   "
    r = p.add_run(); _set(r, 26, bold=True, color=WHITE, font=FONT)
    r.text = title
    ft = textbox(slide, Inches(0.6), Inches(7.02), Inches(9), Inches(0.4))
    fr = ft.paragraphs[0].add_run()
    _set(fr, 9, color=GRAYTX, font=FONT)
    fr.text = "Retention Intelligence"
    if number is not None:
        nt = textbox(slide, Inches(12.4), Inches(7.02), Inches(0.6), Inches(0.4))
        nt.paragraphs[0].alignment = PP_ALIGN.RIGHT
        nr = nt.paragraphs[0].add_run()
        _set(nr, 9, color=GRAYTX, font=FONT)
        nr.text = str(number)
    return slide


def key_message(slide, text, *, y=Inches(1.42)):
    tf = textbox(slide, Inches(0.6), y, Inches(12.1), Inches(0.8))
    r = tf.paragraphs[0].add_run()
    _set(r, 18, bold=True, color=STEEL, font=FONT)
    r.text = text
    return tf


def bullets(slide, items, *, x=Inches(0.6), y=Inches(2.35),
            w=Inches(8.2), h=Inches(4.2), size=15, gap=10):
    tf = textbox(slide, x, y, w, h)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(gap)
        if isinstance(item, tuple):
            text, lvl = item
        else:
            text, lvl = item, 0
        p.level = lvl
        dot = p.add_run()
        _set(dot, size, bold=True, color=AMBER if lvl == 0 else STEEL)
        dot.text = ("•  " if lvl == 0 else "-  ")
        r = p.add_run()
        _set(r, size, color=DARKTX if lvl == 0 else GRAYTX)
        r.text = text
    return tf


def metric_tiles(slide, tiles, *, y=Inches(2.5), h=Inches(1.9)):
    n = len(tiles)
    gap = Inches(0.3)
    total = EMU_W - Inches(1.2)
    w = Emu(int((total - gap * (n - 1)) / n))
    x = Inches(0.6)
    for value, label in tiles:
        box = rect(slide, x, y, w, h, NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
        r = p.add_run(); _set(r, 30, bold=True, color=WHITE); r.text = value
        p2 = tf.add_paragraph(); p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(4)
        r2 = p2.add_run(); _set(r2, 11.5, color=RGBColor(0xC5, 0xD3, 0xDE))
        r2.text = label
        x = Emu(x + w + gap)


def two_col_table(slide, rows, *, y=Inches(2.4), row_h=Inches(0.66)):
    x1, w1 = Inches(0.6), Inches(4.6)
    x2, w2 = Inches(5.35), Inches(7.35)
    cy = y
    for left, right in rows:
        b1 = rect(slide, x1, cy, w1, row_h, NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        tf1 = b1.text_frame; tf1.vertical_anchor = MSO_ANCHOR.MIDDLE; tf1.word_wrap = True
        p1 = tf1.paragraphs[0]; p1.alignment = PP_ALIGN.CENTER
        r1 = p1.add_run(); _set(r1, 14, bold=True, color=WHITE); r1.text = left
        b2 = rect(slide, x2, cy, w2, row_h, LIGHT, line=STEEL, line_w=Pt(0.75),
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        tf2 = b2.text_frame; tf2.vertical_anchor = MSO_ANCHOR.MIDDLE; tf2.word_wrap = True
        tf2.margin_left = Inches(0.2); tf2.margin_right = Inches(0.2)
        p2 = tf2.paragraphs[0]
        r2 = p2.add_run(); _set(r2, 13, color=DARKTX); r2.text = right
        cy = Emu(cy + row_h + Inches(0.12))


def feature_slide(n, number_label, title, what_it_does, why_it_matters, proof=None):
    """Standard 'Feature N' slide: What it does / Why it matters / optional proof line."""
    s = base_slide(title, f"Feature {number_label}", number=n)
    y = Inches(1.55)
    head1 = textbox(s, Inches(0.6), y, Inches(12.1), Inches(0.4))
    hr = head1.paragraphs[0].add_run(); _set(hr, 13, bold=True, color=AMBER)
    hr.text = "WHAT IT DOES"
    tf1 = textbox(s, Inches(0.6), Emu(y + Inches(0.42)), Inches(12.1), Inches(1.7))
    r1 = tf1.paragraphs[0].add_run(); _set(r1, 14.5, color=DARKTX); r1.text = what_it_does

    y2 = Emu(y + Inches(2.15))
    head2 = textbox(s, Inches(0.6), y2, Inches(12.1), Inches(0.4))
    hr2 = head2.paragraphs[0].add_run(); _set(hr2, 13, bold=True, color=STEEL)
    hr2.text = "WHY IT MATTERS"
    tf2 = textbox(s, Inches(0.6), Emu(y2 + Inches(0.42)), Inches(12.1), Inches(1.7))
    r2 = tf2.paragraphs[0].add_run(); _set(r2, 14.5, color=DARKTX); r2.text = why_it_matters

    if proof:
        box = rect(s, Inches(0.6), Inches(6.05), Inches(12.1), Inches(0.8), LIGHT,
                   line=STEEL, line_w=Pt(1), shape=MSO_SHAPE.ROUNDED_RECTANGLE)
        tf3 = box.text_frame; tf3.vertical_anchor = MSO_ANCHOR.MIDDLE; tf3.word_wrap = True
        tf3.margin_left = Inches(0.2); tf3.margin_right = Inches(0.2)
        p = tf3.paragraphs[0]
        d = p.add_run(); _set(d, 12.5, bold=True, color=STEEL); d.text = "PROOF POINT   "
        r = p.add_run(); _set(r, 12.5, color=DARKTX); r.text = proof
    return s


def live_demo_slide(n, title, cues):
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, EMU_W, EMU_H, NAVY)
    rect(s, 0, Inches(1.5), EMU_W, Pt(3), RULE)
    tf = textbox(s, Inches(0.7), Inches(0.35), Inches(10), Inches(1.0),
                 anchor=MSO_ANCHOR.MIDDLE)
    r = tf.paragraphs[0].add_run()
    _set(r, 13, bold=True, color=AMBER)
    r.text = "LIVE DEMO"
    tf2 = textbox(s, Inches(0.7), Inches(0.7), Inches(11.5), Inches(0.8))
    r2 = tf2.paragraphs[0].add_run()
    _set(r2, 26, bold=True, color=WHITE, font=FONT_LIGHT)
    r2.text = title
    body = textbox(s, Inches(0.9), Inches(2.1), Inches(11.4), Inches(4.6))
    for i, cue in enumerate(cues):
        p = body.paragraphs[0] if i == 0 else body.add_paragraph()
        p.space_after = Pt(12)
        d = p.add_run(); _set(d, 15, bold=True, color=AMBER); d.text = f"{i + 1}.  "
        r3 = p.add_run(); _set(r3, 15, color=RGBColor(0xE7, 0xEC, 0xF0)); r3.text = cue
    nt = textbox(s, Inches(12.4), Inches(7.02), Inches(0.6), Inches(0.4))
    nt.paragraphs[0].alignment = PP_ALIGN.RIGHT
    nr = nt.paragraphs[0].add_run()
    _set(nr, 9, color=RGBColor(0x8F, 0xA6, 0xB6), font=FONT)
    nr.text = str(n)
    return s


# --------------------------------------------------------------------------
# TITLE SLIDE
# --------------------------------------------------------------------------
def title_slide():
    slide = prs.slides.add_slide(BLANK)
    rect(slide, 0, 0, EMU_W, EMU_H, NAVY)
    rect(slide, 0, Inches(4.35), EMU_W, Pt(3), RULE)
    tf = textbox(slide, Inches(0.9), Inches(2.1), Inches(11.5), Inches(2.2))
    r = tf.paragraphs[0].add_run()
    _set(r, 44, bold=True, color=WHITE, font=FONT_LIGHT)
    r.text = "Retention Intelligence"
    sub = textbox(slide, Inches(0.95), Inches(3.65), Inches(11.4), Inches(1.4))
    sr = sub.paragraphs[0].add_run()
    _set(sr, 17, color=RGBColor(0xC5, 0xD3, 0xDE))
    sr.text = ("A live customer-retention platform that doesn't just show you "
               "who's churning - it explains why, and lets you ask it anything.")
    meta = textbox(slide, Inches(0.95), Inches(6.2), Inches(11.4), Inches(0.6))
    mr = meta.paragraphs[0].add_run()
    _set(mr, 12, color=RGBColor(0x8F, 0xA6, 0xB6))
    mr.text = "Presented by [Your Name]  ·  [Date]"
    add_notes(slide, """
"Hi, I'm [Your Name]. This is Retention Intelligence - a platform that
doesn't just tell you a customer might leave, it explains why, backs that
with a real model, and lets your team ask it anything in plain language.
Let me show you, before I explain how it works."
""")


def slide_hook(n):
    live_demo_slide(n, "The Hook (~75 sec)", [
        "Switch to the live dashboard - open High-Risk Customers.",
        "Point at the ranked list: \"Every one of these is a real customer, flagged by a fully explainable rule - month-to-month, under a year with us, paying above average.\"",
        "Switch to the Retention Assistant tab.",
        "Ask: \"Is customer 7590-VHVEG one of our high-risk customers, and what's their predicted risk score?\"",
        "Let the answer render, and point at the line showing which tools produced it - don't summarize, let it speak for itself.",
        "Cut back to the deck: \"Every number in that answer came from the exact platform you just saw.\"",
    ])
    add_notes(prs.slides[-1], """
Don't explain anything yet - just show it. Then: "That answer didn't come
from a script. Every number in it was pulled live, through a real tool
call, from the exact platform you just saw. Now let me walk you through it,
feature by feature."
""")


def slide_problem(n):
    s = base_slide("The Problem", "Why this exists", number=n)
    key_message(s, "Every retention team deals with the same three gaps.")
    bullets(s, [
        "Churn shows up in the billing system, not a warning light - teams find out after the cancellation call, not before.",
        "A rule can flag a risky customer, but it can't explain the risk, compare it to a model, or answer a follow-up question.",
        "Every new question means a SQL query and a wait on the data team - or it just doesn't get asked.",
    ], y=Inches(2.5), w=Inches(12.0))
    tf = textbox(s, Inches(0.6), Inches(5.6), Inches(12.1), Inches(1.1))
    r = tf.paragraphs[0].add_run()
    _set(r, 15, bold=True, color=STEEL)
    r.text = ("What a retention team actually needs: a system that knows what's "
              "true about a customer, how risky they are, and what to do about "
              "it - and can explain all three without guessing.")
    add_notes(s, """
"Here's why that matters. Every retention team deals with the same problem:
a customer cancels, and only then does anyone look back and see the warning
signs. A rule-based list can flag risk - it can't explain it, and it
definitely can't answer 'why', or 'what if we offered them a different
contract'."
""")


def slide_promise(n):
    s = base_slide("The Promise", "One design boundary", number=n)
    key_message(s, "Every layer answers exactly one kind of question.")
    two_col_table(s, [
        ("Data + database", "What is true about this customer, right now?"),
        ("Machine learning", "How likely are they to leave?"),
        ("AI assistant", "What does that mean, and what should we do? - grounded in real tool calls, never invented"),
    ], y=Inches(2.5))
    tf = textbox(s, Inches(0.6), Inches(5.1), Inches(12.1), Inches(1.4))
    r = tf.paragraphs[0].add_run()
    _set(r, 15, bold=True, color=STEEL)
    r.text = ('"The database tells you what\'s true. The model tells you how '
              'risky. The AI layer tells you what to do about it - and it '
              'never invents a customer, a number, or a reason."')
    add_notes(s, """
"So the whole product is built around one boundary. The database and
pipeline hold what's actually true about a customer. The model estimates
how risky they are. And the AI layer turns that into a plain-language
answer - grounded in a real tool call every time, never a guess. That
discipline is what you just watched work."
""")


def slide_feature1(n):
    feature_slide(n, "1", "A Trusted Data Foundation",
        "One cleaning class fixes the dataset's two real defects, once: "
        "TotalCharges stored as text with 11 blank cells, and every Yes/No "
        "column that needs to become 1/0 before a rule or a model can use "
        "it. That class is imported everywhere the data is touched again - "
        "the batch pipeline, the ML feature build - rather than re-fixed by "
        "hand each time. The result loads into a proper staging-to-curated "
        "MySQL schema: an untouched staging mirror of the source file, "
        "typed dimension and fact tables, and a rule-based high-risk view.",
        "A dashboard, a trained model, and an AI assistant are only as "
        "honest as the data underneath them. Fixing quality problems in one "
        "reused class - not four different scripts that could quietly "
        "drift apart - means every layer of this system agrees on the same "
        "customer.",
        proof="7,043 customers and 21 source columns, cleaned once and "
              "loaded into a typed schema with zero manual SQL touch-up.")
    add_notes(prs.slides[-1], """
"Let's go feature by feature, starting at the foundation. One cleaning
class fixes the dataset's real problems - once - and everything downstream
imports it instead of re-implementing the fix. That's what lets a
dashboard, a model, and an AI assistant all agree on the same customer."
""")


def slide_feature2(n):
    feature_slide(n, "2", "One Governed Pipeline",
        "The one-off cleaning script became repeatable, quality-gated "
        "stages: schema validation against the 21 expected columns, "
        "cleaning, automated feature building, an independent PySpark "
        "recomputation of the same churn numbers to prove they hold on a "
        "different engine, incremental upsert logic so re-runs don't "
        "duplicate customers, and a programmatic PASS/FAIL quality gate - "
        "all chained into one seven-task pipeline: ingest, validate, "
        "clean, build features, score, brief, notify.",
        "A number that only works when you run the notebook cells in the "
        "right order isn't a number a retention team can trust on a Tuesday "
        "morning. This pipeline is written to run itself, on a schedule, "
        "with a gate that fails loudly instead of publishing a quiet wrong "
        "answer.",
        proof="Every quality check in the most recent run came back PASS - "
              "cross-checked against an independent PySpark recomputation "
              "of the same churn rates.")
    add_notes(prs.slides[-1], """
"That cleaning class feeds a real pipeline - seven stages, from ingestion
through a scheduled daily brief, with a quality gate that has to pass and a
PySpark cross-check proving the numbers hold on a completely different
processing engine, not just in one notebook."
""")


def slide_feature3(n):
    feature_slide(n, "3", "Executive Churn Summary",
        "One glance answers \"how exposed are we right now\" - total "
        "customers, total churned, the overall churn rate, and the "
        "breakdown by contract type and by internet service.",
        "This is the front door for a manager who needs the headline "
        "number without writing a query - and every other feature in this "
        "deck builds on the same live data behind it.")
    add_notes(prs.slides[-1], """
"First stop on the dashboard: the executive summary. Total customers,
churn rate, and the split by contract and service type - the number a
manager actually opens the dashboard to see."
""")


def slide_feature4(n):
    feature_slide(n, "4", "Find Who's At Risk, Today",
        "A transparent rule - month-to-month contract, under 12 months' "
        "tenure, an above-average monthly bill - ranks customers into a "
        "live, sortable, pageable list, each row carrying a plain-English "
        "reason. Search any single customer by ID for their full profile: "
        "services, contract, billing, and whether they've already left.",
        "No black box. A retention rep can read the rule and the number "
        "and know exactly why a name is on the list - and look up any one "
        "customer by name the moment a support call comes in.")
    add_notes(prs.slides[-1], """
"Next, the ranked list retention teams actually work from - fully
explainable, no model required to understand why someone's on it - plus
instant lookup for any single customer by ID."
""")


def slide_feature5(n):
    s = feature_slide(n, "5", "Predictive Risk Scoring - Audited and Fixed",
        "A trained classifier estimates each customer's probability of "
        "churning, evaluated on F1 for the churned class rather than raw "
        "accuracy - because with a 73/27 split, a model that guesses \"no\" "
        "for everyone would score 73% and catch nobody. Feed it a real "
        "customer ID for an exact score using their real data, or a "
        "hypothetical scenario for a live what-if.",
        "We found a real bug in our own prediction code by having Claude "
        "read it, and proved the fix with a real customer, not a "
        "synthetic example. The live endpoint was quietly using only 4 of "
        "the model's 38 trained inputs - every other signal silently "
        "defaulted to zero for every customer, for every request.")
    metric_tiles(s, [
        ("4 / 38", "trained features the old code actually used - before the fix"),
        ("45.8% \u2192 56.5%", "same real customer's risk score, before vs. after"),
        ("2", "git commits bracketing the fix - auditable, not just claimed"),
    ], y=Inches(6.05), h=Inches(0.85))
    add_notes(s, """
"Here's the number I actually want to talk about. We used Claude to audit
our own inference code, and it found a real defect: the live prediction
endpoint was only using four of the model's thirty-eight trained inputs.
For one real customer, 7590-VHVEG, that bug produced 'unlikely to churn' at
45.8% - fixed, using their real data, that same customer scores 56.5% and
flips to 'likely to churn'. Same customer, opposite answer. That's the cost
of the bug, and it's why we don't just say we fixed it - we can show you
the before and after commit."
""")


def slide_feature6(n):
    feature_slide(n, "6", "The Retention Assistant",
        "Ask it anything, in plain language. Four tools - customer "
        "lookup, churn summary, high-risk list, live prediction - each "
        "wired straight into the same functions the dashboard and API "
        "already call, so no business logic is duplicated for the AI "
        "layer. It checks real data through a tool call before it answers "
        "anything - it never recalls a number from memory.",
        "Every reply carries a visible line showing exactly which tools "
        "produced it, so an agent can trace any number back to a real "
        "query. And it's instructed to refuse a question no tool can "
        "answer - like \"why do customers really leave\" - rather than "
        "invent a plausible-sounding cause.",
        proof="The same four functions the React dashboard already calls "
              "become the assistant's tools - no second implementation to "
              "keep in sync.")
    add_notes(prs.slides[-1], """
"And now the payoff - ask it anything. Four tools, wired directly into the
same functions the dashboard already uses, so there's exactly one
implementation of 'what's true about a customer', not two that could drift
apart. Every answer shows its work."
""")


def slide_feature7(n):
    feature_slide(n, "7", "Automation: A Daily Brief and an Automatic Code Reviewer",
        "Two headless uses of Claude, no chat window involved. A "
        "scheduled daily brief compares yesterday's and today's risk "
        "scores by segment and sends only the aggregated deltas - never a "
        "raw customer row - to produce one headline number, a short list "
        "of notable movements, and recommended actions. Separately, every "
        "code change is reviewed for real defects before it reaches the "
        "shared repository, wired into a git pre-push hook.",
        "A retention team and an engineering team both get warned "
        "automatically, instead of someone having to remember to check. "
        "The daily brief only ever sees aggregated numbers - the exact "
        "same \"curated evidence, not raw rows\" discipline that keeps the "
        "chat assistant honest also protects what a scheduled job is "
        "allowed to see.")
    add_notes(prs.slides[-1], """
"Two more places Claude works without anyone chatting with it at all: a
daily brief that only ever sees aggregated risk deltas by segment, never a
raw customer, and a code reviewer that runs automatically before any change
reaches the shared repo."
""")


def slide_demo2(n):
    live_demo_slide(n, "The Retention Assistant, Live (~90 sec)", [
        "Switch to the Retention Assistant tab.",
        "Ask: \"What's the overall churn rate, and how does customer 9237-HQITU's predicted risk compare to that average?\"",
        "Narrate as it runs: \"Watch - it calls the summary tool and the prediction tool, in the same turn, before it says a word.\"",
        "Point at the tools-used line under the answer.",
        "Ask a second, harder one: \"Customer 3668-QPYBK has a month-to-month contract. What would their churn risk look like on a two-year contract instead?\"",
        "Return to slides: \"Nothing here was invented - every number came from a real tool call into the platform you've been watching.\"",
    ])
    add_notes(prs.slides[-1], """
"It's not a lookup box - it reasons across multiple tools in one answer,
and it always shows which ones. Ask it a what-if, and it runs a real
hypothetical prediction rather than guessing."
""")


def slide_trust(n):
    s = base_slide("Why You Can Trust Every Answer", "Rigor", number=n)
    bullets(s, [
        "Every reply is graded against a 15-question evaluation set - five answerable with one tool, five needing two tools together, and five genuinely unanswerable, specifically to check it refuses instead of inventing an answer.",
        "Every tool argument is validated against a strict schema before it ever reaches a database query.",
        "A secret-leakage guard blocks any outbound prompt that contains a credential - called on every single Claude request in the system, not only the chat endpoint.",
        "Every conversation - question, tools called, tokens used - is written to a permanent audit log.",
        "The assistant is capped on every axis that matters: response length, conversation history, and how many tool round-trips one question can trigger.",
    ], y=Inches(2.5), w=Inches(12.0), size=14)
    add_notes(s, """
"A few things make this more than a demo. Every reply is checked against a
fifteen-question evaluation set that specifically includes questions it
should refuse to answer. Every tool argument is schema-validated before it
touches the database. A secret-leakage guard runs on every outbound prompt
in the system. And every conversation is written to a permanent audit log."
""")


def slide_scale(n):
    s = base_slide("The Scale, Recap", "By the numbers", number=n)
    metric_tiles(s, [
        ("7,043", "customers modeled, 21 source columns cleaned into one schema"),
        ("4", "live AI tools wired to the real API - no duplicated logic"),
        ("15", "evaluation questions, scored on 3 separate rates"),
    ], y=Inches(2.4), h=Inches(1.85))
    metric_tiles(s, [
        ("F1 \u2248 0.57-0.58", "on the churned class - the honest metric for a 73/27 split"),
        ("7", "pipeline tasks, one quality gate, one PySpark cross-check"),
        ("2", "headless Claude jobs - a daily brief and an automatic code reviewer"),
    ], y=Inches(4.5), h=Inches(1.85))
    add_notes(s, """
"So, the numbers behind everything you just watched: seven thousand and
forty-three customers, four live AI tools with no duplicated logic, a
fifteen-question evaluation harness, and an honest F1 score on the class
that actually matters."
""")


def slide_roadmap(n):
    s = base_slide("Where This Goes Next", "Roadmap", number=n)
    bullets(s, [
        "Put the seven-task pipeline DAG onto a live scheduler - the orchestration code is written and ready; a running Airflow instance is the next step.",
        "Add per-customer authorization so the assistant's reach matches who's allowed to see what.",
        "Run the full two-model evaluation (fast vs. strongest) to lock in a production cost/quality choice with real measured numbers.",
        "Put the daily brief on a real schedule the moment the DAG is live, instead of running it by hand.",
    ], y=Inches(2.5), w=Inches(12.0))
    add_notes(s, """
"And this isn't a finished, static thing. Next: put the pipeline DAG on a
real scheduler, add per-customer authorization, and run the full two-model
evaluation to lock in a production model choice with real numbers instead
of a documented default."
""")


def slide_close(n):
    s = prs.slides.add_slide(BLANK)
    rect(s, 0, 0, EMU_W, EMU_H, NAVY)
    rect(s, Inches(0.9), Inches(2.5), Inches(0.12), Inches(2.4), RULE)
    tf = textbox(s, Inches(1.3), Inches(2.35), Inches(11.0), Inches(2.8),
                 anchor=MSO_ANCHOR.MIDDLE)
    r = tf.paragraphs[0].add_run()
    _set(r, 24, bold=True, color=WHITE, font=FONT_LIGHT)
    r.text = ("The database tells you what's true.\n"
              "The model tells you how risky.\n"
              "The AI layer tells you what to do about it.")
    sub = textbox(s, Inches(1.3), Inches(5.2), Inches(11.0), Inches(0.8))
    sr = sub.paragraphs[0].add_run()
    _set(sr, 15, color=RGBColor(0xC5, 0xD3, 0xDE))
    sr.text = "Retention Intelligence - 26% of your customers are already telling you they might leave."
    q = textbox(s, Inches(1.3), Inches(6.2), Inches(11), Inches(0.6))
    qr = q.paragraphs[0].add_run()
    _set(qr, 13, bold=True, color=AMBER)
    qr.text = "Thank you - questions?"
    add_notes(s, """
"That's Retention Intelligence - the database tells you what's true, the
model tells you how risky, and the AI layer tells you what to do about it,
grounded in a real tool call every time. Thanks for watching - happy to
answer questions."
""")


# --------------------------------------------------------------------------
# BUILD
# --------------------------------------------------------------------------
title_slide()                  # 1
slide_hook(2)                  # 2   LIVE DEMO
slide_problem(3)                # 3
slide_promise(4)                # 4
slide_feature1(5)               # 5
slide_feature2(6)               # 6
slide_feature3(7)               # 7
slide_feature4(8)               # 8
slide_feature5(9)               # 9
slide_feature6(10)              # 10
slide_feature7(11)              # 11
slide_demo2(12)                 # 12  LIVE DEMO
slide_trust(13)                 # 13
slide_scale(14)                 # 14
slide_roadmap(15)               # 15
slide_close(16)                 # 16

OUT = "presentation/Retention_Intelligence_Demo.pptx"
prs.save(OUT)
print(f"wrote {OUT}  ({len(prs.slides._sldIdLst)} slides)")
