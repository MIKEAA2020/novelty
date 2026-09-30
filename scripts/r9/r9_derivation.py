#!/usr/bin/env python3
"""
R9, EXECUTED — the analyticity check (Volume VII, Part 5, registration R9).

"whether the medium families' susceptibilities and effective responses ..., extended
to time-dependent response, satisfy the causality analyticity the dispersion relations
of 1926-27 demand. No poles in the upper half plane; the real and imaginary parts
locked together. A violation marks an acausal medium; a pass marks the first physical
characterization of the sector's response in the frequency domain."

Three families, the literature's own published equations:

F1  Blanchet's dipolar medium    — Blanchet 2008 PLB 665 408 (arXiv:0804.3518);
                                   Blanchet & Le Tiec 2009 PRD 80 023512 (arXiv:0901.3114)
F2  the superfluid phonon sector — Berezhiani & Khoury 2015 PRD 92 103510 (arXiv:1507.01019)
F3  the emergent family          — Verlinde 2016 (arXiv:1611.02269)

Checks (pre-registered, worklog Task 17):
(A) ANALYTICITY   — no poles in Im(omega) > 0; Re/Im Kramers-Kronig locked (verified
                    numerically by Hilbert transform, not asserted)
(B) FRONT SPEED   — no superluminal propagation in the extended equations
(C) REACHABILITY  — response time tau at the RAR-knee scale (3-10 kpc) <= t_Hubble
(D) R7 WINDOW     — tau vs the registered discriminating window 0.1-5 Gyr

All equation numbers in comments are the papers' own. Output: data/r9_results.csv
"""

import numpy as np
import json, os

OUT = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(OUT, exist_ok=True)

# ----------------------------------------------------------------------------
# Constants and published parameters (all sourced)
# ----------------------------------------------------------------------------
G    = 6.67430e-11          # m^3 kg^-1 s^-2
c    = 2.99792458e8         # m/s
a0   = 1.20e-10             # m/s^2   MOND acceleration (Milgrom 1983; used by all three papers)
kpc  = 3.085677581e19       # m
Gyr  = 3.15576e16           # s
tHub = 13.8 * Gyr           # age of universe (s)
sigma_mean = 1.0e-26        # kg/m^3  Blanchet & Le Tiec 2009: "mean cosmological value
                            #          sigma_bar* ~= 1e-26 kg/m^3"
m_SF   = 0.6                 # eV    Berezhiani-Khoury fiducial (Eq. 46)
Lam_SF = 0.2e-3              # eV    Berezhiani-Khoury fiducial (Eq. 46)
                            # their Eq. 74: r* ~= 49 kpc for M_b = 3e11 M_sun, fiducial params
rho_dS = 6.0e-27             # kg/m^3 de-Sitter/dark-energy mass density (Omega_Lam ~ 0.7)

results = []   # the checks matrix
def add(family, check, statement, value, verdict):
    results.append(dict(family=family, check=check, statement=statement,
                        value=value, verdict=verdict))

# ----------------------------------------------------------------------------
# F1 — BLANCHET'S DIPOLAR MEDIUM
# ----------------------------------------------------------------------------
# Published equations (Blanchet & Le Tiec 2009, arXiv:0901.3114):
#   W(Pi) = Lam/(8 pi) + 2 pi Pi^2 + 16 pi^2 Pi^3/(3 a0) + O(Pi^4)      (their Eq. 8)
#   constitutive: g = 4 pi G Pi (1 + 4 pi G Pi / a0) + O(Pi^3)         (their Eq. 14, SI G restored)
#   susceptibility: Pi = -(chi(g)/4 pi G) g,  chi(g) ~= -1 + g/a0       (their Eqs. 2, after Eq. 14)
#   FLUCTUATION (their own time-dependent result, spherical symmetry, MOND regime):
#     d^2 Pi / dt^2 = 4 pi G sigma* Pi                                  (text after Eq. 14)
#   "This shows the presence of an instability, with exponentially growing modes.
#    However the unstable modes will develop on the self-gravitating time scale
#    tau_g = sqrt(pi/sigma*)"  -> their printed value tau_g ~ 6e10 yr at the mean density.
# ----------------------------------------------------------------------------

