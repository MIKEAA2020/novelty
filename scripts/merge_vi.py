#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the Volume VI cover (html2poster.js output, 794px) with the body
PDF (ReportLab A4) into the final deliverable, normalizing page sizes to
A4."""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

COVER = "/home/z/my-project/novelty/scripts/cover_vi.pdf"
BODY = "/home/z/my-project/scripts/body_vi.pdf"
OUT = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_VI_The_First_Generation.pdf")

A4_W, A4_H = 595.2755905511812, 841.8897637795277

writer = PdfWriter()
cover = PdfReader(COVER)
for page in cover.pages:
    # 794 px at 72 dpi -> 595.5 pt; scale to exact A4
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    sx, sy = A4_W / w, A4_H / h
    page.scale(sx, sy)
    page.mediabox = RectangleObject((0, 0, A4_W, A4_H))
    writer.add_page(page)

body = PdfReader(BODY)
for page in body.pages:
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    if abs(w - A4_W) > 0.2 or abs(h - A4_H) > 0.2:
        sx, sy = A4_W / w, A4_H / h
        page.scale(sx, sy)
        page.mediabox = RectangleObject((0, 0, A4_W, A4_H))
    writer.add_page(page)

writer.add_metadata({
    "/Title": ("The First Generation: Profound Novelty, Volume VI — The "
               "Run for Ourselves"),
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": ("The operators' first generative deployment. The owner "
                 "ordered the switch from audit to discovery: make the "
                 "discoveries ourselves, stop waiting. Generator mode "
                 "opens on the fresh Volume V census of the dark sector: "
                 "twelve candidate moves pre-named before any occupation "
                 "search, five kill rules locked, the honest-kill "
                 "commitment printed in advance. Twelve moves, twelve "
                 "kills — the map of occupied territory, occupiers named, "
                 "the flagship (the causal coincidence a0(z) tracking "
                 "cH0/2pi) killed on every face: theory (Del Popolo "
                 "2024), test (MUSE-DARK, REBELS-25 at z = 7.31), first "
                 "contested results (a claimed ~30 sigma a0 evolution, "
                 "reexamined; LambdaCDM simulations printing only modest "
                 "drift). What survives is not a theory but a "
                 "registration: the dated three-way fork on the "
                 "unspeakable core — knee tracks H(z), knee constant, no "
                 "universal relation — with kill conditions pre-committed "
                 "for all sides and harshest for ours, resolving 2026-"
                 "2031 alongside the carried registrations (DESI DR3, "
                 "Euclid, Gaia DR4, the neutrino floor, CMB-S4) and the "
                 "new conjunction cell. Zero verdicts: registrations are "
                 "not verdicts, and if a cell survives, the series claims "
                 "exactly the surviving cell — and nothing more."),
})

with open(OUT, "wb") as f:
    writer.write(f)
print(f"merged: {OUT} ({len(writer.pages)} pages)")
