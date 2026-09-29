#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover3_v11.pdf (Playwright) + body_v11.pdf (ReportLab) into the
Volume III v1.1 deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover3_v11.pdf"
BODY = "/home/z/my-project/scripts/body_v11.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_III_The_L3_Protocol_v1.1.pdf"


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
        "/Title": "The L3 Protocol: Profound Novelty, Volume III — Version 1.1",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The operating manual reissued under its own six alarms: "
                     "chassis printed, numbers made parameters, the G5-self "
                     "limit derived, the failure census executed, refutation "
                     "clauses armed, primitives measured. The claim is the "
                     "operator delta."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
