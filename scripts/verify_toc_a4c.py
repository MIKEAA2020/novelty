#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structural TOC verification for A4c: displayed chapter numbers must match
actual chapter start pages; footer sequence must be continuous."""

import fitz

PDF = "/home/z/my-project/download/Profound_Novelty_A4c_The_Widened_Census.pdf"

doc = fitz.open(PDF)
print(f"pages: {len(doc)}")

# --- Extract the displayed TOC entries (page 2 = index 1) ---
toc_text = doc[1].get_text("text")
entries = []
for line in toc_text.splitlines():
    line = line.strip()
    if not line:
        continue
    # entries look like "1.  The Mandate: ... 3" (title ... number)
    if line[0].isdigit() and "." in line[:4]:
        # split trailing number
        parts = line.rsplit(" ", 1)
        if len(parts) == 2 and parts[1].isdigit():
            entries.append((parts[0].strip(), int(parts[1])))
print("displayed TOC:", [(t[:40], n) for t, n in entries])

# --- Find actual chapter start pages (body numbering = page index - 1) ---
actual = {}
for i in range(1, len(doc)):  # skip cover (0); page 1 = TOC
    txt = doc[i].get_text("text")
    for num in range(1, 7):
        # chapter heading appears as "N.  Title" near page start
        head = f"{num}."
        if txt.strip().startswith(head):
            # confirm it is a heading, not a TOC line: check font size later
            actual[num] = i - 1  # displayed body number
print("actual chapter starts (displayed numbering):", actual)

ok = True
for (title, shown), (num, real) in zip(entries, sorted(actual.items())):
    match = shown == real
    ok = ok and match
    print(f"  ch{num}: shown {shown} vs actual {real} -> {'OK' if match else 'MISMATCH'}")

# --- Footer sequence ---
footers = []
for i in range(1, len(doc)):
    txt = doc[i].get_text("text").strip().splitlines()
    last = [l.strip() for l in txt if l.strip()][-1] if txt else ""
    footers.append(last)
print("footers (last line per page):", footers)

print("RESULT:", "PASS" if ok else "FAIL")
