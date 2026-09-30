#!/usr/bin/env python3
"""
R8 EXECUTION - Step 4: THE CENSUS.
The correlation matrix of RAR residuals against the five registered probes,
against the pre-registered floor (|r| >= 0.148 at N=175 = 2.2% of variance).

Probes (registered, Vol VII, R8):
  1. bar strength       (RC3 SB vs SA, binary; ordinal variant)
  2. morphology         (T-type)
  3. cosmic-web env.    (2MRS local projected density, log10(N_1Mpc+1))
  4. gas fraction       (Mgas/(Mstar+Mgas), U*=0.5 + 1.33 He)
  5. interaction stage  (log10 nearest-companion distance; close-comp flag;
                        RC3 peculiar flag)

Residuals: Tier-1 (fixed U*=0.5, raw galaxy offsets) and Tier-2
(per-galaxy U* and inclination fitted - the Li+2018 marginalization,
bounded version). PRIMARY = Tier-2 (the registered null is Li+2018's
marginalized residuals). All robustness variants printed.

Verdict logic (registered):
  - any probe with |r| >= floor(N) in the primary tier -> STRUCTURE
    (the "unstructured residuals" reading dies; R7(iii) note)
  - none -> NULL CENSUS at the floor (the deletion's discriminating cell
    holds; no support for the medium's residual-structure face at this floor)
"""
import csv
import math
import os

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def floor_r(n, alpha=0.05):
    """Minimum |r| for two-sided significance at level alpha, df=n-2."""
    t = stats.t.ppf(1 - alpha / 2, n - 2)
    return t / math.sqrt((n - 2) + t * t)


def corr(x, y):
    """Pearson + Spearman with pairwise-finite handling."""
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    x, y = x[ok], y[ok]
    n = len(x)
    if n < 10:
        return dict(n=n, pearson=np.nan, p_pearson=np.nan,
                    spearman=np.nan, p_spearman=np.nan)
    pr, pp = stats.pearsonr(x, y)
    sr, sp = stats.spearmanr(x, y)
    return dict(n=n, pearson=pr, p_pearson=pp, spearman=sr, p_spearman=sp)


def partial_corr(x, y, c):
    """Pearson partial correlation of x,y controlling c."""
    x, y, c = (np.asarray(a, float) for a in (x, y, c))
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(c)
    x, y, c = x[ok], y[ok], c[ok]
    if len(x) < 10:
        return np.nan, np.nan
    rx = x - np.polyval(np.polyfit(c, x, 1), c)
    ry = y - np.polyval(np.polyfit(c, y, 1), c)
    r, p = stats.pearsonr(rx, ry)
    return r, p


def load():
    ds = {r["Name"]: r for r in csv.DictReader(open(os.path.join(DATA, "rar_dataset.csv")))}
    pr = {r["Name"]: r for r in csv.DictReader(open(os.path.join(DATA, "probes.csv")))}
    rows = []
    for name, d in ds.items():
        if name not in pr:
            continue
        p = pr[name]
        rec = dict(
            name=name,
            r1=float(d["resid_fixed"]), r2=float(d["resid_ml"]),
            err=float(d["resid_err"]), T=float(d["T"]), fgas=float(d["fgas"]),
            dist=float(d["Dist"]), inc=float(d["inc"]), qual=int(d["Qual"]),
            Npts=int(d["Npts"]), f_Dist=int(d["f_Dist"]),
            ups=float(d["ups_fit"]),
            bar1=(float(p["bar1"]) if p["bar1"] not in ("", "None") else np.nan),
            bar3=(float(p["bar3"]) if p["bar3"] not in ("", "None") else np.nan),
            pec=(float(p["peculiar"]) if p["peculiar"] not in ("", "None") else np.nan),
            logN1=(math.log10(float(p["N_1Mpc"]) + 1.0)),
            logdnn=(float(p["log_dnn"]) if p["log_dnn"] not in ("", "nan") else np.nan),
            close=float(p["close_comp"]),
            vflat=float(d["Vflat"]) if d["Vflat"] else np.nan,
        )
        rows.append(rec)
    return rows


PROBES = [
    ("bar_strength_SB", "bar1", "binary"),
    ("morphology_T", "T", "cont"),
    ("environment_logN1", "logN1", "cont"),
    ("gas_fraction", "fgas", "cont"),
    ("interaction_logdnn", "logdnn", "cont"),
]


def run_census(rows, resid_key="r2", sel=None, label=""):
    """Correlation matrix of one residual variant against the 5 probes."""
    out = []
    for pname, key, kind in PROBES:
        x = [r[key] for r in rows if sel(r)]
        y = [r[resid_key] for r in rows if sel(r)]
        c = corr(x, y)
        fl = floor_r(c["n"])
        bonf = floor_r(c["n"], alpha=0.05 / 5)
        # linear amplitude: slope (dex per unit) and r*sigma (dex)
        xa, ya = np.asarray(x, float), np.asarray(y, float)
        ok = np.isfinite(xa) & np.isfinite(ya)
        if ok.sum() > 10:
            sl = np.polyfit(xa[ok], ya[ok], 1)[0]
            amp = abs(c["pearson"]) * np.std(ya[ok])
        else:
            sl = amp = np.nan
        out.append(dict(probe=pname, kind=kind, label=label, **c,
                        floor=fl, floor_bonf=bonf, slope=sl, amp_dex=amp))
    return out


