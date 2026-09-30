#!/usr/bin/env python3
"""
Third generation (Task 18/19) — the memory cell, derived.

Input = the operators (per the owner's order), site held fixed (the dark sector,
Vol V census). This script computes, from published inputs only:

  1. THE LOOP FLOOR  — detectability of the signed path-dependent branch offset
     on the RAR plane (the statistic R8's state-variable probes cannot see).
  2. THE PHASE SPECTRUM — delta(drive period) for the three doors:
     Maxwell viscoelastic (falling), Debye relaxational (rising), frozen (zero).
  3. THE WAVE FLOOR — at the RAR knee, every restorative wave family
     (gravity, capillary, internal) has period <= 2*pi*t_dyn; hence any
     deep-window response (1-5 Gyr) at the knee is necessarily OVERDAMPED,
     i.e. memory. Slow response = memory, at the knee.
  4. THE THREE DOORS' TUNING — viscoelastic (ratio tau_M = eta/mu, eta free);
     marginal equilibrium (proximity of gamma to 4/3); frozen creep.
  5. CROSS-CHECKS against R9's own printed numbers (Verlinde's mu vs the
     causal wall rho*v_c^2).

Inputs: a0 = 1.2e-10 m/s^2 (Milgrom 1983); SPARC/Li et al. 2018 published
scatter (0.057 dex, N = 175); the Vol VII knee parameters (v_deep, r_knee);
Verlinde 2016 moduli as printed in the R9 report. No new data collected.

Outputs: printed tables + data/gen3_results.json + the three-panel figure
download/Gen3_memory_cell.png.
"""
import json, math, os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = "/home/z/my-project/scripts/gen3/data"
DL = "/home/z/my-project/download"
os.makedirs(OUT, exist_ok=True)

# --- constants and published inputs ----------------------------------------
G = 6.674e-11            # m^3 kg^-1 s^-2
MSUN = 1.989e30           # kg
KPC = 3.086e19            # m
GYR = 3.156e16            # s
A0 = 1.2e-10              # m/s^2 (Milgrom 1983)
SIGMA_RAR = 0.057         # dex, Li et al. 2018 rms
N_SPARC = 175             # Li et al. 2018 fit sample

# Vol VII knee parameters (two masses, from the pre-registered arithmetic)
KNEES = {
    "1e10": dict(M=1e10 * MSUN, R=3.4 * KPC, v=112e3),    # r_knee = 3.4 kpc
    "1e11": dict(M=1e11 * MSUN, R=10.8 * KPC, v=200e3),   # r_knee = 10.8 kpc
}
for k, p in KNEES.items():
    p["t_dyn"] = math.sqrt(p["R"] ** 3 / (G * p["M"]))           # s
    p["rho_bar"] = p["M"] / (4.0 / 3.0 * math.pi * p["R"] ** 3)  # kg/m^3, mean inside knee
    p["mu_wall"] = p["rho_bar"] * p["v"] ** 2                    # Pa, causal/virial wall

VERLINDE_MU = 4.3e-12        # Pa (R9 report, Verlinde 2016 Eq. 6.9)
R7_WINDOW = (0.1, 5.0)       # Gyr (Vol VII registration)
DRIVERS = [                   # archival driving programmes, period in Gyr
    ("bar pattern", 0.21),
    ("SFH episodes", 0.5),
    ("satellite passage", 0.3),
    ("post-starburst recovery", 1.0),
]

results = {}

# --- 1. the loop floor -------------------------------------------------------
print("=" * 78)
print("1. THE RAR LOOP — signed branch-offset floor (N=%d, sigma=%.3f dex)"
      % (N_SPARC, SIGMA_RAR))
print("-" * 78)
loop = {}
for f in (0.05, 0.10, 0.20, 0.30):
    n2 = int(round(f * N_SPARC)); n1 = N_SPARC - n2
    d1 = 1.64 * SIGMA_RAR * math.sqrt(1.0 / n1 + 1.0 / n2)      # dex, one-sided 95%
    d2 = 1.96 * SIGMA_RAR * math.sqrt(1.0 / n1 + 1.0 / n2)      # dex, two-sided 95%
    loop[f] = dict(N1=n1, N2=n2, dex_1s=d1, dex_2s=d2,
                   pct_1s=(10 ** d1 - 1) * 100, pct_2s=(10 ** d2 - 1) * 100)
    print("  branch fraction %.2f (N2=%3d):  one-sided %5.3f dex (%.1f%% in g)"
          "   two-sided %5.3f dex (%.1f%%)"
          % (f, n2, d1, (10 ** d1 - 1) * 100, d2, (10 ** d2 - 1) * 100))
