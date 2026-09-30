#!/usr/bin/env python3
"""
R8 EXECUTION - Step 3: Build the five probes from public catalogs.

Probes (as registered in R8, Vol VII):
  A. morphology        -> T-type (SPARC table1, RC3 cross-check)
  B. gas fraction      -> M_gas/(M_star+M_gas) (SPARC table1, U*=0.5, 1.33 He)
  C. bar strength      -> RC3 coded type position 3: B=SB(2)/X=S unspecified(1)/
                          A=SA(0); binary bar flag; positional+name crossmatch
  D. cosmic-web environment -> 2MRS (Huchra+2012) local projected surface density
                          of K<11.75 neighbours within 1 Mpc (|dv|<500 km/s)
  E. interaction stage -> projected distance to nearest 2MRS companion
                          (|dv|<500 km/s); close-companion flag (<100 kpc)
Plus: RC3 'P' peculiar flag; galactic latitude (2MRS zone-of-avoidance check).
Output: data/probes.csv
"""
import csv
import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
H0 = 73.0            # SPARC's adopted H0 (Lelli+2016)
DV_WINDOW = 500.0    # km/s
RMAX_MPC = 3.0       # neighbour search radius


def norm_name(s):
    s = (s or "").strip().upper().replace(" ", "")
    # strip leading zeros in numeric part: UGC02885 -> UGC2885
    out = ""
    i = 0
    while i < len(s):
        c = s[i]
        if c.isalpha() or c == "-":
            out += c; i += 1
        elif c.isdigit() or c == "+":
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == "+"):
                j += 1
            num = s[i:j].lstrip("0") or "0"
            out += num
            i = j
        else:                      # any other char: keep it, ADVANCE (no hang)
            out += c; i += 1
    return out


def load_rc3():
    rows = []
    with open(os.path.join(DATA, "rc3_full.csv")) as f:
        for r in csv.DictReader(f):
            t = (r.get("type") or "").ljust(7)
            rows.append(dict(
                ra=float(r["RA2000"]) if r["RA2000"] else None,
                de=float(r["DE2000"]) if r["DE2000"] else None,
                names={norm_name(r.get(k) or "") for k in ("name", "altname")}
                     - {""},
                type=t, T=r.get("T") or "",
            ))
    return rows


def load_2mrs():
    ra, de, cz, glat = [], [], [], []
    with open(os.path.join(DATA, "2mrs_full.csv")) as f:
        for r in csv.DictReader(f):
            try:
                a = float(r["RAJ2000"]); d = float(r["DEJ2000"])
                z = float(r["cz"]) if r["cz"] else np.nan
                b = float(r["GLAT"]) if r["GLAT"] else np.nan
            except ValueError:
                continue
            if not (np.isfinite(a) and np.isfinite(d) and np.isfinite(z)):
                continue
            ra.append(a); de.append(d); cz.append(z); glat.append(b)
    return (np.array(ra), np.array(de), np.array(cz), np.array(glat))


def radec_to_gal(ra_deg, dec_deg):
    """J2000 -> galactic (approx, sufficient for |b| flagging)."""
    ra = np.radians(ra_deg); dec = np.radians(dec_deg)
    # north galactic pole (J2000)
    ra_ngp = np.radians(192.85948); dec_ngp = np.radians(27.12825)
    l_0 = np.radians(122.93192)
    sinb = (np.sin(dec_ngp) * np.sin(dec) +
            np.cos(dec_ngp) * np.cos(dec) * np.cos(ra - ra_ngp))
    b = np.degrees(np.arcsin(np.clip(sinb, -1, 1)))
    cosl = ((np.cos(dec) * np.cos(ra - ra_ngp)) /
            np.cos(np.radians(b)))
    sinl = np.sin(dec - dec_ngp) / np.cos(np.radians(b))
    l = l_0 + np.arctan2(sinl, cosl)
    return np.degrees(l) % 360, b


def ang_sep_deg(ra1, de1, ra2, de2):
    """Vincenty formula, arrays."""
    r1, d1, r2, d2 = map(np.radians, (ra1, de1, ra2, de2))
    sdl = np.sin(r2 - r1); cdl = np.cos(r2 - r1)
    sd1, cd1 = np.sin(d1), np.cos(d1)
    sd2, cd2 = np.sin(d2), np.cos(d2)
    num1 = cd2 * sdl
    num2 = cd1 * sd2 - sd1 * cd2 * cdl
    den = sd1 * sd2 + cd1 * cd2 * cdl
    return np.degrees(np.arctan2(np.hypot(num1, num2), den))


def decode_bar(rc3type):
    """RC3 coded type: pos2 family S/E/I, pos3 bar A/X/B, pos6 'P' peculiar."""
    if len(rc3type.strip()) == 0:
        return None, None
    t = rc3type
    fam = t[1] if len(t) > 1 else ""
    bar = t[2] if len(t) > 2 else ""
    if fam not in ("S",):
        return None, None      # E/I0 - not a disk-family classification
    b3 = {"B": 2, "X": 1, "A": 0}.get(bar, None)
    return b3, (2 if bar == "B" else (0 if bar == "A" else 1))


