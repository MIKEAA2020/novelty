# -*- coding: utf-8 -*-
"""Parse verification for Amendment A4h — the fifth reading (gemini 3.8).

Parses the 'gemini 3.8:' section of the restored 'novelty prompt4.txt'
(832 lines, md5 ab9893a3612e947c4a1ad5bd69f5697c, recovered from git
commit c68fc55) and verifies the 9x12 coding matrix cell by cell against
the GEMINI38 dict in a4h_stats.py. Also verifies the file-level facts the
amendment prints (line counts, section labels, delivery notices).
"""

import hashlib
import re
import sys

sys.path.insert(0, "/home/z/my-project/novelty/scripts")

SRC = "/home/z/my-project/novelty/novelty prompt4.txt"
T12 = ("caloric", "darwin", "epi", "fixity", "germ", "ether",
       "miasma", "newton", "phl", "qm", "rel", "thermo")
POINT_ROWS = {
    "P1": 1, "P2": 2, "P3": 3, "P4": 4, "P5": 5,
    "P6": 6, "P7": 7, "P8": 8, "P9": 9,
}

raw = open(SRC, encoding="utf-8").read()
lines = raw.splitlines()
print(f"file: {len(lines)} lines, md5 "
      f"{hashlib.md5(raw.encode()).hexdigest()}")

# --- file-level facts -------------------------------------------------------
labels = [ln.rstrip(":") for ln in lines if re.match(
    r"^(deepseek|opus inline|opus a4f_alien_coding_12\.md|gemini 3\.1 pro "
    r"preview|gemini 3\.8):$", ln)]
print("section labels:", labels)
assert labels == ["deepseek", "opus inline", "opus a4f_alien_coding_12.md",
                  "gemini 3.1 pro preview", "gemini 3.8"], labels
g38_start = next(i for i, ln in enumerate(lines)
                 if ln == "gemini 3.8:") + 1
g38 = lines[g38_start:]
print(f"gemini 3.8 section: {len(g38)} lines "
      f"(file lines {g38_start + 1}-{len(lines)})")

# tool-availability notice in the kit's demanded form
notice = next(ln for ln in g38 if "Write" in ln and "tool" in ln)
print("notice:", notice.strip()[:100])
assert "No" in notice and "Write" in notice and "tool" in notice

# --- the matrix -------------------------------------------------------------
hdr_idx = next(i for i, ln in enumerate(g38) if ln.startswith("| Point"))
col_heads = [c.strip() for c in g38[hdr_idx].strip("|").split("|")]
print("matrix columns:", col_heads)
assert len(col_heads) == 13, col_heads

parsed = {}
for ln in g38[hdr_idx + 2:hdr_idx + 11]:
    cells = [c.strip() for c in ln.strip("|").split("|")]
    pname = cells[0].replace("*", "").split()[0]   # e.g. "P1"
    assert pname in POINT_ROWS, cells[0]
    codes = []
    for c in cells[1:]:
        m = re.match(r"^(S then D|S|P|F)$", c.replace("·", " ").strip())
        assert m, (pname, c)
        codes.append("SD" if c == "S then D" else c)
    assert len(codes) == 12, (pname, codes)
    parsed[POINT_ROWS[pname]] = codes

# theory order from the header columns (T1..T12 positionally)
assert len(parsed) == 9

# --- verify against a4h_stats.GEMINI38 --------------------------------------
import a4h_stats as S                                     # noqa: E402

mismatches = 0
for i, t in enumerate(T12):
    for p in range(1, 10):
        file_cell = parsed[p][i]
        dict_cell = S.GEMINI38[t][p - 1]
        if file_cell != dict_cell:
            mismatches += 1
            print(f"MISMATCH {t} P{p}: file {file_cell} vs dict {dict_cell}")
print(f"matrix verification: {108 - mismatches}/108 cells match"
      + (" — ALL MATCH" if mismatches == 0 else " — FIX REQUIRED"))

# --- the ether line, both gemini versions, for the drift table --------------
print("\nether line: 3.1 -> 3.8 (census)")
for p in range(1, 10):
    print(f"  P{p}: {S.GEMINI31['ether'][p-1]:<4}"
          f"{S.GEMINI38['ether'][p-1]:<4}{S.CENSUS['ether'][p-1]}")

print("\nPARSE VERIFICATION:", "PASS" if mismatches == 0 else "FAIL")
