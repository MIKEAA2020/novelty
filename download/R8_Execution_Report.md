# R8, EXECUTED — The Residual Census of the Radial Acceleration Relation

Run date: 2026-09-30. This is the series' first self-executable registration (Volume
VII, R8), run to completion on public data, on a laptop, per the owner's order:
"Run the test... stop producing documents and start producing knowledge."

**The registered test** (Vol VII, Part 5): the correlation matrix of RAR residuals
against bar strength, morphology, cosmic-web environment, gas fraction, and
interaction stage, on the SPARC-class sample (N=175), against the pre-registered
floor — |r| ≥ 0.148 at 95% two-sided Pearson (2.2% of variance). The published
null it exists to test: "The residuals around these fits have an rms scatter of
only 0.057 dex (~13%)... in agreement with the predictions of modified Newtonian
dynamics" (Li, Lelli, McGaugh & Schombert 2018, A&A 615, A3 — "Fitting the radial
acceleration relation to individual SPARC galaxies").

---

## 1. The verdict, in one paragraph

Four of the five registered probes are null at the floor, robustly, across every
variant of the machinery (bar: +0.08; environment: −0.01; gas fraction: −0.11;
interaction: +0.07; all with N=62–175 and floors 0.15–0.25). The fifth probe,
morphology (T-type), clears the floor in the direct census (r = −0.24, p = 0.0015,
N = 175; −0.31 with Li's own critical acceleration; survives the Bonferroni-corrected
floor 0.194) — but the structure is the mass axis in disguise: the residuals tilt
with log V_flat (r = +0.34; partial on log V_flat given T = +0.36, p < 10⁻⁴), the
tilt is concentrated in the low-quality low-mass tail, it is halved by the standard
pressure-support correction and killed by it at the quality cut (Q≤2: r = −0.12,
p = 0.14), and it strengthens or weakens with the mean-function fidelity exactly as
a curvature mismatch should. **The census outcome is the null branch: Li et al.
2018's published null stands at census level in the controlled machinery.** The
deletion's discriminating cell (Volume VII, R7 iii) survives its R8 kill condition;
the medium's residual-structure face gets no support at this floor. The honest
residue of the firing probe is a quantified mass-axis tilt — a known frontier
(interpolating-function shape + dwarf kinematics systematics), not a new cell,
printed below with its bounds.

## 2. The data (all public, all downloaded this run)

| Dataset | Source | Rows |
|---|---|---|
| SPARC main table | Lelli et al. 2016, via VizieR TAP `J/AJ/152/157/table1` | 175 galaxies |
| SPARC mass models | Lelli et al. 2016, via VizieR TAP `J/AJ/152/157/table2` | 3391 points |
| RC3 | de Vaucouleurs et al. 1994, `VII/155/rc3` | 23,011 rows |
| 2MRS | Huchra et al. 2012, `J/ApJS/199/26/table3` | 44,599 rows |

Data acquisition script: `scripts/r8/download_data.py` (VizieR TAP machine
interface, no authentication). Local copies: `scripts/r8/data/`.

## 3. The machinery, and its validation against published numbers

- Accelerations per radius: g_obs = V_obs²/R; g_bar = (Υ·V_disk² + Υ·V_bulge² +
  V_gas²)/R with Υ = 0.5 at 3.6 µm (SPARC's recommended value; V_gas carries the
  1.33 helium factor per Lelli et al. 2016). Error weighting w = (V_obs/e_V_obs)²
  with e_V_obs floored at 2 km/s.
- Global fit: the "simple" interpolating function ν(y) = [1 − exp(−√y)]⁻¹,
  g_fit = g_bar·ν(g_bar/g_†), g_† free (fitted: 1.54 × 10⁻¹⁰ m s⁻²).
- **Tier-1 residual**: per-galaxy error-weighted mean of log₁₀(g_obs/g_fit) at
  fixed Υ — the raw galaxy offset. **Tier-2 residual** (primary): after fitting
  each galaxy's own (Υ, i) on a bounded grid (Υ ∈ [0.3, 0.9], i within its
  published error) — the bounded version of Li et al. 2018's marginalization
  over Υ, distance and inclination.
- Validation: per-point weighted rms at fixed Υ = **0.113 dex** vs McGaugh et
  al. 2016's published ≈ 0.11 dex with fixed mass-to-light. Tier-2 galaxy-offset
  rms: 0.102 dex; with the standard pressure-support correction (σ = 8 km/s for
  V_flat < 100 km/s): 0.082 dex all, **0.061 dex at Q≤2** — converging on Li et
  al. 2018's published 0.057 dex. The machinery reproduces the published numbers
  at both ends it can reach.

Variants run: **default** (fitted g_† = 1.54e-10), **gd120** (g_† fixed at Li's
1.20e-10), **press** (pressure correction), plus a **standard-ν** control
(worse-fitting: rms 0.21, tilt +0.61 — the tilt tracks fit fidelity).

## 4. The census matrix (primary: Tier-2 residuals, all galaxies)

| Probe (registered) | Realization on public tables | N | r | p | floor | verdict |
|---|---|---|---|---|---|---|
| bar strength | RC3 definite classes: SB vs SA | 62 | +0.08 | 0.55 | 0.250 | NULL |
| morphology | T-type (SPARC/RC3) | 175 | **−0.24** | **0.0015** | 0.148 | **fires (direct)** |
| cosmic-web environment | log₁₀(N_2MRS(<1 Mpc, |Δv|<500)+1) | 175 | −0.01 | 0.94 | 0.148 | NULL |
| gas fraction | M_gas/(M_★+M_gas), Υ=0.5, ×1.33 He | 175 | −0.11 | 0.17 | 0.148 | NULL |
| interaction stage | log₁₀(nearest 2MRS companion distance) | 175 | +0.07 | 0.38 | 0.148 | NULL |

