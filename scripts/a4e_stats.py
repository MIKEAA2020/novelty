# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4e — the SECOND delivery of the alien
reading: two ten-theory codings (readers labeled "gpt" and "grok" by the
owner's repo file "novelty prompt2.txt"), both administered the ten-theory
replication kit externally by the series' owner.

Readings on file (lineage):
  - Census v1 (author) and the post-A4b / post-A4c / post-A4d states.
  - A4b blind coders A and B (6-theory panel).
  - Third blind reading X3 (8-theory panel, same family).
  - ALIEN = GPT-8 (8-theory panel, first external family, "novelty prompt.txt").
  - BLIND4 = B4 (10-theory panel, same family, fresh context).
  - A4d pre-registration: caloric + thermodynamics, locked before B4 ran.
  - NEW: GPT10 and GROK10 (10-theory panels, external families).

Scoring identical to A4b/A4c/A4d: exact=1.0, adjacent=0.5, distant=0.0;
SD special-handling (SD vs S/P = 0.5, SD vs SD = 1.0); census 'C' read as P.
Dual cells scored on their as-written face.
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}

# ---- Census v1 (phlogiston, ether, epicycles) ------------------------------
CENSUS = {
    1: ("F", "F", "F"), 2: ("S", "S", "S"), 3: ("F", "F", "F"),
    4: ("F", "F", "C"), 5: ("F", "F", "P"), 6: ("F", "P", "P"),
    7: ("S", "S", "S"), 8: ("SD", "SD", "SD"), 9: ("P", "P", "P"),
}

# ---- Post-A4c amended dead side (phl, ether, epi, miasma) -------------------
AMENDED_A4C = {
    1: ("F", "P", "F", "F"), 2: ("P", "S", "P", "P"), 3: ("F", "F", "F", "F"),
    4: ("F", "P", "P", "F"), 5: ("F", "F", "P", "F"), 6: ("F", "S", "S", "F"),
    7: ("F", "P", "P", "F"), 8: ("SD", "SD", "SD", "SD"), 9: ("P", "S", "P", "P"),
}

# ---- POST-A4D CENSUS STATE (the state the new readings are scored against) --
# Dead side letters (as-written faces; duals' first face):
#   phl:    F P F F F F F SD P      (P2 P*, P7 F-dagger)
#   ether:  P S F P P S P SD S      (P5 P*, P6 S-as-written*, P9 S-as-written demoted)
#   epi:    F P F P P S P SD P      (P2 P*, P6 S-as-written*)
#   miasma: F P F F F F F SD F
#   caloric:F P F P P P F SD P
# Living side:
#   newton: S S S S S [S/P dual -> S as written] S S S
#   qm, rel: all S
#   germ:   S S F P P [F as written / S op] P S S
#   thermo: S S P S S S P S S
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

# ---- ALIEN = GPT-8 (epi, germ, ether, miasma, newton, phl, qm, rel) ---------
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

# ---- BLIND4 = B4 (caloric, epi, germ, ether, miasma, newton, phl, qm, rel, thermo)
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

# ---- NEW: GPT-10 and GROK-10 (caloric, epi, germ, ether, miasma, newton,
#      phl, qm, rel, thermo) — parsed and verified by a4e_parse.py -------------
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

