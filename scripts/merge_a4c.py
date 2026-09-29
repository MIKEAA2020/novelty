#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge cover_a4c.pdf (Playwright) + body_a4c.pdf (ReportLab) into the
Amendment A4c deliverable, with A4 normalization and metadata."""

from pypdf import PdfReader, PdfWriter

A4_W, A4_H = 595.28, 841.89

COVER = "/home/z/my-project/scripts/cover_a4c.pdf"
BODY = "/home/z/my-project/scripts/body_a4c.pdf"
OUT = "/home/z/my-project/download/Profound_Novelty_A4c_The_Widened_Census.pdf"


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
        "/Title": "The Widened Census: Profound Novelty, Amendment A4c",
        "/Author": "Z.ai",
        "/Creator": "Z.ai",
        "/Subject": ("The census's extension rule executed — the panel "
                     "widened by the matched pair the rule queued (miasma "
                     "against germ theory) — and the alien-reader clause "
                     "attempted against the genetic-dependence limit: the "
                     "infrastructure refused every request for a different "
                     "model family, the refusal printed as a finding, a "
                     "third blind coding run under a locked pre-registration, "
                     "agreement analysis across five readings, evidence "
                     "adjudication of every contested cell, and a "
                     "replication kit that makes the alien reading "
                     "executable by any true outsider. The amended "
                     "signature: four domain-general discriminators and one "
                     "domain-marked."),
    })
    with open(OUT, "wb") as f:
        writer.write(f)
    n = len(writer.pages)
    print(f"merged: {OUT} ({n} pages)")


if __name__ == "__main__":
    main()
