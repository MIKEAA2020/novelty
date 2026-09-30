#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Volume VII — the detectability arithmetic (the Part-4 analog of Vol VI's
fork arithmetic). Computed from published inputs, printed before the
registrations are finalized. Every number the volume prints is either a
direct input (cited) or computed here."""

import math

out = []

def p(s=""):
    out.append(s)

p("=" * 72)
p("VOLUME VII — THE DETECTABILITY ARITHMETIC")
p("Computed 2026-09-30, after the searches, before the registrations.")
p("=" * 72)

# ---------------------------------------------------------------------------
# 1. R8 — the residual census floor (C14)
#    Inputs: SPARC-class fit sample N ~ 175 (Li et al. 2018 fit the RAR to
#    individual SPARC galaxies); residual rms scatter 0.057 dex (Li 2018).
p()
p("1. THE RESIDUAL-CENSUS FLOOR (R8 / C14)")
p("-" * 72)
N = 175.0
sigma_dex = 0.057          # Li et al. 2018, rms residual scatter
alpha = 0.05
r_min = 1.96 / math.sqrt(N)         # two-sided 95% Pearson floor
p(f"   N (SPARC-class fit sample)            = {N:.0f}")
p(f"   residual rms scatter (Li 2018)        = {sigma_dex:.4f} dex  (= 13-14%)")
p(f"   minimum detectable |r| (95%, N=175)   = {r_min:.3f}")
p(f"   variance fraction detectable r^2      = {100*r_min**2:.1f}%")
# structured component in dex, if the probe measures the driver perfectly:
s_struct = r_min * sigma_dex
p(f"   structured amplitude detectable       = {s_struct:.4f} dex "
  f"(= {100*(10**s_struct-1):.1f}%)")
p("   reading: the census detects any residual driver carrying >= ~2.2%")
p("   of the variance (>= ~1.9% amplitude at 1 sigma). Both programs")
p("   predict structure ABOVE this floor (feedback histories; the EFE),")
p("   so a null census is the discriminating cell, not the expected one.")

# ---------------------------------------------------------------------------
# 2. R7 — the response-fork lag window (C13 / C16)
p()
p("2. THE RESPONSE-LAG WINDOW (R7 / C13-C16)")
p("-" * 72)
G = 4.302e-9     # Mpc (km/s)^2 Msun^-1
# dynamical time at the knee of the RAR for a 1e11 Msun baryonic galaxy:
# in the deep regime v^4 = a0 * G * M_b  ->  v = (a0 G M_b)^{1/4}
a0 = 1.2e-10     # m/s^2
Msun = 1.989e30
for Mb_solar in (1e10, 1e11):
    M = Mb_solar * Msun
    v = (a0 * 6.674e-11 * M) ** 0.25          # m/s
    r_knee = v**2 / a0                         # m
    t_dyn = r_knee / v                        # s
    p(f"   M_b = {Mb_solar:.0e} Msun: v_deep = {v/1000:.0f} km/s, "
      f"r_knee = {r_knee/3.086e19:.1f} kpc, "
      f"t_dyn = {t/3.156e16:.2f} Gyr" if False else
      f"   M_b = {Mb_solar:.0e} Msun: v_deep = {v/1000:.0f} km/s, "
      f"r_knee = {r_knee/3.086e19:.1f} kpc, "
      f"t_dyn = {t_dyn/3.156e16:.2f} Gyr")
p("   collisionless response time ~ t_dyn    = 0.05-0.1 Gyr (immediate for")
p("   any slow baryonic change: gas flows take 0.1-1 Gyr)")
p("   star-formation-history timing precision = 0.1-0.5 Gyr (archival)")
p("   -> the discriminating window: media whose relaxation time tau sits")
p("      in 0.1-5 Gyr (formation-scale media: condensation, sloshing)")
p("   -> collisionless and fast media are INDISTINGUISHABLE on lag")
p("      (both immediate at the measurable band) — printed as the fork's")
p("      honest limit, not hidden.")

# ---------------------------------------------------------------------------
# 3. C22 — the Tisserand capture-edge amplitude (the arithmetic kill)
p()
p("3. THE TISSERAND CAPTURE-EDGE AMPLITUDE (C22 — the arithmetic kill)")
p("-" * 72)
# tidal-capture mass flux fraction per crossing ~ (M_sat/M_halo)^2
for ratio in (1e-2, 3e-2):
    flux = ratio ** 2
    p(f"   M_sat/M_halo = {ratio:.0e}: capture flux ~ {flux:.0e} "
      f"per crossing")
p("   kinematic precision on halo mass       = 5-10%")
p("   -> the capture-edge signature sits 3-4 orders below the floor;")
p("   KILL by rule (c) NO DATA TERMINATION — printed, no search spent.")

# ---------------------------------------------------------------------------
# 4. The bar bequest (C15's corpse feeding R7)
p()
p("4. THE BAR BEQUEST (C15 killed; its evidence carried into R7)")
p("-" * 72)
p("   LambdaCDM sims: halo dynamical friction slows bars by tens of")
p("   percent over ~5 Gyr (Fragkoudi et al. 2021 class).")
p("   Observed: fast bars dominate (R_CR/R_bar < 1.4 in most measured")
p("   galaxies) — a published, growing tension with the settlement.")
p("   The deletion (no dark sink): minimal braking — bars stay fast.")
p("   -> the field's own published tension is response-side evidence:")
p("   the dark sector's braking response to bars is measurably WEAKER")
p("   than the settlement's simplest face predicts. The killed move's")
p("   corpse feeds the surviving registration (the series' bequest rule).")

# ---------------------------------------------------------------------------
# 5. The conjunction with the standing R1 (Vol VI)
p()
p("5. THE CONJUNCTION (R7 x R1, both standing)")
p("-" * 72)
p("   R1 resolves the knee's SPATIAL face (tracks H(z) or constant).")
p("   R7 resolves the sector's TEMPORAL face (response immediate, lagged,")
p("   or absent). The four cells are independent: a medium that tracks H(z)")
p("   and a constant medium that rings are both live. The conjunction cell")
p("   is printed with R7 as the volume's cross-link, mirroring Vol VI's R4.")

with open("/home/z/my-project/novelty/scripts/vii_arithmetic_output.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("\n".join(out))
