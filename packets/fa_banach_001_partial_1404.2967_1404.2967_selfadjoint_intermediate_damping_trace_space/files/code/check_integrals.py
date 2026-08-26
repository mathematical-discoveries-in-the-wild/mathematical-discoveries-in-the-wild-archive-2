"""Numerically guard the two Fourier--spectral trace exponents.

This is a transcription check, not part of the proof.  For each theta and
spectral scale lambda it evaluates I_0 and I_1 after the stable change of
variables tau=lambda*s, then prints the normalized quantities that the proof
shows remain bounded above and below.
"""

from scipy.integrate import quad


def normalized_integrals(theta: float, lam: float) -> tuple[float, float]:
    a = 1.0 / lam

    def j0(s: float) -> float:
        return (a * a + s * s) ** (-theta) / (1.0 + s * s) ** 2

    def j1(s: float) -> float:
        return s * s * (a * a + s * s) ** (-theta) / (1.0 + s * s) ** 2

    # These are exactly lambda^(3+2theta) I_0 and
    # lambda^(1+2theta) I_1 after scaling.
    return 2.0 * quad(j0, 0.0, float("inf"), epsabs=1e-11)[0], 2.0 * quad(
        j1, 0.0, float("inf"), epsabs=1e-11
    )[0]


for theta in (0.1, 0.3, 0.49):
    print(f"theta={theta}")
    for lam in (1.0, 4.0, 16.0, 64.0, 256.0):
        n0, n1 = normalized_integrals(theta, lam)
        print(f"  lambda={lam:6.1f}  normalized_I0={n0:.8f}  normalized_I1={n1:.8f}")


def two_scale_ratios(theta: float, r: float, scale: float) -> tuple[float, float]:
    """Return each integral divided by its predicted two-scale asymptotic."""

    def denominator(tau: float) -> float:
        return (tau * tau + r * r) * (tau * tau + scale * scale)

    def f0(tau: float) -> float:
        return (1.0 + tau * tau) ** (-theta) / denominator(tau)

    def f1(tau: float) -> float:
        return tau * tau * (1.0 + tau * tau) ** (-theta) / denominator(tau)

    value0 = 2.0 * quad(f0, 0.0, float("inf"), epsabs=1e-11)[0]
    value1 = 2.0 * quad(f1, 0.0, float("inf"), epsabs=1e-11)[0]
    predicted0 = 1.0 / (r * scale * scale * (1.0 + r * r) ** theta)
    predicted1 = 1.0 / (scale * (1.0 + scale * scale) ** theta)
    return value0 / predicted0, value1 / predicted1


print("two-scale checks")
for theta in (0.1, 0.3, 0.49):
    for r, scale in ((0.05, 1.0), (1.0, 1.0), (1.0, 32.0), (8.0, 32.0), (32.0, 32.0)):
        ratio0, ratio1 = two_scale_ratios(theta, r, scale)
        print(
            f"  theta={theta:.2f} r={r:5.2f} S={scale:5.2f} "
            f"ratio0={ratio0:.8f} ratio1={ratio1:.8f}"
        )
