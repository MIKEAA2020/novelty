#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the body PDF for 'The L3 Protocol: Profound Novelty, Volume III —
Version 1.1'. Report route (ReportLab). Cover rendered separately via
html2poster.js and merged with pypdf afterwards (see merge_v11.py).

Reissue strategy: unchanged text is imported from the v1.0 content modules
(protocol_content{,_b,_c}); amended and new text comes from v11_{a,b,c};
companion-artifact tables (translation, parameters, delta, census) are
imported from the audit and amendment modules. Table numbers are re-pointed
in place, and every cross-reference shift is patched explicitly.
"""

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
import protocol_content as CA0            # noqa: E402  (v1.0 ch1-2)
import protocol_content_b as CB0         # noqa: E402  (v1.0 ch3 pipeline)
import protocol_content_c as CC0         # noqa: E402  (v1.0 ch4-7)
import audit_content as AUD              # noqa: E402  (translation table)
import a3_content as A3C                  # noqa: E402  (parameters + delta)
import census_content_b as CEN            # noqa: E402  (census matrix + verdicts)
import v11_a as VA                        # noqa: E402  (v1.1 ch1-2)
import v11_b as VB                        # noqa: E402  (v1.1 ch3-4)
import v11_c as VC                        # noqa: E402  (v1.1 ch6-8)

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

OUT_PATH = "/home/z/my-project/scripts/body_v11.pdf"
DIAGRAM = "/home/z/my-project/scripts/diagram3.png"
CARD = "/home/z/my-project/scripts/card3_v11.png"

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
    "TOCL0", fontName="FreeSerif", fontSize=11, leading=22,
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
    canvas.drawString(MARGIN, PAGE_H - 42, "THE L3 PROTOCOL: PROFOUND NOVELTY, VOLUME III — VERSION 1.1")
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
        [Paragraph(f"<b>{k}</b>", stat_style) for k, _, _ in VB.CALLOUT_NUMS_V11],
        [Paragraph(y, stat_year_style) for _, y, _ in VB.CALLOUT_NUMS_V11],
        [Paragraph(lb, stat_label_style) for _, _, lb in VB.CALLOUT_NUMS_V11],
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
    cap = Paragraph(VB.CALLOUT_CAPTION_V11, caption_style)
    return [Spacer(1, 16)] + safe_keep_together([t, Spacer(1, 6), cap]) + [Spacer(1, 16)]

# ---- table-number re-pointing (captions imported from companion modules) --
CAP_T3 = AUD.TABLE1_CAPTION.replace("Table 1 —", "Table 3 —")
CAP_T4 = A3C.TABLE1_CAPTION.replace("Table 1 —", "Table 4 —")
CAP_T5 = A3C.TABLE2_CAPTION.replace("Table 2 —", "Table 5 —")
CAP_T7 = CC0.TABLE3_CAPTION.replace("Table 3 —", "Table 7 —")
CAP_T8 = CC0.TABLE4_CAPTION.replace("Table 4 —", "Table 8 —")
CAP_T9 = CEN.TABLE2_CAPTION.replace("Table 2 —", "Table 9 —")
CAP_T10 = CEN.TABLE3_CAPTION.replace("Table 3 —", "Table 10 —")
CAP_T11 = CC0.TABLE5_CAPTION.replace("Table 5 —", "Table 11 —")
# in-body table reference patch (ch5 vice-ledger lead-in)
CH5_P2_PATCHED = CC0.CH4_P2[0].replace("Table 3 states it", "Table 7 states it")

# ---------------------------------------------------------------- story ----
story = []

# --- TOC page (front matter, roman numbering) ---
story.append(Paragraph("<b>Contents</b>", toc_title_style))
story.append(HRFlowable(width="100%", thickness=1.1, color=ACCENT, spaceAfter=16))
toc = TableOfContents()
toc.levelStyles = [toc_l0]
story.append(toc)
story.append(PageBreak())   # structural break: TOC -> main content (allowed)

# --- Chapter 1: From Diagnosis to Operations, Version 1.1 ---
story += chapter_block("1", VA.CHAPTERS[0][1], CA0.CH1_S1[0])
story.append(Paragraph(VA.CH1_S1_1_V11, body_style))
story.append(Paragraph(CA0.CH1_S1[2], body_style))
story.append(Paragraph(VA.CH1_S1_3_V11, body_style))
for p in VA.CH1_NEW:
    story.append(Paragraph(p, body_style))
story += table_block(VA.AMEND_HEADER, VA.AMEND_ROWS, [0.06, 0.14, 0.54, 0.26],
                     VA.AMEND_CAPTION)
story += blockquote(*CA0.CH1_QUOTE_EINSTEIN)
for p in CA0.CH1_S2:
    story.append(Paragraph(p, body_style))
story += table_block(VA.TABLE2_HEADER, VA.TABLE2_ROWS, [0.26, 0.36, 0.12, 0.26],
                     VA.TABLE2_CAPTION)

# --- Chapter 2: The Chassis and the Delta (new) ---
story += chapter_block("2", VA.CHAPTERS[1][1], VA.CH2_P1[0])
story += blockquote(*VA.CH2_QUOTE_LAKATOS)
story.append(Paragraph(VA.CH2_P1[1], body_style))
story += table_block(AUD.TABLE1_HEADER, AUD.TABLE1_ROWS, [0.32, 0.32, 0.36],
                     CAP_T3)
story.append(Paragraph(VA.CH2_P1[2], body_style))
story += table_block(A3C.TABLE1_HEADER, A3C.TABLE1_ROWS, [0.16, 0.40, 0.22, 0.22],
                     CAP_T4)
story += table_block(A3C.TABLE2_HEADER, A3C.TABLE2_ROWS, [0.22, 0.26, 0.24, 0.28],
                     CAP_T5)
story.append(Paragraph(VA.CH2_P1[3], body_style))

# --- Chapter 3: Doctrine (amended) ---
story += chapter_block("3", VA.CHAPTERS[2][1], VB.CH3_INTRO_V11)
story.append(Paragraph(CA0.CH2[1], body_style))          # D1 unchanged
story.append(Paragraph(VB.D2_V11, body_style))           # D2 amended
story.append(Paragraph(VB.D3_V11, body_style))           # D3 amended
story.append(Paragraph(VB.D4_V11, body_style))           # D4 amended
story.append(Paragraph(CA0.CH2[5], body_style))          # D5 unchanged

# --- Chapter 4: The Pipeline (amended in place) ---
story += chapter_block("4", VA.CHAPTERS[3][1], VB.CH4_INTRO_0_V11)
story.append(Paragraph(CB0.CH3_INTRO[1], body_style))
story += figure_block(DIAGRAM, CB0.FIG1_CAPTION, AVAIL_W, A4[1] * 0.62)
for p in CB0.CH3_P0[:1]:
    story.append(Paragraph(p, body_style))
story.append(Paragraph(VB.P0_PARA2_V11, body_style))
for p in CB0.CH3_P1[:1]:
    story.append(Paragraph(p, body_style))
story.append(Paragraph(VB.P1_PARA2_V11, body_style))
for p in CB0.CH3_P2:
    story.append(Paragraph(p, body_style))
story += blockquote(*CB0.CH3_QUOTE_HEISENBERG)
for p in CB0.CH3_P3:
    story.append(Paragraph(p, body_style))
for p in CB0.CH3_P4[:1]:
    story.append(Paragraph(p, body_style))
story.append(Paragraph(VB.P4_PARA2_V11, body_style))
for p in CB0.CH3_P5:
    story.append(Paragraph(p, body_style))
for p in CB0.CH3_P6:
    story.append(Paragraph(p, body_style))
for p in CB0.CH3_P7[:1]:
    story.append(Paragraph(p, body_style))
story.append(Paragraph(VB.P7_PARA2_V11, body_style))
story += table_block(VB.TABLE6_HEADER, VB.TABLE6_ROWS, [0.17, 0.24, 0.33, 0.26],
                     VB.TABLE6_CAPTION)
story += nums_callout()
story.append(Paragraph(VB.CH4_CLOSE_V11, body_style))

# --- Chapter 5: Running the Protocol as an LLM (unchanged) ---
story += chapter_block("5", VA.CHAPTERS[4][1], CC0.CH4_P1[0])
story.append(Paragraph(CC0.CH4_P1[1], body_style))
story.append(Paragraph(CH5_P2_PATCHED, body_style))
story += table_block(CC0.TABLE3_HEADER, CC0.TABLE3_ROWS, [0.16, 0.42, 0.42],
                     CAP_T7)
story += blockquote(*CC0.CH4_QUOTE_PLANCK)
for p in CC0.CH4_P3:
    story.append(Paragraph(p, body_style))

# --- Chapter 6: Backtest — Living and Dead ---
story += chapter_block("6", VA.CHAPTERS[5][1], VC.CH6_P1)
story += table_block(CC0.TABLE4_HEADER, CC0.TABLE4_ROWS, [0.14, 0.29, 0.28, 0.29],
                     CAP_T8)
story.append(Paragraph(CC0.CH5_P2[0], body_style))
story.append(Paragraph(CC0.CH5_P2[1], body_style))
story += blockquote(*CC0.CH5_QUOTE_NEWTON)
story.append(Paragraph(VC.CH6_SILENCES, body_style))
story.append(Paragraph(VC.CH6_CENSUS_1, body_style))
story += table_block(CEN.TABLE2_HEADER, CEN.TABLE2_ROWS, [0.16, 0.28, 0.28, 0.28],
                     CAP_T9)
story.append(Paragraph(VC.CH6_CENSUS_2, body_style))
story += table_block(CEN.TABLE3_HEADER, CEN.TABLE3_ROWS, [0.15, 0.16, 0.42, 0.27],
                     CAP_T10)

# --- Chapter 7: Alarms, Refutation Clauses, and Honest Limits ---
story += chapter_block("7", VA.CHAPTERS[6][1], CC0.CH6_P1[0])
story += table_block(CC0.TABLE5_HEADER, CC0.TABLE5_ROWS, [0.14, 0.44, 0.42],
                     CAP_T11)
story.append(Paragraph(VC.CLAUSES_INTRO, body_style))
story += table_block(VC.CLAUSES_HEADER, VC.CLAUSES_ROWS, [0.13, 0.35, 0.27, 0.25],
                     VC.CLAUSES_CAPTION)
story.append(Paragraph(VC.SUCC_P1, body_style))
story.append(Paragraph(VC.LIMITS_1, body_style))
story.append(Paragraph(VC.LIMITS_2, body_style))
story.append(Paragraph(VC.LIMITS_3, body_style))

# --- Chapter 8: Invocation: The Card ---
story += chapter_block("8", VA.CHAPTERS[7][1], CC0.CH7[0])
story.append(Paragraph(VC.CH8_P2, body_style))
story += figure_block(CARD, VC.FIG2_CAPTION_V11, AVAIL_W, A4[1] * 0.74)

# ---------------------------------------------------------------- build ----
doc = TocDocTemplate(
    OUT_PATH, pagesize=A4,
    leftMargin=MARGIN, rightMargin=MARGIN, topMargin=TOP_M, bottomMargin=BOT_M,
    title=VA.DOC_TITLE, author="Z.ai", creator="Z.ai", subject=VA.DOC_SUBJECT,
)
doc.multiBuild(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"body built: {OUT_PATH}")
