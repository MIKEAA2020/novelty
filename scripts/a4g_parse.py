# -*- coding: utf-8 -*-
"""Parse and verify the FOURTH delivery's matrices from the owner's repo file
"novelty prompt4.txt" — the first multi-family delivery: three readers
(labeled deepseek, opus, gemini 3.1 pro preview), each returning the
twelve-theory kit's full output. Opus delivered its output TWICE — once
inline, once as its own saved file (a4f_alien_coding_12.md) — and states
the two deliveries are identical; this script verifies that claim too.

Column order (the kit's T12 order, alphabetical):
  caloric, darwin, epi, fixity, germ, ether, miasma, newton, phl,
  qm, rel, thermo.
"S then D" is normalized to SD.

This script transcribes the matrices from the file itself and verifies
the hand transcriptions used by a4g_stats.py (D12, O12, G12), cell by
cell.
"""

import re

SRC = "/home/z/my-project/novelty/novelty prompt4.txt"

CANON = ("caloric", "darwin", "epi", "fixity", "germ", "ether",
         "miasma", "newton", "phl", "qm", "rel", "thermo")

# Hand transcriptions to verify (as used in a4g_stats.py):

# deepseek (T1..T12 in kit order)
DEEPSEEK = {
    1: ("P", "S", "F", "F", "S", "F", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "F", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("P", "S", "P", "F", "F", "P", "F", "S", "P", "S", "S", "P"),
    5: ("F", "P", "F", "F", "F", "F", "F", "S", "F", "S", "S", "S"),
    6: ("S", "F", "P", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    7: ("F", "S", "F", "F", "P", "F", "F", "S", "P", "S", "S", "P"),
    8: ("SD", "S", "SD", "P", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "F", "S", "S", "F", "S", "P", "S", "S", "S"),
}

# opus (inline delivery; the file delivery is stated identical and is
# verified against this one)
OPUS = {
    1: ("P", "S", "P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
    2: ("P", "S", "P", "P", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "P", "F", "P", "F", "S", "S", "P"),
    4: ("P", "S", "P", "P", "F", "S", "F", "S", "P", "P", "S", "S"),
    5: ("F", "P", "P", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "P", "P", "F", "F", "P", "F", "P", "P", "S", "S", "S"),
    7: ("F", "S", "P", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
}

# gemini 3.1 pro preview
GEMINI = {
    1: ("F", "S", "F", "F", "S", "S", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "F", "S", "S", "F", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    4: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "P"),
    5: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "F", "F", "F", "F", "P", "F", "F", "F", "S", "S", "S"),
    7: ("F", "S", "P", "F", "F", "F", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "S", "P", "P", "S", "F", "S", "P", "S", "S", "S"),
}


def norm(cell):
    c = cell.strip().strip("*").strip()
    if c.startswith("S then D"):
        return "SD"
    if c in ("S", "P", "F"):
        return c
    raise ValueError(f"unparseable cell: {c!r}")


def split_sections(text):
    """Return {label: section_text} for the four labeled sections."""
    marks = [
        ("deepseek", re.compile(r"(?m)^deepseek:\s*$")),
        ("opus_inline", re.compile(r"(?m)^opus inline:\s*$")),
        ("opus_file", re.compile(r"(?m)^opus a4f_alien_coding_12\.md:\s*$")),
        ("gemini", re.compile(r"(?m)^gemini 3\.1 pro preview:\s*$")),
    ]
    bounds = []
    for label, rx in marks:
        m = rx.search(text)
        assert m, f"section marker not found: {label}"
        bounds.append((m.start(), m.end(), label))
    bounds.sort()
    out = {}
    for i, (s, e, label) in enumerate(bounds):
        end = bounds[i + 1][0] if i + 1 < len(bounds) else len(text)
        out[label] = text[e:end]
    return out


def parse_matrix(section):
    """Extract the 9x12 matrix from a section's FIRST 'PART 1' block."""
    rows = {}
    for line in section.splitlines():
        m = re.match(r"^\|\s*\**P([1-9])[^|]*\|(.+)\|\s*$", line)
        if m:
            p = int(m.group(1))
            cells = [norm(c) for c in m.group(2).split("|")]
            assert len(cells) == 12, f"P{p}: {len(cells)} cells -> {cells}"
            rows[p] = tuple(cells)
    assert len(rows) == 9, f"found {len(rows)} point rows"
    return rows


def main():
    text = open(SRC, encoding="utf-8").read()
    secs = split_sections(text)

    parsed = {k: parse_matrix(v) for k, v in secs.items()}

    names = {"deepseek": "DEEPSEEK", "opus_inline": "OPUS",
             "gemini": "GEMINI"}
    hand = {"DEEPSEEK": DEEPSEEK, "OPUS": OPUS, "GEMINI": GEMINI}

    total_bad = 0
    for sec, var in names.items():
        print(f"PARSED FROM FILE ({sec}, T1..T12 = "
              f"{', '.join(CANON)}):")
        for p in range(1, 10):
            print(f"  {p}: {parsed[sec][p]},")
        mism = 0
        for p in range(1, 10):
            for i, t in enumerate(CANON):
                if parsed[sec][p][i] != hand[var][p][i]:
                    print(f"MISMATCH P{p}/{t}: file "
                          f"{parsed[sec][p][i]} vs hand "
                          f"{hand[var][p][i]}")
                    mism += 1
        print(f"  -> {var}: "
              f"{'VERIFIED, 0 mismatches on 108 cells' if mism == 0 else str(mism) + ' MISMATCHES'}\n")
        total_bad += mism

    # The opus double-delivery identity claim.
    same = all(parsed["opus_inline"][p] == parsed["opus_file"][p]
               for p in range(1, 10))
    print("OPUS DOUBLE DELIVERY (inline vs saved file "
          "a4f_alien_coding_12.md): " +
          ("IDENTICAL on all 108 cells — the reader's own identity "
           "claim VERIFIED." if same else "DIFFER — see above."))

    return 0 if (total_bad == 0 and same) else 1


if __name__ == "__main__":
    raise SystemExit(main())
