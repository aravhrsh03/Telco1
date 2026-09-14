"""
Generates Retention_Intelligence_Demo.pptx -- a real, editable PowerPoint
file matching presentation/DEMO_SCRIPT.md slide for slide.

Run:
    python presentation/build_deck.py
"""
from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Inches, Pt

OUT_PATH = Path(__file__).resolve().parent / "Retention_Intelligence_Demo.pptx"

# ---------------------------------------------------------------- palette --
STAGE = RGBColor(0x0B, 0x0F, 0x14)
SURFACE = RGBColor(0x12, 0x1A, 0x22)
LINE = RGBColor(0x22, 0x30, 0x40)
INK = RGBColor(0xEE, 0xF3, 0xF5)
INK_SOFT = RGBColor(0x9F, 0xB0, 0xB8)
INK_FAINT = RGBColor(0x5F, 0x71, 0x7A)
ACCENT = RGBColor(0x33, 0xD6, 0xC6)
ACCENT_STRONG = RGBColor(0x94, 0xF5, 0xEA)
ENERGY = RGBColor(0xFF, 0x8A, 0x5C)

HEAD_FONT = "Segoe UI Semibold"
BODY_FONT = "Segoe UI"
MONO_FONT = "Consolas"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def new_deck() -> Presentation:
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def add_slide(prs: Presentation):
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank layout
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    bg.fill.solid()
    bg.fill.fore_color.rgb = STAGE
    bg.line.fill.background()
    bg.shadow.inherit = False
    # send to back
    bg._element.addprevious(bg._element)
    slide.shapes._spTree.remove(bg._element)
    slide.shapes._spTree.insert(2, bg._element)
    return slide


def add_text(slide, text, left, top, width, height, size, color=INK,
             bold=False, italic=False, font=BODY_FONT, align=PP_ALIGN.CENTER,
             anchor=MSO_ANCHOR.TOP, spacing=None, line_spacing=1.15):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = line_spacing
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font
    run.font.color.rgb = color
    if spacing is not None:
        # letter-spacing isn't directly supported by python-pptx; emulate
        # with a lighter visual weight via caps for eyebrow-style labels.
        pass
    return box


def eyebrow(slide, text, top=Inches(0.7)):
    return add_text(slide, text.upper(), Inches(1), top, SLIDE_W - Inches(2), Inches(0.4),
                     14, ACCENT, bold=True, font=MONO_FONT, align=PP_ALIGN.CENTER)


def rounded_card(slide, left, top, width, height, fill=SURFACE, line_color=LINE):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.adjustments[0] = 0.08
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = line_color
    shape.line.width = Pt(1)
    shape.shadow.inherit = False
    return shape


def card_text(shape, lines, top_offset=Inches(0.18)):
    """lines: list of (text, size, color, bold, font)"""
    tf = shape.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.22)
    tf.margin_right = Inches(0.22)
    tf.margin_top = top_offset
    for i, (text, size, color, bold, font) in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        run.text = text
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.name = font
        run.font.color.rgb = color


# ------------------------------------------------------------------ slides --

def slide_title(prs):
    s = add_slide(prs)
    eyebrow(s, "Product Walkthrough", top=Inches(1.9))
    add_text(s, "Retention Intelligence", Inches(1), Inches(2.5), SLIDE_W - Inches(2), Inches(1.3),
              54, INK, bold=True, font=HEAD_FONT)
    add_text(s, "Turn churn data into a conversation — and a conversation into action.",
              Inches(2), Inches(3.9), SLIDE_W - Inches(4), Inches(0.7), 20, INK_SOFT, font=BODY_FONT)
    add_text(s, "IBM / Telco Customer Churn  ·  7,043 customers  ·  live system, not a mockup",
              Inches(1), Inches(5.6), SLIDE_W - Inches(2), Inches(0.5), 13, INK_FAINT, font=MONO_FONT)