r8_floor = 1.96 / math.sqrt(N_SPARC)
print("  R8 comparison floor: |r| >= %.3f  <->  variance %.1f%%  (same N, same 95%%)"
      % (r8_floor, 100 * r8_floor ** 2))
print("  -> the floor is the SAME in variance-equivalent terms; the gain is the")
print("     VARIABLE (the path derivative d(baryons)/dt, sign pre-specified) and")
print("     the 1-dof pre-specified test, not a lower floor. Printed honestly.")
results["loop_floor"] = {str(k): v for k, v in loop.items()}
results["r8_floor"] = dict(r=r8_floor, var_pct=100 * r8_floor ** 2)

# --- 2. the phase spectrum --------------------------------------------------
print()
print("=" * 78)
print("2. THE PHASE SPECTRUM — delta(T_drive) for the three doors")
print("-" * 78)
print("  Maxwell (viscoelastic):  tan(delta) = 1/(w*tau_M)   -> delta FALLS with w")
print("  Debye (relaxational):    tan(delta) = w*tau        -> delta RISES with w")
print("  Frozen (creep):          delta = 0, offset != 0")
Tg = np.logspace(-1.3, 1.0, 400)          # Gyr, driver period axis
w = 2 * math.pi / Tg                        # Gyr^-1
phase = {}
for tau in (0.3, 1.0, 3.0):
    phase[tau] = dict(
        maxwell=np.degrees(np.arctan(1.0 / (w * tau))),
        debye=np.degrees(np.arctan(w * tau)),
    )
print("  driver band (archival): " + "; ".join("%s T~%.2f Gyr" % d for d in DRIVERS))
for tau in (0.3, 1.0, 3.0):
    sel = (Tg > 0.05) & (Tg < 2.0)
    dM = phase[tau]["maxwell"][sel]; dD = phase[tau]["debye"][sel]
    print("    tau=%4.1f Gyr: Maxwell delta in [%4.1f, %5.1f] deg, Debye in [%5.1f, %4.1f] deg"
          % (tau, dM.min(), dM.max(), dD.min(), dD.max()))
results["phase_spectrum"] = {
    "maxwell_tan_delta": "1/(w*tau_M)", "debye_tan_delta": "w*tau",
    "drivers": {d[0]: d[1] for d in DRIVERS}}

# --- 3. the wave floor at the knee -------------------------------------------
print()
print("=" * 78)
print("3. THE WAVE FLOOR — every restorative wave at the knee is faster than 2*pi*t_dyn")
print("-" * 78)
print("  gravity-capillary dispersion (stable stratification, Atwood A<=1):")
print("     w^2 = A*g*k + gamma*k^3/rho  — both restorative terms >= 0;")
print("     at wavelength = knee radius R:  w >= sqrt(g/R) = 1/t_dyn, so the period")
print("     of ANY wave family is <= 2*pi*t_dyn(R) evaluated at the knee.")
wave = {}
for k, p in KNEES.items():
    Tstar = 2 * math.pi * p["t_dyn"] / GYR
    wave[k] = dict(t_dyn_Gyr=p["t_dyn"] / GYR, wave_period_cap_Gyr=Tstar)
    print("  knee M=%s:  t_dyn = %.3f Gyr  ->  wave period cap = 2*pi*t_dyn = %.3f Gyr"
          % (k, p["t_dyn"] / GYR, Tstar))
    for r in (30.0, 100.0):
        td = (r * KPC / p["v"]) / GYR
        print("     outer grav mode at r=%3d kpc: t_dyn = %.2f Gyr, period %.2f Gyr"
              % (r, td, 2 * math.pi * td))
Tstar11 = wave["1e11"]["wave_period_cap_Gyr"]
print("  -> the R7 window SPLITS at the knee: the 0.1-%.2f Gyr band is wave-accessible" % Tstar11)
print("     (outer modes; the patched-superfluid core-edge at ~0.3 Gyr sits there),")
print("     and the deep band (%.2f-5 Gyr) is reachable ONLY by overdamped/" % Tstar11)
print("     relaxational response, i.e. MEMORY.  Slow response = memory, at the knee.")
results["wave_floor"] = wave
results["wave_theorem"] = ("at the knee, any wave family's period <= 2*pi*t_dyn; "
                           "deep-window (1-5 Gyr) response at the knee is necessarily "
                           "overdamped/relaxational = memory")

