# R9, EXECUTED — The Analyticity Check of the Dark-Medium Families

Run date: 2026-09-30. The series' second self-executable registration (Volume VII,
R9), run at derivation level on the literature's own published equations, per the
owner's order: "Run R9... Either way, you learn something."

**The registered test** (Vol VII, Part 5): "the analyticity check, derivation-level,
terminating at the literature's own published equations: whether the medium
families' susceptibilities and effective responses (Blanchet's dipolar medium and
successors; the superfluid sector's phonon mediator; the emergent families), extended
to time-dependent response, satisfy the causality analyticity the dispersion
relations of 1926-27 demand. No poles in the upper half plane; the real and imaginary
parts locked together. A violation marks an acausal medium; a pass marks the first
physical characterization of the sector's response in the frequency domain."

The concrete realization was pre-registered (worklog Task 17, commit e1c830b) before
any literature was fetched: checks (A) no UHP poles + KK locking verified numerically;
(B) front speed ≤ c; (C) response time τ at the RAR-knee scale ≤ t_Hubble; (D) τ
placed against the R7 window (0.1–5 Gyr). Decision rule: ≥2 of 3 families violating
= the media's response faces die at derivation level.

---

## 1. The verdict, in one paragraph

**All three medium families fail the registered check, each by a different door, and
one of them was already dead in the literature.** The dipolar medium (F1) fails by the
sign of its own self-gravity: its authors' own fluctuation equation, ∂²Π/∂t² = 4πGσ*Π,
is a growing exponential — a pole at ω = +i√(4πGσ*) in the upper half plane — with the
growth time crossing t_Hubble exactly where their own cluster-scale application puts
the density, and with tracking (τ ≤ 0.1 Gyr) demanding Mpc-scale dipoles at 300 km/s.
The superfluid sector (F2) fails by branch structure: the MOND force it exists to
deliver lives on the X<0 branch, whose phonon fluctuations have a wrong-sign kinetic
term — the ghost their own paper prints — growing in ~14 Myr at the RAR-knee scale;
the Lorentz-invariant completions are moreover acausal, which is already published
(Hertzberg 2021 — the honest-kill for this family's cell, found by this run's
searches, missed by Volume VII's degraded query). The emergent family (F3) fails by
having no dynamics at all: the theory's main formula is explicitly for "non-dynamical
situations," its moduli sit exactly on the author's own stability boundary
(λ+2μ = 0), and the minimal dynamic extension has a negative bulk modulus — a
compressional pole in the upper half plane growing in ~3×10⁵ yr. Per the
pre-registered decision rule (≥2 of 3 violating), this is the kill branch: **the
dark-sector medium lead is exhausted at derivation level.** The one bounded residue:
the patched (finite-temperature) superfluid does reach its static profile — in ~14 Myr
at the RAR knee, effectively instantaneous, consistent with R8's null census, with a
core-edge relaxation ~0.3 Gyr sitting at the bottom of the R7 window.

## 2. The literature it terminated at (all equations pinned from full texts)

| Family | Flagship papers (fetched, ar5iv) | The equations R9 rode |
|---|---|---|
| F1 dipolar | Blanchet 2008 (arXiv:0804.3518, PLB 665, 408); Blanchet & Le Tiec 2009 (arXiv:0901.3114, PRD 80, 023512) | the action L = −σ + J·ξ̇ − W(Π⊥); W(Π) = Λ/8π + 2πΠ² + 16π²Π³/3a₀ (Eq. 8); the constitutive relation g = 4πGΠ(1+4πGΠ/a₀) (Eq. 14); **their own fluctuation equation ∂²Π/∂t² = 4πGσ*Π with "exponentially growing modes"** |
| F2 superfluid | Berezhiani & Khoury 2015 (arXiv:1507.01019, PRD 92, 103510) | P(X) = (2Λ(2m)^{3/2}/3)X√\|X\| (Eq. 25); L_int ~ (Λ/M_Pl)θρ_b (Eq. 6); α^{3/2}Λ = √(a₀M_Pl) (Eq. 27); fiducial m = 0.6 eV, Λ = 0.2 meV (Eq. 46); c_s = √(2μ/m) (Eq. 32), c_s ~ φ̄′/m in the MOND regime; v_s ≈ 0.008(M_b/10¹¹M☉)^½(m/eV)⁻¹(Λ/meV)^{−1/3} kpc/r c (Eq. 82); r* ≈ 49 kpc (Eq. 74); **"The kinetic term φ̇² has the wrong sign for X<0"**; the finite-T patch ΔL = M²Y² (Eq. 65) |
| F3 emergent | Verlinde 2016 (arXiv:1611.02269, SciPost Phys. 2, 016) | ε_ij = (∇u + ∇uᵀ)/2 (Eq. 6.1); **the moduli μ = a₀²/16πG, λ+2μ = 0 (Eq. 6.9)** sitting on his own stability boundary μ ≥ 0, λ+2μ ≥ 0 (Eq. 6.3); the main formula ∫GM_D²/r′²dr′ = M_B a₀ r/6 (Eq. 7.40), valid "in non-dynamical situations" |
| Occupier | Hertzberg 2021 (arXiv:2105.02241), "Acausality in Superfluid Dark Matter and MOND-like Theories" | "Lorentz invariant completions... violate the condition for hyperbolicity... ghost behavior... In the transition from CDM towards MOND, the sound speed can become large, leading to superluminality... deeper into the MOND regime, hyperbolicity is broken" |
| Adjacent (read, bounded) | Mistele 2021 (arXiv:2009.03003); Blanchet et al. 2017 (arXiv:1701.07747); the bimetric no-polarization proof 2023 (arXiv:2302.02690) | Mistele's three problems (the phonon's double role in tension; the split-role fix); the bigravity DDM is ghost-free as an EFT but the canonical bimetric theory "cannot achieve a consistent gravitational polarization" |

