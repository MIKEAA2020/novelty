# -*- coding: utf-8 -*-
"""Agreement analysis for the independent recoding (Amendment A4b).

Data: the three codings of the six-theory panel.
  - Coder 0 = the census (author-coded, unblinded) - dead side only, from
    census_content_b.py TABLE2_ROWS; trio side implied S by Vol I Table 4.
  - Coder A = blind coder A (fresh context, run 1)
  - Coder B = blind coder B (fresh context, run 2)

Scale ranks: F=0, P=1, S=2. "SD" (S then D) counts as rank 2 with a
degeneration flag; adjacency for SD is the same as S.
Weighted agreement: exact=1.0, adjacent (rank diff 1)=0.5, distant=0.0.
Census "confounded" on epicycles P4 is treated as P (rank 1).
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}  # C = census 'confounded'

# ---- Census Table 2 (dead theories) ---------------------------------------
# (point, phlogiston, ether, epicycles)
CENSUS = {
    1: ("F", "F", "F"),          # deletion at birth
    2: ("S", "S", "S"),          # unification
    3: ("F", "F", "F"),          # universal constant
    4: ("F", "F", "C"),          # derivation-first (epicycles = confounded)
    5: ("F", "F", "P"),          # conservative embedding
    6: ("F", "P", "P"),          # formalism / meaning
    7: ("S", "S", "S"),          # founders' resistance
    8: ("SD", "SD", "SD"),       # generative slope
    9: ("P", "P", "P"),          # crisis-chaining
}

# ---- Blind coder A (from the returned result) -----------------------------
CODER_A = {
    # T1 epicycles, T2 ether, T3 Newton, T4 phlogiston, T5 quantum, T6 relativity
    1: ("F", "P", "S", "F", "S", "S"),
    2: ("P", "S", "S", "S", "S", "S"),
    3: ("F", "F", "S", "F", "S", "S"),
    4: ("P", "S", "S", "F", "S", "S"),
    5: ("F", "S", "S", "F", "S", "S"),
    6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"),
    8: ("P", "SD", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
}

# ---- Blind coder B (from the returned result) -----------------------------
CODER_B = {
    1: ("F", "P", "S", "F", "S", "S"),
    2: ("P", "S", "S", "P", "S", "S"),
    3: ("F", "P", "S", "F", "S", "S"),
    4: ("P", "P", "S", "F", "S", "S"),
    5: ("P", "S", "S", "F", "S", "S"),
    6: ("S", "S", "S", "F", "S", "S"),
    7: ("F", "P", "S", "F", "S", "S"),
    8: ("SD", "S", "S", "SD", "S", "S"),
    9: ("P", "S", "S", "P", "S", "S"),
}

# Theory order in the blind tuples: (epicycles, ether, Newton, phlogiston,
# quantum, relativity) -> indices for the dead side: 0, 1, 3
DEAD_IDX = {"epicycles": 0, "ether": 1, "phlogiston": 3}
DEAD_ORDER = ["epicycles", "ether", "phlogiston"]  # census order: phl, ether, epi
CENSUS_ORDER = ["phlogiston", "ether", "epicycles"]
POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}


def score(c1, c2):
    """Weighted agreement. SD ('S then D') is a distinct code: the
    degeneration flag is the load-bearing half of P8, so SD vs S (flag
    missed) or SD vs P scores 0.5; SD vs SD scores 1.0."""
    if c1 == c2:
        return 1.0
    if {c1, c2} in ({"SD", "S"}, {"SD", "P"}):
        return 0.5
    d = abs(RANK[c1] - RANK[c2])
    if d == 0:
        return 1.0
    if d == 1:
        return 0.5
    return 0.0


def kind(c1, c2):
    if c1 == c2:
        return "exact"
    if {c1, c2} in ({"SD", "S"}, {"SD", "P"}):
        return "adjacent"
    d = abs(RANK[c1] - RANK[c2])
    return {0: "exact", 1: "adjacent", 2: "DISTANT"}[d]


def main():
    print("=" * 72)
    print("INDEPENDENT RECODING - AGREEMENT ANALYSIS")
    print("=" * 72)

    # --- Trio side (living): both coders vs Vol I's all-S profile ---
    for name, coder in (("A", CODER_A), ("B", CODER_B)):
        trio_S = all(coder[p][i] == "S" for p in coder for i in (2, 4, 5))
        print(f"\nTrio side, coder {name}: all 27 cells S -> {trio_S}")

    # --- Dead side: cell table ---
    print("\n--- Dead-side cells (census vs A vs B) ---")
    print(f"{'Point':<24}{'Phl (0/A/B)':<16}{'Ether (0/A/B)':<18}{'Epi (0/A/B)':<16}")
    tot_a = tot_b = 0.0
    exact_a = exact_b = 0
    distant_a = distant_b = 0
    per_point = {}
    for p in range(1, 10):
        row = []
        for theory in CENSUS_ORDER:
            c0 = CENSUS[p][CENSUS_ORDER.index(theory)]
            blind_idx = {"phlogiston": 3, "ether": 1, "epicycles": 0}[theory]
            ca = CODER_A[p][blind_idx]
            cb = CODER_B[p][blind_idx]
            sa, sb = score(c0, ca), score(c0, cb)
            tot_a += sa; tot_b += sb
            per_point.setdefault(p, []).extend([sa, sb])
            exact_a += (sa == 1.0); exact_b += (sb == 1.0)
            distant_a += (sa == 0.0); distant_b += (sb == 0.0)
            row.append(f"{c0}/{ca}/{cb}[{kind(c0, ca)},{kind(c0, cb)}]")
        print(f"P{p} {POINT_NAMES[p]:<22}" + "  ".join(row))

    n = 27
    print(f"\nCoder A vs census : weighted {tot_a:.1f}/{n} = {tot_a/n:.1%}"
          f" | exact {exact_a}/{n} = {exact_a/n:.1%} | distant {distant_a}")
    print(f"Coder B vs census : weighted {tot_b:.1f}/{n} = {tot_b/n:.1%}"
          f" | exact {exact_b}/{n} = {exact_b/n:.1%} | distant {distant_b}")

    print("\n--- Per-point weighted agreement (census vs A+B, 6 comparisons) ---")
    for p in range(1, 10):
        pts = per_point[p]
        print(f"P{p} {POINT_NAMES[p]:<22} {sum(pts):.1f}/6 = {sum(pts)/6:.1%}")

    # --- A vs B, all 54 cells ---
    exact = adjacent = distant = 0
    for p in range(1, 10):
        for i in range(6):
            k = kind(CODER_A[p][i], CODER_B[p][i])
            if k == "exact":
                exact += 1
            elif k == "adjacent":
                adjacent += 1
            else:
                distant += 1
    print(f"\nA vs B, all 54 cells: exact {exact}, adjacent {adjacent}, "
          f"distant {distant} -> weighted {(exact + 0.5*adjacent)/54:.1%}")

    dead_exact = dead_adj = dead_dist = 0
    for p in range(1, 10):
        for i in (0, 1, 3):
            k = kind(CODER_A[p][i], CODER_B[p][i])
            if k == "exact":
                dead_exact += 1
            elif k == "adjacent":
                dead_adj += 1
            else:
                dead_dist += 1
    print(f"A vs B, 27 dead cells: exact {dead_exact}, adjacent {dead_adj}, "
          f"distant {dead_dist} -> weighted {(dead_exact + 0.5*dead_adj)/27:.1%}")

    # --- Three-way exact agreement (census, A, B) on dead side ---
    three_way = 0
    three_way_cells = []
    norm = {"C": "P"}  # census 'confounded' ~ P
    for p in range(1, 10):
        for j, theory in enumerate(CENSUS_ORDER):
            c0 = norm.get(CENSUS[p][j], CENSUS[p][j])
            blind_idx = {"phlogiston": 3, "ether": 1, "epicycles": 0}[theory]
            if c0 == CODER_A[p][blind_idx] == CODER_B[p][blind_idx]:
                three_way += 1
                three_way_cells.append(f"P{p}-{theory[:3]}")
    print(f"\nThree-way exact (census=A=B), dead side: {three_way}/27 "
          f"= {three_way/27:.1%}")
    print("  cells:", ", ".join(three_way_cells))

    # --- Cells where BOTH coders contradict the census outright -------------
    print("\nBoth-coder outright contradictions of the census:")
    for p in range(1, 10):
        for j, theory in enumerate(CENSUS_ORDER):
            c0 = CENSUS[p][j]
            blind_idx = {"phlogiston": 3, "ether": 1, "epicycles": 0}[theory]
            ca, cb = CODER_A[p][blind_idx], CODER_B[p][blind_idx]
            if score(c0, ca) == 0 and score(c0, cb) == 0:
                print(f"  P{p} {POINT_NAMES[p]} / {theory}: census {c0} vs "
                      f"A {ca}, B {cb}")

    # --- Discriminator check: does any dead theory pass a discriminator ----
    # as-written (rank S) under the blind codings?
    print("\nDead theories coded S by any blind coder, by point:")
    for p in range(1, 10):
        hits = []
        for i, theory in ((0, "epicycles"), (1, "ether"), (3, "phlogiston")):
            if CODER_A[p][i] == "S" or CODER_B[p][i] == "S":
                hits.append(f"{theory} (A={CODER_A[p][i]}, B={CODER_B[p][i]})")
        if hits:
            print(f"  P{p} {POINT_NAMES[p]}: " + "; ".join(hits))


if __name__ == "__main__":
    main()
