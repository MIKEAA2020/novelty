#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural TOC verification for Volume VIII (coordinate/font-based): the displayed
TOC entries on the contents page must match the actual chapter start pages,
and the footer page-number sequence must be continuous (i, 1..N)."""

import re
import fitz

PDF = ("/home/z/my-project/novelty/download/"
       "Profound_Novelty_VII_The_Second_Generation.pdf")

doc = fitz.open(PDF)
print(f"pages: {len(doc)}")

# --- 1. Displayed TOC entries (page index 1) ---------------------------
# Extraction order on this page interleaves: number line, then entry line.
raw = [l.strip() for l in doc[1].get_text("text").splitlines() if l.strip()]
entries = []
i = 0
while i < len(raw):
    line = raw[i]
    m = re.match(r"^(\d+)$", line)
    if m and i + 1 < len(raw):
        nxt = raw[i + 1]
        m2 = re.match(r"^(\d)\.\s+(.+)$", nxt)
        if m2:
            entries.append((int(m2.group(1)), m2.group(2), int(m.group(1))))
            i += 2
            continue
    i += 1
print("displayed TOC:", [(n, t[:38], p) for n, t, p in entries])

# --- 2. Actual chapter starts via >17.5pt heading spans ---------------
actual = {}
for i in range(1, len(doc)):
    for block in doc[i].get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for sp in line["spans"]:
                if sp["size"] > 17.5 and sp["text"].strip():
                    m = re.match(r"^(\d)\.\s", sp["text"].strip())
                    if m:
                        n = int(m.group(1))
                        # displayed body numbering = internal page - 1
                        # (internal page 1 is the TOC, printed as roman i)
                        actual.setdefault(n, i - 1)
print("actual chapter starts (displayed numbering):",
      dict(sorted(actual.items())))

ok = True
for n, title, shown in entries:
    real = actual.get(n)
    match = shown == real
    ok = ok and match
    print(f"  ch{n}: shown {shown} vs actual {real} -> "
          f"{'OK' if match else 'MISMATCH'}")

# --- 3. Footer sequence: roman i on TOC page, then 1..N ----------------
def footer_num(page):
    cands = []
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for sp in line["spans"]:
                if sp["bbox"][1] > 795 and re.match(r"^\d+$", sp["text"].strip()):
                    cands.append((sp["bbox"][0], sp["text"].strip()))
    return int(max(cands)[1]) if cands else None

toc_footer = None
for block in doc[1].get_text("dict")["blocks"]:
    for line in block.get("lines", []):
        for sp in line["spans"]:
            if sp["bbox"][1] > 795 and sp["text"].strip() == "i":
                toc_footer = "i"
nums = [footer_num(doc[i]) for i in range(2, len(doc))]
expect = list(range(1, len(nums) + 1))
seq_ok = toc_footer == "i" and nums == expect
print("footer numbers:", toc_footer, nums[:5], "...", nums[-3:])
print("footer sequence continuous:", seq_ok)

print("RESULT:", "PASS" if (ok and entries and seq_ok) else "FAIL")