Occupation search: 12 pre-registered queries + the arXiv API sweep (both families'
full lineages), run 2026-09-30; queries q5 and q11 degraded (the series' documented
junk class). **Volume VII's occupation search missed Hertzberg 2021 because its
relevant query (q7, "MOND gravitational polarization dielectric susceptibility
response function") degraded** — the horizon's failure is printed as part of this
record, per the series' standing rule.

## 3. F1 — the dipolar medium: killed by its own fluctuation equation

The Blanchet–Le Tiec action defines the polarization Π = σ*ξ with the internal-force
potential W. Their statics work: the constitutive relation g = 4πGΠ(1+4πGΠ/a₀)
inverts to Π(g) = (a₀/8πG)(√(1+4g/a₀) − 1), reproducing the deep-MOND scaling
Π → √(a₀g)/4πG (verified numerically: the inversion's two published limits are
recovered to <10⁻³). The time-dependent extension is also theirs, not mine: in
spherical symmetry, "the two last terms of (12) cancel each other, and we get
∂²Π/∂t² = 4πσ*Π in the MOND regime. This shows the presence of an instability, with
exponentially growing modes."

- **Check (A)**: Π̈ = +4πGσ*Π ⟹ ω² = −4πGσ* ⟹ **poles at ω = ±i√(4πGσ*), one in the
  upper half plane.** The response to any perturbation contains e^{+t/τ_g}. A UHP
  pole is the exact object the 1926-27 relations forbid: the causal Green function
  grows without bound (non-tempered), and Re/Im cannot be KK-locked (verified in the
  KK suite below: a response whose spectral weight sits at the UHP pole has Im χ ≡ 0
  on the real axis, so KK demands Re χ = 0, while the theory has Re χ(0) = −1/γ²).
  **VIOLATION.**
- **Check (C), the timescale squeeze.** Their defense: "the unstable modes will
  develop on the self-gravitating time scale τ_g = √(π/σ*)... Using the mean
  cosmological value σ̄* ≃ 10⁻²⁶ kg/m³ we get τ_g ≃ 6×10¹⁰ years. Thus this
  instability is not a problem classically." Computed here: at σ̄* the literal
  equation gives τ_g = 1/√(4πGσ̄*) ≈ 11 Gyr ≈ t_Hubble, and their printed definition
  gives ≈ 69 Gyr (their 6×10¹⁰ yr corresponds to σ̄* ≈ 1.3×10⁻²⁶ kg/m³) — the
  defense holds only at the cosmological mean. But the medium's density is not
  theirs to choose freely at every scale: (i) their own cluster application (Angus
  et al. 2008, carried in the same paper) needs cluster-scale σ* ~ 10⁻²⁴ kg/m³, where
  the growth time is 1.1–6.9 Gyr — **the instability is active within the age of the
  universe**; (ii) tracking the baryons within the R7 window's floor (τ ≤ 0.1 Gyr)
  needs σ* ≥ 5.3×10⁻²⁴ kg/m³ — at which point the model's own polarization
  requirement forces the dipole length ξ = Π/σ* ≈ 24 kpc with internal pair
  velocities ~300 km/s: the "medium" is a gas of galaxy-sized molecules.
- **The dipole-length arithmetic** (their own weak-clustering hypothesis, σ* ≈ σ̄*):
  the MOND constitutive relation requires |Π| ≈ 0.14 kg/m² at the RAR knee, so
  ξ = Π/σ* ≈ **2.9×10⁵ kpc ≈ 0.9 Gpc** — the medium's atoms are Hubble-scale. This
  is the quantitative face of their own printed limitation ("the model lacks some
  connection to microscopic physics... W is for the moment purely phenomenological").

**Verdict F1: VIOLATION (primary — their own equations, the R9 lens applied for the
first time).**

## 4. F2 — the superfluid phonon sector: the MOND branch is the ghost branch

The Berezhiani–Khoury phonon EFT has two branches. The X>0 branch is continuously
connected to the homogeneous condensate and "has stable perturbations. However, this
branch does not admit a MONDian regime." The MOND force lives on the X<0 branch —
where their own quadratic Lagrangian (their Eq. 62) has "the kinetic term φ̇² with
the wrong sign": a ghost. Their patch: a finite-temperature operator ΔL = M²Y² with
M ≳ 0.5(10¹¹M☉/M_b)^¼(Λ/meV)^½(r/10kpc)^½ m ~ eV, "remarkably, of order eV."

- **Check (A)**: with the kinetic coefficient A < 0 and gradient coefficients
  B > 0, the fluctuation dispersion is ω² = −(B/|A|)k²: **poles at ω = ±i|c_s|k, one
  in the upper half plane.** With their fiducial parameters (Eq. 46) and their own
  Eq. 82 for the gradient scale, the growth time at k = 1/10 kpc is
  **1/(|c_s|k) ≈ 14 Myr** — the zero-temperature MOND branch is violently unstable on
  galaxy scales, which is why the finite-T patch is not an option but a necessity.
  **VIOLATION at T=0 (their own admission).**
- **Check (B)**: in the non-relativistic EFT the MOND-regime sound speed c_s ~ φ̄′/m
  ~ v_s ≈ 0.0023c at 10 kpc — subluminal. But the Lorentz-invariant completions are
  acausal: superluminal in the CDM→MOND transition, hyperbolicity-broken deeper in —
  **published by Hertzberg 2021**. VIOLATION at completion level, OCCUPIED.
- **Check (C) — the one pass**: the patched medium does reach its static profile. The
  response time at the RAR knee (local c_s ~ v_s(10 kpc) ≈ 0.0023c): **≈ 14 Myr**;
  the core-edge relaxation across r* = 49 kpc (local speed at the transition, using
  their enhanced-c_s formula at its validity edge): **≈ 0.3 Gyr**. Both << t_Hubble.
  PASS.
- **Check (D)**: 14 Myr << the 0.1 Gyr window floor — **no lag at the RAR knee:
  effectively instantaneous on star-formation-history timing**, consistent with R8's
  null census. The core-edge value ~0.3 Gyr sits at the window's floor — a marginal,
  scale-dependent lag signature, printed as the bounded residue (the family's cell
  is occupied, so nothing is claimed).

**Verdict F2: VIOLATION, and OCCUPIED (Hertzberg 2021; their own ghost; Mistele's
three problems). The honest kill is printed for C20's superfluid face.**

## 5. F3 — the emergent family: no dynamics published, and the minimal extension is unstable

- **Check (A), reading (i) — the instantaneous reading**: the static theory ties
  u_i = (Φ/a₀)n_i to the *current* baryonic potential (their Eq. 6.4). Read as a
  response, χ(ω) = χ₀ for all ω: Im χ ≡ 0 with χ(0) ≠ 0 and χ(∞) = 0 — the KK sum
  rule χ(0) = (2/π)∫Im χ(ω′)/ω′ dω′ = 0 fails. Instantaneous action at a distance is
  the trivial acausality. **VIOLATION.**
- **Check (A), reading (ii) — the glassy reading** (the paper's own microscopic
  story: "glassy behavior leading to slow relaxation and memory effects... residual
  strain and stress... can only relax very slowly"): no relaxation time is computed
  anywhere in the paper; the only available scale is the Hubble time. A medium frozen
  on all sub-Hubble timescales cannot both keep the apparent dark matter (needs the
  memory to persist ~t_Hubble) and track the current baryons (needs the RAR's
  tightness — R8's census: no memory, interaction, or environment structure in the
  residuals at the 2.2%-of-variance floor). **VIOLATION (the squeeze, with R8).**
- **Check (A), reading (iii) — the minimal dynamic extension**: the published moduli
  (their Eq. 6.9) are μ = a₀²/16πG = 4.3×10⁻¹² Pa (0.8% of the dark-energy density)
  and **λ+2μ = 0 exactly** — sitting on the boundary of their own stability condition
  (Eq. 6.3: "Requiring that both velocities are real-valued leads to μ ≥ 0 and
  λ+2μ ≥ 0"). The P-wave velocity is exactly zero; the bulk modulus K = λ+2μ/3 =
  **−4μ/3 < 0**: the compressional channel — the one that carries baryonic density
  information — has ω² = Kk²/ρ < 0: **a UHP pole, growth time ≈ 3×10⁵ yr at 10 kpc**
  (with the de-Sitter density as the inertia; the shear channel propagates at
  ~0.09c and is healthy). **VIOLATION.**
- **The honest statement of scope**: the main formula (7.40) is the theory's central
  result and is explicitly for "(approximately) spherically symmetric and isolated
  astronomical systems in non-dynamical situations" — the theory as published is a
  static constraint, not a medium with a response function.

**Verdict F3: VIOLATION (primary — the three readings, the moduli arithmetic, and
the R8 squeeze are the R9 lens; the published critiques (Brouwer 2016's test; the
internal-consistency letters) are adjacent, not this cell).**

## 6. The KK verification suite (the "locked together" clause, verified not asserted)

- **Control (causal, stable damped oscillator)**: Re χ reconstructed from Im χ by the
  principal-value Kramers-Kronig integral (subtraction method, symmetric grid):
  max |Re − KK[Im]| / max|Re| = **7.3×10⁻⁴** on the band — the machinery is verified.
- **F1's response** (pole at +iγ): Im χ ≡ 0 on the real axis; KK demands Re χ(1) = 0;
  the theory has Re χ = −0.50 there. Unlocked.
- **F3's instantaneous reading**: KK demands χ(0) = 0; the theory has χ(0) = χ₀.
  Unlocked.

## 7. What dies, what survives (the registration's own logic)

- **C20's registration resolves to its kill branch.** The move survives nothing: F1
  and F3 die by primary derivation; F2 dies by occupation (Hertzberg 2021) with the
  verification run anyway. Per the honest-kill commitment, the occupation is printed
  with the horizon's failure that missed it (Vol VII's degraded query 7).
- **The dark-sector medium lead is exhausted at derivation level.** The user's clean
  answer: no published medium family — dipolar, superfluid, or emergent — passes the
  causality-analyticity check the 1926-27 relations demand. The three failure modes
  are different and worth the record: F1 fails by the sign of its self-gravity (the
  Jeans pole at the polarization's heart); F2 fails by branch structure (the MOND
  regime and stability live on different branches); F3 fails by the absence of
  dynamics (statics only, marginal moduli, negative bulk modulus).
- **R7 (the response fork) stands, sharpened.** Its data-side resolution is untouched
  and its medium branch is now strictly stronger evidence than it was: a detected
  lag/ringing in the 0.1–5 Gyr window would falsify all three published families at
  once. The only in-window number this run produced — the patched superfluid's
  core-edge relaxation ~0.3 Gyr — belongs to an occupied cell and is printed as a
  bound, not a prediction.
- **R8's null census gains its theoretical counterpart**: the RAR's tightness is
  consistent with the only medium that can actually respond (the patched superfluid,
  ~14 Myr at the knee — effectively instantaneous) and inconsistent with the frozen
  readings (F1 at weak clustering, F3's glassy memory).
- **The deletion (R7-iii) remains the surviving face** after R8 (null census) and now
  R9 (no causal medium published). The settlement (ΛCDM) is untouched by R9 — it has
  no medium to check.
- Standing registrations after this run: R1–R7 unchanged (R7 sharpened as above);
  R8 resolved (null branch); **R9 resolved (kill branch)**. The next fork dates
  unchanged.

## 8. The one-line census record (the series' claim protocol)

> R9 executed 2026-09-30 at derivation level on the literature's own equations
> (Blanchet & Le Tiec 2009; Berezhiani & Khoury 2015; Verlinde 2016): all three
> medium families fail the causality-analyticity check as registered — the dipolar
> medium's own fluctuation equation carries the UHP pole ω = +i√(4πGσ*) (growth
> 1.1–69 Gyr by density; tracking demands Mpc-scale dipoles; Gpc dipoles at weak
> clustering); the superfluid's MOND branch is ghost-unstable at T=0 (~14 Myr growth
> at 10 kpc) with the acausality of its completions already published (Hertzberg
> 2021 — C20's superfluid face dies by the honest-kill rule); the emergent family
> publishes no dynamics and its minimal extension has bulk modulus K = −4μ/3 < 0
> (compressional UHP pole, ~3×10⁵ yr); the patched superfluid alone reaches its
> static profile, in ~14 Myr at the RAR knee — effectively instantaneous, consistent
> with R8's null. No new cell claimed; the dark-sector medium lead is exhausted.

## 9. Replication

```
python3 scripts/r9/r9_derivation.py     # all checks, the KK suite -> data/r9_results.csv
python3 scripts/r9/r9_figure.py          # the figure -> download/R9_analyticity.png
bash scripts/r9/searches/run_searches.sh # the 12 pre-registered queries (q5, q11 degraded)
bash scripts/r9/papers/fetch.sh           # the nine full texts from ar5iv
```

Files: `scripts/r9/` (derivation + figure + searches + fetched papers),
`scripts/r9/data/r9_results.csv` (the 19-row checks matrix),
`scripts/r9/data/r9_numbers.json`, `download/R9_analyticity.png` (the three-panel
figure, VQA-passed), this report.

Known caveats, printed rather than hidden: the τ_g normalization differs by ~2π
between the literal equation and the authors' printed definition (both computed,
both printed); the superfluid's core-edge relaxation uses the enhanced sound-speed
formula at its validity edge (the transition-region speed is not pinned by the
papers); the emergent family's minimal extension takes the de-Sitter density as the
medium inertia because the papers specify no inertia; the occupation horizon is
bounded by this run's queries with two degraded.

The ledger is open. The next fork date on a standing registration is unchanged.
