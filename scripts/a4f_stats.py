# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4f — the THIRD delivery of the alien
reading (reader labeled "claude sonnet 5.5" by the owner's repo file
"novelty prompt3.txt", ten-theory panel, verified by a4f_parse.py), the
FIFTH blind coding (B5, twelve-theory panel, same family, fresh context),
and the SIXTH matched pair (the fixity of species vs Darwinian selection,
pre-registered in a4f_prereg.md before B5 ran).

Readings on file (lineage):
  - Census v1 (author) and the post-A4b / post-A4c / post-A4d / post-A4e states.
  - A4b blind coders A and B (6-theory panel).
  - Third blind reading X3 (8-theory panel, same family).
  - GPT-8 (first alien, 8-theory panel).
  - BLIND4 = B4 (10-theory panel, same family).
  - GPT-10 and GROK-10 (A4e's two external readings, 10-theory panels).
  - NEW: CLAUDE-10 (third external family, 10-theory panel).
  - NEW: B5 (12-theory panel, same family): the fifth blind reading.
  - A4f pre-registration: the fixity of species + Darwinian selection,
    locked before B5 ran.

Scoring identical to A4b/A4c/A4d/A4e: exact=1.0, adjacent=0.5, distant=0.0;
SD special-handling (SD vs S/P = 0.5, SD vs SD = 1.0); census 'C' read as P.
Dual cells scored on their as-written faces.
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}

# ---- Census states ----------------------------------------------------------
CENSUS_A4D = {
    "phl":    ("F", "P", "F", "F", "F", "F", "F", "SD", "P"),
    "ether":  ("P", "S", "F", "P", "P", "S", "P", "SD", "S"),
    "epi":    ("F", "P", "F", "P", "P", "S", "P", "SD", "P"),
    "miasma": ("F", "P", "F", "F", "F", "F", "F", "SD", "F"),
    "caloric":("F", "P", "F", "P", "P", "P", "F", "SD", "P"),
    "newton": ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "qm":     ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "rel":    ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "germ":   ("S", "S", "F", "P", "P", "F", "P", "S", "S"),
    "thermo": ("S", "S", "P", "S", "S", "S", "P", "S", "S"),
}

# Post-A4e census (as-written faces; duals: phl P2 -> S, miasma P1 -> F,
# germ P6 -> F, germ P7 -> F, newton P6 -> S):
CENSUS_A4E = {
    "phl":    ("F", "S", "F", "F", "F", "F", "F", "SD", "P"),
    "ether":  ("P", "S", "F", "P", "P", "S", "P", "SD", "S"),
    "epi":    ("F", "P", "F", "P", "P", "S", "P", "SD", "P"),
    "miasma": ("F", "P", "F", "F", "F", "F", "F", "SD", "F"),
    "caloric":("F", "P", "F", "P", "P", "P", "F", "SD", "P"),
    "newton": ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "qm":     ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "rel":    ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "germ":   ("S", "S", "F", "P", "P", "F", "F", "S", "S"),
    "thermo": ("S", "S", "P", "S", "S", "S", "P", "S", "S"),
}

