#!/usr/bin/env python3
"""
R8 EXECUTION - Step 5 (FINAL): the census matrix, the figure, the verdict.

Final probe set (registered five, executable realizations):
  bar       : RC3 definite classes only: SB(1) vs SA(0); X/'.'/I/unmatched -> excluded
  morphology: T-type (SPARC)
  environment: log10(N_2MRS_1Mpc + 1)
  gas fraction: Mgas/(Mstar+Mgas), U*=0.5, He x1.33
  interaction: log10(d_nn) nearest 2MRS companion

Residual tiers: T1 = fixed U*; T2 = per-galaxy (U*, i) marginalization (PRIMARY).
Variants: default (fitted g_dagger), gd120 (g_dagger=1.20e-10), press (sigma=8 km/s
pressure support for Vflat<100).
Panels: all galaxies; Q<=2 (the SPARC quality cut).
"""
import csv
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r8_census import corr, floor_r, partial_corr  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def load(dsfile="rar_dataset.csv"):
    ds = {r["Name"]: r for r in csv.DictReader(open(os.path.join(DATA, dsfile)))}
    pr = {r["Name"]: r for r in csv.DictReader(open(os.path.join(DATA, "probes.csv")))}
    rows = []
    for name, d in ds.items():
        if name not in pr:
            continue
        p = pr[name]
        b3 = p["bar3"]
        bar = np.nan
        if b3 not in ("", "None"):
            b3 = float(b3)
            if b3 == 2:
                bar = 1.0
            elif b3 == 0:
                bar = 0.0
        vf = float(d["Vflat"]) if d["Vflat"] else np.nan
        rows.append(dict(
            name=name, r1=float(d["resid_fixed"]), r2=float(d["resid_ml"]),
            err=float(d["resid_err"]), T=float(d["T"]), fgas=float(d["fgas"]),
            dist=float(d["Dist"]), qual=int(d["Qual"]), inc=float(d["inc"]),
            vflat=vf, lvf=(math.log10(vf) if vf == vf and vf > 0 else np.nan),
            logN1=math.log10(int(p["N_1Mpc"]) + 1.0),
            logdnn=(float(p["log_dnn"]) if p["log_dnn"] not in ("", "nan") else np.nan),
            bar=bar))
    return rows


PROBES = [
    ("bar_SB_vs_SA", "bar"),
    ("morphology_T", "T"),
    ("environment_logN1", "logN1"),
    ("gas_fraction", "fgas"),
    ("interaction_logdnn", "logdnn"),
]


def census(rows, resid="r2", qcut=None):
    out = []
    sub = [r for r in rows if (qcut is None or r["qual"] <= qcut)]
    y = np.array([r[resid] for r in sub])
    for pname, key in PROBES:
        x = np.array([r[key] for r in sub])
        c = corr(x, y)
        out.append(dict(probe=pname, n=c["n"], r=c["pearson"], p=c["p_pearson"],
                        rho=c["spearman"], p_rho=c["p_spearman"],
                        floor=floor_r(c["n"]),
                        floor_bonf=floor_r(c["n"], 0.05 / 5)))
    # tilt documentation (systematics panel, not a registered probe)
    x = np.array([r["lvf"] for r in sub])
    c = corr(x, y)
    out.append(dict(probe="[tilt] logVflat", n=c["n"], r=c["pearson"],
                    p=c["p_pearson"], rho=c["spearman"], p_rho=c["p_spearman"],
                    floor=floor_r(c["n"]), floor_bonf=floor_r(c["n"], 0.05 / 5)))
    pr, pp = partial_corr(x, y, np.array([r["T"] for r in sub]))
    out.append(dict(probe="[tilt] logVflat|T", n=c["n"], r=pr, p=pp, rho=np.nan,
                    p_rho=np.nan, floor=floor_r(c["n"]),
                    floor_bonf=floor_r(c["n"], 0.05 / 5)))
    return out


def main():
    variants = [("default", "rar_dataset.csv"),
                ("gd120", "rar_dataset_gd120.csv"),
                ("press", "rar_dataset_press.csv")]
    all_out = []
    print(f"{'variant':9s} {'panel':6s} {'resid':5s} {'probe':22s} {'N':>4s} "
          f"{'r':>7s} {'p':>8s} {'floor':>6s} {'clears':>6s}")
    for vname, fname in variants:
        rows = load(fname)
        for panel, qcut, resid in [("all", None, "r2"), ("Q<=2", 2, "r2"),
                                    ("all", None, "r1")]:
            rlab = "T2" if resid == "r2" else "T1"
            for rec in census(rows, resid, qcut):
                clears = ("YES" if (np.isfinite(rec["r"]) and abs(rec["r"]) >= rec["floor"])
                          else "-")
                all_out.append(dict(variant=vname, panel=panel, tier=rlab, **rec))
                print(f"{vname:9s} {panel:6s} {rlab:5s} {rec['probe']:22s} "
                      f"{rec['n']:4d} {rec['r']:+7.3f} {rec['p']:8.4f} "
                      f"{rec['floor']:6.3f} {clears:>6s}")

    cols = ["variant", "panel", "tier", "probe", "n", "r", "p", "rho", "p_rho",
            "floor", "floor_bonf"]
    with open(os.path.join(DATA, "r8_results_final.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in all_out:
            w.writerow({k: (f"{r[k]:.4f}" if isinstance(r[k], float) else r[k])
                        for k in cols})
    print("\nsaved data/r8_results_final.csv")


if __name__ == "__main__":
    main()
