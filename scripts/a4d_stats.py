# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4d — the alien reading (GPT, delivered
via the owner's repository after the kit's verbatim prompt was administered
externally) and the fourth blind coding (fresh context, same family, the
10-theory widened panel).

Readings on file:
  - Census v1 (author-coded dead side) and post-A4b adjudicated matrix
    (a4c_stats.py conventions).
  - Post-A4c amended census: dead side (phl, ether, epi, miasma) with the
    A4c rulings applied; living side: Newton/QM/Rel all-S; germ theory
    S S F P P F(as-written)/S(operationalized) P S S.
  - A4b blind coders A and B (6-theory panel).
  - Third blind reading X3 (8-theory panel).
  - ALIEN (GPT): 8-theory panel, from the owner's repository file.
  - BLIND4: 10-theory panel, fresh context, this run.
  - A4d pre-registration: caloric + thermodynamics, locked before BLIND4 ran.

Scoring identical to A4b/A4c: exact=1.0, adjacent=0.5, distant=0.0;
SD special-handling (SD vs S/P = 0.5, SD vs SD = 1.0); census 'C' read as P.
Dual cells scored on their as-written face (the operationalized face is an
annotation, per the A4c convention).
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}

# ---- Census v1 (phlogiston, ether, epicycles) ------------------------------
CENSUS = {
    1: ("F", "F", "F"), 2: ("S", "S", "S"), 3: ("F", "F", "F"),
    4: ("F", "F", "C"), 5: ("F", "F", "P"), 6: ("F", "P", "P"),
    7: ("S", "S", "S"), 8: ("SD", "SD", "SD"), 9: ("P", "P", "P"),
}

# ---- Post-A4c amended dead side (phl, ether, epi, miasma) -------------------
AMENDED = {
    1: ("F", "P", "F", "F"), 2: ("P", "S", "P", "P"), 3: ("F", "F", "F", "F"),
    4: ("F", "P", "P", "F"), 5: ("F", "F", "P", "F"), 6: ("F", "S", "S", "F"),
    7: ("F", "P", "P", "F"), 8: ("SD", "SD", "SD", "SD"), 9: ("P", "S", "P", "P"),
}
# Germ theory amended (P6 as-written F, operationalized S noted)
GERM_ADJ = {1: "S", 2: "S", 3: "F", 4: "P", 5: "P", 6: "F", 7: "P",
            8: "S", 9: "S"}

# ---- A4b blind coders (epi, ether, newton, phl, qm, rel) ---------------------
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

# ---- Third blind reading (epi, germ, ether, miasma, newton, phl, qm, rel) ----
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

# ---- ALIEN (GPT): (epi, germ, ether, miasma, newton, phl, qm, rel) -----------
ALIEN = {
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

# ---- BLIND4: (caloric, epi, germ, ether, miasma, newton, phl, qm, rel, thermo)
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

# ---- A4d pre-registration: (caloric, thermo) ---------------------------------
PREREG_A4D = {  # (caloric, thermo)
    1: ("F", "S"), 2: ("P", "S"), 3: ("F", "P"), 4: ("P", "S"),
    5: ("P", "S"), 6: ("P", "S"), 7: ("F", "P"), 8: ("SD", "S"),
    9: ("P", "S"),
}

# ---- A4c pre-registration (miasma, germ) --------------------------------------
PREREG_A4C = {
    1: ("F", "S"), 2: ("P", "S"), 3: ("F", "F"), 4: ("F", "S"),
    5: ("P", "P"), 6: ("F", "S"), 7: ("F", "P"), 8: ("SD", "S"),
    9: ("P", "S"),
}

POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}

# index maps
XI = {"epi": 0, "germ": 1, "ether": 2, "miasma": 3, "newton": 4,
      "phl": 5, "qm": 6, "rel": 7}
B4I = {"caloric": 0, "epi": 1, "germ": 2, "ether": 3, "miasma": 4,
       "newton": 5, "phl": 6, "qm": 7, "rel": 8, "thermo": 9}