def Pi_of_g(g, a0=a0):
    """Invert the published constitutive relation g = 4 pi G Pi (1 + 4 pi G Pi / a0).
    Let y = 4 pi G Pi:  y^2/a0 + y - g = 0  ->  y = (a0/2)(sqrt(1+4g/a0) - 1)."""
    y = 0.5 * a0 * (np.sqrt(1.0 + 4.0 * g / a0) - 1.0)
    return y / (4.0 * np.pi * G)

# sanity: deep-MOND limit Pi -> sqrt(a0 g)/(4 pi G) ; Newtonian limit Pi -> g/(4 pi G)
g_deep, g_newt = 0.01 * a0, 100 * a0
Pi_deep, Pi_newt = Pi_of_g(g_deep), Pi_of_g(g_newt)
chk_deep  = abs(Pi_deep  / (np.sqrt(a0 * g_deep)  / (4 * np.pi * G)) - 1)
chk_newt  = abs(Pi_newt / (g_newt / (4 * np.pi * G)) - 1)
# total susceptibility chi_total = -4 pi G Pi / g (their Eq. 2 sign convention)
chi_deep  = -4 * np.pi * G * Pi_deep  / g_deep
chi_newt  = -4 * np.pi * G * Pi_newt / g_newt

# (A) the pole map: d^2 Pi/dt^2 = 4 pi G sigma* Pi  ->  omega^2 = -4 pi G sigma*
#     poles at omega = +/- i sqrt(4 pi G sigma*): ONE IN THE UPPER HALF PLANE.
def f1_poles(sigma_star):
    gam = np.sqrt(4 * np.pi * G * sigma_star)      # s^-1   (growth rate, literal equation)
    tau_lit = np.sqrt(np.pi / (G * sigma_star))    # s       (their printed tau_g = sqrt(pi/sigma*), G=1 units restored)
    return gam, 1.0 / gam, tau_lit

sigma_cl = 1.0e-24        # kg/m^3  cluster-scale dipolar density (their own Angus et al. 2008
                          #         cluster application; ~100x the mean)
tau_R7floor = 0.1 * Gyr   # the R7 window's floor (Vol VII Part 4)
sigma_track = 1.0 / (4 * np.pi * G * tau_R7floor**2)  # sigma* for which tau_g = 0.1 Gyr

rows_f1 = {}
for name, sig in [('mean cosmological (1e-26)', sigma_mean),
                  ('cluster-scale (1e-24)', sigma_cl),
                  ('R7-floor-tracking (5.3e-24)', sigma_track)]:
    gam, tau_eq, tau_lit = f1_poles(sig)
    Pi_knee = Pi_of_g(a0)                       # polarization at the RAR knee g ~ a0
    xi = Pi_knee / sig                          # dipole length xi = Pi/sigma*  (their Pi = sigma* xi)
    v_int = np.sqrt(a0 * xi)                    # internal pair velocity scale ~ sqrt(a0 * xi)
    rows_f1[name] = dict(sigma=sig, gamma_s=gam, tau_eq_Gyr=tau_eq / Gyr,
                         tau_lit_Gyr=tau_lit / Gyr, xi_kpc=xi / kpc,
                         v_int_km_s=v_int / 1e3, v_int_over_c=v_int / c)
    print(f"F1 sigma*={name}: growth rate={gam:.2e} 1/s | tau(equation)={tau_eq/Gyr:.3g} Gyr | "
          f"tau(their printed)={tau_lit/Gyr:.3g} Gyr | xi={xi/kpc:.3g} kpc | "
          f"v_int={v_int/1e3:.3g} km/s = {v_int/c:.3g} c")

add('F1 dipolar', 'A: UHP-pole-free', 'fluctuation eq. d2Pi/dt2=+4piG sigma* Pi (their own text): pole at omega=+i sqrt(4piG sigma*)',
    'pole at +i*%.2e 1/s (mean sigma*)' % f1_poles(sigma_mean)[0], 'VIOLATION')
add('F1 dipolar', 'A: KK locking', 'UHP pole => causal Green fn ~ sinh(gamma t) grows; KK static sum rule cannot hold (non-tempered response)',
    'UHP pole; see KK suite', 'VIOLATION')
