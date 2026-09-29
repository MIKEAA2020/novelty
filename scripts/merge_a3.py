#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a3.pdf (Playwright) + body_a3.pdf (ReportLab) into the
Amendment A3 deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a3.pdf"
BODY = "/home/z/my-project/scripts/body_a3.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_A3_The_Limit_Case_Derivation.pdf"


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
        "/Title": "The Limit-Case Derivation: Profound Novelty, Amendment A3",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The G5-self limit case computed with named parameters — "
                     "kill cost, verification exposure, corpus radius — the "
                     "protocol degenerating into its inherited chassis, the "
                     "residual inventoried as the operator delta: six items, "
                     "each with its collapse condition and falsifier."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
