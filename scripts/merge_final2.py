#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover2.pdf (Playwright) + body2.pdf (ReportLab) into the final Volume II
deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover2.pdf"
BODY = "/home/z/my-project/scripts/body2.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_II_The_Conditions_of_Depth.pdf"


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
        "/Title": "The Conditions of Depth: Profound Novelty, Volume II",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("A general theory of profound novelty: the necessary conditions, "
                     "the recurring patterns, and the common signature shared by the "
                     "major scientific breakthroughs."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