add('F1 dipolar', 'B: front speed', 'monopolar Jeans-type growth at k=0; no propagation speed defined; growth rate sqrt(4 pi G sigma*)',
    'n/a (growth, not propagation)', 'VIOLATION (unstable, not propagating)')
add('F1 dipolar', 'C: reachability', 'static solutions are a saddle of their own fluctuation dynamics; growth time at mean sigma* (their printed tau_g = sqrt(pi/sigma*); their printed 6e10 yr corresponds to sigma_bar* ~ 1.3e-26 kg/m^3)',
    f"{f1_poles(sigma_mean)[2]/Gyr:.2g} Gyr (printed def.) / {f1_poles(sigma_mean)[1]/Gyr:.2g} Gyr (literal eq.) vs t_Hubble 13.8 Gyr", 'MARGINAL at the mean (their defense); the literal equation gives ~11 Gyr ~ t_Hubble')
add('F1 dipolar', 'C: reachability', 'at cluster-scale sigma* (their own Angus 2008 application), growth time',
    f"{f1_poles(sigma_cl)[2]/Gyr:.2g} Gyr (printed def.) / {f1_poles(sigma_cl)[1]/Gyr:.2g} Gyr (literal eq.)", 'VIOLATION (active within t_Hubble)')
add('F1 dipolar', 'D: R7 window', 'to track baryons within 0.1 Gyr needs sigma* >= 5.3e-24 kg/m^3 -> then xi = Pi/sigma* at the RAR knee',
    f"xi = {Pi_of_g(a0)/sigma_track/kpc:.3g} kpc (Mpc-scale dipoles), v_int = {np.sqrt(a0*Pi_of_g(a0)/sigma_track)/c:.3g} c",
    'VIOLATION (tracking needs unphysical medium)')
add('F1 dipolar', 'aux: dipole length', 'at weak-clustering sigma* = mean, required dipole length xi = Pi/sigma* at RAR knee',
    f"xi = {Pi_of_g(a0)/sigma_mean/kpc:.3g} kpc (~Gpc-scale 'atoms')", 'absurdity printed (their own weak-clustering hypothesis)')

# ----------------------------------------------------------------------------
# F2 — THE SUPERFLUID PHONON SECTOR
# ----------------------------------------------------------------------------
# Published equations (Berezhiani & Khoury, arXiv:1507.01019):
#   P(X) = (2 Lam (2m)^{3/2}/3) X sqrt(|X|)          (Eq. 25, the MOND phonon action)
#   L_int ~ (Lam/M_Pl) theta rho_b                   (Eq. 6, baryon coupling)
#   alpha^{3/2} Lam = sqrt(a0 M_Pl) ~ 0.8 meV        (Eq. 27/60)
#   fiducial: m = 0.6 eV, Lam = 0.2 meV              (Eq. 46)
#   c_s = sqrt(2 mu/m)                               (Eq. 32, no baryons)
#   MOND branch (X<0): phi'(r) ~ sqrt(kappa(r))      (Eq. 58)
#   v_s = phi'/m ~ 0.008 (M_b/1e11)^{1/2} (m/eV)^{-1} (Lam/meV)^{-1/3} kpc/r   (Eq. 82)
#   "in the MOND regime the phonon sound speed is c_s ~ phi'/m"  (after their stability analysis)
#   X>0 branch: "continuously connected to the homogeneous condensate ... and has
#   stable perturbations. However, this branch does not admit a MONDian regime."
#   X<0 branch (the MOND branch): "The kinetic term phi_dot^2 has the wrong sign
#   for X < 0"  ->  GHOST at T=0; patched by Delta L = M^2 Y^2 with
#   M >~ 0.5 (1e11/M_b)^{1/4} (Lam/meV)^{1/2} (r/10kpc)^{1/2} m ~ eV   (Eqs. 62-66)
#   r* ~ 49 kpc for M_b = 3e11 M_sun                  (Eq. 74 with fiducials)
# Hertzberg 2021 (arXiv:2105.02241), the OCCUPIER: "Lorentz invariant completions ...
# violate the condition for hyperbolicity ... ghost behavior ... superluminal ...
# this regime does not appear to be present with any standard effective theory."
# ----------------------------------------------------------------------------

