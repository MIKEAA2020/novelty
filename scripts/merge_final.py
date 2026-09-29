#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover.pdf (Playwright) + body.pdf (ReportLab) into the final deliverable."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover.pdf"
BODY = "/home/z/my-project/scripts/body.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_A_Study_by_Example.pdf"


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
        "/Title": "Profound Novelty: A Study by Example",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("A comparative study of profound novelty, read through the state of "
                     "physics before and after Newton, Einstein, and the quantum."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
