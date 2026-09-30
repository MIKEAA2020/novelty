# -*- coding: utf-8 -*-
"""Agreement analysis for Amendment A4g — the FOURTH delivery of the
alien reading (three readers at once: deepseek, opus [delivered twice,
verified identical], gemini 3.1 pro preview — twelve-theory panels,
verified by a4g_parse.py), the SIXTH blind coding (B6, fourteen-theory
panel, same family, fresh context), and the SEVENTH matched pair (the
fixity of the crust vs plate tectonics, pre-registered in
a4g_prereg.md before B6 ran).

Readings on file (lineage):
  - Census v1 (author) and the post-A4b / post-A4c / post-A4d /
    post-A4e / post-A4f states.
  - A4b blind coders A and B (6-theory panel, AB6 order).
  - Third blind reading X3 (8-theory panel, T8 order, same family).
  - GPT-8 (first alien, 8-theory panel, T8 order).
  - BLIND4 = B4 (10-theory panel, T10 order, same family).
  - GPT-10 and GROK-10 (A4e's two external readings, T10 order).
  - CLAUDE-10 (third external family, T10 order).
  - B5 (12-theory panel, T12 order, same family).
  - NEW: DEEPSEEK-12, OPUS-12, GEMINI-12 (fourth delivery — families
    four, five, and six; T12 order).
  - NEW: B6 (14-theory panel, T14 = T12 + crust + plate; same family).
  - A4g pre-registration: the fixity of the crust + plate tectonics,
    locked before B6 ran.

Scoring identical to A4b/A4c/A4d/A4e/A4f: exact=1.0, adjacent=0.5,
distant=0.0; SD special-handling (SD vs S/P = 0.5, SD vs SD = 1.0);
census 'C' read as P. Dual cells scored on their as-written faces.
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

DISCRIM = (1, 3, 5, 6, 8)   # deletion, constant, embedding, measurables,
                            # slope

POINT_NAMES = {
    1: "Deletion at birth", 2: "Unification", 3: "Universal constant",
    4: "Derivation-first", 5: "Conservative embedding",
    6: "Formalism / meaning", 7: "Founders' resistance",
    8: "Generative slope", 9: "Crisis-chaining",
}


def mk(order, mat):
    """mat: {point: tuple of cells in 'order' order} -> {theory: profile}"""
    return {t: tuple(mat[p][i] for p in range(1, 10))
            for i, t in enumerate(order)}


# ---- Census state: post-A4f, as-written faces -------------------------------
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
}

# ---- Readings (converted to theory-keyed profiles) ---------------------------
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

# ---- NEW: the fourth delivery (verified against the file by a4g_parse.py) ---
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
GEMINI = mk(T12, {
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

# ---- NEW: B6 — sixth blind reading, 14-theory panel (T14 order) --------------
B6 = mk(T14, {
    1: ("F", "S", "F", "F", "S", "P", "F", "S", "F", "S", "S", "S", "F", "S"),
    2: ("F", "S", "P", "F", "S", "S", "F", "S", "P", "S", "S", "S", "F", "S"),
    3: ("F", "F", "F", "F", "F", "P", "F", "S", "F", "S", "S", "P", "F", "F"),
    4: ("P", "S", "F", "F", "P", "P", "F", "S", "F", "S", "S", "P", "F", "P"),
    5: ("F", "P", "F", "F", "P", "P", "F", "S", "F", "S", "S", "S", "F", "P"),
    6: ("P", "F", "P", "F", "F", "S", "F", "P", "F", "S", "S", "S", "F", "P"),
    7: ("F", "S", "F", "F", "P", "F", "F", "S", "F", "S", "S", "S", "F", "P"),
    8: ("SD", "SD", "SD", "SD", "S", "SD", "SD", "S", "SD", "S", "S", "S", "SD", "S"),
    9: ("P", "S", "P", "F", "S", "P", "F", "S", "P", "S", "S", "S", "F", "S"),
})

# ---- A4g pre-registration (the seventh pair) ----------------------------------
PREREG = {
    "crust": ("F", "P", "F", "F", "P", "F", "F", "SD", "P"),
    "plate": ("S", "S", "F", "P", "P", "P", "P", "S", "S"),
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
    print("A4g UNBLINDING - FOURTH DELIVERY (3 FAMILIES) + SIXTH BLIND "
          "READING + SEVENTH PAIR")
    print("=" * 76)

    # ===== PART 1: THE FOURTH DELIVERY'S INTERNAL CONVERGENCE ==============
    print("\n" + "-" * 76)
    print("PART 1 - THE THREE NEW FAMILIES AMONG THEMSELVES (T12 panels)")
    print("-" * 76)
    cmp_theories("DEEPSEEK vs OPUS (108 cells)", DEEPSEEK, OPUS, T12)
    cmp_theories("DEEPSEEK vs GEMINI (108 cells)", DEEPSEEK, GEMINI, T12)
    cmp_theories("OPUS vs GEMINI (108 cells)", OPUS, GEMINI, T12)
    print("\n-- for scale, the prior aliens' mutuals (A4e/A4f) --")
    print("   GPT-10 vs GROK-10: 97.8% (both 100% with GPT-8)")
    print("   CLAUDE-10 vs GPT-10 / GROK-10: 86.7% / 86.7%")
    print("\n-- the new three vs the prior three (shared ten, 90 cells) --")
    for nm, rd in (("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS),
                   ("GEMINI", GEMINI)):
        cmp_theories(f"{nm} vs GPT-10 (90)", rd, GPT10, T10)
        cmp_theories(f"{nm} vs GROK-10 (90)", rd, GROK10, T10)
        cmp_theories(f"{nm} vs CLAUDE-10 (90)", rd, CLAUDE10, T10)

    # ===== PART 2: OUTGROUP TEST v4 (family band with B6) ==================
    print("\n" + "-" * 76)
    print("PART 2 - OUTGROUP TEST v4 (family band extended with B6)")
    print("-" * 76)
    fam = []
    fam.append(cmp_theories("FAMILY: B6 vs A (54)", B6, CODER_A, AB6))
    fam.append(cmp_theories("FAMILY: B6 vs B (54)", B6, CODER_B, AB6))
    fam.append(cmp_theories("FAMILY: B6 vs X3 (72)", B6, X3, T8))
    fam.append(cmp_theories("FAMILY: B6 vs B4 (90)", B6, B4, T10))
    fam.append(cmp_theories("FAMILY: B6 vs B5 (108)", B6, B5, T12))
    print("\n>>> B6's family agreements: "
          + ", ".join(f"{v:.1%}" for v in fam)
          + f" | mean {sum(fam)/len(fam):.1%}")
    print(">>> (A4f family mutual band: 88.0-94.4, mean 90.8)")

    print("\n-- the six aliens vs the family readings (shared cells) --")
    aliens = [("GPT-10", GPT10), ("GROK-10", GROK10), ("CLAUDE-10", CLAUDE10),
              ("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS), ("GEMINI", GEMINI)]
    for an, rd in aliens:
        vals = [
            cmp_theories(f"{an} vs A (54)", rd, CODER_A, AB6),
            cmp_theories(f"{an} vs B (54)", rd, CODER_B, AB6),
            cmp_theories(f"{an} vs X3 (72)", rd, X3, T8),
            cmp_theories(f"{an} vs B4 (90)", rd, B4, T10),
            cmp_theories(f"{an} vs B5 (90)", rd, B5, T10),
            cmp_theories(f"{an} vs B6 (90)", rd, B6, T10),
        ]
        print(f"  >>> {an} vs family mean: {sum(vals)/len(vals):.1%}")

    # ===== PART 3: THE NEW READINGS vs THE CENSUS (post-A4f) ===============
    print("\n" + "-" * 76)
    print("PART 3 - THE NEW READINGS vs THE CENSUS (post-A4f state)")
    print("-" * 76)
    for nm, rd in (("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS),
                   ("GEMINI", GEMINI), ("B6", B6)):
        cmp_theories(f"{nm} vs census (108 cells)", rd, CENSUS, T12)
    for nm, rd in (("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS),
                   ("GEMINI", GEMINI), ("B6", B6)):
        cmp_theories(f"{nm} vs census DEAD (54)", rd, CENSUS, DEAD12)
        cmp_theories(f"{nm} vs census LIVING (54)", rd, CENSUS, LIVE12)

    # ===== PART 4: PER-POINT BANDS (new readings vs census, 12 cells) ======
    print("\n" + "-" * 76)
    print("PART 4 - PER-POINT BANDS (new readings vs census, 12 cells each)")
    print("-" * 76)
    for p in range(1, 10):
        line = f"P{p} {POINT_NAMES[p]:<24}"
        for nm, rd in (("D", DEEPSEEK), ("O", OPUS), ("G", GEMINI),
                       ("B6", B6)):
            tot = sum(score(rd[t][p - 1], CENSUS[t][p - 1])
                      for t in T12)
            line += f" {nm} {tot:.1f}/12 = {tot/12:.1%}"
        print(line)

    # ===== PART 5: THE SEVENTH PAIR: B6 vs THE LOCKED PRE-REG ==============
    print("\n" + "-" * 76)
    print("PART 5 - THE SEVENTH PAIR: B6 vs THE LOCKED PRE-REGISTRATION")
    print("-" * 76)
    for nm, key in (("CRUST", "crust"), ("PLATE", "plate")):
        print(f"\n{nm}:")
        for p in range(1, 10):
            mark = ("  <-- differs" if B6[key][p - 1] != PREREG[key][p - 1]
                    else "")
            print(f"  P{p} {POINT_NAMES[p]:<24} prereg "
                  f"{PREREG[key][p-1]:<3} B6 {B6[key][p-1]}{mark}")
        tot = sum(score(B6[key][p - 1], PREREG[key][p - 1])
                  for p in range(1, 10))
        ex = sum(1 for p in range(1, 10)
                 if B6[key][p - 1] == PREREG[key][p - 1])
        print(f"  -> prereg vs B6: {tot/9:.1%} weighted, {ex}/9 exact")

    print("\n--- the earth-science middle band vs the biology residents "
          "(E2 test) ---")
    print("  Point                     germ  darwin  plate(B6)  "
          "plate(prereg)")
    for p in (3, 4, 5, 6, 7):
        print(f"  P{p} {POINT_NAMES[p]:<24} {CENSUS['germ'][p-1]:<6}"
              f"{CENSUS['darwin'][p-1]:<8}"
              f"{B6['plate'][p-1]:<11}{PREREG['plate'][p-1]}")

    # ===== PART 6: DOCKETS AND READING RECORDS ==============================
    print("\n" + "-" * 76)
    print("PART 6 - DOCKETS AND READING RECORDS")
    print("-" * 76)
    print("--- 6a. each new reading's unanimous-alone dissents vs census "
          "(the 12) ---")
    new4 = [("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS), ("GEMINI", GEMINI),
            ("B6", B6)]
    for nm, rd in new4:
        others = [m for n, m in new4 if n != nm]
        count = 0
        print(f"\n  {nm}:")
        for p in range(1, 10):
            for t in T12:
                c = CENSUS[t][p - 1]
                v = rd[t][p - 1]
                if v != c and all(o[t][p - 1] != v for o in others):
                    print(f"    P{p} {POINT_NAMES[p]:<22} {t:<8} "
                          f"census {c} | {nm} {v}")
                    count += 1
        if count == 0:
            print("    (none)")

    print("\n--- 6b. reading records on the elastic cells (13 coders) ---")
    readers = [("A", CODER_A), ("B", CODER_B), ("X3", X3), ("G8", GPT8),
               ("B4", B4), ("G10", GPT10), ("K10", GROK10),
               ("C10", CLAUDE10), ("B5", B5), ("D", DEEPSEEK),
               ("O", OPUS), ("G", GEMINI), ("B6", B6)]
    print("  Cell            " + " ".join(f"{n:<4}" for n, _ in readers)
          + "census")
    watch = [("newton", 3), ("newton", 6), ("ether", 5), ("ether", 6),
             ("epi", 6), ("phl", 2), ("caloric", 5), ("caloric", 9),
             ("thermo", 3), ("thermo", 4), ("germ", 7), ("miasma", 9),
             ("darwin", 4), ("darwin", 6), ("darwin", 7), ("darwin", 8),
             ("fixity", 5), ("fixity", 7), ("fixity", 9),
             ("crust", 2), ("crust", 5), ("crust", 9),
             ("plate", 4), ("plate", 6), ("plate", 7)]
    for t, p in watch:
        row = f"  {t} P{p:<12}"[:16].ljust(16)
        for _, rd in readers:
            v = rd[t][p - 1] if t in rd else "-"
            row += f"{v:<4}"
        row += CENSUS[t][p - 1] if t in CENSUS else "-"
        print(row)

    # ===== PART 7: CENSUS-KILLING CLAUSES UNDER THE NEW READINGS ============
    print("\n" + "-" * 76)
    print("PART 7 - CENSUS-KILLING CLAUSES (6 dead x 3 aliens; crust x B6)")
    print("-" * 76)
    print("  (five discriminators: deletion, constant, embedding, "
          "measurables, slope)")
    for nm, rd in (("DEEPSEEK", DEEPSEEK), ("OPUS", OPUS),
                   ("GEMINI", GEMINI)):
        for t in DEAD12:
            passes = [d for p, d in zip(DISCRIM, ("deletion", "constant",
                     "embedding", "measurables", "slope"))
                     if rd[t][p - 1] == "S"]
            print(f"  {nm:<9} {t:<8} passes-as-S: "
                  f"{passes if passes else 'NONE of the 5'}")
    passes = [d for p, d in zip(DISCRIM, ("deletion", "constant",
             "embedding", "measurables", "slope"))
             if B6["crust"][p - 1] == "S"]
    print(f"  {'B6':<9} {'crust':<8} passes-as-S: "
          f"{passes if passes else 'NONE of the 5'}")

    print("\n  The living residents, five discriminators (B6):")
    for t in list(LIVE12) + ["plate"]:
        pr = B6[t]
        print(f"    B6 {t:<8} deletion={pr[0]}, constant={pr[2]}, "
              f"embedding={pr[4]}, measurables={pr[5]}, slope={pr[7]}")

    # ===== PART 8: E1/E2/E6 EXPECTATION CHECKS ==================================
    print("\n" + "-" * 76)
    print("PART 8 - E1/E2/E6 EXPECTATION CHECKS (A4g pre-registration)")
    print("-" * 76)
    crust, plate = B6["crust"], B6["plate"]

    def check(msg, cond):
        print(f"  {'CONFIRMED' if cond else 'NOT CONFIRMED':<14} {msg}")

    check("E1: crust P1/P3/P6/P7 F under B6 (dead-row F's)",
          all(crust[p - 1] == "F" for p in (1, 3, 6, 7)))
    check("E1: crust P8 'S then D' (the settlement's generative phase)",
          crust[7] == "SD")
    check("E1: crust fails all five discriminators under B6 (no S)",
          all(crust[p - 1] != "S" for p in DISCRIM))
    check("E1: crust P2/P5/P9 = F (B6 emptier than prereg, the dissents "
          "printed)",
          all(crust[p - 1] == "F" for p in (2, 5, 9)))
    check("E2: plate P3 F (the domain-marked constant replicates in "
          "earth science)", plate[2] == "F")
    check("E2: plate P5 P (archive+machinery embedding, no limit "
          "recovery)", plate[4] == "P")
    check("E2: plate P6 P (the data-rereading face; B6's hedge)",
          plate[5] == "P")
    check("E2: plate P7 P (the graduated scale; the young-founders "
          "dissent printed)", plate[6] == "P")
    check("E6: plate profile = prereg EXACTLY (9/9)",
          plate == PREREG["plate"])
    check("E2: plate middle band P3/P4/P5/P6 = F/P/P/P",
          (plate[2], plate[3], plate[4], plate[5]) == ("F", "P", "P", "P"))
    check("E3: zero distant among the three new families' mutuals",
          all(kind(DEEPSEEK[t][p - 1], OPUS[t][p - 1]) != "DISTANT" and
              kind(DEEPSEEK[t][p - 1], GEMINI[t][p - 1]) != "DISTANT" and
              kind(OPUS[t][p - 1], GEMINI[t][p - 1]) != "DISTANT"
              for t in T12 for p in range(1, 10)))

    print("\n" + "=" * 76)
    print("END OF A4g UNBLINDING")
    print("=" * 76)


if __name__ == "__main__":
    main()
