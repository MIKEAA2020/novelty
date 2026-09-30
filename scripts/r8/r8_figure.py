#!/usr/bin/env python3
"""R8 EXECUTION - Step 6: the figure (3 panels)."""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import matplotlib.font_manager as fm
for _fp in ('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',):
    try:
        fm.fontManager.addfont(_fp)
    except Exception:
        pass
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
OUT = "/home/z/my-project/download"

C_DATA = "#9aa5b1"
C_FIT = "#1f6feb"
C_TILT = "#b3541e"
C_NULL = "#548235"
C_FLAG = "#c0392b"

gd = 1.544e-10   # fitted default


def nu_simple(y):
    return 1.0 / (1.0 - np.exp(-np.sqrt(y)))


def main():
    from r8_census_final import load, census
    rows = load("rar_dataset.csv")

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.4),
                             constrained_layout=True)

    # ---------------- Panel A: the RAR ----------------
    ax = axes[0]
    pts = list(csv.DictReader(open(os.path.join(DATA, "rar_points.csv"))))
    gb = np.array([float(p["gbar"]) for p in pts])
    go = np.array([float(p["gobs"]) for p in pts])
    ax.loglog(gb, go, ".", ms=2.2, color=C_DATA, alpha=0.5, rasterized=True)
    xs = np.logspace(-13.3, -8.4, 400)
    ax.loglog(xs, xs * nu_simple(xs / gd), "-", lw=2.0, color=C_FIT,
              label=f"fit: $g_\\dagger$ = {gd:.2e} m s$^{{-2}}$")
    ax.loglog(xs, xs, ":", lw=1.2, color="#333333", label="Newtonian ($g_{obs}=g_{bar}$)")
    ax.set_xlabel("$g_{bar}$  [m s$^{-2}$]")
    ax.set_ylabel("$g_{obs}$  [m s$^{-2}$]")
    ax.set_title("(a) The Radial Acceleration Relation\nSPARC, 175 galaxies, 3391 points",
                 fontsize=10.5)
    ax.legend(fontsize=8.5, loc="upper left", frameon=False)
    ax.set_xlim(1e-13, 10**-8.4)
    ax.set_ylim(1e-13, 10**-8.4)

    # ---------------- Panel B: the tilt ----------------
    ax = axes[1]
    lvf = np.array([r["lvf"] for r in rows if np.isfinite(r["lvf"])])
    r2 = np.array([r["r2"] for r in rows if np.isfinite(r["lvf"])])
    q = np.array([r["qual"] for r in rows if np.isfinite(r["lvf"])])
    ax.axhline(0, color="#666666", lw=0.8)
    ax.plot(lvf[q <= 2], r2[q <= 2], "o", ms=4.5, mfc=C_TILT, mec="none",
            alpha=0.65, label=f"Q$\\leq$2 (N={np.sum(q<=2)})")
    ax.plot(lvf[q == 3], r2[q == 3], "o", ms=4.5, mfc="#d9a066", mec="none",
            alpha=0.6, label=f"Q=3 (N={np.sum(q==3)})")
    sl, ic = np.polyfit(lvf, r2, 1)
    xf = np.linspace(lvf.min(), lvf.max(), 100)
    ax.plot(xf, np.polyval([sl, ic], xf), "-", lw=1.8, color="#7a3b0a")
    from scipy import stats as st
    rr = st.pearsonr(lvf, r2)
    ax.text(0.04, 0.955,
            f"r = {rr.statistic:+.2f}  (p = {rr.pvalue:.1e})\n"
            f"tilt = {sl*1.0:+.2f} dex per decade in $V_{{flat}}$",
            transform=ax.transAxes, va="top", fontsize=9,
            bbox=dict(fc="white", ec="#cccccc", alpha=0.9, pad=3))
    ax.set_xlabel("$\\log_{10}(V_{flat}$ / km s$^{-1}$)")
    ax.set_ylabel("RAR residual  [dex]")
    ax.set_title("(b) The residual tilt: the mass axis\n(Tier-2 residuals, default variant)",
                 fontsize=10.5)
    ax.legend(fontsize=8.5, loc="lower right", frameon=False)

    # ---------------- Panel C: the census ----------------
    ax = axes[2]
    recs = census(rows, "r2", None)
    names = ["bar\n(SB vs SA)", "morphology\n(T-type)", "environment\n(2MRS density)",
             "gas\nfraction", "interaction\n(nearest comp.)"]
    keys = ["bar_SB_vs_SA", "morphology_T", "environment_logN1", "gas_fraction",
            "interaction_logdnn"]
    rs = [next(x["r"] for x in recs if x["probe"] == k) for k in keys]
    ns = [next(x["n"] for x in recs if x["probe"] == k) for k in keys]
    fls = [next(x["floor"] for x in recs if x["probe"] == k) for k in keys]
    ps = [next(x["p"] for x in recs if x["probe"] == k) for k in keys]

    ypos = np.arange(5)[::-1]
    cols = [C_FLAG if abs(r) >= f else C_NULL for r, f in zip(rs, fls)]
    ax.barh(ypos, rs, height=0.62, color=cols, alpha=0.9)
    for y, r, f, n, p in zip(ypos, rs, fls, ns, ps):
        ax.text(0.02 if r >= 0 else -0.02, y,
                f"r={r:+.2f}, p={p:.3f}, N={n}",
                va="center", ha="left" if r >= 0 else "right",
                fontsize=7.6, transform=ax.get_yaxis_transform())
    ax.axvline(0.148, color="#c0392b", ls="--", lw=1.2)
    ax.axvline(-0.148, color="#c0392b", ls="--", lw=1.2)
    ax.axvline(0.194, color="#c0392b", ls=":", lw=1.2)
    ax.axvline(-0.194, color="#c0392b", ls=":", lw=1.2)
    ax.text(0.152, 4.62, "floor\n|r|=0.148", fontsize=7.3, color="#c0392b", va="top")
    ax.text(-0.152, 4.62, "floor\n|r|=0.148", fontsize=7.3, color="#c0392b",
            va="top", ha="right")
    ax.set_yticks(ypos)
    ax.set_yticklabels(names, fontsize=8.2)
    ax.set_xlim(-0.42, 0.42)
    ax.set_xlabel("Pearson r  (residual vs probe)")
    ax.set_title("(c) The five-probe census vs the floor\nred = clears floor; "
                 "dotted = Bonferroni (0.194)", fontsize=10.5)

    fig.suptitle("R8 executed: the residual census of the radial acceleration relation "
                 "(pre-registered floor: |r| = 0.148, N = 175)",
                 fontsize=11.5, y=1.06)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "R8_residual_census.png")
    fig.savefig(path, dpi=200)
    print("saved", path)


if __name__ == "__main__":
    main()
