#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4f.pdf (Playwright) + body_a4f.pdf (ReportLab) into the
Amendment A4f deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4f.pdf"
BODY = "/home/z/my-project/scripts/body_a4f.pdf"
OUT = ("/home/z/my-project/download/"
       "Profound_Novelty_A4f_The_Third_Family_and_the_Sixth_Pair.pdf")


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
        "/Title": ("The Third Family and the Sixth Pair: Profound Novelty, "
                   "Amendment A4f"),
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The standing offer accepted a third time: the "
                     "ten-theory kit administered externally to a reader "
                     "labeled claude sonnet 5.5, verified cell for cell "
                     "against the delivery — the first external family not "
                     "to converge cell for cell with the first (86.7 "
                     "percent), and the first to land inside the family "
                     "band (88.0-89.8). The extension rule executes again: "
                     "the fixity of species admitted as the sixth dead "
                     "theory against Darwinian selection, three weapons "
                     "forged inside the dead program, the barnacle years "
                     "the census's most intimate weapon. Both new readings "
                     "score 90.0 percent against the amended census, the "
                     "highest yet. An A4e erratum is found, paid, and "
                     "corrected; three cells move against the author's own "
                     "pre-registration; the census stands at twelve "
                     "theories, ten readings, six duals, no killing clause "
                     "fired."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