# --- 4. the three doors' tuning ---------------------------------------------
print()
print("=" * 78)
print("4. THE THREE DOORS INTO THE DEEP WINDOW (1-5 Gyr at the knee)")
print("-" * 78)
p11 = KNEES["1e11"]
td = p11["t_dyn"] / GYR
doors = {}
print("  DOOR A (viscoelastic): tau_M = eta/mu; tuning = the RATIO only")
A = {"door": "A viscoelastic"}
for tau in (0.1, 0.5, 1.0, 5.0):
    ratio = tau / td
    eta_wall = tau * GYR * p11["mu_wall"]       # Pa s at the causal wall mu
    eta_verl = tau * GYR * VERLINDE_MU          # Pa s at Verlinde's mu
    print("    tau_M=%4.1f Gyr:  tau_M/t_dyn = %5.0f   eta = %.2e (Verlinde mu) "
          "to %.2e Pa s (wall mu)" % (tau, ratio, eta_verl, eta_wall))
    A[("tau_%.1f" % tau)] = dict(ratio=ratio, eta_verl=eta_verl, eta_wall=eta_wall)
print("    -> eta is an UNCONSTRAINED new parameter (causality bounds mu, not eta):")
print("       door A buys the deep window with a large ratio, NOT a near-cancellation.")
print("       For scale: required eta sits 4+ decades below glacier ice (1e13 Pa s).")
doors["A"] = A

B = {"door": "B marginal equilibrium"}
print("  DOOR B (marginal equilibrium): breathing mode w^2 = (3/5)(3g-4)/t_dyn^2")
print("     (homologous motion of a uniform sphere; structured equilibria")
print("      renormalize the prefactor, not the (3g-4) gate — Chandrasekhar 1930s)")
for tau in (0.5, 1.0, 5.0):
    x = (2 * math.pi * td / tau) ** 2 * 5.0 / 3.0     # = 3*gamma - 4
    if x > 0:
        gamma = (4 + x) / 3.0
        prox = abs(gamma - 4.0 / 3.0) / (4.0 / 3.0) * 100
        print("    tau=%4.1f Gyr:  3g-4 = %.2e  ->  gamma = %.4f,  %.2f%% from the "
              "marginal surface" % (tau, x, gamma, prox))
        B[("tau_%.1f" % tau)] = dict(three_g_minus_4=x, gamma=gamma, pct_from_marginal=prox)
print("    -> slowness here is NEAR-CANCELLATION: within 0.2-5%% of gamma = 4/3.")
print("       A detected slow equilibrium mode implies protected smallness.")
doors["B"] = B

C = {"door": "C frozen creep"}
print("  DOOR C (frozen creep): metastable reference configuration; hysteresis")
print("     WITHOUT phase lag (delta = 0, offset != 0). Barrier heights ~")
print("     (t_dyn/tau)^2 in dimensionless units ~ 1e2-1e4 kT-equivalents.")
print("     R9 already killed the published face (Verlinde K = -4mu/3 < 0); the")
print("     generic surviving face is creep with a metastable reference state.")
doors["C"] = C
results["doors"] = doors

# --- 5. cross-checks vs R9's printed numbers --------------------------------
print()
print("=" * 78)
print("5. CROSS-CHECKS against the R9 record")
print("-" * 78)
verl_frac = VERLINDE_MU / p11["mu_wall"]
print("  causal wall at the 1e11 knee: mu_wall = rho_bar * v_c^2 = %.2e Pa" % p11["mu_wall"])
print("  Verlinde's mu = %.1e Pa  = %.2f x wall  (below the wall, as it must be:" % (VERLINDE_MU, verl_frac))
print("  shear speed ~ 0.3 v_c) — consistent with R9's print.")
print("  patched-superfluid core-edge relaxation 0.3 Gyr (R9's bounded residue)")
print("  vs the 1e11 wave cap %.2f Gyr -> it sits at the wave/relaxation boundary," % Tstar11)
print("  as an occupied cell's number should. Consistency holds.")
results["crosschecks"] = dict(mu_wall_1e11=p11["mu_wall"], verlinde_frac=verl_frac)

# --- the figure (three panels) ----------------------------------------------
plt.rcParams.update({"font.size": 8.5, "axes.titlesize": 9.5,
                     "font.family": "DejaVu Sans"})
fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.4), constrained_layout=True)
NAVY, ACCENT, WARM, GREY = "#455b72", "#3b7fc3", "#c0504d", "#8a8f98"

# (a) the loop
ax = axes[0]
gbar = np.logspace(-1.5, 1.8, 200)
gobs = np.where(gbar < 1e-1, gbar, gbar + A0)   # RAR schematic (Newtonian + deep-MOND)
ax.loglog(gbar, gobs, color=GREY, lw=1.4, label="RAR (instantaneous law)")
ax.loglog(gbar, gobs * 10 ** 0.024, color=WARM, lw=1.2, ls="--",
          label="falling-baryons branch\n(above: medium answers\nthe larger past field)")