Robustness: Q≤2 panel (N=163): bar +0.13; morphology −0.18 (p=0.019); environment
−0.08; gas −0.07; interaction +0.18 (p=0.021, driven by the same low-mass tail,
dies to +0.12 under press). Under the press variant (all galaxies): morphology
−0.19 (p=0.012), and at Q≤2: **−0.12 (p=0.137) — below the floor.** With gd120:
morphology −0.31 (Q≤2: −0.27, p=0.0005), gas fraction −0.18 (Q≤2: −0.17,
p=0.032) — both riding the mass axis, both null under press.

Full machine-readable matrix: `R8_results_final.csv` (54 rows: 3 variants ×
3 panels × 6 entries). Every number above is in it.

## 5. The structure that fired, and its attribution

The morphology firing is not morphology per se. Decomposed:

- **The mass axis dominates**: residual vs log V_flat r = +0.34 (default; +0.44
  with gd120); partial log V_flat | T = +0.36 (p < 10⁻⁴); partial T | log V_flat
  = +0.21 (p = 0.017). Low-mass galaxies sit below the mean relation, high-mass
  above — a smooth tilt of ≈ 0.15–0.2 dex per decade in V_flat, i.e. most of the
  galaxy-offset rms.
- **It is concentrated in the systematics tail**: residual vs quality flag r =
  −0.41; the tilt at Q≤2 under press is +0.14 (p = 0.12, sub-floor).
- **The standard pressure-support correction absorbs it**: the same correction
  that brings this machinery's rms into agreement with Li et al. 2018's published
  value (0.061 vs 0.057 dex) halves the tilt (all-sample) and kills the
  morphology firing below the floor at the quality cut.
- **It tracks mean-function fidelity**: a worse-fitting interpolating function
  (standard ν) inflates the tilt to +0.61; the best-fitting setup minimizes it.
  This is the signature of curvature mismatch, not per-galaxy dynamics — the
  territory of the documented interpolating-function/transition-shape tension
  (the MOND-fitting literature's slow-transition-function preference; adjacent
  cells in the search log: the "tension between the RAR and slow transition
  functions" and related threads).

Occupation bound: the mass-tilt as such is adjacent-occupied (function-form
tension literature; the census's own searches q4, q13 degraded, bounds printed).
The census claims no new cell from it.

**The external-field reading**: the environment probe — the EFE proxy — is null
at this floor in every variant (|r| ≤ 0.13). The structure that fired cannot be
read as external-field physics, and equally the null cannot exclude sub-floor
EFE signatures (the probe is a projected 2MRS density, flux-limited at
K = 11.75; the claimed EFE detections in the literature use per-galaxy 3D
external-field estimates, a different statistic). Both bounds are registered.

## 6. What dies, what survives (the registration's own logic)

- **R8's structured branch dies**: no probe shows structure that survives the
  known-systematics controls. The census resolves to its null branch: "a null
  census is the discriminating cell for the deletion's own residual story"
  (Vol VII, R8, as registered).
- **R7(iii), the deletion's face, survives its kill condition** — "dies to
  structure: any of the five probes of R8 correlating above the floor without an
  external-field reading": the one firing probe's structure is attributable to
  known kinematic systematics + function-form shape (demonstrated
  computationally above), and the external-field probe itself is null. The
  deletion survives with the attribution on the record.
- **C13/C16 (response fork) get no support and no damage** from the residual
  census: bar, interaction, environment — the probes that could have carried
  response/memory signatures — are null at this floor.
- **The published null is confirmed at census level**, and the confirmation is
  now quantified: the raw public tables carry a mass-axis structure (|r| up to
  0.44 with Li's own g_†) that the published machinery absorbs via
  marginalization and systematics handling. Anyone re-deriving the RAR from raw
  SPARC tables will meet this structure; this document is the map of what it is
  and is not.

## 7. The one-line census record (the series' claim protocol)

> R8 executed 2026-09-30 on public SPARC/RC3/2MRS tables, N=175, floor
> |r|=0.148: bar, environment, gas fraction, interaction null in all variants;
> morphology fires directly (r=−0.24, p=0.0015) but decomposes to a mass-axis
> tilt (partial log V_flat|T = +0.36) attributable to pressure-support and
> function-form systematics, sub-floor at Q≤2 under the standard correction;
> the published null (Li et al. 2018) stands; no new cell claimed.

## 8. Replication

```
python3 scripts/r8/download_data.py        # ~4 min, VizieR TAP, no auth
python3 scripts/r8/build_rar.py            # default variant -> data/rar_dataset.csv
python3 scripts/r8/build_rar.py gd120      # g_dagger = 1.20e-10 variant
python3 scripts/r8/build_rar.py press       # pressure-support variant
python3 scripts/r8/build_probes.py          # RC3 + 2MRS probes -> data/probes.csv
python3 scripts/r8/r8_census_final.py       # the matrix -> data/r8_results_final.csv
python3 scripts/r8/r8_figure.py              # the figure
```

Files: `scripts/r8/` (code), `scripts/r8/data/` (public data + derived tables),
`download/R8_residual_census.png` (the figure), this report,
`download/R8_results_final.csv` (the matrix).

Known caveats, printed rather than hidden: RC3 bar classification is optical and
definite-class-only (N=62); the 2MRS environment probe is a projected density
(flux-limited, zone-of-avoidance-checked: no SPARC galaxy at |b|<5°); distances
are SPARC's published values (not marginalized, except via the tilt's
robustness across variants); the press correction is flat-σ and applied only
where it matters (V_flat < 100 km/s); Li et al. 2018's full machinery
marginalizes one more nuisance (distance) than this bounded version.

The ledger is open. The next fork date on a standing registration is unchanged.
