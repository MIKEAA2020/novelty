#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the Volume VII cover (html2poster.js output, 794px) with the body
PDF (ReportLab A4) into the final deliverable, normalizing page sizes to
A4."""

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

COVER = "/home/z/my-project/novelty/scripts/cover_vii.pdf"
BODY = "/home/z/my-project/scripts/body_vii.pdf"
OUT = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_VII_The_Second_Generation.pdf")

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
    "/Title": ("The Second Generation: Profound Novelty, Volume VII — The "
               "Generator Changed"),
    "/Author": "Z.ai",
    "/Creator": "Z.ai",
    "/Subject": ("The operators' second generative deployment, on the same "
                 "site as a controlled test. The situation report verified: "
                 "the first generation's twelve moves all died to occupation "
                 "because they were drawn from the census — the field's "
                 "stated walls, each with a rival camped on its deletion. "
                 "The generator changes: three lattices outside the census "
                 "(the unstated-assumption lattice, the far-domain import "
                 "lattice, the old-math lattice), and the unit of novelty "
                 "changes from the idea to the signature — the discriminating "
                 "statistic computable on named data. Twelve moves pre-named "
                 "in a pre-registration locked and pushed before any search "
                 "ran, with six kill rules (two new: no data termination, "
                 "absorption by a standing registration). Twenty-two queries "
                 "logged verbatim, seven degraded. Eight kills with occupiers "
                 "named — the bar dynamometer killed by the field's own "
                 "fast-bar tension (Fragkoudi et al. 2021), the cosmic-web "
                 "spectrum killed by the persistent-homology family — and "
                 "four bounded survivors converging on one unstated "
                 "assumption: the dark sector's gravitational response to "
                 "baryons is treated as instantaneous and memoryless by "
                 "every static fit ever run. The registrations: the response "
                 "fork (immediate and monotone, lagged and ringing, or "
                 "absent with the law algebraic) with kill conditions on all "
                 "sides, ours harshest, resolvable on archival data now and "
                 "scheduled data through 2031, the field's fast-bar tension "
                 "carried in as its first line of evidence; the residual "
                 "census with its 2.2-percent floor computed and five probes "
                 "pre-registered, executable by anyone on public tables; and "
                 "the analyticity check on the medium families' published "
                 "susceptibilities. Consciousness carried with an honest "
                 "pre-read: it fails the site criterion's dated-data clause "
                 "as it stands. Zero verdicts: registrations are not "
                 "verdicts, and if a cell survives, the series claims "
                 "exactly the surviving cell — and nothing more."),
})

with open(OUT, "wb") as f:
    writer.write(f)
print(f"merged: {OUT} ({len(writer.pages)} pages)")