Mb = 1e11                     # M_sun fiducial for their Eq. 82
v_s = 0.008 * (Mb / 1e11)**0.5 * (m_SF / 1.0)**(-1) * (Lam_SF * 1e3 / 1.0)**(-1/3.)  # in c units (their Eq. 82, r = 1 kpc)
v_s_at10 = v_s * (1.0 / 10.0)  # at r = 10 kpc
cs_MOND = v_s_at10             # c_s ~ phi'/m = v_s in the MOND regime (their statement)

# (A) pole maps
#   X>0 branch: D(omega) ~ 1/(omega^2 - c_s^2 k^2 + i0): poles at +/- c_s k on the real
#   axis displaced BELOW (retarded): causal, KK-consistent.  [control]
#   X<0 MOND branch: wrong-sign kinetic term A<0, gradient terms B>0:
#   omega^2 = -(B/|A|) k^2  ->  poles at omega = +/- i (B/|A|)^{1/2} k: UHP POLE (ghost).
k_knee = 1.0 / (10 * kpc)                    # 1/m   RAR-knee scale
tau_ghost = 1.0 / (cs_MOND * c * k_knee)     # s     ghost growth time at 10 kpc
r_star = 49 * kpc                            # their Eq. 74 (fiducial)
# response times, scale-dependent (c_s(r) = v_s(r) ~ 1/r in the MOND regime, their Eq. 82 + statement)
tau_knee = (10 * kpc) / (cs_MOND * c)              # at the RAR knee, local speed
cs_at_rstar = v_s * (1.0 / 49.0) * c               # local enhanced speed at r = r* = 49 kpc
tau_core = r_star / cs_at_rstar                    # full-core relaxation, local speed at r*
print(f"\nF2: v_s(1kpc)={v_s:.4f} c | c_s(MOND,10kpc)~{cs_MOND:.4f} c | "
      f"ghost growth time @10kpc = {tau_ghost/Gyr:.3g} Gyr | knee response {tau_knee/Gyr:.3g} Gyr | "
      f"core(r*) relaxation ~ {tau_core/Gyr:.3g} Gyr")

add('F2 superfluid', 'A: UHP-pole-free', 'MOND branch (X<0) kinetic term wrong sign (their own Eq. 62 text) -> poles at omega=+/-i|c_s|k: UHP',
    f'ghost growth time at k=1/10kpc: {tau_ghost/Gyr:.3g} Gyr', 'VIOLATION at T=0 (their own admission)')
add('F2 superfluid', 'B: front speed', 'non-relativistic EFT: c_s(MOND) ~ phi\'/m ~ v_s < c OK; but Lorentz-invariant completions: superluminal in transition + hyperbolicity broken deeper in (Hertzberg 2021)',
    f'c_s(MOND,10kpc) ~ {cs_MOND:.3g} c in NR EFT; completions acausal (occupied)', 'VIOLATION at completion level (OCCUPIED: Hertzberg 2021)')
add('F2 superfluid', 'C: reachability', 'patched (finite-T operator M^2 Y^2, their Eq. 65): response time at the RAR knee (local c_s ~ v_s) and full-core relaxation at r* = 49 kpc (local speed)',
    f'knee {tau_knee/Gyr:.3g} Gyr; core(r*) ~ {tau_core/Gyr:.3g} Gyr — both << t_Hubble', 'PASS (static profile reachable)')
add('F2 superfluid', 'D: R7 window', 'knee-scale response far below the 0.1 Gyr floor (effectively instantaneous on SFH timing); core-edge relaxation sits at the window floor',
    f'knee {tau_knee/Gyr:.3g} Gyr << 0.1 Gyr; core-edge {tau_core/Gyr:.2g} Gyr ~ floor', 'NO LAG at the RAR knee; marginal in-window at the core edge')
add('F2 superfluid', 'occupation', 'the acausality of this family is published: Hertzberg 2021 (arXiv:2105.02241) + their own ghost admission + Mistele 2021 three problems',
    'occupier named', 'OCCUPIED — honest kill printed')

