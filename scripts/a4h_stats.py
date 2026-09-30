# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4h — the FIFTH reading of the fourth
delivery (gemini 3.8, twelve-theory panel, delivered by the owner at 02:32
UTC and recovered from git after the A4g sync's overwrite; verified against
the restored prompt4.txt), and the ADVICE VERIFICATION (the owner's deepseek
chat: the umbrella-hypothesis mapping, the cluster tables, the P10 question).

Readings on file (unchanged lineage):
  - Census post-A4g (as-written faces; duals scored as-written).
  - All thirteen coders from a4g_stats.py.
  - NEW: GEMINI38 — the seventh external reading, sixth lineage at two
    versions (gemini 3.1 pro preview vs gemini 3.8): the series' first
    within-lineage version-drift measurement.

Scoring identical to A4b-A4g: exact=1.0, adjacent=0.5, distant=0.0;
SD special-handling (SD vs S/P = 0.5, SD vs SD = 1.0); census dual cells
scored on their as-written faces.
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}

T10 = ("caloric", "epi", "germ", "ether", "miasma", "newton",
       "phl", "qm", "rel", "thermo")
T8 = ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel")
AB6 = ("epi", "ether", "newton", "phl", "qm", "rel")
T12 = ("caloric", "darwin", "epi", "fixity", "germ", "ether",
       "miasma", "newton", "phl", "qm", "rel", "thermo")
T14 = T12 + ("crust", "plate")
DEAD12 = ("caloric", "epi", "fixity", "ether", "miasma", "phl")
LIVE12 = ("darwin", "germ", "newton", "qm", "rel", "thermo")

DISCRIM = (1, 3, 5, 6, 8)   # deletion, constant, embedding, measurables, slope

POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}


def mk(order, mat):
    return {t: tuple(mat[p][i] for p in range(1, 10))
            for i, t in enumerate(order)}


# ---- Census state: post-A4g, as-written faces (duals as-written) -----------
# The twelve: identical to post-A4f as-written (A4g's duals kept as-written
# faces). Crust and plate entered at A4g: crust P2 moved P->F; crust P5 is
# dual P/F (as-written P); plate confirmed as pre-registered.
CENSUS = {
    "caloric": ("F", "P", "F", "P", "P", "P", "F", "SD", "P"),
    "darwin":  ("S", "S", "F", "S", "P", "F", "S", "S", "S"),
    "epi":     ("F", "P", "F", "P", "P", "S", "P", "SD", "P"),
    "fixity":  ("F", "P", "F", "F", "F", "F", "P", "SD", "P"),
    "germ":    ("S", "S", "F", "P", "P", "F", "F", "S", "S"),
    "ether":   ("P", "S", "F", "P", "P", "S", "P", "SD", "S"),
    "miasma":  ("F", "P", "F", "F", "F", "F", "F", "SD", "F"),
    "newton":  ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "phl":     ("F", "S", "F", "F", "F", "F", "F", "SD", "P"),
    "qm":      ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "rel":     ("S", "S", "S", "S", "S", "S", "S", "S", "S"),
    "thermo":  ("S", "S", "P", "S", "S", "S", "P", "S", "S"),
    "crust":   ("F", "F", "F", "F", "P", "F", "F", "SD", "P"),
    "plate":   ("S", "S", "F", "P", "P", "P", "P", "S", "S"),
}
DEAD14 = DEAD12 + ("crust",)
LIVE14 = LIVE12 + ("plate",)