# ---- A4d pre-registration (caloric, thermo) ----------------------------------
PREREG_A4D = {
    1: ("F", "S"), 2: ("P", "S"), 3: ("F", "P"), 4: ("P", "S"),
    5: ("P", "S"), 6: ("P", "S"), 7: ("F", "P"), 8: ("SD", "S"),
    9: ("P", "S"),
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
    print("A4e UNBLINDING - THE SECOND DELIVERY: TWO TEN-THEORY ALIEN READINGS")
    print("=" * 76)

    # ===== PART 1: THE CONVERGENCE (alien vs alien, and vs the first alien) ==
    print("\n" + "-" * 76)
    print("PART 1 - THE CONVERGENCE BEFORE THE COMPARISON")
    print("-" * 76)
    g_vs_g = report_pair("GPT-10 vs GROK-10 (90 cells)",
        [(f"P{p}/{t}", GPT10[p][i], GROK10[p][i])
         for p in range(1, 10) for i, t in enumerate(T10)])
    g10_vs_g8 = report_pair("GPT-10 vs GPT-8 (72 shared cells)",
        [(f"P{p}/{t}", GPT10[p][1 + i], GPT8[p][i])
         for p in range(1, 10) for i, t in enumerate(T8)])
    k10_vs_g8 = report_pair("GROK-10 vs GPT-8 (72 shared cells)",
        [(f"P{p}/{t}", GROK10[p][1 + i], GPT8[p][i])
         for p in range(1, 10) for i, t in enumerate(T8)])

    # ===== PART 2: THE OUTGROUP TEST, RE-RUN ==================================
    print("\n" + "-" * 76)
    print("PART 2 - THE OUTGROUP TEST v2 (aliens vs every family reading)")
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
    fam.append(report_pair("FAMILY: B4 vs A4b coder A (54 cells)",
        [(f"P{p}/{t}", CODER_A[p][i], B4[p][1 + j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: B4 vs A4b coder B (54 cells)",
        [(f"P{p}/{t}", CODER_B[p][i], B4[p][1 + j])
         for p in range(1, 10) for i, t in enumerate(AB6)
         for j, t2 in enumerate(T8) if t2 == t]))
    fam.append(report_pair("FAMILY: B4 vs X3 (72 cells)",
        [(f"P{p}/{t}", X3[p][j], B4[p][1 + j])
         for p in range(1, 10) for j, t in enumerate(T8)]))
    fam.append(report_pair("FAMILY: A vs B (54 cells, for scale)",
        [(f"P{p}/{t}", CODER_A[p][i], CODER_B[p][i])
         for p in range(1, 10) for i, t in enumerate(AB6)]))
    print(f"\n>>> FAMILY MUTUAL BAND: {min(fam):.1%}-{max(fam):.1%} "
          f"(mean {sum(fam)/len(fam):.1%})")

    alien_fam = []
    for nm, RD, off in (("GPT-10", GPT10, 1), ("GROK-10", GROK10, 1)):
        alien_fam.append(report_pair(f"{nm} vs B4 (90 cells)",
            [(f"P{p}/{t}", B4[p][i], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10)]))
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        alien_fam.append(report_pair(f"{nm} vs X3 (72 cells)",
            [(f"P{p}/{t}", X3[p][j], RD[p][1 + j])
             for p in range(1, 10) for j, t in enumerate(T8)]))
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        for cn, CD in (("A", CODER_A), ("B", CODER_B)):
            alien_fam.append(report_pair(f"{nm} vs A4b coder {cn} (54 cells)",
                [(f"P{p}/{t}", CD[p][i], RD[p][1 + j])
                 for p in range(1, 10) for i, t in enumerate(AB6)
                 for j, t2 in enumerate(T8) if t2 == t]))
    print(f"\n>>> ALIEN-vs-FAMILY BAND: {min(alien_fam):.1%}-{max(alien_fam):.1%} "
          f"(mean {sum(alien_fam)/len(alien_fam):.1%})")
    print(f">>> ALIEN-vs-ALIEN: {g_vs_g:.1%}  |  ALIEN STABILITY (GPT-10 vs "
          f"GPT-8): {g10_vs_g8:.1%}")

    # ===== PART 3: ALIENS VS THE POST-A4D CENSUS =============================
    print("\n" + "-" * 76)
    print("PART 3 - THE TWO READINGS vs THE CENSUS (post-A4d state)")
    print("-" * 76)
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        report_pair(f"{nm} vs census post-A4d (90 cells)",
            [(f"P{p}/{t}", CENSUS_A4D[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10)])
    dead = ("phl", "ether", "epi", "miasma", "caloric")
    living = ("newton", "qm", "rel", "germ", "thermo")
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        report_pair(f"{nm} vs census DEAD side (45 cells)",
            [(f"P{p}/{t}", CENSUS_A4D[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10) if t in dead])
        report_pair(f"{nm} vs census LIVING side (45 cells)",
            [(f"P{p}/{t}", CENSUS_A4D[t][p - 1], RD[p][i])
             for p in range(1, 10) for i, t in enumerate(T10) if t in living])
    # new pair vs prereg
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        report_pair(f"{nm} vs A4d pre-registration (caloric+thermo, 18 cells)",
            [(f"P{p}/{t}", PREREG_A4D[p][j], RD[p][i])
             for p in range(1, 10) for j, t in enumerate(("caloric", "thermo"))
             for i, t2 in enumerate(T10) if t2 == t])

    # ===== PART 4: PER-POINT BANDS ===========================================
    print("\n" + "-" * 76)
    print("PART 4 - PER-POINT BANDS (aliens vs census, 10 cells per point)")
    print("-" * 76)
    for p in range(1, 10):
        sg = sum(score(CENSUS_A4D[t][p - 1], GPT10[p][i])
                 for i, t in enumerate(T10))
        sk = sum(score(CENSUS_A4D[t][p - 1], GROK10[p][i])
                 for i, t in enumerate(T10))
        print(f"P{p} {POINT_NAMES[p]:<24} gpt {sg:.1f}/10 = {sg/10:.1%}"
              f"   grok {sk:.1f}/10 = {sk/10:.1%}")

    # ===== PART 5: THE MOTION DOCKET ========================================
    print("\n" + "-" * 76)
    print("PART 5 - DOCKETS AND READING RECORDS")
    print("-" * 76)
    print("--- 5a. alien-vs-alien differing cells (all four) ---")
    for p in range(1, 10):
        for i, t in enumerate(T10):
            if GPT10[p][i] != GROK10[p][i]:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<8} "
                      f"gpt {GPT10[p][i]} vs grok {GROK10[p][i]}")
    print("--- 5b. unanimous external dissent vs census (both new aliens) ---")
    for p in range(1, 10):
        for i, t in enumerate(T10):
            c = CENSUS_A4D[t][p - 1]
            if GPT10[p][i] != c and GROK10[p][i] != c:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<8} census {c} | "
                      f"gpt {GPT10[p][i]} | grok {GROK10[p][i]}")
    print("--- 5c. full reading records on the elastic cells ---")
    recs = [
        ("phl P2",   ["S", "S", "P", "S", "P", "S", "S"], CENSUS_A4D["phl"][1]),
        ("miasma P1", ["-", "-", "P", "P", "F", "P", "P"], CENSUS_A4D["miasma"][0]),
        ("germ P7",  ["-", "-", "P", "F", "F", "F", "F"], CENSUS_A4D["germ"][6]),
        ("Newton P6", ["S", "S", "P", "P", "P", "P", "P"], "dual S/P"),
        ("epi P6",   ["S", "S", "P", "P", "P", "P", "P"], CENSUS_A4D["epi"][5]),
        ("ether P6", ["S", "S", "S", "P", "P", "P", "P"], CENSUS_A4D["ether"][5]),
        ("phl P6",   ["F", "F", "F", "P", "F", "P", "P"], CENSUS_A4D["phl"][5]),
        ("ether P3", ["F", "F", "F", "P", "F", "P", "P"], CENSUS_A4D["ether"][2]),
        ("ether P9", ["S", "S", "S", "P", "S", "P", "P"], CENSUS_A4D["ether"][8]),
        ("germ P2",  ["-", "-", "S", "P", "S", "P", "P"], CENSUS_A4D["germ"][1]),
        ("germ P6",  ["-", "-", "F", "P", "F", "P", "P"], "dual F/S"),
        ("caloric P1", ["-", "-", "-", "-", "F", "P", "P"], CENSUS_A4D["caloric"][0]),
        ("caloric P5", ["-", "-", "-", "-", "P", "F", "F"], CENSUS_A4D["caloric"][4]),
        ("caloric P7", ["-", "-", "-", "-", "F", "P", "F"], CENSUS_A4D["caloric"][6]),
        ("thermo P3", ["-", "-", "-", "-", "P", "P", "F"], CENSUS_A4D["thermo"][2]),
        ("thermo P4", ["-", "-", "-", "-", "S", "S", "P"], CENSUS_A4D["thermo"][3]),
        ("thermo P6", ["-", "-", "-", "-", "S", "P", "S"], CENSUS_A4D["thermo"][5]),
        ("thermo P7", ["-", "-", "-", "-", "P", "S", "S"], CENSUS_A4D["thermo"][6]),
    ]
    print(f"{'Cell':<13} {'A':>2} {'B':>2} {'X3':>3} {'G8':>3} {'B4':>3} "
          f"{'G10':>4} {'K10':>4}  census")
    for name, rec, cc in recs:
        print(f"{name:<13} {rec[0]:>2} {rec[1]:>2} {rec[2]:>3} {rec[3]:>3} "
              f"{rec[4]:>3} {rec[5]:>4} {rec[6]:>4}  {cc}")

    # ===== PART 6: KILLING CLAUSES ==========================================
    print("\n" + "-" * 76)
    print("PART 6 - CENSUS-KILLING CLAUSES UNDER THE NEW READINGS")
    print("-" * 76)
    core = {1: "deletion", 3: "constant", 5: "embedding",
            6: "measurables", 8: "slope"}
    for nm, RD in (("GPT-10", GPT10), ("GROK-10", GROK10)):
        for t in dead:
            codes = {p: RD[p][T10.index(t)] for p in range(1, 10)}
            passed = [n for p, n in core.items() if codes[p] == "S"]
            print(f"  {nm} {t:<8} passes-as-S: "
                  f"{passed if passed else 'NONE of the 5'}")
    print("\n  Thermodynamics five discriminators:")
    for nm, RD in (("census", None), ("GPT-10", GPT10), ("GROK-10", GROK10),
                   ("B4", B4)):
        if RD is None:
            vals = [CENSUS_A4D["thermo"][p - 1] for p in core]
        else:
            vals = [RD[p][T10.index("thermo")] for p in core]
        print(f"    {nm:<8} " + ", ".join(f"{n}={v}" for n, v in zip(core.values(), vals)))

    # ===== PART 7: EXPECTATION CHECKS =======================================
    print("\n" + "-" * 76)
    print("PART 7 - E1/E2 EXPECTATION CHECKS (A4d pre-registration)")
    print("-" * 76)
    checks = [
        ("E1: caloric P1 dissent expected (aliens P) - printed",
         GPT10[1][0] == "P" and GROK10[1][0] == "P"),
        ("E1: caloric disagreement concentrated P5/P6 (P5 F, P6 P)",
         GPT10[5][0] == "F" and GPT10[6][0] == "P"
         and GROK10[5][0] == "F" and GROK10[6][0] == "P"),
        ("E2: thermo P3 dissent-if-k-S read; aliens bracket P (gpt P / grok F)",
         GPT10[3][9] == "P" and GROK10[3][9] == "F"),
        ("E2: thermo P7 dissent-if-S read (aliens S)",
         GPT10[7][9] == "S" and GROK10[7][9] == "S"),
        ("Newton P6 dual's P-face replicated by both new aliens",
         GPT10[6][5] == "P" and GROK10[6][5] == "P"),
        ("Living trio still all-S except Newton P6 (both aliens)",
         all(GPT10[p][i] == "S" for p in range(1, 10)
             for i, t in enumerate(T10) if t in ("newton", "qm", "rel")
             and not (t == "newton" and p == 6))
         and all(GROK10[p][i] == "S" for p in range(1, 10)
                 for i, t in enumerate(T10) if t in ("newton", "qm", "rel")
                 and not (t == "newton" and p == 6))),
        ("GPT family self-replication 72/72 (gpt-10 = gpt-8)",
         all(GPT10[p][1 + j] == GPT8[p][j] for p in range(1, 10)
             for j in range(8))),
        ("GROK = GPT on the whole shared 8 (72/72)",
         all(GROK10[p][1 + j] == GPT8[p][j] for p in range(1, 10)
             for j in range(8))),
        ("Zero distant disagreements anywhere among the three aliens",
         all(kind(GPT10[p][i], GROK10[p][i]) != "DISTANT"
             for p in range(1, 10) for i in range(10))),
    ]
    for label, ok in checks:
        print(f"  {'CONFIRMED' if ok else 'NOT AS EXPECTED':<15} {label}")

    # ===== PART 8: THE UPDATED CENSUS (post-A4e) ============================
    print("\n" + "-" * 76)
    print("PART 8 - THE CENSUS AFTER A4e (rulings applied)")
    print("-" * 76)
    print("Moves by the motion rule (stable history-forks -> duals):")
    print("  phl P2    P*  -> dual  S original-wording / P law-vs-vocabulary")
    print("  miasma P1 F   -> dual  F birth-window / P tradition-at-large")
    print("  germ P7   P   -> dual  F as-written / P under the graduation")
    print("Confirmed: Newton P6 dual (P-face now 5 readings)")
    print("Defended (rule-forks recorded as cross-family constants):")
    print("  ether P3 F, epi/ether P6 S-as-written, phl P6 F(op), ether P9,")
    print("  germ P2 S, caloric P1/P5/P7, thermo P3/P4/P6/P7")


if __name__ == "__main__":
    main()