AB_IDX = {"epi": 0, "ether": 1, "newton": 2, "phl": 3, "qm": 4, "rel": 5}


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
    print("A4d UNBLINDING - THE ALIEN READING (GPT) AND THE FOURTH BLIND CODING")
    print("=" * 76)

    # ===== PART 1: THE OUTGROUP TEST =====
    print("\n" + "-" * 76)
    print("PART 1 - THE ALIEN (GPT) READING AGAINST EVERY FAMILY READING")
    print("-" * 76)

    fam_pairs = []

    def cells_ab(C, t_keys, x_map, y_map, y_is_alien=False):
        pass  # helper defined inline below

    # alien vs A4b A and B (54 cells each)
    a_vs_A = report_pair("ALIEN vs A4b coder A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][AB_IDX[t]], ALIEN[p][XI[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    a_vs_B = report_pair("ALIEN vs A4b coder B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][AB_IDX[t]], ALIEN[p][XI[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    # alien vs X3 (72 cells)
    a_vs_X3 = report_pair("ALIEN vs third blind reading X3 (72 cells)",
        [(f"P{p}/{t}", X3[p][XI[t]], ALIEN[p][XI[t]])
         for p in range(1, 10)
         for t in ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel")])
    # alien vs B4 (72 shared cells)
    a_vs_B4 = report_pair("ALIEN vs fourth blind coding B4 (72 shared cells)",
        [(f"P{p}/{t}", B4[p][B4I[t]], ALIEN[p][XI[t]])
         for p in range(1, 10)
         for t in ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel")])

    # the family mutual band (now 4 family runs: A, B, X3, B4)
    ab = report_pair("FAMILY: X3 vs A4b coder A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][AB_IDX[t]], X3[p][XI[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    xb = report_pair("FAMILY: X3 vs A4b coder B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][AB_IDX[t]], X3[p][XI[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    b4A = report_pair("FAMILY: B4 vs A4b coder A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][AB_IDX[t]], B4[p][B4I[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    b4B = report_pair("FAMILY: B4 vs A4b coder B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][AB_IDX[t]], B4[p][B4I[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])
    b4X3 = report_pair("FAMILY: B4 vs X3 (72 cells)",
        [(f"P{p}/{t}", X3[p][XI[t]], B4[p][B4I[t]])
         for p in range(1, 10)
         for t in ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel")])
    aabb = report_pair("FAMILY: A4b A vs A4b B (54 cells, for scale)",
        [(f"P{p}/{t}", CODER_A[p][AB_IDX[t]], CODER_B[p][AB_IDX[t]])
         for p in range(1, 10) for t in ("epi", "ether", "newton", "phl", "qm", "rel")])

    fam = [ab, xb, b4A, b4B, b4X3]
    aabbv = aabb
    alien_fam = [a_vs_A, a_vs_B, a_vs_X3, a_vs_B4]
    print(f"\n>>> OUTGROUP VERDICT: family mutual band = "
          f"{min(fam):.1%}-{max(fam):.1%} (mean {sum(fam)/len(fam):.1%}); "
          f"alien vs family = {min(alien_fam):.1%}-{max(alien_fam):.1%} "
          f"(mean {sum(alien_fam)/len(alien_fam):.1%}); "
          f"gap = {sum(fam)/len(fam) - sum(alien_fam)/len(alien_fam):.1%}")

    # alien vs census v1 (27 dead cells)
    report_pair("ALIEN vs census v1 (27 dead cells)",
        [(f"P{p}/{t}", CENSUS[p][j], ALIEN[p][XI[t]])
         for p in range(1, 10)
         for j, t in enumerate(("phl", "ether", "epi"))])
    # alien vs amended census (27 dead cells)
    a_vs_am = report_pair("ALIEN vs post-A4c amended census (36 dead cells: phl, ether, epi, miasma)",
        [(f"P{p}/{t}", AMENDED[p][j], ALIEN[p][XI[t]])
         for p in range(1, 10)
         for j, t in enumerate(("phl", "ether", "epi", "miasma"))])
    # alien vs A4c prereg (miasma, germ - 18 cells)
    report_pair("ALIEN vs A4c pre-registration (miasma+germ, 18 cells)",
        [(f"P{p}/{t}", PREREG_A4C[p][j], ALIEN[p][XI[t]])
         for p in range(1, 10) for j, t in enumerate(("miasma", "germ"))])
    # alien vs germ amended (9 cells)
    report_pair("ALIEN vs amended germ theory (9 cells)",
        [(f"P{p}/germ", GERM_ADJ[p], ALIEN[p][XI["germ"]]) for p in range(1, 10)])

    # alien living side vs Vol I all-S
    breaks = [(p, t) for p in range(1, 10) for t in ("newton", "qm", "rel")
              if ALIEN[p][XI[t]] != "S"]
    print(f"\nALIEN living side (physics trio) vs Vol I's all-S: "
          f"{27 - len(breaks)}/27 exact; breaks at: "
          + (", ".join(f"P{p} {t}" for p, t in breaks) if breaks else "none"))

    # ===== PART 2: THE FOURTH BLIND CODING =====
    print("\n" + "-" * 76)
    print("PART 2 - THE FOURTH BLIND CODING (10-THEORY PANEL)")
    print("-" * 76)

    # B4 vs census v1 (27 old dead cells)
    report_pair("B4 vs census v1 (27 dead cells)",
        [(f"P{p}/{t}", CENSUS[p][j], B4[p][B4I[t]])
         for p in range(1, 10)
         for j, t in enumerate(("phl", "ether", "epi"))])
    # B4 vs amended census (27 dead cells: phl, ether, epi, miasma)
    b4_vs_am = report_pair("B4 vs post-A4c amended census (36 dead cells: phl, ether, epi, miasma)",
        [(f"P{p}/{t}", AMENDED[p][j], B4[p][B4I[t]])
         for p in range(1, 10)
         for j, t in enumerate(("phl", "ether", "epi", "miasma"))])
    # B4 vs germ amended (9)
    report_pair("B4 vs amended germ theory (9 cells)",
        [(f"P{p}/germ", GERM_ADJ[p], B4[p][B4I["germ"]]) for p in range(1, 10)])
    # B4 living side vs all-S
    breaks = [(p, t) for p in range(1, 10) for t in ("newton", "qm", "rel")
              if B4[p][B4I[t]] != "S"]
    print(f"\nB4 living side (physics trio) vs Vol I's all-S: "
          f"{27 - len(breaks)}/27 exact; breaks at: "
          + (", ".join(f"P{p} {t}" for p, t in breaks) if breaks else "none"))
    # B4 vs prereg A4d (new pair, 18 cells)
    report_pair("B4 vs A4d pre-registration (caloric+thermo, 18 cells)",
        [(f"P{p}/{t}", PREREG_A4D[p][j], B4[p][B4I[t]])
         for p in range(1, 10) for j, t in enumerate(("caloric", "thermo"))])

    # ===== PART 3: PER-POINT BANDS =====
    print("\n" + "-" * 76)
    print("PART 3 - PER-POINT BANDS")
    print("-" * 76)
    print("--- alien vs the four family runs, per point (dead side, 3 old cells "
          "x A/B + 4 cells x X3/B4 = up to 14 comparisons) ---")
    for p in range(1, 10):
        cells = []
        for t in ("epi", "ether", "newton", "phl", "qm", "rel"):
            cells.append((CODER_A[p][AB_IDX[t]], ALIEN[p][XI[t]]))
            cells.append((CODER_B[p][AB_IDX[t]], ALIEN[p][XI[t]]))
        s = sum(score(x, y) for x, y in cells)
        print(f"P{p} {POINT_NAMES[p]:<24} alien-vs-A4b: {s:.1f}/12 = {s/12:.1%}")
    print("--- alien vs X3+B4 per point (16 cells) ---")
    for p in range(1, 10):
        cells = []
        for t in ("epi", "germ", "ether", "miasma", "newton", "phl", "qm", "rel"):
            cells.append((X3[p][XI[t]], ALIEN[p][XI[t]]))
            cells.append((B4[p][B4I[t]], ALIEN[p][XI[t]]))
        s = sum(score(x, y) for x, y in cells)
        print(f"P{p} {POINT_NAMES[p]:<24} {s:.1f}/16 = {s/16:.1%}")

    # ===== PART 4: READING RECORDS ON THE ELASTIC CELLS =====
    print("\n" + "-" * 76)
    print("PART 4 - READING RECORDS (A, B, X3, ALIEN, B4)")
    print("-" * 76)
    records = [
        ("Newton P6 (formalism)", ["S", "S", "P", "P", "P"]),
        ("Quantum P4 (derivation)", ["S", "S", "P", "S", "S"]),
        ("Germ P7 (founders)", ["-", "-", "P", "F", "F"]),
        ("Germ P4 (derivation)", ["-", "-", "F", "P", "P"]),
        ("Germ P6 (formalism as written)", ["-", "-", "F", "P", "F"]),
        ("Ether P6 (formalism)", ["S", "S", "S", "P", "P"]),
        ("Ether P3 (constant)", ["F", "F", "F", "P", "F"]),
        ("Ether P9 (crisis)", ["S", "S", "S", "P", "S"]),
        ("Epi P6 (formalism)", ["S", "S", "P", "P", "P"]),
        ("Phl P2 (unification)", ["S", "S", "P", "S", "P"]),
        ("Miasma P5 (embedding)", ["-", "-", "F", "F", "P"]),
        ("Miasma P9 (crisis)", ["-", "-", "F", "F", "F"]),
    ]
    print(f"{'Cell':<34} {'A':>2} {'B':>2} {'X3':>3} {'ALN':>4} {'B4':>3}")
    for name, rec in records:
        print(f"{name:<34} {rec[0]:>2} {rec[1]:>2} {rec[2]:>3} "
              f"{rec[3]:>4} {rec[4]:>3}")

    # ===== PART 5: DISCRIMINATOR CHECKS =====
    print("\n" + "-" * 76)
    print("PART 5 - CENSUS-KILLING CLAUSES (amended reading)")
    print("-" * 76)
    core = {1: "deletion", 3: "constant", 5: "embedding",
            6: "minted measurables", 8: "slope"}
    for t in ("epi", "ether", "phl", "miasma", "caloric"):
        codes = {p: B4[p][B4I[t]] for p in range(1, 10)}
        passed = [n for p, n in core.items() if codes[p] == "S"]
        print(f"  {t:<8} passes-as-S (B4): {passed if passed else 'NONE of the 5'}")
    print("\n  Thermodynamics, five discriminators (B4): "
          + ", ".join(f"{n}={B4[p][B4I['thermo']]}" for p, n in core.items()))
    print("  Thermodynamics, five discriminators (prereg): "
          + ", ".join(f"{n}={PREREG_A4D[p][1]}" for p, n in core.items()))
    print("  Caloric, five discriminators (prereg): "
          + ", ".join(f"{n}={PREREG_A4D[p][0]}" for p, n in core.items()))

    # ===== PART 6: AMENDMENT REPLICATION =====
    print("\n" + "-" * 76)
    print("PART 6 - AMENDMENT REPLICATION (does the alien / B4 land on the "
          "amended cells?)")
    print("-" * 76)
    checks = [
        ("A4c: Newton P6 elasticity (B4 reads P)", B4[6][B4I["newton"]] == "P"),
        ("A4c: Newton P6 elasticity (alien reads P)", ALIEN[6][XI["newton"]] == "P"),
        ("A4c: Newton P6 NOT replicated by alien-era pre-amendment A/B (both S)",
         CODER_A[6][AB_IDX["newton"]] == "S" and CODER_B[6][AB_IDX["newton"]] == "S"),
        ("A4b: phl P7 F (B4)", B4[7][B4I["phl"]] == "F"),
        ("A4b: ether P7 P (B4)", B4[7][B4I["ether"]] == "P"),
        ("A4c: epi P7 P - payment graduated (B4)", B4[7][B4I["epi"]] == "P"),
        ("A4c: phl P2 P - substance is not a joint (B4)", B4[2][B4I["phl"]] == "P"),
        ("A4b: ether P4 P (B4)", B4[4][B4I["ether"]] == "P"),
        ("A4c: ether P3 F under every family reading (B4)",
         B4[3][B4I["ether"]] == "F"),
        ("A4c: miasma P1 F with birth-window (B4)", B4[1][B4I["miasma"]] == "F"),
        ("A4c: germ P4 P revision (B4 + alien)",
         B4[4][B4I["germ"]] == "P" and ALIEN[4][XI["germ"]] == "P"),
        ("A4c: germ P3 F domain-marked (B4 + alien)",
         B4[3][B4I["germ"]] == "F" and ALIEN[3][XI["germ"]] == "F"),
        ("A4d prereg: caloric profile exact (B4)",
         all(B4[p][B4I["caloric"]] == PREREG_A4D[p][0] for p in range(1, 10))),
        ("A4d prereg: thermo 8/9 (only P4 contested)",
         sum(1 for p in range(1, 10)
             if B4[p][B4I["thermo"]] == PREREG_A4D[p][1]) == 8),
    ]
    for label, ok in checks:
        print(f"  {'CONFIRMED' if ok else 'NOT REPRODUCED':<14} {label}")

    # ===== PART 7: ALL-RUNS DOCKET =====
    print("\n" + "-" * 76)
    print("PART 7 - DOCKET: dead-side cells with any cross-run disagreement "
          "(5 readings)")
    print("-" * 76)
    for p in range(1, 10):
        for j, t in enumerate(("phl", "ether", "epi", "miasma")):
            vals = [CENSUS[p][j] if j < 3 else "-",
                    AMENDED[p][j], "-", "-",
                    X3[p][XI[t]], ALIEN[p][XI[t]], B4[p][B4I[t]]]
            vals = [v for v in vals if v != "-"]
            norm = {"C": "P"}
            vset = {norm.get(v, v) for v in vals}
            if len(vset) > 1:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<7} "
                      f"census {CENSUS[p][j] if j < 3 else '-'} | "
                      f"amended {AMENDED[p][j]} | X3 {X3[p][XI[t]]} | "
                      f"ALN {ALIEN[p][XI[t]]} | B4 {B4[p][B4I[t]]}")


if __name__ == "__main__":
    main()
