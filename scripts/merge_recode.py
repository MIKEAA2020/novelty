#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4b.pdf (Playwright) + body_recode.pdf (ReportLab) into the
Amendment A4b deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4b.pdf"
BODY = "/home/z/my-project/scripts/body_recode.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_A4b_The_Independent_Recoding.pdf"


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
        "/Title": "The Independent Recoding: Profound Novelty, Amendment A4b",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The census's third falsifier executed: two blind "
                     "codings of six theories against the nine-point "
                     "signature, cell-by-cell agreement analysis, evidence "
                     "adjudication of every contested cell, and the amended "
                     "instrument — smaller, harder, and no longer only the "
                     "author's."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
