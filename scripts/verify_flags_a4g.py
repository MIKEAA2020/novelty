#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Objective verification of the VQA flags for A4g, body-only spans
(header y<60 and footer y>785 excluded), with per-page rightmost body
edge, vertical extent, and fill ratio against the 70..775 body band."""
import fitz

PDF = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_A4g_The_Fourth_Delivery_and_the_Seventh_Pair.pdf")
A4_W = 595.28
RIGHT_EDGE = A4_W - 72.0     # 523.28pt
BODY_TOP, BODY_BOT = 60.0, 785.0

doc = fitz.open(PDF)
names = {2: "p02 TOC", 4: "p04 ch1 end/T1", 5: "p05 diagram",
         10: "p10 T5 B6 matrix", 17: "p17 T9 ledger",
         18: "p18 T10 dead matrix", 19: "p19 T10 cont/T11",
         21: "p21 callout"}

for idx in sorted(names):
    page = doc[idx]
    d = page.get_text("dict")
    max_x1 = 0.0
    min_y0, max_y1 = 1e9, 0.0
    n = 0
    for block in d["blocks"]:
        for line in block.get("lines", []):
            for sp in line["spans"]:
                x0, y0, x1, y1 = sp["bbox"]
                if y1 < BODY_TOP or y0 > BODY_BOT:   # header/footer
                    continue
                if not sp["text"].strip():
                    continue
                n += 1
                max_x1 = max(max_x1, x1)
                min_y0 = min(min_y0, y0)
                max_y1 = max(max_y1, y1)
    if n == 0:
        print(f"[{names[idx]:>18}] no body spans")
        continue
    content_h = max_y1 - min_y0
    fill = content_h / (BODY_BOT - BODY_TOP)
    over = max_x1 > RIGHT_EDGE + 1.5
    print(f"[{names[idx]:>18}] body spans={n:>4} rightmost={max_x1:7.2f} "
          f"(limit {RIGHT_EDGE:.2f}) -> {'OVER' if over else 'within'} | "
          f"body {min_y0:.0f}..{max_y1:.0f} fill={fill:.1%}")
doc.close()