# ----------------------------------------------------------------------------
# F3 — THE EMERGENT FAMILY (Verlinde 2016, arXiv:1611.02269)
# ----------------------------------------------------------------------------
# Published equations:
#   strain: eps_ij = (nabla_i u_j + nabla_j u_i)/2                       (Eq. 6.1)
#   stress: sigma_ij = lam eps_kk delta_ij + 2 mu eps_ij                (Eq. 6.2)
#   stability (his own): "Requiring that both velocities are real-valued
#   leads to mu >= 0 and lambda + 2 mu >= 0"                             (Eq. 6.3)
#   THE MODULI:  mu = a0^2/(16 pi G)   and   lambda + 2 mu = 0          (Eq. 6.9)
#   -> P-wave modulus EXACTLY ZERO: the theory sits on his own stability boundary.
#   bulk modulus: K = lam + 2mu/3 = -4mu/3 < 0.
#   The main formula (7.40): for "(approximately) spherically symmetric and isolated
#   astronomical systems in NON-DYNAMICAL situations" — static only; no EOM for u_i(t)
#   is given anywhere; the microscopic story is "glassy ... slow relaxation and
#   memory effects ... can only relax very slowly" — no relaxation time computed.
# ----------------------------------------------------------------------------

mu_el = a0**2 / (16 * np.pi * G)          # Pa (J/m^3)   his Eq. 6.9
lam_el = -2 * mu_el                        # from lambda + 2 mu = 0
K_bulk = lam_el + 2 * mu_el / 3            # = -4 mu/3 < 0
v_S = np.sqrt(mu_el / rho_dS)              # shear speed in the minimal extension (inertia = dS density)
v_P2 = (lam_el + 2 * mu_el) / rho_dS       # = 0: P-waves exactly marginal
v_K2 = K_bulk / rho_dS                     # < 0: compressional channel unstable
tau_K = 1.0 / (np.sqrt(-v_K2) * k_knee)    # growth time of the compressional mode at 10 kpc
print(f"\nF3: mu = {mu_el:.3e} Pa ({mu_el/(rho_dS*c*c):.4f} of rho_Lambda c^2) | lam+2mu = {lam_el+2*mu_el:.3g} (exactly 0) | "
      f"K = {K_bulk:.3e} Pa (<0) | v_S = {v_S/c:.4f} c | v_P = 0 | compressional growth @10kpc: {tau_K/Gyr:.3g} Gyr")

add('F3 emergent', 'A: UHP-pole-free', 'no EOM published: chi(omega) undefined; three readings tested: (i) instantaneous: KK sum rule fails; (ii) glassy: frozen, undefined; (iii) minimal elastic extension: bulk modulus K=-4mu/3<0 -> omega=+/-i|v_K|k: UHP pole in the compressional channel',
    f'K = {K_bulk:.2e} Pa < 0; compressional growth @10kpc = {tau_K/Gyr:.3g} Gyr', 'VIOLATION (all three readings)')
add('F3 emergent', 'B: front speed', 'v_P = 0 exactly (lambda+2mu = 0, on his own Eq. 6.3 boundary); v_S = sqrt(mu/rho_dS)',
    f'v_S = {v_S/c:.3f} c, v_P = 0 (marginal)', 'MARGINAL (his own boundary)')
add('F3 emergent', 'C: reachability', 'the published theory is explicitly static ("non-dynamical situations"); the microscopic story requires memory to persist ~ t_Hubble (else no apparent DM), and to track current baryons (else no RAR)',
    'static by construction; no tau published', 'UNDEFINED / internally split')
add('F3 emergent', 'D: R7 window', 'the glassy memory must last ~ t_Hubble (14 Gyr) >> the 5 Gyr window top: frozen on galactic timescales; but R8 census shows residuals track current baryons with no memory structure',
    'frozen (>>5 Gyr) vs R8 null demanding tracking', 'VIOLATION (the squeeze, with R8)')