ax.loglog(gbar, gobs / 10 ** 0.024, color=ACCENT, lw=1.2, ls="--",
          label="rising-baryons branch\n(below)")
ax.fill_between(gbar, gobs / 10 ** 0.024, gobs * 10 ** 0.024, color=GREY, alpha=0.12)
ax.text(1.2e-2, 4e-3,
        "loop width hides inside\n$\\sigma=0.057$ dex; the\nSIGNED offset is the\n"
        "statistic (floor 0.018-\n0.024 dex, N=175, f=0.1-0.2)",
        fontsize=6.4, va="top")
ax.set_xlabel("$g_{bar}$  [m s$^{-2}$]")
ax.set_ylabel("$g_{obs}$  [m s$^{-2}$]")
ax.set_title("(a) the RAR loop — the deleted\ncontemporaneity, made visible")
ax.legend(fontsize=6.2, loc="upper left", framealpha=0.9)

# (b) the phase spectrum
ax = axes[1]
for tau, sty in zip((0.3, 1.0, 3.0), ("-", "--", ":")):
    ax.plot(Tg, phase[tau]["maxwell"], color=ACCENT, ls=sty, lw=1.2,
            label="Maxwell $\\tau_M$=%.1f Gyr" % tau)
    ax.plot(Tg, phase[tau]["debye"], color=WARM, ls=sty, lw=1.2,
            label="Debye $\\tau$=%.1f Gyr" % tau)
ax.axhline(0, color="k", lw=0.6)
for d, T in DRIVERS:
    ax.axvline(T, color=GREY, lw=0.6, alpha=0.5)
    ax.text(T, 88, " " + d, rotation=90, fontsize=5.6, va="top", ha="right", color=GREY)
ax.set_xscale("log"); ax.set_ylim(-4, 94)
ax.set_xlabel("driving period $T$  [Gyr]")
ax.set_ylabel("response phase lag $\\delta$  [deg]")
ax.set_title("(b) the phase spectrum — monotonicity\nseparates the doors")
ax.legend(fontsize=6.2, loc="center left")

# (c) the window map
ax = axes[2]
ax.set_xscale("log")
ax.axvspan(0.1, 5, color=ACCENT, alpha=0.10)
ax.axvspan(0.1, Tstar11, color=WARM, alpha=0.18)
ax.axvspan(Tstar11, 5, color=NAVY, alpha=0.12)
ax.axvline(wave["1e10"]["wave_period_cap_Gyr"], color=WARM, lw=1.0, ls=":")
ax.axvline(Tstar11, color=WARM, lw=1.4)
ax.text(0.22, 0.88, "wave-accessible\n(all wave families,\nperiod $\\leq 2\\pi t_{dyn}$)",
        fontsize=7, ha="center", transform=ax.get_xaxis_transform(), color=WARM)
ax.text(1.7, 0.88, "deep window:\nrelaxation only\n= memory",
        fontsize=7, ha="center", transform=ax.get_xaxis_transform(), color=NAVY)
pts = [
    (0.03, "collisionless $t_{dyn}$\n(knee, $10^{10}$)", 0.60),
    (0.053, "collisionless $t_{dyn}$\n(knee, $10^{11}$)", 0.40),
    (0.3, "patched superfluid\ncore-edge (R9 residue,\noccupied cell)", 0.20),
]
for x, lab, ypos in pts:
    ax.plot([x], [0.13], marker="o", ms=4, color="k")
    ax.text(x * 1.15, ypos, lab, fontsize=6.4, ha="left", va="bottom")
ax.text(1.35, 0.045,
        "door A: $\\eta/\\mu$ ratio, $\\eta$ free\n"
        "door B: $\\gamma$ within 0.2-5% of 4/3 (protected)\n"
        "door C: creep, $\\delta=0$, offset $\\neq 0$",
        fontsize=6.6, va="bottom")
ax.set_xlim(0.015, 10); ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xlabel("response time at the knee  [Gyr]")
ax.set_title("(c) the window map — slow response\nat the knee is memory")
ax.text(1.9, 0.13, "R7 window 0.1-5 Gyr", fontsize=6.5, color=NAVY, va="bottom")

fig.savefig(os.path.join(DL, "Gen3_memory_cell.png"), dpi=220)
with open(os.path.join(OUT, "gen3_results.json"), "w") as f:
    json.dump(results, f, indent=1, default=float)
print()
print("figure -> download/Gen3_memory_cell.png ; numbers -> scripts/gen3/data/gen3_results.json")