def slide_stat(prs):
    s = add_slide(prs)
    eyebrow(s, "The Problem", top=Inches(0.8))
    add_text(s, "26.5%", Inches(1), Inches(1.5), SLIDE_W - Inches(2), Inches(2.2),
              120, ENERGY, bold=True, font=HEAD_FONT)
    add_text(s, "of this operator's customers churn — better than one in four, gone.",
              Inches(2), Inches(3.75), SLIDE_W - Inches(4), Inches(0.8), 22, INK_SOFT, font=BODY_FONT)
    line = slide_hr(s, Inches(3.5), Inches(4.75), Inches(6.3))
    add_text(s, "Winning a customer back costs several times more than keeping one. "
                 "The question was never “can we survive churn” — it's “do we see it coming.”",
              Inches(2.7), Inches(4.9), SLIDE_W - Inches(5.4), Inches(1.0), 14, INK_FAINT, font=BODY_FONT)


def slide_hr(slide, left, top, width):
    ln = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, left, top, left + width, top)
    ln.line.color.rgb = LINE
    ln.line.width = Pt(1)
    return ln


def three_cards(prs, headline, items):
    s = add_slide(prs)
    add_text(s, headline, Inches(1), Inches(0.9), SLIDE_W - Inches(2), Inches(1.1),
              34, INK, bold=True, font=HEAD_FONT)
    card_w, card_h, gap = Inches(3.6), Inches(2.6), Inches(0.4)
    total_w = card_w * 3 + gap * 2
    left0 = (SLIDE_W - total_w) / 2
    top = Inches(3.1)
    for i, text in enumerate(items):
        left = left0 + i * (card_w + gap)
        card = rounded_card(s, left, top, card_w, card_h)
        card_text(card, [
            (f"0{i+1}", 13, ACCENT, True, MONO_FONT),
            (text, 16, INK, False, BODY_FONT),
        ])
    return s


def slide_statement(prs, eyebrow_text, headline, accent_word_start, sub):
    s = add_slide(prs)
    eyebrow(s, eyebrow_text, top=Inches(1.6))
    box = add_text(s, headline, Inches(1.2), Inches(2.3), SLIDE_W - Inches(2.4), Inches(1.8),
                    40, INK, bold=True, font=HEAD_FONT)
    add_text(s, sub, Inches(2), Inches(4.2), SLIDE_W - Inches(4), Inches(1.0), 18, INK_SOFT, font=BODY_FONT)
    return s


def slide_architecture(prs):
    s = add_slide(prs)
    eyebrow(s, "How It's Built", top=Inches(0.6))
    add_text(s, "One pipeline, end to end", Inches(1), Inches(1.05), SLIDE_W - Inches(2), Inches(0.8),
              30, INK, bold=True, font=HEAD_FONT)

    nodes = [
        ("Raw Data", "7,043 rows"),
        ("Cleaned + DB", "MySQL"),
        ("ML Model", "F1 ≈ 0.58"),
        ("API", "FastAPI"),
        ("Dashboard", "React"),
    ]
    n = len(nodes)
    y = Inches(3.3)
    left0 = Inches(1.2)
    right0 = SLIDE_W - Inches(1.2)
    span = right0 - left0
    step = span / (n - 1)

    line = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, left0, y, right0, y)
    line.line.color.rgb = LINE
    line.line.width = Pt(2)

    centers = []
    for i, (label, sub) in enumerate(nodes):
        cx = left0 + step * i
        centers.append(cx)
        dot = s.shapes.add_shape(MSO_SHAPE.OVAL, cx - Inches(0.09), y - Inches(0.09), Inches(0.18), Inches(0.18))
        dot.fill.solid(); dot.fill.fore_color.rgb = ACCENT; dot.line.fill.background(); dot.shadow.inherit = False
        add_text(s, label, cx - Inches(1.0), y - Inches(0.75), Inches(2.0), Inches(0.4),
                  15, INK, bold=True, font=HEAD_FONT)
        add_text(s, sub, cx - Inches(1.0), y + Inches(0.2), Inches(2.0), Inches(0.35),
                  12, INK_SOFT, font=MONO_FONT)

    # dashed branch down to AI Assistant from the API node
    api_cx = centers[3]
    dash = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, api_cx, y + Inches(0.12),
                                   centers[4], y + Inches(2.0))
    dash.line.color.rgb = ENERGY
    dash.line.width = Pt(2)
    dash.line.dash_style = 2  # dashed
    aidot = s.shapes.add_shape(MSO_SHAPE.OVAL, centers[4] - Inches(0.09), y + Inches(2.0) - Inches(0.09),
                                Inches(0.18), Inches(0.18))
    aidot.fill.solid(); aidot.fill.fore_color.rgb = ENERGY; aidot.line.fill.background(); aidot.shadow.inherit = False
    add_text(s, "AI Assistant", centers[4] + Inches(0.15), y + Inches(1.75), Inches(2.6), Inches(0.4),
              15, ENERGY, bold=True, font=HEAD_FONT, align=PP_ALIGN.LEFT)
    add_text(s, "new — same API, as tools", centers[4] + Inches(0.15), y + Inches(2.15), Inches(2.8), Inches(0.35),
              12, ENERGY, font=MONO_FONT, align=PP_ALIGN.LEFT)


