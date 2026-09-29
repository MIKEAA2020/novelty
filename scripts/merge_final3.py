#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover3.pdf (Playwright) + body3.pdf (ReportLab) into the final
Volume III deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover3.pdf"
BODY = "/home/z/my-project/scripts/body3.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_III_The_L3_Protocol.pdf"


def normalize_page_to_a4(page):
    box = page.mediabox
    w, h = float(box.width), float(box.height)
    if abs(w - A4_W) > 0.2 or abs(h - A4_H) > 0.2:
        page.scale_to(A4_W, A4_H)
    return page


def main():
    writer = PdfWriter()
    cover_page = PdfReader(COVER).pages[0]
    writer.add_page(normalize_page_to_a4(cover_page))
    for page in PdfReader(BODY).pages:
        writer.add_page(normalize_page_to_a4(page))
    writer.add_metadata({
        "/Title": "The L3 Protocol: Profound Novelty, Volume III",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("An operating manual for the production of profound novelty: "
                     "doctrine, an eight-phase pipeline with gates, LLM operator "
                     "constraints, a backtest against the founding revolutions, "
                     "and the alarms that separate depth from decoration."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
