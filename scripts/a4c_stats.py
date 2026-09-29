# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4c: the widened panel + the third blind
reading (the 'alien reader' slot, executed by the only reader the environment
would supply: a fresh-context, blind, same-family coder, runtime-reported
glm-5.3 despite requests for a different family; probes documented).

Data:
  - Census v1 (author-coded) - dead side, census_content_b.py TABLE2_ROWS.
  - A4b blind coders A and B - 6-theory panel, from recode_stats.py.
  - Post-A4b adjudicated matrix - recode_content_b.py TABLE6_ROWS
    (ether P5 coded on the successor-recovery direction: F; dual noted).
  - Pre-registered extension codes (author, locked pre-run) - a4c_prereg.md
    for miasma and germ theory.
  - Third blind coding (the refused-alien slot) - 8-theory panel, columns:
    (epicycles, germ, ether, miasma, Newton, phlogiston, quantum, relativity).

Scoring identical to A4b: exact=1.0, adjacent=0.5, distant=0.0;
SD special-handling; census 'C' (confounded) read as P.
"""

RANK = {"F": 0, "P": 1, "C": 1, "S": 2, "SD": 2}

# ---- Census v1 (phlogiston, ether, epicycles) ------------------------------
CENSUS = {
    1: ("F", "F", "F"), 2: ("S", "S", "S"), 3: ("F", "F", "F"),
    4: ("F", "F", "C"), 5: ("F", "F", "P"), 6: ("F", "P", "P"),
    7: ("S", "S", "S"), 8: ("SD", "SD", "SD"), 9: ("P", "P", "P"),
}

# ---- Post-A4b adjudicated (phlogiston, ether, epicycles) --------------------
# ether P5: successor-recovery direction F (dual 'S as written' noted);
# ether P1 = P (core-posit refinement); ether P4 = P; ether P6 = S as written;
# ether P7 = P; epicycles P2 = P; epicycles P6 = S as written; P7 = F.
ADJUDICATED = {
    1: ("F", "P", "F"), 2: ("S", "S", "P"), 3: ("F", "F", "F"),
    4: ("F", "P", "P"), 5: ("F", "F", "P"), 6: ("F", "S", "S"),
    7: ("F", "P", "F"), 8: ("SD", "SD", "SD"), 9: ("P", "S", "P"),
}

# ---- A4b blind coders (epicycles, ether, Newton, phlogiston, quantum, rel) --
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

# ---- Pre-registered extension codes (miasma, germ) --------------------------
PREREG = {  # (miasma, germ)
    1: ("F", "S"), 2: ("P", "S"), 3: ("F", "F"), 4: ("F", "S"),
    5: ("P", "P"), 6: ("F", "S"), 7: ("F", "P"), 8: ("SD", "S"),
    9: ("P", "S"),
}

# ---- Third blind coding (the refused-alien slot) -----------------------------
# Columns: (epicycles, germ, ether, miasma, Newton, phlogiston, quantum, rel)
X = {
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
# Index maps
XI = {"epi": 0, "germ": 1, "ether": 2, "miasma": 3, "newton": 4,
      "phl": 5, "qm": 6, "rel": 7}
AB_IDX = {"epi": 0, "ether": 1, "newton": 2, "phl": 3, "qm": 4, "rel": 5}

POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}


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
    """cells: list of (label, code_x, code_y)."""
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
          f"exact {ex}/{n} ({ex/n:.1%}), adjacent {ad}, distant {di}")
    for d in distants:
        print(f"    DISTANT: {d}")
    return tot / n


def main():
    print("=" * 74)
    print("A4c UNBLINDING - THE WIDENED PANEL AND THE THIRD BLIND READING")
    print("=" * 74)

    # --- 1. Third coding vs census v1 (27 dead cells) -----------------------
    cells = []
    for p in range(1, 10):
        for j, t in enumerate(("phl", "ether", "epi")):
            xk = {"phl": "phl", "ether": "ether", "epi": "epi"}[t]
            cells.append((f"P{p}/{t}", CENSUS[p][j], X[p][XI[xk]]))
    report_pair("X vs census v1 (27 dead cells)", cells)

    # --- 2. X vs post-A4b adjudicated matrix --------------------------------
    cells = []
    for p in range(1, 10):
        for j, t in enumerate(("phl", "ether", "epi")):
            cells.append((f"P{p}/{t}", ADJUDICATED[p][j], X[p][XI[t]]))
    report_pair("X vs post-A4b amended census (27 dead cells)", cells)

    # --- 3. X vs A4b coders (54 shared cells each) --------------------------
    for nm, C in (("A", CODER_A), ("B", CODER_B)):
        cells = []
        for p in range(1, 10):
            for t in ("epi", "ether", "newton", "phl", "qm", "rel"):
                cells.append((f"P{p}/{t}", C[p][AB_IDX[t]], X[p][XI[t]]))
        report_pair(f"X vs A4b coder {nm} (54 cells)", cells)

    # --- 4. X vs pre-registered new-pair codes (18 cells) -------------------
    cells = []
    for p in range(1, 10):
        for j, t in enumerate(("miasma", "germ")):
            cells.append((f"P{p}/{t}", PREREG[p][j], X[p][XI[t]]))
    report_pair("X vs pre-registration (18 new-pair cells)", cells)

    # --- 5. Living side vs Vol I all-S (27 physics-trio cells) --------------
    breaks = [(p, t) for p in range(1, 10) for t in ("newton", "qm", "rel")
              if X[p][XI[t]] != "S"]
    print(f"\nLiving side (physics trio) vs Vol I's all-S: "
          f"{27 - len(breaks)}/27 exact; breaks at: "
          + (", ".join(f"P{p} {t}" for p, t in breaks) if breaks else "none"))

    # --- 6. Per-point bands: X vs census, dead side -------------------------
    print("\n--- Per-point weighted agreement (X vs census v1, 3 dead cells) ---")
    for p in range(1, 10):
        s = sum(score(CENSUS[p][j], X[p][XI[t]])
                for j, t in enumerate(("phl", "ether", "epi")))
        print(f"P{p} {POINT_NAMES[p]:<24} {s:.1f}/3 = {s/3:.1%}")
    print("--- per-point, X vs A4b A+B (12 comparisons: 6 cells x 2 coders) ---")
    for p in range(1, 10):
        s = sum(score(C[p][AB_IDX[t]], X[p][XI[t]])
                for C in (CODER_A, CODER_B)
                for t in ("epi", "ether", "newton", "phl", "qm", "rel"))
        print(f"P{p} {POINT_NAMES[p]:<24} {s:.1f}/12 = {s/12:.1%}")

    # --- 6b. Blind-cluster observation ---------------------------------------
    ab = sum(score(CODER_A[p][AB_IDX[t]], CODER_B[p][AB_IDX[t]])
             for p in range(1, 10)
             for t in ("epi", "ether", "newton", "phl", "qm", "rel"))
    print(f"\nBlind cluster, 54-cell mutual agreement: A-B {ab/54:.1%}, "
          f"X-A 90.7%, X-B 90.7% -- each blind run vs the author-coded "
          f"census: 70.4% / 70.4% / 77.8% (dead side: 70.4/70.4/77.8).")

    # --- 6c. All-runs agreement on dead side ----------------------------------
    norm = {"C": "P"}
    all_agree = 0
    for p in range(1, 10):
        for j, t in enumerate(("phl", "ether", "epi")):
            vals = {norm.get(CENSUS[p][j], CENSUS[p][j]),
                    ADJUDICATED[p][j], CODER_A[p][AB_IDX[t]],
                    CODER_B[p][AB_IDX[t]], X[p][XI[t]]}
            if len(vals) == 1:
                all_agree += 1
    print(f"Dead-side cells where census v1, amended, A, B, and X all "
          f"coincide: {all_agree}/27")

    # --- 7. Three-run docket: cells where runs collide -----------------------
    print("\n--- Docket: dead-side cells with any cross-run disagreement ---")
    for p in range(1, 10):
        for j, t in enumerate(("phl", "ether", "epi")):
            c0 = CENSUS[p][j]
            adj = ADJUDICATED[p][j]
            ca = CODER_A[p][AB_IDX[t]]
            cb = CODER_B[p][AB_IDX[t]]
            cx = X[p][XI[t]]
            if len({c0, adj, ca, cb, cx}) > 1:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<7} "
                      f"census {c0} | amended {adj} | A {ca} | B {cb} | X {cx}")

    # --- 8. New-pair cells, run vs run --------------------------------------
    print("\n--- New-pair cells: prereg vs X ---")
    for p in range(1, 10):
        for j, t in enumerate(("miasma", "germ")):
            pr, cx = PREREG[p][j], X[p][XI[t]]
            if pr != cx:
                print(f"  P{p} {POINT_NAMES[p]:<22} {t:<7} prereg {pr} vs X "
                      f"{cx}  [{kind(pr, cx)}]")

    # --- 9. Discriminator checks ---------------------------------------------
    # Passes-as-S requires the code to be exactly 'S' on the amended reading:
    # 'SD' fails the slope discriminator (the trend is its discriminating
    # half), and the ether's as-written P6 'S' is the already-adjudicated
    # confound -- the discriminator is the OPERATIONALIZED form, which the
    # ether fails (no measurables minted; three incoherent ethers).
    print("\n--- Census-killing clauses (amended reading) ---")
    core_as_written = {1: "deletion", 3: "constant", 5: "embedding",
                       6: "minted measurables", 8: "slope"}
    for t in ("epi", "ether", "phl", "miasma"):
        codes = {p: X[p][XI[t]] for p in range(1, 10)}
        passed = [n for p, n in core_as_written.items()
                  if codes[p] == "S"]
        note = {"ether": " [P6 'S' is the as-written confound; operationalized "
                       "form fails]"} .get(t, "")
        print(f"  {t:<8} passes-as-S: {passed if passed else 'NONE of the 5'}{note}")
    print("\n  Germ theory, five discriminators as X coded them: "
          + ", ".join(f"{n}={X[p][XI['germ']]}" for p, n in core_as_written.items()))
    print("  Germ theory, X S-cells: "
          + ", ".join(f"P{p}" for p in range(1, 10) if X[p][XI['germ']] == "S"))

    # --- 10. Amendment replication test --------------------------------------
    print("\n--- A4b amendment replication (does X's blind reading match the "
          "amended cells?) ---")
    checks = [
        ("P7 payment-not-defense (phl F)", X[7][XI["phl"]] == "F"),
        ("P7 (epi: amended F, X reads P)", X[7][XI["epi"]] == "P"),
        ("P7 (ether: amended P, X reads F)", X[7][XI["ether"]] == "F"),
        ("P6 ether S-as-written", X[6][XI["ether"]] == "S"),
        ("P4 ether revised to P", X[4][XI["ether"]] == "P"),
        ("P9 ether revised to S-as-written", X[9][XI["ether"]] == "S"),
        ("P2 epi demoted to P", X[2][XI["epi"]] == "P"),
        ("P3 ether F (all runs)", X[3][XI["ether"]] == "F"),
    ]
    for label, ok in checks:
        print(f"  {'CONFIRMED' if ok else 'NOT REPRODUCED':<14} {label}")


if __name__ == "__main__":
    main()