def slide_demo(prs, title, hint, metric=None, chips=None):
    s = add_slide(prs)
    badge = rounded_card(s, Inches(5.17), Inches(1.1), Inches(3.0), Inches(0.55), fill=ACCENT, line_color=ACCENT)
    badge.adjustments[0] = 0.5
    card_text(badge, [("LIVE DEMO", 15, STAGE, True, MONO_FONT)], top_offset=Inches(0.08))
    badge.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

    add_text(s, title, Inches(1), Inches(2.0), SLIDE_W - Inches(2), Inches(1.0),
              36, INK, bold=True, font=HEAD_FONT)
    add_text(s, hint, Inches(1), Inches(3.0), SLIDE_W - Inches(2), Inches(0.5),
              15, INK_FAINT, font=MONO_FONT)

    if metric:
        add_text(s, metric, Inches(1.5), Inches(3.8), SLIDE_W - Inches(3), Inches(0.6),
                  17, ACCENT_STRONG, font=MONO_FONT)

    if chips:
        chip_w, chip_h, gap = Inches(4.6), Inches(0.55), Inches(0.25)
        total_w = chip_w * len(chips) + gap * (len(chips) - 1)
        left0 = (SLIDE_W - total_w) / 2
        for i, chip in enumerate(chips):
            left = left0 + i * (chip_w + gap)
            c = rounded_card(s, left, Inches(4.0), chip_w, chip_h)
            c.adjustments[0] = 0.5
            card_text(c, [(chip, 12, INK_SOFT, False, BODY_FONT)], top_offset=Inches(0.12))
            c.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    return s


def slide_point_list(prs, headline, items):
    s = add_slide(prs)
    add_text(s, headline, Inches(1), Inches(0.85), SLIDE_W - Inches(2), Inches(1.0),
              32, INK, bold=True, font=HEAD_FONT)
    top = Inches(2.2)
    width = Inches(8.6)
    left = (SLIDE_W - width) / 2
    row_h = Inches(1.1)
    gap = Inches(0.22)
    for i, (icon, text) in enumerate(items):
        y = top + i * (row_h + gap)
        card = rounded_card(s, left, y, width, row_h)
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.3)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        r1 = p.add_run(); r1.text = f"{icon}   "; r1.font.name = MONO_FONT
        r1.font.size = Pt(14); r1.font.bold = True; r1.font.color.rgb = ACCENT
        r2 = p.add_run(); r2.text = text; r2.font.name = BODY_FONT
        r2.font.size = Pt(16); r2.font.color.rgb = INK
    return s