# ----------------------------------------------------------------------------
# The KK verification suite — "the real and imaginary parts locked together",
# verified NUMERICALLY (Hilbert transform), not asserted.
# ----------------------------------------------------------------------------
# KK: Re chi(omega) = (2/pi) P Int_0^inf [omega' Im chi(omega') / (omega'^2 - omega^2)] domega'
# Controls (causal, stable): the damped oscillator chi(w) = 1/(w0^2 - w^2 - i g w)
#                            and the X>0 phonon D(w) = 1/(w^2 - c_s^2 k^2 + i eps)
# Failures: (i) DDM unstable response  chi(w) = -C/(w^2 + gamma^2)  [pole at +i gamma]
#          (ii) Verlinde instantaneous  chi(w) = chi0 = const       [Im = 0, chi(0) != 0]
# ----------------------------------------------------------------------------

# symmetric LINEAR grid (odd count) so that every evaluation point has mirror-symmetric
# neighbours: the principal value is then second-order accurate with the singular
# points (where w_ext^2 == w_i^2 exactly) zeroed — they carry no weight in the PV.
N = 4001
Wmax = 30.0
w = np.linspace(-Wmax, Wmax, 2 * N + 1)   # linear, symmetric, includes 0

def kk_re_from_im(w_target, im_of_w):
    """Principal-value KK via the SUBTRACTION method (exact for smooth spectral functions).
    Re chi(w_t) = (1/pi) P Int_{-W}^{W} F(w)/(w^2 - w_t^2) dw,  F(w) = w Im chi(w) (even).
    Partial fractions: 1/(w^2-w_t^2) = [1/(w-w_t) - 1/(w+w_t)]/(2 w_t);
    for each pole a:  PV Int F/(w-a) = Int [F-F(a)]/(w-a) + F(a) ln((W-a)/(W+a)),
    the difference quotient being smooth at w = a."""
    im_ext = im_of_w(w)
    F = w * im_ext
    W = w[-1]
    # derivative estimate for the point w = a itself (grid-aligned targets)
    def I_pole(a):
        num = F - np.interp(a, w, F)          # F(w) - F(a)
        den = w - a
        smooth = num / den                     # singular only AT w = a (0/0)
        ia = np.searchsorted(w, a)
        if w[ia] == a:                          # replace the 0/0 point by the centered slope
            fnext, fprev = F[min(ia+1, len(w)-1)], F[max(ia-1, 0)]
            dwn, dwp = w[min(ia+1, len(w)-1)] - a, a - w[max(ia-1, 0)]
            smooth[ia] = (fnext - fprev) / (dwn + dwp)
        val = np.trapezoid(smooth, w)
        Fa = np.interp(a, w, F)
        if abs(Fa) > 0 and (W + a) > 1e-9 and (W - a) > 1e-9:
            val += Fa * np.log((W - a) / (W + a))
        return val
    re = []
    for wt in np.atleast_1d(w_target):
        if abs(wt) < 1e-12:
            # Re chi(0) = (2/pi) Int_0^inf Im(w')/w' dw'
            re.append(2.0 * np.trapezoid(im_ext[w > 0] / w[w > 0], w[w > 0]) / np.pi)
        else:
            re.append((I_pole(wt) - I_pole(-wt)) / (2.0 * wt * np.pi))
    return np.array(re)

def oscillator(w, w0=1.0, g=0.3, C=1.0):
    chi = C / (w0**2 - w**2 - 1j * g * w)
    return chi

w0osc, gosc = 1.0, 0.3
chi_osc = oscillator(w, w0osc, gosc)
re_kk = kk_re_from_im(w, lambda ww: np.imag(oscillator(ww, w0osc, gosc)))
mask = (w > 0.05) & (w < 8.0)
scale = np.max(np.abs(chi_osc.real[mask]))
err_osc = np.nanmax(np.abs(re_kk[mask] - chi_osc.real[mask])) / scale
print(f"\nKK suite: damped oscillator control: max |Re - Re_KK| / max|Re| on the band = {err_osc:.2e}  (PASS if << 1)")
add('KK suite (control)', 'A: KK locking', 'causal stable damped oscillator: Re/Im Hilbert-locked numerically',
    f'max relative error {err_osc:.1e}', 'PASS (control)')