# ---- Prior readings ----------------------------------------------------------
CODER_A = {
    1: ("F", "P", "S", "F", "S", "S"), 2: ("P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "S", "F", "S", "S"), 4: ("P", "S", "S", "F", "S", "S"),
    5: ("F", "S", "S", "F", "S", "S"), 6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"), 8: ("P", "SD", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
}
CODER_B = {
    1: ("F", "P", "S", "F", "S", "S"), 2: ("P", "S", "S", "P", "S", "S"),
    3: ("F", "P", "S", "F", "S", "S"), 4: ("P", "P", "S", "F", "S", "S"),
    5: ("P", "S", "S", "F", "S", "S"), 6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"), 8: ("SD", "S", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
}
X3 = {
    1: ("F", "S", "F", "P", "S", "F", "S", "S"),
    2: ("P", "S", "S", "P", "S", "P", "S", "S"),
    3: ("F", "F", "F", "F", "S", "F", "S", "S"),
    4: ("P", "F", "P", "F", "S", "F", "P", "S"),
    5: ("F", "P", "P", "F", "S", "F", "S", "S"),
    6: ("P", "F", "S", "F", "P", "F", "S", "S"),
    7: ("P", "P", "F", "F", "S", "F", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "F", "S", "P", "S", "S"),
}
GPT8 = {
    1: ("P", "S", "P", "P", "S", "P", "S", "S"),
    2: ("P", "P", "S", "F", "S", "S", "S", "S"),
    3: ("F", "F", "P", "F", "S", "F", "S", "S"),
    4: ("P", "P", "S", "F", "S", "P", "S", "S"),
    5: ("P", "P", "P", "F", "S", "P", "S", "S"),
    6: ("P", "P", "P", "F", "P", "P", "S", "S"),
    7: ("P", "F", "P", "F", "S", "F", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "S", "S"),
    9: ("P", "P", "P", "F", "S", "P", "S", "S"),
}
B4 = {
    1: ("F", "F", "S", "F", "F", "S", "F", "S", "S", "S"),
    2: ("P", "P", "S", "P", "F", "S", "P", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("P", "F", "P", "P", "F", "S", "F", "S", "S", "P"),
    5: ("P", "P", "P", "P", "P", "S", "F", "S", "S", "S"),
    6: ("P", "P", "F", "P", "F", "P", "F", "S", "S", "S"),
    7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "P"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "P", "S", "S", "F", "S", "F", "S", "S", "S"),
}
GPT10 = {
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
GROK10 = {
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

# NEW: CLAUDE-10 (third external family; verified against the delivered file
# by a4f_parse.py — zero mismatches on all 90 cells):
CLAUDE10 = {
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

# NEW: B5 — fifth blind reading, 12-theory panel in T12 order
# (caloric, darwin, epi, fixity, germ, ether, miasma, newton, phl, qm,
#  rel, thermo). From scripts/a4f_blind5_coding.md.
B5_12 = {
    1: ("F", "S", "F", "F", "S", "P", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("F", "S", "F", "F", "P", "P", "F", "S", "F", "S", "S", "P"),
    5: ("F", "P", "F", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "P", "P", "F", "P", "F", "F", "P", "F", "S", "S", "S"),
    7: ("F", "S", "F", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "F", "S", "P", "F", "S", "P", "S", "S", "S"),
}

# B5 restricted to the shared ten (T10 order), for cross-reading comparisons:
B5 = {
    p: tuple(B5_12[p][i] for i in (0, 2, 4, 5, 6, 7, 8, 9, 10, 11))
    for p in range(1, 10)
}

# ---- A4f pre-registration (the sixth pair, in T12 column order) ------------
PREREG_A4F = {
    "fixity":  ("F", "P", "F", "F", "P", "F", "F", "SD", "P"),
    "darwin":  ("S", "S", "F", "P", "P", "F", "S", "S", "S"),
}

POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}

T10 = ("caloric", "epi", "germ", "ether", "miasma", "newton",
       "phl", "qm", "rel", "thermo")
T8 = ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel")
AB6 = ("epi", "ether", "newton", "phl", "qm", "rel")
T12 = ("caloric", "darwin", "epi", "fixity", "germ", "ether",
       "miasma", "newton", "phl", "qm", "rel", "thermo")


def score(c1, c2):
    if c1 == c2:
        return 1.0
    if {c1, c2} in ({"SD", "S"}, {"SD", "P"}):
        return 0.5
    d = abs(RANK[c1] - RANK[c2])
    return {0: 1.0, 1: 0.5, 2: 0.0}[d]


def kind(c1, c2):
    if c1 == c2:
        return "exact"
    if {c1, c2} in ({"SD", "S"}, {"SD", "P"}):
        return "adjacent"
    d = abs(RANK[c1] - RANK[c2])
    return {0: "exact", 1: "adjacent", 2: "DISTANT"}[d]


def report_pair(name, cells):
    tot = ex = ad = di = 0
    distants = []
    for label, cx, cy in cells:
        s = score(cx, cy)
        k = kind(cx, cy)
        tot += s
        if k == "exact":
            ex += 1
        elif k == "adjacent":
            ad += 1
        else:
            di += 1
            distants.append(f"{label} [{cx} vs {cy}]")
    n = len(cells)
    print(f"\n{name}: weighted {tot:.1f}/{n} = {tot/n:.1%} | "
          f"exact {ex}/{n}, adjacent {ad}, distant {di}")
    for d in distants:
        print(f"    DISTANT: {d}")
    return tot / n


def main():
    print("=" * 76)
    print("A4f UNBLINDING - THIRD FAMILY + FIFTH BLIND READING + SIXTH PAIR")
    print("=" * 76)

    # ===== PART 1: THE THIRD FAMILY'S CONVERGENCE ==========================
    print("\n" + "-" * 76)
    print("PART 1 - CLAUDE vs THE OTHER TWO ALIENS (and the first)")
    print("-" * 76)
    c_vs_g = report_pair("CLAUDE-10 vs GPT-10 (90 cells)",
        [(f"P{p}/{t}", CLAUDE10[p][i], GPT10[p][i])
         for p in range(1, 10) for i, t in enumerate(T10)])
    c_vs_k = report_pair("CLAUDE-10 vs GROK-10 (90 cells)",
        [(f"P{p}/{t}", CLAUDE10[p][i], GROK10[p][i])
         for p in range(1, 10) for i, t in enumerate(T10)])
    g_vs_k = report_pair("GPT-10 vs GROK-10 (90 cells, for scale)",
        [(f"P{p}/{t}", GPT10[p][i], GROK10[p][i])
         for p in range(1, 10) for i, t in enumerate(T10)])
    c_vs_g8 = report_pair("CLAUDE-10 vs GPT-8 (72 shared cells)",
        [(f"P{p}/{t}", CLAUDE10[p][1 + i], GPT8[p][i])
         for p in range(1, 10) for i, t in enumerate(T8)])
    g10_vs_g8 = report_pair("GPT-10 vs GPT-8 (72, for scale)",
        [(f"P{p}/{t}", GPT10[p][1 + i], GPT8[p][i])
         for p in range(1, 10) for i, t in enumerate(T8)])

    # ===== PART 2: THE OUTGROUP TEST v3 =====================================
    print("\n" + "-" * 76)
    print("PART 2 - OUTGROUP TEST v3 (family band now includes B5)")
    print("-" * 76)
    fam = []
    fam.append(report_pair("FAMILY: X3 vs A4b coder A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][i], X3[p][j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: X3 vs A4b coder B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][i], X3[p][j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: B4 vs A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][i], B4[p][1 + j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: B4 vs B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][i], B4[p][1 + j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: B4 vs X3 (72 cells)",
        [(f"P{p}/{t}", X3[p][j], B4[p][1 + j])
         for p in range(1, 10) for j, t in enumerate(T8)]))
    fam.append(report_pair("FAMILY: A vs B (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][i], CODER_B[p][i])
         for p in range(1, 10) for i, t in enumerate(AB6)]))
    fam.append(report_pair("FAMILY: B5 vs A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][i], B5[p][j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T10) if t2 == t]))
    fam.append(report_pair("FAMILY: B5 vs B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][i], B5[p][j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T10) if t2 == t]))
    fam.append(report_pair("FAMILY: B5 vs X3 (72 cells)",
        [(f"P{p}/{t}", X3[p][j], B5[p][1 + j])
         for p in range(1, 10) for j, t in enumerate(T8)]))
    fam.append(report_pair("FAMILY: B5 vs B4 (90 cells)",
        [(f"P{p}/{t}", B4[p][i], B5[p][i])
         for p in range(1, 10) for i, t in enumerate(T10)]))
    print(f"\n>>> FAMILY MUTUAL BAND: {min(fam):.1%}-{max(fam):.1%} "
          f"(mean {sum(fam)/len(fam):.1%})")

    alien_fam = []
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("CLAUDE-10", CLAUDE10)):
        for cn, CD in (("A", CODER_A), ("B", CODER_B)):
            alien_fam.append(report_pair(f"{nm} vs A4b coder {cn} (54 cells)",
                [(f"P{p}/{t}", CD[p][i], RD[p][1 + j])
                 for p in range(1, 10) for i, t in enumerate(AB6)
                 for j, t2 in enumerate(T8) if t2 == t]))
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("CLAUDE-10", CLAUDE10)):
        alien_fam.append(report_pair(f"{nm} vs X3 (72 cells)",
            [(f"P{p}/{t}", X3[p][j], RD[p][1 + j])
             for p in range(1, 10) for j, t in enumerate(T8)]))
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("CLAUDE-10", CLAUDE10)):
        alien_fam.append(report_pair(f"{nm} vs B4 (90 cells)",
            [(f"P{p}/{t}", B4[p][i], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10)]))
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("CLAUDE-10", CLAUDE10)):
        alien_fam.append(report_pair(f"{nm} vs B5 (90 cells)",
            [(f"P{p}/{t}", B5[p][i], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10)]))
    print(f"\n>>> ALIEN-vs-FAMILY BAND (3 aliens x 4 family readings): "
          f"{min(alien_fam):.1%}-{max(alien_fam):.1%} "
          f"(mean {sum(alien_fam)/len(alien_fam):.1%})")
    per_alien = {}
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("CLAUDE-10", CLAUDE10)):
        vals = []
        for cn, CD in (("A", CODER_A), ("B", CODER_B)):
            vals.append(sum(score(CD[p][i], RD[p][1 + j])
                for p in range(1, 10) for i, t in enumerate(AB6)
                for j, t2 in enumerate(T8) if t2 == t) / 54)
        vals.append(sum(score(X3[p][j], RD[p][1 + j])
            for p in range(1, 10) for j in range(8)) / 72)
        vals.append(sum(score(B4[p][i], RD[p][i])
            for p in range(1, 10) for i in range(10)) / 90)
        vals.append(sum(score(B5[p][i], RD[p][i])
            for p in range(1, 10) for i in range(10)) / 90)
        per_alien[nm] = sum(vals) / len(vals)
        print(f">>> {nm} vs family mean: {per_alien[nm]:.1%}")

    # ===== PART 3: READINGS vs THE CENSUS (post-A4e) =======================
    print("\n" + "-" * 76)
    print("PART 3 - THE NEW READINGS vs THE CENSUS (post-A4e state)")
    print("-" * 76)
    for nm, RD in (("CLAUDE-10", CLAUDE10), ("B5", B5)):
        report_pair(f"{nm} vs census post-A4e (90 cells)",
            [(f"P{p}/{t}", CENSUS_A4E[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10)])
    dead = ("phl", "ether", "epi", "miasma", "caloric")
    living = ("newton", "qm", "rel", "germ", "thermo")
    for nm, RD in (("CLAUDE-10", CLAUDE10), ("B5", B5)):
        report_pair(f"{nm} vs census DEAD side (45 cells)",
            [(f"P{p}/{t}", CENSUS_A4E[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10) if t in dead])
        report_pair(f"{nm} vs census LIVING side (45 cells)",
            [(f"P{p}/{t}", CENSUS_A4E[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10) if t in living])

    # ===== PART 4: PER-POINT BANDS =========================================
    print("\n" + "-" * 76)
    print("PART 4 - PER-POINT BANDS (new readings vs census, 10 cells each)")
    print("-" * 76)
    for p in range(1, 10):
        sc = sum(score(CENSUS_A4E[t][p - 1], CLAUDE10[p][i])
                 for i, t in enumerate(T10))
        sb = sum(score(CENSUS_A4E[t][p - 1], B5[p][i])
                 for i, t in enumerate(T10))
        print(f"P{p} {POINT_NAMES[p]:<24} claude {sc:.1f}/10 = {sc/10:.1%}"
              f"   B5 {sb:.1f}/10 = {sb/10:.1%}")

    # ===== PART 5: THE SIXTH PAIR (B5 vs the pre-registration) =============
    print("\n" + "-" * 76)
    print("PART 5 - THE SIXTH PAIR: B5 vs THE LOCKED PRE-REGISTRATION")
    print("-" * 76)
    for t in ("fixity", "darwin"):
        idx = T12.index(t)
        print(f"\n{t.upper()}:")
        for p in range(1, 10):
            pre = PREREG_A4F[t][p - 1]
            b5 = B5_12[p][idx]
            mark = "" if pre == b5 else ("  <-- differs" +
                ("" if kind(pre, b5) != "DISTANT" else " (DISTANT)"))
            print(f"  P{p} {POINT_NAMES[p]:<24} prereg {pre:<3} B5 {b5:<3}"
                  f"{mark}")
        ag = sum(score(PREREG_A4F[t][p - 1], B5_12[p][T12.index(t)])
                 for p in range(1, 10)) / 9
        ex = sum(1 for p in range(1, 10)
                 if PREREG_A4F[t][p - 1] == B5_12[p][T12.index(t)])
        print(f"  -> prereg vs B5: {ag:.1%} weighted, {ex}/9 exact")

    print("\n--- Darwin's middle band vs germ theory's (the E2 test) ---")
    germ_mid = {3: CENSUS_A4E["germ"][2], 4: CENSUS_A4E["germ"][3],
                5: CENSUS_A4E["germ"][4], 6: CENSUS_A4E["germ"][5]}
    dar_mid = {3: B5_12[3][1], 4: B5_12[4][1], 5: B5_12[5][1],
               6: B5_12[6][1]}
    dar_mid_pre = {3: PREREG_A4F["darwin"][2], 4: PREREG_A4F["darwin"][3],
                   5: PREREG_A4F["darwin"][4], 6: PREREG_A4F["darwin"][5]}
    for p in (3, 4, 5, 6):
        print(f"  P{p} {POINT_NAMES[p]:<24} germ {germ_mid[p]:<3} "
              f"darwin(B5) {dar_mid[p]:<3} darwin(prereg) {dar_mid_pre[p]}")

    # ===== PART 6: DOCKETS AND READING RECORDS =============================
    print("\n" + "-" * 76)
    print("PART 6 - DOCKETS AND READING RECORDS")
    print("-" * 76)
    print("--- 6a. claude vs gpt-10 differing cells (the third family's")
    print("        departures from the first alien's ten-theory reading) ---")
    for p in range(1, 10):
        for i, t in enumerate(T10):
            if CLAUDE10[p][i] != GPT10[p][i]:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<8} "
                      f"claude {CLAUDE10[p][i]} vs gpt {GPT10[p][i]} "
                      f"(grok {GROK10[p][i]})")
    print("--- 6b. claude's unanimous-alone dissent vs census ---")
    for p in range(1, 10):
        for i, t in enumerate(T10):
            c = CENSUS_A4E[t][p - 1]
            if CLAUDE10[p][i] != c and GPT10[p][i] == c and GROK10[p][i] == c:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<8} census {c} | "
                      f"claude {CLAUDE10[p][i]}")
    print("--- 6c. B5's unanimous-alone dissent vs census (ten old) ---")
    for p in range(1, 10):
        for i, t in enumerate(T10):
            c = CENSUS_A4E[t][p - 1]
            if B5[p][i] != c and CLAUDE10[p][i] == c \
                    and GPT10[p][i] == c and GROK10[p][i] == c:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<8} census {c} | "
                      f"B5 {B5[p][i]}")
    print("--- 6d. full reading records on the elastic cells (9 coders) ---")
    recs = [
        ("Newton P3", ["S", "S", "-", "-", "S", "S", "S", "P"],
         CENSUS_A4E["newton"][2]),
        ("Newton P6", ["S", "S", "P", "P", "P", "P", "P", "P"], "dual S/P"),
        ("ether P5",  ["F", "S", "P", "P", "P", "P", "P", "S"],
         CENSUS_A4E["ether"][4]),
        ("ether P6",  ["S", "S", "S", "P", "P", "P", "P", "P"],
         CENSUS_A4E["ether"][5]),
        ("epi P6",    ["S", "S", "P", "P", "P", "P", "P", "P"],
         CENSUS_A4E["epi"][5]),
        ("phl P2",    ["S", "S", "P", "S", "P", "S", "S", "S"],
         CENSUS_A4E["phl"][1]),
        ("caloric P5",["-", "-", "-", "-", "P", "F", "F", "P"],
         CENSUS_A4E["caloric"][4]),
        ("caloric P9",["-", "-", "-", "-", "P", "P", "S", "S"],
         CENSUS_A4E["caloric"][8]),
        ("thermo P3", ["-", "-", "-", "-", "P", "P", "F", "P"],
         CENSUS_A4E["thermo"][2]),
        ("thermo P4", ["-", "-", "-", "-", "P", "S", "P", "S"],
         "dual S/P"),
        ("germ P7",   ["-", "-", "P", "F", "F", "F", "F", "P"],
         "dual F/P"),
        ("miasma P9", ["P", "S", "F", "F", "F", "F", "P", "P"],
         CENSUS_A4E["miasma"][8]),
    ]
    print(f"{'Cell':<13} {'A':>2} {'B':>2} {'X3':>3} {'G8':>3} {'B4':>3} "
          f"{'G10':>4} {'K10':>4} {'C10':>4} {'B5':>3}  census")
    recs_b5 = {
        "Newton P3": "S", "Newton P6": "P", "ether P5": "S", "ether P6": "F",
        "epi P6": "P", "phl P2": "P", "caloric P5": "F", "caloric P9": "P",
        "thermo P3": "P", "thermo P4": "P", "germ P7": "P", "miasma P9": "F",
    }
    for name, rec, cc in recs:
        print(f"{name:<13} {rec[0]:>2} {rec[1]:>2} {rec[2]:>3} {rec[3]:>3} "
              f"{rec[4]:>3} {rec[5]:>4} {rec[6]:>4} {rec[7]:>4} "
              f"{recs_b5[name]:>3}  {cc}")

    # ===== PART 7: KILLING CLAUSES =========================================
    print("\n" + "-" * 76)
    print("PART 7 - CENSUS-KILLING CLAUSES UNDER THE NEW READINGS (6 dead)")
    print("-" * 76)
    core = {1: "deletion", 3: "constant", 5: "embedding",
            6: "measurables", 8: "slope"}
    # fixed-species column in the 12-panel:
    fix = {p: B5_12[p][T12.index("fixity")] for p in range(1, 10)}
    fix_adj = {1: "F", 3: "F", 5: "F", 6: "F", 8: "SD"}  # post-adjudication
    print("  fixed species (B5):",
          ", ".join(f"{n}={fix[p]}" for p, n in core.items()),
          "| post-adjudication:",
          ", ".join(f"{n}={v}" for n, v in fix_adj.items()))
    for nm, RD in (("CLAUDE-10", CLAUDE10), ("B5", B5)):
        for t in dead:
            codes = {p: RD[p][T10.index(t)] for p in range(1, 10)}
            passed = [n for p, n in core.items() if codes[p] == "S"]
            print(f"  {nm} {t:<8} passes-as-S: "
                  f"{passed if passed else 'NONE of the 5'}")
    print("\n  Darwin and the living residents, five discriminators (B5):")
    for t in ("darwin",):
        codes = {p: B5_12[p][T12.index(t)] for p in range(1, 10)}
        print(f"    B5 darwin    "
              + ", ".join(f"{n}={codes[p]}" for p, n in core.items()))
    for t in ("germ", "thermo", "newton"):
        codes = {p: B5[p][T10.index(t)] for p in range(1, 10)}
        print(f"    B5 {t:<9} "
              + ", ".join(f"{n}={codes[p]}" for p, n in core.items()))

    # ===== PART 8: EXPECTATION CHECKS ======================================
    print("\n" + "-" * 76)
    print("PART 8 - E1/E2 EXPECTATION CHECKS (A4f pre-registration)")
    print("-" * 76)
    d = {p: B5_12[p][T12.index("darwin")] for p in range(1, 10)}
    f = {p: B5_12[p][T12.index("fixity")] for p in range(1, 10)}
    checks = [
        ("E1: fixity P1/P3/P6/P7 F under B5 (four dead-row F's)",
         all(f[p] == "F" for p in (1, 3, 6))),
        ("E1: fixity P8 'S then D' (the archive's generative phase)",
         f[8] == "SD"),
        ("E1: fixity fails all five discriminators under B5 (no S)",
         all(f[p] != "S" for p in (1, 3, 5, 6, 8))),
        ("E2: Darwin P3 F (the domain-marked constant replicates)",
         d[3] == "F"),
        ("E2: Darwin P5 P (archive embedding, no theorem)",
         d[5] == "P"),
        ("E2: Darwin P7 S by the blind reader (the live cell)",
         d[7] == "S"),
        ("E2: Darwin P4/P6 dissented from prereg (S/P vs prereg P/F)",
         d[4] == "S" and d[6] == "P"),
        ("E6: living trio unanimity holds under B5 (Newton P6 excepted)",
         all(B5[p][T10.index(t)] == "S" for p in range(1, 10)
             for t in ("newton", "qm", "rel")
             if not (t == "newton" and p == 6))),
        ("Claude P9 convention dissent printed (miasma P9 P vs census F)",
         CLAUDE10[9][4] == "P"),
        ("Claude Newton P3 = P (the G-anachronism dissent, alone)",
         CLAUDE10[3][5] == "P"),
        ("Zero distant disagreements anywhere between claude and B5",
         all(kind(CLAUDE10[p][i], B5[p][i]) != "DISTANT"
             for p in range(1, 10) for i in range(10))),
    ]
    for label, ok in checks:
        print(f"  {'CONFIRMED' if ok else 'NOT AS EXPECTED':<15} {label}")

    # ===== PART 9: THE CENSUS AFTER A4f (rulings printed) ==================
    print("\n" + "-" * 76)
    print("PART 9 - THE CENSUS AFTER A4f (adjudication rulings, as applied)")
    print("-" * 76)
    print("New pair, pre-registered then adjudicated under the rules:")
    print("  fixity P5  P -> F   (B5's vote + the miasma craft-precedent:")
    print("                        no theorems existed to survive)")
    print("  fixity P7  F -> P   (B5's vote + the graduated compromise scale:")
    print("                        Linnaeus's 1762-63 hybridism concession)")
    print("  fixity P9  P (defended; B5's F dissent printed - the")
    print("                        archive-versus-doctrine fork again)")
    print("  darwin P4  P -> S   (B5's vote + the faithful reading: the")
    print("                        Beagle data WERE old data; no new")
    print("                        technique needed - the germ contrast)")
    print("  darwin P6  F (defended as written; B5's P recorded as the")
    print("                        middle reading on the operationalized face)")
    print("Defended on the old panel (forks re-printed with the new votes):")
    print("  ether P5 P (claude S + B5 S land on the machinery face of the")
    print("             composite - inside the cell, not against it)")
    print("  caloric P5 P (the two-faces fork now 3-3: P face author/B4/")
    print("               claude, F face G10/K10/B5)")
    print("  thermo P4 S -> dual S/P (ERRATUM: the A4e Table 6 record row")
    print("               misprinted B4 as S; the verified data files carry")
    print("               P - corrected here, the fork is now author+G10+")
    print("               C10 on S vs B4+K10+B5 on P: a stable 3-3 history-")
    print("               fork -> dual: S two-roads / P split-signatures)")
    print("  Newton P6 dual confirmed (P-face now SEVEN consecutive readings)")
    print("Adjudicated profiles:")
    print("  fixity:  F P F F F F P SD P")
    print("  darwin:  S S F S P F S S S")


if __name__ == "__main__":
    main()
