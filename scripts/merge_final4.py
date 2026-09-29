#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover4.pdf (Playwright) + body4.pdf (ReportLab) into the final
Volume IV deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover4.pdf"
BODY = "/home/z/my-project/scripts/body4.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_IV_Under_Its_Own_Alarms.pdf"


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
        "/Title": "Under Its Own Alarms: Profound Novelty, Volume IV",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("An adversarial audit of the L3 Protocol: each of the six "
                     "alarms of Volume III turned at full strength against the "
                     "protocol that issued it, with verdicts rendered, evidence "
                     "named, and amendments written that demote, derive, "
                     "operationalize, control, and refute rather than add."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
