# -*- coding: utf-8 -*-
"""Parse the two alien readings from the owner's repo file
"novelty prompt2.txt" (gpt: ten-theory panel; grok: ten-theory panel)
into canonical form and verify the transcription used by a4e_stats.py.

Canonical panel order (alphabetical, as presented to the coders):
  caloric, epi, germ, ether, miasma, newton, phl, qm, rel, thermo
"""

import re
import sys

SRC = "/home/z/my-project/novelty/novelty prompt2.txt"

CANON = ["caloric", "epi", "germ", "ether", "miasma",
         "newton", "phl", "qm", "rel", "thermo"]

# theory headers as they appear in the file's Part 2 sections
THEORY_HEADERS = {
    "T1": "caloric", "T2": "epi", "T3": "germ", "T4": "ether",
    "T5": "miasma", "T6": "newton", "T7": "phl", "T8": "qm",
    "T9": "rel", "T10": "thermo",
}

POINT_ROWS = [
    ("P1", 1), ("P2", 2), ("P3", 3), ("P4", 4), ("P5", 5),
    ("P6", 6), ("P7", 7), ("P8", 8), ("P9", 9),
]


def parse_reader(text, label):
    """Extract the 9x10 matrix for one reader's Part 1 table."""
    # find the section starting with the label
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if ln.strip().rstrip(":").lower() == label.rstrip(":").lower():
            start = i
            break
    if start is None:
        raise SystemExit(f"reader label {label!r} not found")
    # find the matrix table (the first table after the label)
    rows = {}
    for ln in lines[start:]:
        s = ln.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) != 11:
            continue
        head = cells[0]
        m = re.match(r"^(P[1-9])\s*[·.]", head)
        if not m:
            continue
        pnum = int(m.group(1)[1])
        vals = []
        for c in cells[1:]:
            c = c.replace("S then D", "SD").replace("then", "").strip()
            c = c.upper()
            if c not in ("S", "P", "F", "SD"):
                raise SystemExit(f"bad cell {c!r} in row {head!r} of {label}")
            vals.append(c)
        if len(vals) != 10:
            raise SystemExit(f"row {head!r} of {label} has {len(vals)} cells")
        rows[pnum] = vals
        if len(rows) == 9:
            break
    if len(rows) != 9:
        raise SystemExit(f"{label}: only {len(rows)} rows parsed")
    # order check: the file's columns are T1..T10 = CANON already
    return {p: tuple(rows[p]) for p in range(1, 10)}


def main():
    text = open(SRC, encoding="utf-8").read()
    gpt = parse_reader(text, "gpt:")
    grok = parse_reader(text, "grok:")
    print("GPT-10  (caloric epi germ ether miasma newton phl qm rel thermo)")
    for p in range(1, 10):
        print(f"  P{p}: " + " ".join(f"{v:>2}" for v in gpt[p]))
    print("\nGROK-10 (caloric epi germ ether miasma newton phl qm rel thermo)")
    for p in range(1, 10):
        print(f"  P{p}: " + " ".join(f"{v:>2}" for v in grok[p]))

    # cross-check against the hand transcription
    HAND_GPT = {
        1: ("P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
        2: ("P", "P", "P", "S", "F", "S", "S", "S", "S", "S"),
        3: ("F", "F", "F", "P", "F", "S", "F", "S", "S", "P"),
        4: ("P", "P", "P", "S", "F", "S", "P", "S", "S", "S"),
        5: ("F", "P", "P", "P", "F", "S", "P", "S", "S", "P"),
        6: ("P", "P", "P", "P", "F", "P", "P", "S", "S", "P"),
        7: ("P", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
        8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
        9: ("P", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
    }
    HAND_GROK = {
        1: ("P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
        2: ("P", "P", "P", "S", "F", "S", "S", "S", "S", "S"),
        3: ("F", "F", "F", "P", "F", "S", "F", "S", "S", "F"),
        4: ("P", "P", "P", "S", "F", "S", "P", "S", "S", "P"),
        5: ("F", "P", "P", "P", "F", "S", "P", "S", "S", "P"),
        6: ("P", "P", "P", "P", "F", "P", "P", "S", "S", "S"),
        7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
        8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
        9: ("P", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
    }
    ok = True
    for p in range(1, 10):
        if gpt[p] != HAND_GPT[p]:
            ok = False
            print(f"\nMISMATCH gpt P{p}: parsed {gpt[p]} vs hand {HAND_GPT[p]}")
        if grok[p] != HAND_GROK[p]:
            ok = False
            print(f"\nMISMATCH grok P{p}: parsed {grok[p]} vs hand {HAND_GROK[p]}")
    print("\nTRANSCRIPTION VERIFIED" if ok else "\nFIX NEEDED")

    # where do the two aliens differ from each other?
    print("\nAlien-vs-alien differing cells:")
    n = 0
    for p in range(1, 10):
        for t, i in zip(CANON, range(10)):
            if gpt[p][i] != grok[p][i]:
                n += 1
                print(f"  P{p}/{t}: gpt {gpt[p][i]} vs grok {grok[p][i]}")
    print(f"  total {n}/90")


if __name__ == "__main__":
    main()
