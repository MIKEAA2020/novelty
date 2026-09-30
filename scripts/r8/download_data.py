#!/usr/bin/env python3
"""
R8 EXECUTION - Step 1: Data acquisition (v2, corrected table names).
Public data for the R8 residual census, via VizieR TAP:
  1. SPARC main table  (J/AJ/152/157/table1) - 175 galaxies
  2. SPARC mass models (J/AJ/152/157/table2) - 3391 points (Rad,Vobs,eVobs,Vgas,Vdisk,Vbulge)
  3. RC3               (VII/155/rc3)        - 23011 rows (coded type incl. bars + peculiar)
  4. 2MRS              (J/ApJS/199/26/table3) - 44599 rows (RA,Dec,cz,K: environment tracer)
"""
import os
import subprocess

TAP = "https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(OUT, exist_ok=True)


def tap_query(adql):
    """POST ADQL to VizieR TAP via curl (urllib proved flaky), return stdout text."""
    cmd = ["curl", "-s", "--max-time", "300", "-X", "POST", TAP,
           "--data-urlencode", "REQUEST=doQuery",
           "--data-urlencode", "LANG=ADQL",
           "--data-urlencode", "FORMAT=csv",
           "--data-urlencode", f"QUERY={adql}"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=320)
    if r.returncode != 0:
        raise RuntimeError(f"curl failed: {r.stderr[:300]}")
    out = r.stdout
    if out.lstrip().startswith("<?xml"):
        raise RuntimeError(f"TAP error: {out[:300]}")
    return out


def save(name, text):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write(text)
    n = max(0, len(text.strip().split("\n")) - 1)
    print(f"  saved {name}: {n} rows, {len(text)} bytes")
    return n


JOBS = [
    ("sparc_table1.csv",          'SELECT * FROM "J/AJ/152/157/table1"'),
    ("sparc_table2_massmodels.csv", 'SELECT * FROM "J/AJ/152/157/table2"'),
    ("rc3_full.csv",              'SELECT * FROM "VII/155/rc3"'),
    ("2mrs_full.csv",             'SELECT * FROM "J/ApJS/199/26/table3"'),
]

if __name__ == "__main__":
    for fname, adql in JOBS:
        print(f"[download] {fname}")
        try:
            save(fname, tap_query(adql))
        except Exception as e:
            print(f"  FAILED: {e}")
    print("DONE")
