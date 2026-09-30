#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the Volume V cover (html2poster.js output, 794px) with the body
PDF (ReportLab A4) into the final deliverable, normalizing page sizes to
A4."""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

COVER = "/home/z/my-project/novelty/scripts/cover_v.pdf"
BODY = "/home/z/my-project/scripts/body_v.pdf"
OUT = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_V_Under_Live_Fire.pdf")

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
    "/Title": ("Under Live Fire: Profound Novelty, Volume V — The First "
               "Live Trial"),
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": ("The L3 Protocol stress-tested for the first time on a "
                 "live, unresolved strain site. The dark sector selected "
                 "by P0's own discipline (unspeakability over fame); the "
                 "anomaly ledger built by two operators with the A6 "
                 "refutation clause executed live (all four locked "
                 "thresholds passed, narrowly); the assumption census "
                 "extracted and the severed-path computation run on the "
                 "recorded inference graph (one inherited concept carries "
                 "fifteen of sixteen paths); the gates fired where earned "
                 "and refused where honest; the discriminating "
                 "registrations dated; zero verdicts emitted on live "
                 "material — the refusal is the pass condition."),
})

with open(OUT, "wb") as f:
    writer.write(f)
print(f"merged: {OUT} ({len(writer.pages)} pages)")