def main():
    # SPARC main table
    sparc = {}
    with open(os.path.join(DATA, "sparc_table1.csv")) as f:
        for r in csv.DictReader(f):
            sparc[r["Name"]] = dict(
                ra=float(r["_RA"]), de=float(r["_DE"]),
                dist=float(r["Dist"]) if r["Dist"] else np.nan,
                T=float(r["Type"]) if r["Type"] else np.nan,
                L36=float(r["L3_6"]) if r["L3_6"] else 0.0,
                MHI=float(r["MHI"]) if r["MHI"] else 0.0,
                Qual=int(r["Qual"]) if r["Qual"] else 0,
                NEDname=(r.get("NEDname") or "").strip(),
            )

    rc3 = load_rc3()
    ra2, de2, cz2, glat2 = load_2mrs()
    rc3_ra = np.array([r["ra"] if r["ra"] is not None else np.nan for r in rc3])
    rc3_de = np.array([r["de"] if r["de"] is not None else np.nan for r in rc3])
    print(f"RC3 rows: {len(rc3)}; 2MRS rows: {len(ra2)}")

    # index rc3 by normalized name
    by_name = {}
    for i, r in enumerate(rc3):
        for nm in r["names"]:
            by_name.setdefault(nm, []).append(i)

    # galactic latitude for SPARC galaxies
    sp_names = list(sparc.keys())
    sp_ra = np.array([sparc[n]["ra"] for n in sp_names])
    sp_de = np.array([sparc[n]["de"] for n in sp_names])
    _, sp_glat = radec_to_gal(sp_ra, sp_de)

    out = []
    for k, name in enumerate(sp_names):
        g = sparc[name]
        norm = norm_name(name)
        cand_names = {norm}
        if g["NEDname"]:
            cand_names.add(norm_name(g["NEDname"]))
        # 1. name match
        idx = None; how = "none"
        for nm in cand_names:
            if nm in by_name:
                idx = by_name[nm][0]; how = "name"
                break
        # 2. positional fallback within 1.5 arcmin
        if idx is None:
            seps = ang_sep_deg(g["ra"], g["de"], rc3_ra, rc3_de)
            seps[~np.isfinite(seps)] = 999
            j = int(np.argmin(seps))
            if seps[j] <= 1.5 / 60:
                idx = j; how = "pos"
        bar3 = bar1 = pec = None
        if idx is not None:
            bar3, bar1 = decode_bar(rc3[idx]["type"])
            pec = 1 if "P" in rc3[idx]["type"] else 0

        # ---- 2MRS environment ----
        v = H0 * g["dist"]
        sel = np.abs(cz2 - v) < DV_WINDOW
        nra, nde = ra2[sel], de2[sel]
        if len(nra):
            sep = ang_sep_deg(g["ra"], g["de"], nra, nde)
            # exclude the galaxy itself (matches within 2 arcmin AND similar cz)
            selfmask = sep > 2.0 / 60
            proj = g["dist"] * 1000.0 * np.sin(np.radians(sep))  # kpc
            proj = proj[selfmask]; sep_ok = sep[selfmask]
            n1 = int(np.sum(proj < 1000.0))
            n2 = int(np.sum(proj < 2000.0))
            dnn = float(np.min(proj)) if len(proj) else np.nan
            close = 1 if (np.isfinite(dnn) and dnn < 100.0) else 0
        else:
            n1 = n2 = 0; dnn = np.nan; close = 0

        out.append(dict(
            Name=name, match=how, bar3=bar3, bar1=bar1, peculiar=pec,
            rc3_type=(rc3[idx]["type"].strip() if idx is not None else ""),
            N_1Mpc=n1, N_2Mpc=n2, d_nn_kpc=dnn,
            log_dnn=(math.log10(dnn) if np.isfinite(dnn) and dnn > 0 else np.nan),
            close_comp=close, v_est=v,
            GLAT=round(float(sp_glat[k]), 2),
            zoa=(1 if abs(sp_glat[k]) < 5 else 0),
        ))

    cols = list(out[0].keys())
    with open(os.path.join(DATA, "probes.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow(r)

    nm = sum(1 for r in out if r["match"] != "none")
    print(f"RC3 matched: {nm}/{len(out)}  (name: "
          f"{sum(1 for r in out if r['match']=='name')}, pos: "
          f"{sum(1 for r in out if r['match']=='pos')})")
    b = [r["bar3"] for r in out if r["bar3"] is not None]
    print(f"RC3 bar classes: SB(2)={b.count(2)}, S/X(1)={b.count(1)}, "
          f"SA(0)={b.count(0)}, unmatched={len(out)-len(b)}")
    print(f"peculiar flags: {sum(1 for r in out if r['peculiar']==1)}")
    print(f"close companions (<100 kpc): {sum(1 for r in out if r['close_comp']==1)}")
    print(f"ZoA galaxies (|b|<5): {sum(1 for r in out if r['zoa']==1)}")
    print("saved data/probes.csv")


if __name__ == "__main__":
    main()
