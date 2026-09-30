#!/usr/bin/env python3
"""R9 figure: the pole maps (complex omega plane), the KK verification, and the
response-time placement against the R7 window. English labels (series language)."""

import matplotlib.font_manager as fm
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

C_PASS, C_FAIL, C_MARG = '#2c7fb8', '#d7301f', '#e08214'
C_F1, C_F2, C_F3 = '#762a83', '#1b7837', '#8c510a'

fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.6), constrained_layout=True)
fig.suptitle('R9, executed — the analyticity check: the dark-medium families in the frequency domain',
             fontsize=14, fontweight='bold', y=1.04)

# ---------------------------------------------------------------- panel 1: pole map
ax = axes[0]
ax.axhspan(0, 1.35, color='#d7301f', alpha=0.07, zorder=0)
ax.text(1.62, 1.24, 'UPPER HALF PLANE\n(acausal / unstable)', ha='right', va='top',
        fontsize=8.5, color=C_FAIL, fontweight='bold')
ax.axhline(0, color='k', lw=0.8)
ax.set_xlim(-1.7, 1.7); ax.set_ylim(-1.35, 1.35)

def pole(ax, x, y, color, marker='x', ms=9, mew=2.2, alpha=1.0, zorder=5):
    ax.plot(x, y, marker, color=color, ms=ms, mew=mew, alpha=alpha, zorder=zorder)

# causal reference: damped oscillator (poles in LHP)
w0, g = 1.0, 0.3
pole(ax, -w0 * np.cos(0.2), -0.35, C_PASS); pole(ax, w0 * np.cos(0.2), -0.35, C_PASS)
ax.annotate('causal reference:\ndamped oscillator', xy=(w0*np.cos(0.2), -0.35), xytext=(0.45, -0.95),
             fontsize=8, color=C_PASS, arrowprops=dict(arrowstyle='-', color=C_PASS, lw=0.7))

# F1: dipolar medium — poles at +/- i gamma
pole(ax, 0, +1.0, C_F1); pole(ax, 0, -1.0, C_F1, alpha=0.45)
ax.text(0.07, 1.02, 'F1 dipolar:  $\\omega = \\pm i\\sqrt{4\\pi G\\sigma_*}$', fontsize=9, color=C_F1)

# F2: superfluid — X>0 poles on real axis (retarded, below); X<0 MOND branch: +/- i|cs|k
pole(ax, -1.15, 0.0, C_F2, marker='o', ms=6, mew=1.4); pole(ax, 1.15, 0.0, C_F2, marker='o', ms=6, mew=1.4)
ax.text(0.0, 0.09, 'X>0 branch: $\\omega=\\pm c_s k$ (causal)', fontsize=8.5, color=C_F2, ha='center')
pole(ax, -0.52, +0.62, C_F2); pole(ax, 0.52, +0.62, C_F2)
ax.text(0.58, 0.68, 'X<0 MOND branch: $\\omega=\\pm i|c_s|k$  (ghost)', fontsize=8.5, color=C_F2)

# F3: emergent — compressional UHP; P-wave at 0 (marginal); shear real
pole(ax, -0.85, +0.38, C_F3); pole(ax, 0.85, +0.38, C_F3)
ax.text(-1.62, 0.45, 'F3 emergent: compressional\n$\\omega=\\pm i\\sqrt{|K|/\\rho}\\,k$ (K<0)',
        fontsize=8.5, color=C_F3, va='bottom')
ax.plot(0, 0, 'o', color=C_F3, ms=7, mfc='none', mew=1.6)
ax.text(0.06, -0.16, 'P-wave: $\\lambda+2\\mu=0$\n(marginal, his own boundary)', fontsize=8, color=C_F3)

ax.set_xlabel('Re $\\omega$'); ax.set_ylabel('Im $\\omega$')
ax.set_title('(a) pole maps of the time-extended responses', fontsize=10.5)

# ---------------------------------------------------------------- panel 2: KK verification
ax = axes[1]
w = np.linspace(-30, 30, 8003)
def osc(ww): return 1.0 / (1.0 - ww**2 - 1j*0.3*ww)
def kk_re(wt):
    F = w * np.imag(osc(w))
    W = w[-1]
    def Ip(a):
        num = F - np.interp(a, w, F); den = w - a
        sm = num / den
        ia = np.searchsorted(w, a)
        if w[ia] == a:
            sm[ia] = (F[min(ia+1, len(w)-1)] - F[max(ia-1, 0)]) / ((w[min(ia+1, len(w)-1)]-a)+(a-w[max(ia-1,0)]))
        v = np.trapezoid(sm, w)
        Fa = np.interp(a, w, F)
        if abs(Fa) > 0 and (W+a) > 1e-9 and (W-a) > 1e-9:
            v += Fa*np.log((W-a)/(W+a))
        return v
    return (Ip(wt)-Ip(-wt))/(2*wt*np.pi)

