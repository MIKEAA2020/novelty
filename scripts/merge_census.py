#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4.pdf (Playwright) + body_census.pdf (ReportLab) into the
Amendment A4 deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4.pdf"
BODY = "/home/z/my-project/scripts/body_census.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_A4_The_Failure_Census.pdf"


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
        "/Title": "The Failure Census: Profound Novelty, Amendment A4",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("Three dead theories — phlogiston, the ether, the epicycle "
                     "tradition — coded against the nine-point signature under a "
                     "pre-registered sampling rule: the amended signature, with "
                     "its discriminators, confounds, and falsifiers."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