# ---- Prior readings (verbatim from a4g_stats.py) ----------------------------
CODER_A = mk(AB6, {
    1: ("F", "P", "S", "F", "S", "S"), 2: ("P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "S", "F", "S", "S"), 4: ("P", "S", "S", "F", "S", "S"),
    5: ("F", "S", "S", "F", "S", "S"), 6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"), 8: ("P", "SD", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
})
CODER_B = mk(AB6, {
    1: ("F", "P", "S", "F", "S", "S"), 2: ("P", "S", "S", "P", "S", "S"),
    3: ("F", "P", "S", "F", "S", "S"), 4: ("P", "P", "S", "F", "S", "S"),
    5: ("P", "S", "S", "F", "S", "S"), 6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"), 8: ("SD", "S", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
})
X3 = mk(T8, {
    1: ("F", "S", "F", "P", "S", "F", "S", "S"),
    2: ("P", "S", "S", "P", "S", "P", "S", "S"),
    3: ("F", "F", "F", "F", "S", "F", "S", "S"),
    4: ("P", "F", "P", "F", "S", "F", "P", "S"),
    5: ("F", "P", "P", "F", "S", "F", "S", "S"),
    6: ("P", "F", "S", "F", "P", "F", "S", "S"),
    7: ("P", "P", "F", "F", "S", "F", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "F", "S", "P", "S", "S"),
})
GPT8 = mk(T8, {
    1: ("P", "S", "P", "P", "S", "P", "S", "S"),
    2: ("P", "P", "S", "F", "S", "S", "S", "S"),
    3: ("F", "F", "P", "F", "S", "F", "S", "S"),
    4: ("P", "P", "S", "F", "S", "P", "S", "S"),
    5: ("P", "P", "P", "F", "S", "P", "S", "S"),
    6: ("P", "P", "P", "F", "P", "P", "S", "S"),
    7: ("P", "F", "P", "F", "S", "F", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "S", "S"),
    9: ("P", "P", "P", "F", "S", "P", "S", "S"),
})
B4 = mk(T10, {
    1: ("F", "F", "S", "F", "F", "S", "F", "S", "S", "S"),
    2: ("P", "P", "S", "P", "F", "S", "P", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("P", "F", "P", "P", "F", "S", "F", "S", "S", "P"),
    5: ("P", "P", "P", "P", "P", "S", "F", "S", "S", "S"),
    6: ("P", "P", "F", "P", "F", "P", "F", "S", "S", "S"),
    7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "P"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "P", "S", "S", "F", "S", "F", "S", "S", "S"),
})
GPT10 = mk(T10, {
    1: ("P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
    2: ("P", "P", "P", "S", "F", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "P", "F", "S", "F", "S", "S", "P"),
    4: ("P", "P", "P", "S", "F", "S", "P", "S", "S", "S"),
    5: ("F", "P", "P", "P", "F", "S", "P", "S", "S", "P"),
    6: ("P", "P", "P", "P", "F", "P", "P", "S", "S", "P"),
    7: ("P", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
})
GROK10 = mk(T10, {
    1: ("P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
    2: ("P", "P", "P", "S", "F", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "P", "F", "S", "F", "S", "S", "F"),
    4: ("P", "P", "P", "S", "F", "S", "P", "S", "S", "P"),
    5: ("F", "P", "P", "P", "F", "S", "P", "S", "S", "P"),
    6: ("P", "P", "P", "P", "F", "P", "P", "S", "S", "S"),
    7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
})
CLAUDE10 = mk(T10, {
    1: ("P", "F", "S", "P", "P", "S", "F", "S", "S", "S"),
    2: ("P", "P", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "P", "F", "P", "F", "S", "S", "P"),
    4: ("P", "F", "P", "P", "P", "S", "F", "S", "S", "S"),
    5: ("P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
    6: ("P", "P", "F", "P", "F", "P", "F", "S", "S", "S"),
    7: ("F", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("S", "S", "S", "S", "P", "S", "S", "S", "S", "S"),
})
B5 = mk(T12, {
    1: ("F", "S", "F", "F", "S", "P", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("F", "S", "F", "F", "P", "P", "F", "S", "F", "S", "S", "P"),
    5: ("F", "P", "F", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "P", "P", "F", "P", "F", "F", "P", "F", "S", "S", "S"),
    7: ("F", "S", "F", "P", "P", "P", "F", "S", "P", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "F", "S", "P", "F", "S", "P", "S", "S", "S"),
})
DEEPSEEK = mk(T12, {
    1: ("P", "S", "F", "F", "S", "F", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "F", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "F", "F", "S", "F", "S", "S", "P"),
    4: ("P", "S", "P", "F", "F", "P", "F", "S", "P", "S", "S", "P"),
    5: ("F", "P", "F", "F", "F", "F", "F", "S", "F", "S", "S", "S"),
    6: ("S", "F", "P", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    7: ("F", "S", "F", "F", "P", "F", "F", "S", "P", "S", "S", "P"),
    8: ("SD", "S", "SD", "P", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "F", "S", "S", "F", "S", "P", "S", "S", "S"),
})
OPUS = mk(T12, {
    1: ("P", "S", "P", "P", "S", "P", "P", "S", "P", "S", "S", "S"),
    2: ("P", "S", "P", "P", "S", "S", "P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "P", "F", "P", "F", "S", "S", "P"),
    4: ("P", "S", "P", "P", "F", "S", "F", "S", "P", "P", "S", "S"),
    5: ("F", "P", "P", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "P", "P", "F", "F", "P", "F", "P", "P", "S", "S", "S"),
    7: ("F", "S", "P", "P", "F", "P", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "P", "P", "S", "S", "P", "S", "P", "S", "S", "S"),
})
GEMINI31 = mk(T12, {
    1: ("F", "S", "F", "F", "S", "S", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "P", "F", "S", "S", "F", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    4: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "P"),
    5: ("F", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    6: ("F", "F", "F", "F", "F", "P", "F", "F", "F", "S", "S", "S"),
    7: ("F", "S", "P", "F", "F", "F", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("P", "S", "S", "P", "P", "S", "F", "S", "P", "S", "S", "S"),
})
B6 = mk(T14, {
    1: ("F", "S", "F", "F", "S", "P", "F", "S", "F", "S", "S", "S", "F", "S"),
    2: ("F", "S", "P", "F", "S", "S", "F", "S", "P", "S", "S", "S", "F", "S"),
    3: ("F", "F", "F", "F", "F", "P", "F", "S", "F", "S", "S", "P", "F", "F"),
    4: ("P", "S", "F", "F", "P", "P", "F", "S", "F", "S", "S", "P", "F", "P"),
    5: ("F", "P", "F", "F", "P", "P", "F", "S", "F", "S", "S", "S", "F", "P"),
    6: ("P", "F", "P", "F", "F", "S", "F", "P", "F", "S", "S", "S", "F", "P"),
    7: ("F", "S", "F", "F", "P", "F", "F", "S", "F", "S", "S", "S", "F", "P"),
    8: ("SD", "SD", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S",
        "SD", "S"),
    9: ("P", "S", "P", "F", "S", "P", "F", "S", "P", "S", "S", "S", "F", "S"),
})

# ---- NEW: the fifth reading — gemini 3.8 (verified against the restored
# prompt4.txt lines 645-831) --------------------------------------------------
GEMINI38 = mk(T12, {
    1: ("F", "S", "F", "F", "S", "F", "F", "S", "F", "S", "S", "S"),
    2: ("P", "S", "F", "F", "S", "S", "F", "S", "S", "S", "S", "S"),
    3: ("F", "F", "F", "F", "F", "P", "F", "S", "F", "S", "S", "S"),
    4: ("F", "P", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    5: ("F", "P", "P", "F", "P", "S", "F", "S", "F", "S", "S", "S"),
    6: ("P", "F", "F", "F", "F", "S", "F", "S", "F", "S", "S", "S"),
    7: ("F", "S", "F", "F", "F", "F", "F", "S", "F", "S", "S", "S"),
    8: ("SD", "S", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S"),
    9: ("F", "S", "P", "P", "S", "S", "F", "S", "F", "S", "S", "S"),
})


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


def cmp_theories(name, ra, rb, shared):
    return report_pair(name,
        [(f"P{p}/{t}", ra[t][p - 1], rb[t][p - 1])
         for p in range(1, 10) for t in shared])


def main():
    print("=" * 76)
    print("A4h UNBLINDING - THE FIFTH READING (GEMINI 3.8) + THE ADVICE "
          "VERIFICATION")
    print("=" * 76)

    # ===== PART 1: THE FOURTH DELIVERY, COMPLETED ==========================
    print("\n" + "-" * 76)
    print("PART 1 - THE FIFTH READING vs THE FOURTH DELIVERY'S OTHER THREE")
    print("-" * 76)
    cmp_theories("GEMINI38 vs DEEPSEEK (108 cells)", GEMINI38, DEEPSEEK, T12)
    cmp_theories("GEMINI38 vs OPUS (108 cells)", GEMINI38, OPUS, T12)
    cmp_theories("GEMINI38 vs GEMINI31 (108 cells)", GEMINI38, GEMINI31, T12)
    print("\n-- the delivery's six mutuals, for scale (A4g values) --")
    print("   D-O 85.2 / D-G31 85.6 / O-G31 85.6")

    # ===== PART 2: THE VERSION-DRIFT MEASUREMENT ===========================
    print("\n" + "-" * 76)
    print("PART 2 - WITHIN-LINEAGE VERSION DRIFT (gemini 3.1 -> 3.8)")
    print("-" * 76)
    print("-- every cell that moved between the two gemini versions --")
    moves = []
    for p in range(1, 10):
        for t in T12:
            a, b = GEMINI31[t][p - 1], GEMINI38[t][p - 1]
            if a != b:
                moves.append((t, p, a, b))
    for t, p, a, b in moves:
        c = CENSUS[t][p - 1]
        print(f"  {t:<8} P{p} {POINT_NAMES[p]:<24} 3.1 {a} -> 3.8 {b}"
              f"   (census {c})")
    toward = sum(1 for t, p, a, b in moves
                 if score(b, CENSUS[t][p - 1]) > score(a, CENSUS[t][p - 1]))
    away = sum(1 for t, p, a, b in moves
               if score(b, CENSUS[t][p - 1]) < score(a, CENSUS[t][p - 1]))
    print(f"\n  {len(moves)} cells moved between versions; "
          f"toward census {toward}, away {away}, lateral "
          f"{len(moves) - toward - away}")

    # the ether line under both versions (A4g's deepest challenge)
    print("\n-- the ether line, both versions (A4g's three-discriminator "
          "challenge) --")
    print("  Point                     3.1   3.8   census")
    for p in range(1, 10):
        mark = " <-- discriminator" if p in DISCRIM else ""
        print(f"  P{p} {POINT_NAMES[p]:<24} {GEMINI31['ether'][p-1]:<5}"
              f"{GEMINI38['ether'][p-1]:<5}{CENSUS['ether'][p-1]}{mark}")
    d31 = [GEMINI31["ether"][p - 1] for p in DISCRIM]
    d38 = [GEMINI38["ether"][p - 1] for p in DISCRIM]
    print(f"  discriminators as S: 3.1 {sum(1 for c in d31 if c == 'S')}/5"
          f"  ->  3.8 {sum(1 for c in d38 if c == 'S')}/5")

    # ===== PART 3: OUTGROUP TEST v5 ========================================
    print("\n" + "-" * 76)
    print("PART 3 - OUTGROUP TEST v5 (the seventh external reading)")
    print("-" * 76)
    aliens = [("GPT-10", GPT10), ("GROK-10", GROK10),
              ("CLAUDE-10", CLAUDE10), ("DEEPSEEK", DEEPSEEK),
              ("OPUS", OPUS), ("GEMINI31", GEMINI31),
              ("GEMINI38", GEMINI38)]
    means = {}
    for an, rd in aliens:
        vals = [
            cmp_theories(f"{an} vs A (54)", rd, CODER_A, AB6),
            cmp_theories(f"{an} vs B (54)", rd, CODER_B, AB6),
            cmp_theories(f"{an} vs X3 (72)", rd, X3, T8),
            cmp_theories(f"{an} vs B4 (90)", rd, B4, T10),
            cmp_theories(f"{an} vs B5 (90)", rd, B5, T10),
            cmp_theories(f"{an} vs B6 (90)", rd, B6, T10),
        ]
        m = sum(vals) / len(vals)
        means[an] = m
        print(f"  >>> {an} vs family mean: {m:.1%}")
    print("\n  family-band check (88.0-94.4): "
          + "; ".join(f"{k} {v:.1%}{' (INSIDE)' if 0.88 <= v <= 0.944 else ' (outside)'}"
                      for k, v in means.items()))

    # ===== PART 4: vs THE CENSUS (post-A4g) ================================
    print("\n" + "-" * 76)
    print("PART 4 - GEMINI38 vs THE AMENDED CENSUS (post-A4g)")
    print("-" * 76)
    cmp_theories("GEMINI38 vs census (108 cells)", GEMINI38, CENSUS, T12)
    cmp_theories("GEMINI38 vs census DEAD (54)", GEMINI38, CENSUS, DEAD12)
    cmp_theories("GEMINI38 vs census LIVING (54)", GEMINI38, CENSUS, LIVE12)
    print("\n-- for scale, the prior readings vs the same census (A4g "
          "values) --")
    print("   deepseek 90.7 (0 distant) / opus 89.8 (0) / gemini31 86.6 (4)"
          " / B6 91.2 (0)")

    # ===== PART 5: PER-POINT BANDS =========================================
    print("\n" + "-" * 76)
    print("PART 5 - PER-POINT BANDS (gemini38 vs census, 12 cells each)")
    print("-" * 76)
    for p in range(1, 10):
        tot = sum(score(GEMINI38[t][p - 1], CENSUS[t][p - 1]) for t in T12)
        print(f"  P{p} {POINT_NAMES[p]:<24} {tot:.1f}/12 = {tot/12:.1%}")

    # ===== PART 6: READING RECORDS + DOCKETS ===============================
    print("\n" + "-" * 76)
    print("PART 6 - DOCKETS AND READING RECORDS (14 coders)")
    print("-" * 76)
    print("--- 6a. gemini38's unanimous-alone dissents vs census (the 12) ---")
    others = [DEEPSEEK, OPUS, GEMINI31, B6]
    count = 0
    for p in range(1, 10):
        for t in T12:
            c = CENSUS[t][p - 1]
            v = GEMINI38[t][p - 1]
            if v != c and all(o[t][p - 1] != v for o in others):
                print(f"    P{p} {POINT_NAMES[p]:<22} {t:<8} census {c} | "
                      f"gemini38 {v}")
                count += 1
    if count == 0:
        print("    (none)")

    print("\n--- 6b. the elastic cells' reading records, now 14 coders ---")
    readers = [("A", CODER_A), ("B", CODER_B), ("X3", X3), ("G8", GPT8),
               ("B4", B4), ("G10", GPT10), ("K10", GROK10),
               ("C10", CLAUDE10), ("B5", B5), ("D", DEEPSEEK),
               ("O", OPUS), ("G31", GEMINI31), ("38", GEMINI38),
               ("B6", B6)]
    print("  Cell            " + " ".join(f"{n:<4}" for n, _ in readers)
          + "census")
    watch = [("newton", 3), ("newton", 6), ("ether", 5), ("ether", 6),
             ("epi", 6), ("phl", 2), ("caloric", 5), ("caloric", 9),
             ("thermo", 3), ("thermo", 4), ("germ", 7), ("miasma", 9),
             ("darwin", 4), ("darwin", 6), ("darwin", 7), ("darwin", 8),
             ("fixity", 5), ("fixity", 7), ("fixity", 9),
             ("ether", 1), ("ether", 3), ("epi", 9), ("germ", 5),
             ("phl", 9), ("caloric", 6)]
    for t, p in watch:
        row = f"  {t} P{p:<12}"[:16].ljust(16)
        for _, rd in readers:
            v = rd[t][p - 1] if t in rd else "-"
            row += f"{v:<4}"
        row += CENSUS[t][p - 1]
        print(row)

    print("\n--- 6c. face counts on the dual cells (14 coders) ---")
    duals = [("ether", 6), ("epi", 6), ("newton", 6), ("phl", 2),
             ("miasma", 1), ("germ", 6), ("germ", 7), ("thermo", 4),
             ("crust", 5)]
    for t, p in duals:
        faces = {}
        for _, rd in readers:
            if t in rd:
                v = rd[t][p - 1]
                faces[v] = faces.get(v, 0) + 1
        print(f"  {t} P{p}: " + " / ".join(f"{k} {v}" for k, v in
              sorted(faces.items())) + f"  (census {CENSUS[t][p-1]})")

    # ===== PART 7: KILLING CLAUSES UNDER THE 14TH READING ==================
    print("\n" + "-" * 76)
    print("PART 7 - CENSUS-KILLING CLAUSES (dead theories x gemini38)")
    print("-" * 76)
    print("  (five discriminators: deletion, constant, embedding, "
          "measurables, slope)")
    for t in DEAD12:
        passes = [d for p, d in zip(DISCRIM, ("deletion", "constant",
                 "embedding", "measurables", "slope"))
                 if GEMINI38[t][p - 1] == "S"]
        print(f"  GEMINI38  {t:<8} passes-as-S: "
              f"{passes if passes else 'NONE of the 5'}")

    # ===== PART 8: THE ADVICE VERIFICATION ================================
    print("\n" + "-" * 76)
    print("PART 8 - THE ADVICE: THE UMBRELLA CLUSTERS vs THE CENSUS RECORD")
    print("-" * 76)
    print("  (the advice's claim: the nine points JOINTLY operationalize")
    print("   'challenges fundamental assumptions -> counter-intuitive,")
    print("   broad conclusions'; assumption cluster P1/P2/P5/P6/P9,")
    print("   breadth cluster P3/P8/P9)")
    print("\n  S-rates by point, dead (7) vs living (7), census post-A4g:")
    print("  Point                     dead-S   living-S   discriminates?")
    discrim_set = set(DISCRIM)
    for p in range(1, 10):
        d = sum(1 for t in DEAD14 if CENSUS[t][p - 1] == "S")
        l = sum(1 for t in LIVE14 if CENSUS[t][p - 1] == "S")
        tag = "DISCRIMINATOR" if p in discrim_set else (
            "confounded" if d > 0 else "living-only")
        print(f"  P{p} {POINT_NAMES[p]:<24} {d}/7      {l}/7"
              f"       {tag}")

    clusterA = (1, 2, 5, 6, 9)   # the advice's assumption-challenge cluster
    clusterB = (3, 8, 9)          # the advice's breadth cluster
    for nm, cl in (("assumption cluster (P1,P2,P5,P6,P9)", clusterA),
                   ("breadth cluster (P3,P8,P9)", clusterB),
                   ("five discriminators (P1,P3,P5,P6,P8)", DISCRIM)):
        ds = sum(1 for t in DEAD14 for p in cl if CENSUS[t][p - 1] == "S")
        ls = sum(1 for t in LIVE14 for p in cl if CENSUS[t][p - 1] == "S")
        n = 7 * len(cl)
        print(f"\n  {nm}: dead-S {ds}/{n} ({ds/n:.0%}), "
              f"living-S {ls}/{n} ({ls/n:.0%})")

    print("\n  -- the dead theories that DID challenge assumptions --")
    print("     (the umbrella is necessary, not sufficient)")
    for t, p in (("phl", 2), ("ether", 2), ("ether", 9), ("epi", 6),
                 ("ether", 6), ("epi", 5), ("caloric", 5), ("crust", 5)):
        print(f"     {t} P{p} = {CENSUS[t][p-1]}"
              f" ({POINT_NAMES[p]})")

    print("\n" + "=" * 76)
    print("END OF A4h UNBLINDING")
    print("=" * 76)


if __name__ == "__main__":
    main()