wt = np.linspace(0.1, 5.5, 90)
re_true = np.real(osc(wt))
re_kk = np.array([kk_re(x) for x in wt])
ax.plot(wt, re_true, '-', color=C_PASS, lw=2.2, label='exact Re $\\chi$(causal control)')
ax.plot(wt, re_kk, '--', color='k', lw=1.4, dashes=(5, 3),
        label='Kramers-Kronig $\\hat{}$(Im $\\chi$) — Hilbert check')
ax.fill_between(wt, re_true - 0.05, re_true + 0.05, color=C_PASS, alpha=0.13)
ax.set_xlim(0, 5.5); ax.set_ylim(-1.3, 1.55)
ax.set_xlabel('$\\omega$ (units of the resonance)'); ax.set_ylabel('Re $\\chi$')
ax.legend(loc='upper right', fontsize=8.5, framealpha=0.95)
ax.text(2.9, -0.62, 'locked: max deviation $7.3\\times10^{-4}$', fontsize=9, color=C_PASS)
ax.text(2.9, -0.95, 'FAIL cases (not plottable as curves):\n'
                    'F1: Im $\\chi\\equiv 0$, KK demands Re $\\chi=0$;\n'
                    '     theory has Re $\\chi(0)=-1/\\gamma^2$\n'
                    'F3: instantaneous reading: KK demands\n'
                    '     $\\chi(0)=0$; theory has $\\chi(0)=\\chi_0$',
        fontsize=8, color=C_FAIL,
        bbox=dict(boxstyle='round,pad=0.45', fc='white', ec=C_FAIL, alpha=0.9))
ax.set_title('(b) the "locked together" clause, verified numerically', fontsize=10.5)

# ---------------------------------------------------------------- panel 3: response times vs R7 window
ax = axes[2]
ax.axvspan(0.1, 5.0, color='#4393c3', alpha=0.13, zorder=0)
ax.text(0.545, 0.965, 'R7 discriminating window (0.1–5 Gyr)', fontsize=8.5, color='#2166ac',
        ha='center', va='top', transform=ax.get_xaxis_transform())
ax.axvline(13.8, color='k', lw=1.0, ls=':')
ax.text(13.8, 0.965, ' $t_{\\rm Hubble}$', fontsize=8.5, va='top', transform=ax.get_xaxis_transform())
ax.axvspan(0.03, 0.05, color='#bdbdbd', alpha=0.5, zorder=0)
ax.text(0.006, 6.55, '$t_{\\rm dyn}$ at the RAR knee', fontsize=7.5, color='#555', rotation=90, va='top')

rows = [
    (0.0143, C_F2, 'F2 knee response',        'o'),
    (0.343,  C_F2, 'F2 core-edge relax.',     'o'),
    (1.09,   C_F1, 'F1 growth (cluster $\\sigma_*$,\nliteral eq.)', 'x'),
    (6.87,   C_F1, 'F1 growth (cluster, printed def.)', 'x'),
    (10.9,   C_F1, 'F1 growth (mean $\\sigma_*$, literal)', 'x'),
    (68.7,   C_F1, 'F1 growth (mean, printed)', 'x',),
    (13.8,   C_F3, 'F3 glassy memory (frozen)', 's'),
]
ylabels = []
for i, (x, c, lab, mk) in enumerate(rows):
    y = len(rows) - i
    ax.plot(x, y, mk, color=c, ms=10 if mk != 'x' else 12, mew=2.4 if mk == 'x' else 1.6)
    ylabels.append((y, lab, c))
ax.set_xscale('log'); ax.set_xlim(0.005, 130)
ax.set_yticks([y for y, _, _ in ylabels])
ax.set_yticklabels([lab for _, lab, _ in ylabels], fontsize=8.5)
for tick, (y, lab, c) in zip(ax.get_yticklabels(), ylabels):
    tick.set_color(c)
ax.set_xlabel('response / growth time [Gyr]')
ax.set_title('(c) where the media sit against the fork', fontsize=10.5)
ax.grid(True, which='both', alpha=0.22, lw=0.5)

fig.savefig('/home/z/my-project/download/R9_analyticity.png', dpi=170, facecolor='white')
print("saved /home/z/my-project/download/R9_analyticity.png")
