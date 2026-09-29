#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4d.pdf (Playwright) + body_a4d.pdf (ReportLab) into the
Amendment A4d deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4d.pdf"
BODY = "/home/z/my-project/scripts/body_a4d.pdf"
OUT = ("/home/z/my-project/download/"
       "Profound_Novelty_A4d_The_Alien_Reading_Executed.pdf")


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
        "/Title": "The Alien Reading, Executed: Profound Novelty, Amendment A4d",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The standing offer accepted: the replication kit's "
                     "verbatim blind-coding prompt administered outside this "
                     "environment on a reader of a different model family, "
                     "the reading returned through the owner's repository, "
                     "and the genetic-dependence limit broken as an "
                     "availability fact and measured — 3.3 points below the "
                     "family band, zero inversions, every disagreement on a "
                     "cell the census had already marked elastic. Executed "
                     "alongside it, the fifth matched pair the extension "
                     "rule queued (caloric against thermodynamics), admitted "
                     "under CR-1..CR-4, pre-registered before a fourth blind "
                     "coding ran the widened ten-theory panel, and adjudicated "
                     "under the pre-registered motion rules: three cells "
                     "move, the alien's vote among the movers each time. The "
                     "kit re-issues at ten theories."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
