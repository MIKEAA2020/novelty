#!/usr/bin/env python3
"""
R8 EXECUTION - Step 2 (v3): Build the RAR dataset, final methodology.

Published-null anchor (Li et al. 2018, A&A 615, A3, arXiv:1803.00022):
"We use the Markov Chain Monte Carlo method to fit the mean RAR to 175 individual
galaxies in the SPARC database, marginalizing over stellar mass-to-light ratio,
galaxy distance, and disk inclination... The residuals around these fits have an
rms scatter of only 0.057 dex."

Implementation here (documented deviations, all conservative):
- Global g_dagger: error-weighted, each galaxy normalized to equal total weight
  ("the mean RAR of 175 galaxies"), simple interpolating function.
- TIER 1 residual: per-galaxy error-weighted mean of log10(g_obs/g_fit) at
  fixed U*=0.5, published distance & inclination  [the raw galaxy offset]
- TIER 2 residual: after per-galaxy nuisance fit of (U*, i) on a bounded grid
  U* in [0.3,0.9], i in [i0-e_i, i0+e_i] (Li's marginalization, bounded
  version; distance held at published value)
Weights: w = (Vobs/e_Vobs)^2, e_Vobs floored at 2 km/s (SPARC systematics floor).
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

EV_FLOOR = 2.0
UPS_DEFAULT = 0.5
G_UNIT = 1e6 / 3.0857e19  # (km/s)^2/kpc -> m/s^2

VARIANT = (sys.argv[1] if len(sys.argv) > 1 else "default")
# default      : as documented (fitted g_dagger)
# gd120        : g_dagger fixed at 1.20e-10 (Li+2018 value)
# press        : pressure-support correction for low-V systems (sigma=8 km/s,
#                applied where Vflat<100 km/s or unknown: Vc^2 = Vobs^2 + 2 sigma^2)
GD_FIXED = 1.20e-10
SIGMA_PRESS = 8.0

NU_UPS = [(0.30 + 0.01 * k) for k in range(61)]   # 0.30..0.90


def nu_simple(y):
    return 1.0 / (1.0 - np.exp(-np.sqrt(y)))


def g_fit(gbar, gdagger, nu=nu_simple):
    return gbar * nu(gbar / gdagger)


def load_all():
    gal = {}
    with open(os.path.join(DATA, "sparc_table1.csv")) as f:
        for r in csv.DictReader(f):
            gal[r["Name"]] = dict(
                T=float(r["Type"]) if r["Type"] else np.nan,
                Dist=float(r["Dist"]) if r["Dist"] else np.nan,
                f_Dist=int(r["f_Dist"]) if r["f_Dist"] else 0,
                inc=float(r["i"]) if r["i"] else np.nan,
                e_inc=float(r["e_i"]) if r["e_i"] else 0.0,
                L36=float(r["L3_6"]) if r["L3_6"] else 0.0,
                MHI=float(r["MHI"]) if r["MHI"] else 0.0,
                Vflat=float(r["Vflat"]) if r["Vflat"] else np.nan,
                Qual=int(r["Qual"]) if r["Qual"] else 0,
                S4G=int(r["S4G"]) if r["S4G"] else 0,
                RA=float(r["_RA"]) if r["_RA"] else np.nan,
                DE=float(r["_DE"]) if r["_DE"] else np.nan,
            )
    pts = {}
    with open(os.path.join(DATA, "sparc_table2_massmodels.csv")) as f:
        for r in csv.DictReader(f):
            name = r["Name"]
            try:
                R = float(r["Rad"]); Vobs = float(r["Vobs"])
                eV = float(r["e_Vobs"]); Vgas = float(r["Vgas"]) if r["Vgas"] else 0.0
                Vdisk = float(r["Vdisk"]) if r["Vdisk"] else 0.0
                Vbul = float(r["Vbulge"]) if r["Vbulge"] else 0.0
            except ValueError:
                continue
            if R <= 0 or Vobs <= 0 or np.isnan(Vobs):
                continue
            eV = max(eV, EV_FLOOR)
            vf = gal.get(name, {}).get("Vflat", np.nan)
            if VARIANT == "press" and ((np.isfinite(vf) and vf < 100.0) or
                                        (not np.isfinite(vf))):
                Vobs_corr = math.sqrt(Vobs**2 + 2.0 * SIGMA_PRESS**2)
            else:
                Vobs_corr = Vobs
            d = pts.setdefault(name, {"R": [], "Vobs": [], "eV": [], "gobs": [],
                                       "glum": [], "ggas": []})
            d["R"].append(R); d["Vobs"].append(Vobs_corr); d["eV"].append(eV)
            d["gobs"].append(G_UNIT * Vobs_corr**2 / R)
            d["glum"].append(G_UNIT * (Vdisk**2 + Vbul**2) / R)
            d["ggas"].append(G_UNIT * Vgas**2 / R)
    for name, d in pts.items():
        for k in d:
            d[k] = np.array(d[k], float)
    return gal, pts


def galaxy_offset(d, gd, ups, inc, inc0):
    """Error-weighted mean log-residual with inclination-adjusted gobs."""
    gobs = d["gobs"] * (math.sin(math.radians(inc0)) /
                        math.sin(math.radians(inc)))**2
    gbar = ups * d["glum"] + d["ggas"]
    resid = np.log10(gobs) - np.log10(g_fit(gbar, gd))
    w = (d["Vobs"] / d["eV"])**2
    return float(np.sum(w * resid) / w.sum()), float(np.std(resid))


def _global_sse(log_gd, names, pts, w_pre, ups=UPS_DEFAULT):
    gd = 10**log_gd
    tot = 0.0
    for n in names:
        d = pts[n]
        gbar = ups * d["glum"] + d["ggas"]
        resid = np.log10(d["gobs"]) - np.log10(g_fit(gbar, gd))
        w = w_pre[n]
        tot += np.sum(w * resid**2) / w.sum()
    return tot


def main():
    gal, pts = load_all()
    names = [n for n in pts if n in gal]
    print(f"galaxies with mass models + table1 entries: {len(names)}")

    # ---- global g_dagger: per-galaxy-normalized error weighting ----
    w_pre = {n: (pts[n]["Vobs"] / pts[n]["eV"])**2 for n in names}
    from scipy.optimize import minimize_scalar as _ms
    _res = _ms(lambda lg: _global_sse(lg, names, pts, w_pre),
               bounds=(-10.6, -8.7), method="bounded", options={"xatol": 1e-9})
    if VARIANT == "gd120":
        gd = 1.20e-10
    else:
        gd = 10**_res.x
    print(f"VARIANT={VARIANT}; global g_dagger = {gd:.3e} m/s^2  "
          f"[Li+2018: 1.20e-10; MOND a0 1.2e-10]")

    rows = []
    for n in names:
        d, g = pts[n], gal[n]
        # Tier 1: fixed U*, published i
        r1, scat = galaxy_offset(d, gd, UPS_DEFAULT, g["inc"], g["inc"])
        # Tier 2: nuisance grid (U*, i)
        i0, ei = g["inc"], g["e_inc"] if g["e_inc"] > 0 else 3.0
        i_grid = np.linspace(max(20, i0 - ei), min(89.9, i0 + ei), 15)
        best2 = (np.inf, None, None)
        for ups in NU_UPS:
            for ii in i_grid:
                r2, _ = galaxy_offset(d, gd, ups, ii, i0)
                if abs(r2) < abs(best2[0]):
                    best2 = (r2, ups, ii)
        r2, ups_fit, inc_fit = best2
        w = w_pre[n]
        sig = math.sqrt(1.0 / w.sum()) * 2.0 / math.log(10)
        rows.append(dict(
            Name=n, Npts=len(d["gobs"]),
            resid_fixed=r1, resid_ml=r2, ups_fit=ups_fit, inc_fit=inc_fit,
            internal_scatter=scat, resid_err=sig,
            T=g["T"], Dist=g["Dist"], f_Dist=g["f_Dist"], inc=g["inc"],
            L36=g["L36"], MHI=g["MHI"], Vflat=g["Vflat"], Qual=g["Qual"],
            S4G=g["S4G"], RA=g["RA"], DE=g["DE"],
            fgas=(1.33 * g["MHI"]) / (UPS_DEFAULT * g["L36"] + 1.33 * g["MHI"])
            if (g["L36"] > 0 or g["MHI"] > 0) else np.nan,
        ))

    r1s = np.array([r["resid_fixed"] for r in rows])
    r2s = np.array([r["resid_ml"] for r in rows])
    q12 = np.array([r["Qual"] <= 2 for r in rows])
    print(f"N = {len(rows)}")
    print(f"Tier-1 (fixed U*, published i) galaxy-offset rms: "
          f"{np.std(r1s):.4f} dex  [{r1s.min():+.3f}, {r1s.max():+.3f}]")
    print(f"Tier-1 rms, Q<=2 subsample (N={q12.sum()}): "
          f"{np.std(r1s[q12]):.4f} dex")
    print(f"Tier-2 (free U*, i) residual rms: {np.std(r2s):.4f} dex  "
          f"[{r2s.min():+.3f}, {r2s.max():+.3f}]")
    print(f"Tier-2 rms, Q<=2 subsample: {np.std(r2s[q12]):.4f} dex")
    print("[Li+2018 with full marginalization: 0.057 dex per-galaxy fits]")

    cols = list(rows[0].keys())
    suffix = "" if VARIANT == "default" else "_" + VARIANT
    with open(os.path.join(DATA, f"rar_dataset{suffix}.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"saved data/rar_dataset{suffix}.csv")


if __name__ == "__main__":
    main()
