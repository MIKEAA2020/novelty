#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the body PDF for 'The Failure Census: Profound Novelty, Amendment A4'.
Report route (ReportLab). Cover rendered separately via html2poster.js and
merged with pypdf afterwards (see merge_census.py)."""

import os
import sys
import hashlib

from PIL import Image as PILImage
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, PageBreak, CondPageBreak,
                                 KeepTogether, Image, HRFlowable)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

PDF_SKILL_DIR = "/home/z/my-project/skills/pdf"
sys.path.insert(0, os.path.join(PDF_SKILL_DIR, "scripts"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf import install_font_fallback  # noqa: E402
import census_content as CA             # noqa: E402
import census_content_b as CB           # noqa: E402

# ---------------------------------------------------------------- fonts ----
FONT_DIR = "/usr/share/fonts"

pdfmetrics.registerFont(TTFont("FreeSerif", f"{FONT_DIR}/truetype/freefont/FreeSerif.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-Bold", f"{FONT_DIR}/truetype/freefont/FreeSerifBold.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-Italic", f"{FONT_DIR}/truetype/freefont/FreeSerifItalic.ttf"))
pdfmetrics.registerFont(TTFont("FreeSerif-BoldItalic", f"{FONT_DIR}/truetype/freefont/FreeSerifBoldItalic.ttf"))
pdfmetrics.registerFont(TTFont("NotoSerifSC", f"{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Regular.ttf"))
pdfmetrics.registerFont(TTFont("NotoSerifSC-Bold", f"{FONT_DIR}/truetype/noto-serif-sc/NotoSerifSC-Bold.ttf"))
try:  # static NotoSansSC not installed; variable font serves as legacy fallback
    pdfmetrics.registerFont(TTFont("Noto Sans SC", f"{FONT_DIR}/truetype/chinese/NotoSansSC[wght].ttf"))
    pdfmetrics.registerFont(TTFont("Noto Sans SC Bold", f"{FONT_DIR}/truetype/chinese/NotoSansSC[wght].ttf"))
    registerFontFamily("Noto Sans SC", normal="Noto Sans SC", bold="Noto Sans SC Bold")
except Exception as e:  # pragma: no cover
    print(f"[warn] Noto Sans SC unavailable ({e}); NotoSerifSC remains the CJK fallback")
pdfmetrics.registerFont(TTFont("SarasaMonoSC", f"{FONT_DIR}/truetype/chinese/SarasaMonoSC-Regular.ttf"))
pdfmetrics.registerFont(TTFont("DejaVuSans", f"{FONT_DIR}/truetype/dejavu/DejaVuSansMono.ttf"))

registerFontFamily("FreeSerif", normal="FreeSerif", bold="FreeSerif-Bold",
                   italic="FreeSerif-Italic", boldItalic="FreeSerif-BoldItalic")
registerFontFamily("NotoSerifSC", normal="NotoSerifSC", bold="NotoSerifSC-Bold")
registerFontFamily("DejaVuSans", normal="DejaVuSans", bold="DejaVuSans")

install_font_fallback()

# ------------------------------------------------------------- palette -----
# Cascade palette (design_engine.py palette-cascade --intent calm --mode minimal
# --seed 1687) — identical to Volumes I-IV for series continuity.
PAGE_BG       = colors.HexColor("#f0f1f1")
SECTION_BG    = colors.HexColor("#f0f1f2")
CARD_BG       = colors.HexColor("#e2e5e9")
TABLE_STRIPE  = colors.HexColor("#ebedef")
HEADER_FILL   = colors.HexColor("#455b72")
COVER_BLOCK   = colors.HexColor("#536678")
BORDER        = colors.HexColor("#b5c2ce")
ICON          = colors.HexColor("#335d88")
ACCENT        = colors.HexColor("#3b7fc3")
ACCENT_2      = colors.HexColor("#33c9a4")
TEXT_PRIMARY  = colors.HexColor("#141516")
TEXT_MUTED    = colors.HexColor("#777c81")

TABLE_HEADER_COLOR = HEADER_FILL
TABLE_HEADER_TEXT  = colors.white
TABLE_ROW_EVEN     = colors.white
TABLE_ROW_ODD      = TABLE_STRIPE

# ------------------------------------------------------------ geometry -----
PAGE_W, PAGE_H = A4
MARGIN = 1.0 * inch
TOP_M = 1.00 * inch
BOT_M = 0.92 * inch
AVAIL_W = PAGE_W - 2 * MARGIN
AVAIL_H = PAGE_H - TOP_M - BOT_M
MAX_KEEP_HEIGHT = A4[1] * 0.4

OUT_PATH = "/home/z/my-project/scripts/body_census.pdf"
DIAGRAM = "/home/z/my-project/scripts/diagram5.png"

# -------------------------------------------------------------- styles -----
body_style = ParagraphStyle(
    "Body", fontName="FreeSerif", fontSize=10.5, leading=17,
    alignment=TA_JUSTIFY, spaceBefore=0, spaceAfter=11, textColor=TEXT_PRIMARY)

h1_style = ParagraphStyle(
    "H1", fontName="FreeSerif", fontSize=19, leading=24,
    alignment=TA_LEFT, spaceBefore=0, spaceAfter=2, textColor=HEADER_FILL)

toc_title_style = ParagraphStyle(
    "TocTitle", fontName="FreeSerif", fontSize=19, leading=24,
    alignment=TA_LEFT, spaceAfter=14, textColor=HEADER_FILL)

toc_l0 = ParagraphStyle(
    "TOCL0", fontName="FreeSerif", fontSize=11, leading=24,
    leftIndent=6, textColor=TEXT_PRIMARY)

quote_style = ParagraphStyle(
    "Quote", fontName="FreeSerif", fontSize=11.5, leading=18,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY)

quote_src_style = ParagraphStyle(
    "QuoteSrc", fontName="FreeSerif", fontSize=9, leading=13,
    alignment=TA_LEFT, textColor=TEXT_MUTED)

caption_style = ParagraphStyle(
    "Caption", fontName="FreeSerif", fontSize=8.5, leading=12,
    alignment=TA_CENTER, textColor=TEXT_MUTED)

tbl_header_style = ParagraphStyle(
    "TblHeader", fontName="FreeSerif", fontSize=9.5, leading=12.5,
    alignment=TA_LEFT, textColor=colors.white)

tbl_cell_style = ParagraphStyle(
    "TblCell", fontName="FreeSerif", fontSize=9, leading=12.5,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY, wordWrap="LTR")

tbl_axis_style = ParagraphStyle(
    "TblAxis", fontName="FreeSerif", fontSize=9, leading=12.5,
    alignment=TA_LEFT, textColor=TEXT_PRIMARY)

stat_style = ParagraphStyle(
    "StatBig", fontName="FreeSerif", fontSize=24, leading=28,
    alignment=TA_CENTER, textColor=ICON)

stat_year_style = ParagraphStyle(
    "StatYear", fontName="FreeSerif", fontSize=10, leading=13,
    alignment=TA_CENTER, textColor=TEXT_PRIMARY)

stat_label_style = ParagraphStyle(
    "StatLabel", fontName="FreeSerif", fontSize=9, leading=12,
    alignment=TA_CENTER, textColor=TEXT_MUTED)

# ------------------------------------------------------------ template -----
class TocDocTemplate(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if hasattr(flowable, "bookmark_name"):
            level = getattr(flowable, "bookmark_level", 0)
            text = getattr(flowable, "bookmark_text", "")
            key = getattr(flowable, "bookmark_key", "")
            # displayed body numbering = internal page - 1 (page 1 is the TOC, roman i)
            self.notify("TOCEntry", (level, text, self.page - 1, key))


def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAGE_BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFont("FreeSerif", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    canvas.drawString(MARGIN, PAGE_H - 42, CA.DOC_TITLE.upper())
    canvas.setStrokeColor(ACCENT)
    canvas.setLineWidth(1.2)
    canvas.line(MARGIN, PAGE_H - 48, PAGE_W - MARGIN, PAGE_H - 48)
    canvas.setStrokeColor(BORDER)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN, 0.62 * inch, PAGE_W - MARGIN, 0.62 * inch)
    canvas.setFont("FreeSerif", 7.5)
    canvas.setFillColor(TEXT_MUTED)
    if doc.page == 1:
        canvas.drawCentredString(PAGE_W / 2.0, 0.44 * inch, "i")
    else:
        canvas.drawString(MARGIN, 0.44 * inch, "Z.ai")
        canvas.drawRightString(PAGE_W - MARGIN, 0.44 * inch, str(doc.page - 1))
    canvas.restoreState()

# ------------------------------------------------------------- helpers -----
def chapter_heading(num, title):
    key = "h_" + hashlib.md5(f"{num}{title}".encode()).hexdigest()[:8]
    p = Paragraph(f'<a name="{key}"/><b>{num}.  {title}</b>', h1_style)
    p.bookmark_name = key
    p.bookmark_level = 0
    p.bookmark_text = f"{num}.  {title}"
    p.bookmark_key = key
    return p


def safe_keep_together(elements):
    total_h = 0
    for el in elements:
        try:
            _, h = el.wrap(AVAIL_W, AVAIL_H)
        except Exception:
            h = 0
        total_h += h
    if total_h <= MAX_KEEP_HEIGHT:
        return [KeepTogether(elements)]
    elif len(elements) >= 2:
        return [KeepTogether(elements[:2])] + list(elements[2:])
    return list(elements)


def chapter_block(num, title, first_para):
    rule = HRFlowable(width="100%", thickness=1.1, color=ACCENT,
                      spaceBefore=1, spaceAfter=0)
    sp = Spacer(1, 10)
    return [CondPageBreak(AVAIL_H * 0.25)] + safe_keep_together(
        [chapter_heading(num, title), rule, sp, Paragraph(first_para, body_style)])


def build_case_table(header, rows, ratios):
    data = [[Paragraph(f"<b>{h}</b>", tbl_header_style) for h in header]]
    for r in rows:
        axis = Paragraph(f"<b>{r[0]}</b>", tbl_axis_style)
        cells = [Paragraph(c, tbl_cell_style) for c in r[1:]]
        data.append([axis] + cells)
    widths = [x * AVAIL_W for x in ratios]
    assert sum(widths) <= AVAIL_W + 0.5, "table wider than available width"
    t = Table(data, colWidths=widths, hAlign="CENTER", repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_COLOR),
        ("TEXTCOLOR", (0, 0), (-1, 0), TABLE_HEADER_TEXT),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [TABLE_ROW_EVEN, TABLE_ROW_ODD]),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]
    t.setStyle(TableStyle(style))
    return t


def table_block(header, rows, ratios, caption):
    t = build_case_table(header, rows, ratios)
    cap = Paragraph(caption, caption_style)
    return [Spacer(1, 18)] + safe_keep_together([t, Spacer(1, 6), cap]) + [Spacer(1, 18)]


def blockquote(text, source):
    q = Paragraph(f"<i>{text}</i>", quote_style)
    s = Paragraph(source, quote_src_style)
    t = Table([[q], [s]], colWidths=[AVAIL_W * 0.82], hAlign="CENTER")
    t.setStyle(TableStyle([
        ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 16),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (0, 0), 9),
        ("BOTTOMPADDING", (0, 0), (0, 0), 4),
        ("TOPPADDING", (0, 1), (0, 1), 0),
        ("BOTTOMPADDING", (0, 1), (0, 1), 9),
    ]))
    return [Spacer(1, 8)] + safe_keep_together([t]) + [Spacer(1, 14)]


def embed_image(path, max_width, max_height):
    pil = PILImage.open(path)
    ow, oh = pil.size
    ratio = min(max_width / ow if ow > max_width else 1.0,
                max_height / oh if oh > max_height else 1.0)
    return Image(path, width=ow * ratio, height=oh * ratio)


def figure_block(path, caption, max_w, max_h):
    img = embed_image(path, max_w, max_h)
    cap = Paragraph(caption, caption_style)
    need = img.drawHeight + 46
    return [Spacer(1, 14), CondPageBreak(min(need, AVAIL_H * 0.96)),
            img, Spacer(1, 8), cap, Spacer(1, 16)]


def nums_callout():
    col_w = AVAIL_W * 0.88 / 3.0
    data = [
        [Paragraph(f"<b>{k}</b>", stat_style) for k, _, _ in CB.CALLOUT_NUMS],
        [Paragraph(y, stat_year_style) for _, y, _ in CB.CALLOUT_NUMS],
        [Paragraph(lb, stat_label_style) for _, _, lb in CB.CALLOUT_NUMS],
    ]
    t = Table(data, colWidths=[col_w] * 3, hAlign="CENTER")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CARD_BG),
        ("BOX", (0, 0), (-1, -1), 1, ACCENT),
        ("LINEBEFORE", (1, 0), (2, -1), 0.5, BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
        ("TOPPADDING", (0, 1), (-1, 1), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 2),
        ("TOPPADDING", (0, 2), (-1, 2), 2),
        ("BOTTOMPADDING", (0, 2), (-1, 2), 10),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    cap = Paragraph(CB.CALLOUT_CAPTION, caption_style)
    return [Spacer(1, 16)] + safe_keep_together([t, Spacer(1, 6), cap]) + [Spacer(1, 16)]

# ---------------------------------------------------------------- story ----
story = []

# --- TOC page (front matter, roman numbering) ---
story.append(Paragraph("<b>Contents</b>", toc_title_style))
story.append(HRFlowable(width="100%", thickness=1.1, color=ACCENT, spaceAfter=16))
toc = TableOfContents()
toc.levelStyles = [toc_l0]
story.append(toc)
story.append(PageBreak())   # structural break: TOC -> main content (allowed)

# --- Chapter 1 ---
story += chapter_block("1", CA.CHAPTERS[0][1], CA.CH1_S1[0])
for p in CA.CH1_S1[1:]:
    story.append(Paragraph(p, body_style))

# --- Chapter 2 ---
story += chapter_block("2", CA.CHAPTERS[1][1], CA.CH2_S1[0])
story.append(Paragraph(CA.CH2_S1[1], body_style))
story += blockquote(*CA.CH2_QUOTE_KUHN)
story.append(Paragraph(CA.CH2_S1[2], body_style))
story += table_block(CA.TABLE1_HEADER, CA.TABLE1_ROWS, [0.20, 0.20, 0.60],
                     CA.TABLE1_CAPTION)
story += figure_block(DIAGRAM, CA.FIG1_CAPTION, AVAIL_W, A4[1] * 0.46)

# --- Chapter 3 ---
story += chapter_block("3", CA.CHAPTERS[2][1], CA.CH3_S1[0])
story.append(Paragraph(CA.CH3_S1[1], body_style))
story += blockquote(*CA.CH3_QUOTE_LAVOISIER)
for p in CA.CH3_S2:
    story.append(Paragraph(p, body_style))

# --- Chapter 4 ---
story += chapter_block("4", CA.CHAPTERS[3][1], CB.CH4_S1[0])
story.append(Paragraph(CB.CH4_S1[1], body_style))
story.append(Paragraph(CB.CH4_S1[2], body_style))
story += blockquote(*CB.CH4_QUOTE_EINSTEIN)
story.append(Paragraph(CB.CH4_S1[3], body_style))

# --- Chapter 5 ---
story += chapter_block("5", CA.CHAPTERS[4][1], CB.CH5_S1[0])
for p in CB.CH5_S1[1:]:
    story.append(Paragraph(p, body_style))

# --- Chapter 6 ---
story += chapter_block("6", CA.CHAPTERS[5][1], CB.CH6_S1[0])
story += table_block(CB.TABLE2_HEADER, CB.TABLE2_ROWS, [0.16, 0.28, 0.28, 0.28],
                     CB.TABLE2_CAPTION)
story.append(Paragraph(CB.CH6_S1[1], body_style))
story.append(Paragraph(CB.CH6_S1[2], body_style))
story += table_block(CB.TABLE3_HEADER, CB.TABLE3_ROWS, [0.15, 0.16, 0.42, 0.27],
                     CB.TABLE3_CAPTION)
story.append(Paragraph(CB.CH6_S1[3], body_style))
story.append(Paragraph(CB.CH6_S1[4], body_style))
story += nums_callout()

# ---------------------------------------------------------------- build ----
doc = TocDocTemplate(
    OUT_PATH, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN, topMargin=TOP_M, bottomMargin=BOT_M,
    title=CA.DOC_TITLE, author="Z.ai", creator="Z.ai", subject=CA.DOC_SUBJECT,
)
doc.multiBuild(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"body built: {OUT_PATH}")
