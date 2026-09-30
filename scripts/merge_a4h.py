#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the A4h cover (html2poster.js output, 794px) with the body PDF
(ReportLab A4) into the final deliverable, normalizing page sizes to A4."""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

COVER = "/home/z/my-project/novelty/scripts/cover_a4h.pdf"
BODY = "/home/z/my-project/scripts/body_a4h.pdf"
OUT = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_A4h_The_Fifth_Reading_and_the_Owners_Advice.pdf")

A4_W, A4_H = 595.2755905511812, 841.8897637795277

writer = PdfWriter()
cover = PdfReader(COVER)
for page in cover.pages:
    # 794 px at 72 dpi -> 595.5 pt; scale to exact A4
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    sx, sy = A4_W / w, A4_H / h
    page.scale(sx, sy)
    page.mediabox = RectangleObject((0, 0, A4_W, A4_H))
    writer.add_page(page)

body = PdfReader(BODY)
for page in body.pages:
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    if abs(w - A4_W) > 0.2 or abs(h - A4_H) > 0.2:
        sx, sy = A4_W / w, A4_H / h
        page.scale(sx, sy)
        page.mediabox = RectangleObject((0, 0, A4_W, A4_H))
    writer.add_page(page)

writer.add_metadata({
    "/Title": ("The Fifth Reading and the Owner's Advice: Profound "
               "Novelty, Amendment A4h"),
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": ("The fifth reading (gemini 3.8, recovered from the "
                 "repository history after the A4g sync's overwrite) "
                 "processed under the locked rules — the series' first "
                 "within-lineage version-drift measurement, eleven of "
                 "sixteen moved cells toward the amended census, the "
                 "ether's three-discriminator challenge collapsed. The "
                 "owner's deepseek advice verified, augmented, and "
                 "placed: the umbrella confirmed as premise, the physics "
                 "shape measured three ways, the AI blueprint re-derived "
                 "blind against Volume III. No census cell moves; the "
                 "killing clauses unfired under fourteen readings."),
})

with open(OUT, "wb") as f:
    writer.write(f)
print(f"merged: {OUT} ({len(writer.pages)} pages)")