def slide_compare(prs):
    s = add_slide(prs)
    eyebrow(s, "Built The Way It's Audited", top=Inches(0.6))
    add_text(s, "Same customer. Different answer.", Inches(1), Inches(1.05), SLIDE_W - Inches(2), Inches(0.9),
              30, INK, bold=True, font=HEAD_FONT)

    card_w, card_h = Inches(3.6), Inches(2.3)
    gap = Inches(1.6)
    total_w = card_w * 2 + gap
    left0 = (SLIDE_W - total_w) / 2
    top = Inches(3.0)

    before = rounded_card(s, left0, top, card_w, card_h)
    card_text(before, [
        ("BEFORE THE FIX", 12, INK_FAINT, True, MONO_FONT),
        ("45.8%", 40, INK_SOFT, True, HEAD_FONT),
        ("“Unlikely to churn”", 14, INK, False, BODY_FONT),
    ])

    add_text(s, "→", left0 + card_w, top + Inches(0.6), gap, Inches(1.0),
              36, INK_FAINT, font=HEAD_FONT)

    after = rounded_card(s, left0 + card_w + gap, top, card_w, card_h, line_color=ACCENT)
    card_text(after, [
        ("AFTER THE FIX", 12, ACCENT, True, MONO_FONT),
        ("56.5%", 40, ENERGY, True, HEAD_FONT),
        ("“Likely to churn”", 14, INK, False, BODY_FONT),
    ])

    add_text(s, "Found by using Claude to audit our own prediction code — "
                 "before it ever reached a customer-facing decision.",
              Inches(2.2), Inches(5.7), SLIDE_W - Inches(4.4), Inches(0.8), 13, INK_FAINT, font=BODY_FONT)


def slide_close(prs):
    s = add_slide(prs)
    add_text(s, "26% of your customers are telling you they might leave.",
              Inches(1.3), Inches(2.5), SLIDE_W - Inches(2.6), Inches(1.8), 38, INK, bold=True, font=HEAD_FONT)
    add_text(s, "Let's talk about a pilot for your team.", Inches(2), Inches(4.4), SLIDE_W - Inches(4), Inches(0.6),
              18, ACCENT_STRONG, font=MONO_FONT)


def build() -> None:
    prs = new_deck()

    slide_title(prs)                                                             # 1
    slide_stat(prs)                                                              # 2
    three_cards(prs, "Three ways teams miss it", [                               # 3
        "They find out after the cancellation, not before.",
        "No ranked list of who's actually at risk today.",
        "Every question means a SQL query and a wait on the data team.",
    ])
    slide_statement(prs, "The Answer", "One pipeline. One API. One conversation.",
                     None, "A single system, from a raw customer extract to a "
                     "trained model to a retention analyst you can talk to.")  # 4
    slide_architecture(prs)                                                      # 5
    slide_demo(prs, "Executive Summary", "→ switch to the Churn Summary tab",
               metric="Month-to-month: 42.7% churn   ·   Two-year: 2.8% churn")  # 6
    slide_demo(prs, "Find Who's At Risk", "→ switch to the High-Risk Customers tab",
               metric="Rule: month-to-month + tenure < 12 + above-average bill")  # 7
    slide_demo(prs, "What-If Prediction", "→ switch to the Churn Prediction tab",
               metric="Type in a scenario. Get a live, color-coded risk score.")  # 8
    slide_statement(prs, "The Differentiator", "Now, ask it anything.",
                     None, "You no longer need to know which tab has the answer.")  # 9
    slide_demo(prs, "The Retention Assistant", "→ switch to the Retention Assistant tab",
               chips=["“What's our overall churn rate?”",
                      "“Is 7590-VHVEG high-risk, and what's their score?”"])  # 10
    slide_point_list(prs, "Why you can trust the answer", [                       # 11
        ("01", "Every number it states comes from a real tool call — never invented."),
        ("02", "It can't dump your whole customer list, and won't claim a cause your data doesn't support."),
        ("03", "Every conversation is written to an audit log — question, tools, tokens."),
    ])
    slide_compare(prs)                                                           # 12
    slide_point_list(prs, "What's next", [                                       # 13
        ("→", "A scheduled daily brief flagging which segments moved overnight."),
        ("→", "An automatic code review on every change, before it reaches production."),
        ("→", "A standing evaluation suite — every model choice justified by numbers."),
    ])
    slide_close(prs)                                                             # 14

    prs.save(OUT_PATH)
    print(f"Wrote {OUT_PATH} ({len(prs.slides)} slides)")


if __name__ == "__main__":
    build()
