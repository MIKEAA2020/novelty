# -*- coding: utf-8 -*-
"""Parse and verify the third family's ten-theory matrix from the owner's
repo file "novelty prompt3.txt" (label line: "claude sonnet 5.5:").

The file's PART 1 matrix has 9 rows (P1..P9) and 10 theory columns in the
kit's canonical order (caloric, epi, germ, ether, miasma, newton, phl, qm,
rel, thermo). "S then D" is normalized to SD.

This script transcribes the matrix from the file itself and verifies the
hand transcription used by a4f_stats.py (C10), cell by cell.
"""

import re

SRC = "/home/z/my-project/novelty/novelty prompt3.txt"

CANON = ("caloric", "epi", "germ", "ether", "miasma",
         "newton", "phl", "qm", "rel", "thermo")

# Hand transcription to verify (as used in a4f_stats.py):
HAND = {
    1: ("P", "F", "S", "P", "P", "S", "F", "S", "S", "S"),
    2: ("P", "P", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "P", "F", "P", "F", "S", "S", "P"),
    4: ("P", "F", "P", "P", "P", "S", "F", "S", "S", "S"),
    5: ("P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
    6: ("P", "P", "F", "P", "F", "P", "F", "S", "S", "S"),
    7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("S", "S", "S", "S", "P", "S", "S", "S", "S", "S"),
}


def norm(cell):
    c = cell.strip()
    if c.startswith("S then D"):
        return "SD"
    if c in ("S", "P", "F"):
        return c
    raise ValueError(f"unparseable cell: {c!r}")


def main():
    text = open(SRC, encoding="utf-8").read()
    # The matrix block: lines starting with "| P<n>" after the header row.
    rows = {}
    for line in text.splitlines():
        m = re.match(r"^\|\s*P([1-9])[^|]*\|(.+)\|\s*$", line)
        if m:
            p = int(m.group(1))
            cells = [norm(c) for c in m.group(2).split("|")]
            assert len(cells) == 10, f"P{p}: {len(cells)} cells"
            rows[p] = tuple(cells)
    assert len(rows) == 9, f"found {len(rows)} point rows"

    print("PARSED FROM FILE (claude, T1..T10 =", ", ".join(CANON) + "):")
    for p in range(1, 10):
        print(f"  {p}: {rows[p]},")

    mismatches = 0
    for p in range(1, 10):
        for i, t in enumerate(CANON):
            if rows[p][i] != HAND[p][i]:
                print(f"MISMATCH P{p}/{t}: file {rows[p][i]} vs hand {HAND[p][i]}")
                mismatches += 1
    print()
    if mismatches == 0:
        print("VERIFIED: hand transcription C10 matches the delivered file "
              "on all 90 cells.")
    else:
        print(f"FAILED: {mismatches} mismatches.")
    return 0 if mismatches == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