def main():
    rows = load()
    print(f"N galaxies loaded: {len(rows)}")
    r2s = np.array([r["r2"] for r in rows])
    print(f"Tier-2 residual: rms {np.std(r2s):.4f} dex")

    results = []

    # ---------- PRIMARY: Tier-2 (marginalized), all galaxies ----------
    results += run_census(rows, "r2", lambda r: True, "PRIMARY Tier-2 all")
    # Tier-1 (raw fixed-U* offsets)
    results += run_census(rows, "r1", lambda r: True, "Tier-1 all")

    # ---------- robustness ----------
    results += run_census(rows, "r2", lambda r: r["qual"] <= 2, "T2 Q<=2")
    results += run_census(rows, "r2", lambda r: r["inc"] >= 50, "T2 i>=50")
    results += run_census(rows, "r2", lambda r: r["dist"] <= 40, "T2 D<=40")

    # ---------- write machine-readable matrix ----------
    cols = ["label", "probe", "kind", "n", "pearson", "p_pearson",
            "spearman", "p_spearman", "floor", "floor_bonf", "slope", "amp_dex"]
    with open(os.path.join(DATA, "r8_results.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in results:
            w.writerow({k: (f"{r[k]:.4f}" if isinstance(r[k], float) else r[k])
                        for k in cols})

    # ---------- console report ----------
    def show(label):
        print(f"\n===== {label} =====")
        print(f"{'probe':22s} {'N':>4s} {'r':>7s} {'p':>9s} {'rho':>7s} "
              f"{'floor':>6s} {'r>fl':>5s} {'amp(dex)':>8s}")
        for r in results:
            if r["label"] != label:
                continue
            flag = "YES" if (np.isfinite(r["pearson"]) and
                            abs(r["pearson"]) >= r["floor"]) else "-"
            print(f"{r['probe']:22s} {r['n']:4d} {r['pearson']:+7.3f} "
                  f"{r['p_pearson']:9.4f} {r['spearman']:+7.3f} "
                  f"{r['floor']:6.3f} {flag:>5s} "
                  f"{r['amp_dex'] if np.isfinite(r['amp_dex']) else float('nan'):8.4f}")

    show("PRIMARY Tier-2 all")
    show("Tier-1 all")

    # ---------- systematics panel (not probes) ----------
    print("\n===== systematics panel (Tier-2 residuals) =====")
    for nm, key in [("log Dist", lambda r: math.log10(r["dist"])),
                    ("inclination", lambda r: r["inc"]),
                    ("quality flag", lambda r: float(r["qual"])),
                    ("N points", lambda r: float(r["Npts"])),
                    ("Vflat", lambda r: r["vflat"])]:
        x = np.array([key(r) for r in rows])
        y = np.array([r["r2"] for r in rows])
        c = corr(x, y)
        print(f"  vs {nm:12s}: r={c['pearson']:+.3f} (p={c['p_pearson']:.3f}, "
              f"N={c['n']})  floor={floor_r(c['n']):.3f}")

    # ---------- partial correlations of interest ----------
    print("\n===== partial correlations (Tier-2) =====")
    x = np.array([r["fgas"] for r in rows]); y = np.array([r["r2"] for r in rows])
    c1 = np.array([r["T"] for r in rows])
    pr, pp = partial_corr(x, y, c1)
    print(f"  fgas | T       : r={pr:+.3f} (p={pp:.3f})")
    x = np.array([r["logN1"] for r in rows])
    c2 = np.array([math.log10(r["dist"]) for r in rows])
    pr, pp = partial_corr(x, y, c2)
    print(f"  env  | log D   : r={pr:+.3f} (p={pp:.3f})")
    pr, pp = partial_corr(x, y, c1)
    print(f"  env  | T       : r={pr:+.3f} (p={pp:.3f})")
    x = np.array([r["T"] for r in rows])
    c3 = np.array([r["fgas"] for r in rows])
    pr, pp = partial_corr(x, y, c3)
    print(f"  T    | fgas    : r={pr:+.3f} (p={pp:.3f})")

    # ---------- EFE direction check ----------
    print("\n===== EFE direction check =====")
    x = np.array([r["logN1"] for r in rows]); y = np.array([r["r2"] for r in rows])
    ok = np.isfinite(x) & np.isfinite(y)
    sl = np.polyfit(x[ok], y[ok], 1)[0]
    print(f"  MOND EFE predicts residual<0 in dense environments "
          f"(slope of resid vs env should be NEGATIVE)")
    print(f"  measured slope: {sl:+.4f} dex per dex "
          f"({'consistent' if sl < 0 else 'NOT consistent'} in sign)")

    # ---------- binary-flag probes ----------
    print("\n===== binary flags (Tier-2 residual means) =====")
    for nm, key in [("SB bars (1)", "bar1"), ("close comp (1)", "close"),
                    ("peculiar (1)", "pec")]:
        a = np.array([r["r2"] for r in rows if r[key] == 1 and np.isfinite(r[key])])
        b = np.array([r["r2"] for r in rows if r[key] == 0 and np.isfinite(r[key])])
        if len(a) < 3 or len(b) < 3:
            print(f"  {nm}: insufficient N ({len(a)}/{len(b)})")
            continue
        t, p = stats.ttest_ind(a, b, equal_var=False)
        print(f"  {nm:14s}: mean {a.mean():+.4f} (N={len(a)}) vs "
              f"{b.mean():+.4f} (N={len(b)}); diff {a.mean()-b.mean():+.4f} dex "
              f"(Welsh t={t:+.2f}, p={p:.4f})")

    print("\nsaved data/r8_results.csv")


if __name__ == "__main__":
    main()
