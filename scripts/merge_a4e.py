#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4e.pdf (Playwright) + body_a4e.pdf (ReportLab) into the
Amendment A4e deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4e.pdf"
BODY = "/home/z/my-project/scripts/body_a4e.pdf"
OUT = ("/home/z/my-project/download/"
       "Profound_Novelty_A4e_The_Second_Family.pdf")


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
        "/Title": "The Second Family: Profound Novelty, Amendment A4e",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The standing offer accepted twice more: two external "
                     "families read the ten-theory kit and return identical "
                     "verdicts on the seventy-two shared cells; the outgroup "
                     "converges above the family band, the lineage offset "
                     "replicates at 3.5 points with zero inversions, three "
                     "cells move to duals under the pre-registered motion "
                     "rules, and no dead theory passes any discriminator "
                     "under any of the eight readings. The census's error "
                     "bars are its amendments, printed."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