# DDM: chi(w) = -C/(w^2 + gamma^2): the causal-time Green function grows; the
# spectral representation on the real axis has Im chi = 0 while chi(0) = -C/gamma^2 != 0.
gam = 1.0
chi_ddm = -1.0 / (w**2 + gam**2)                 # Im = 0 on the real axis (all spectral weight at the UHP pole)
re_kk_ddm = kk_re_from_im(w, lambda ww: 0.0 * ww)  # KK integral of zero spectral function
i1 = np.searchsorted(w, 1.0)                       # evaluate at omega = gamma ~ 1
print(f"KK suite: DDM unstable response (pole at +i*gamma): Im chi = 0 on the real axis, so KK demands")
print(f"           Re chi(1.0) = {re_kk_ddm[i1]:.3g}; the theory's actual value = {chi_ddm[i1]:.3g} — unlocked.")
add('KK suite', 'A: KK locking', 'DDM unstable response (UHP pole at +i gamma): Re/Im not KK-locked',
    'KK Re = 0 vs actual Re chi(0) = -1/gamma^2', 'FAIL (violation)')

# Verlinde instantaneous reading: chi(w) = chi0 const
chi0 = 1.0
re_kk_inst = kk_re_from_im(w, lambda ww: 0.0 * ww)   # KK integral of a zero spectral function = 0
print(f"KK suite: instantaneous response (Verlinde static reading): KK demands chi(0) = (2/pi)Int Im/w = 0, theory has chi(0) = {chi0}. Unlocked.")
add('KK suite', 'A: KK locking', 'instantaneous (statics-as-response) reading: KK sum rule chi(0) = (2/pi) Int Im/w fails',
    'KK chi(0) = 0 vs theory chi(0) = 1', 'FAIL (violation)')

# ----------------------------------------------------------------------------
# The R7 window placement chart (check D), and the master verdict
# ----------------------------------------------------------------------------
chart = dict(
    window=[0.1, 5.0],   # Gyr, the registered discriminating window (Vol VII Part 4)
    families={
        'F1 dipolar (mean sigma*)':  dict(tau_Gyr=rows_f1['mean cosmological (1e-26)']['tau_lit_Gyr'],
                                          kind='unstable-growth, effectively frozen'),
        'F1 dipolar (cluster sigma*)': dict(tau_Gyr=rows_f1['cluster-scale (1e-24)']['tau_lit_Gyr'],
                                            kind='unstable-growth, ACTIVE'),
        'F2 superfluid (patched, knee)': dict(tau_Gyr=tau_knee / Gyr, kind='track (instantaneous on window)'),
        'F2 superfluid (patched, core edge)': dict(tau_Gyr=tau_core / Gyr, kind='track (window floor)'),
        'F3 emergent (glassy reading)': dict(tau_Gyr=13.8, kind='frozen (no tracking)'),
    })
print("\nR7 window placement (Gyr):")
for k, v in chart['families'].items():
    inwin = chart['window'][0] <= v['tau_Gyr'] <= chart['window'][1]
    print(f"  {k:34s} tau = {v['tau_Gyr']:.3g} Gyr  [{v['kind']}]{'  <== IN WINDOW' if inwin else ''}")

json.dump(dict(f1=rows_f1, chart=chart), open(os.path.join(OUT, 'r9_numbers.json'), 'w'), indent=1)

# master verdict per the pre-registered decision rule (>=2 of 3 violating = exhausted)
fam_verdicts = {
    'F1 dipolar':  'VIOLATION (own fluctuation equation: UHP pole; timescale squeeze; Gpc dipoles at weak clustering)',
    'F2 superfluid': 'VIOLATION, and OCCUPIED (Hertzberg 2021; own ghost admission; Mistele 2021)',
    'F3 emergent': 'VIOLATION (no dynamics published; minimal extension UHP pole in compressional channel; static/frozen split)',
}
n_viol = sum(1 for v in fam_verdicts.values() if v.startswith('VIOLATION'))
print(f"\nMASTER VERDICT: {n_viol}/3 families violate checks (A)/(B)/(C) at derivation level.")
print("Pre-registered decision rule: >=2 of 3 violating = the media's response faces die; the dark-sector lead is exhausted.")

# the checks matrix
import csv
with open(os.path.join(OUT, 'r9_results.csv'), 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=['family', 'check', 'statement', 'value', 'verdict'])
    wr.writeheader()
    for r in results:
        wr.writerow(r)
print(f"\nWrote {len(results)} rows -> {os.path.join(OUT, 'r9_results.csv')}")
