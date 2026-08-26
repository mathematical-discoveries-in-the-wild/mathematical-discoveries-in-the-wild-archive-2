"""Checks for the parabolic counterexample to Question 3.3 of arXiv:1601.02925.

The proof is analytic.  This script independently checks the exact second
variation and evaluates large compact ellipses converging to the parabolic
model.  Numerical output is supporting evidence only.
"""

from __future__ import annotations

import math

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr


SQRT_2PI = math.sqrt(2.0 * math.pi)
ALPHA = math.sqrt(math.pi / 2.0)
A_OPT = -(math.pi + 4.0) / (4.0 * SQRT_2PI)


def phi(x: float) -> float:
    return math.exp(-0.5 * x * x) / SQRT_2PI


def w_derivatives(x: float) -> tuple[float, float, float, float]:
    # w=Phi/phi.  erfcx would be preferable in extreme tails, but all
    # quadrature below is truncated at x=-10 where this formula is stable.
    w0 = float(ndtr(x)) / phi(x)
    w1 = 1.0 + x * w0
    w2 = x * w1 + w0
    w3 = x * w2 + 2.0 * w1
    return w0, w1, w2, w3


def rho(y: float) -> float:
    return (1.0 - y * y) / math.sqrt(2.0)


def rho_prime(y: float) -> float:
    return -math.sqrt(2.0) * y


def energy_density(x: float, y: float, eps: float) -> float:
    w0, w1, w2, w3 = w_derivatives(x)
    r, rp, rpp = rho(y), rho_prime(y), -math.sqrt(2.0)
    ux = w0 + eps * A_OPT * w2 * r
    uy = eps * A_OPT * w1 * rp
    uxx = w1 + eps * A_OPT * w3 * r
    uxy = eps * A_OPT * w2 * rp
    uyy = eps * A_OPT * w1 * rpp
    return uxx * uxx + 2.0 * uxy * uxy + uyy * uyy + ux * ux + uy * uy


def ellipse_bounds(y: float, eps: float, radius: float, shift: float) -> tuple[float, float]:
    vertical_sq = radius / (math.sqrt(2.0) * eps)
    root = math.sqrt(max(0.0, 1.0 - y * y / vertical_sq))
    center = shift + eps / math.sqrt(2.0) - radius
    return center - radius * root, center + radius * root


def ellipse_volume(eps: float, radius: float, shift: float) -> float:
    vertical = math.sqrt(radius / (math.sqrt(2.0) * eps))

    def outer(y: float) -> float:
        left, right = ellipse_bounds(y, eps, radius, shift)
        return phi(y) * (float(ndtr(right)) - float(ndtr(left)))

    return quad(outer, -vertical, vertical, epsabs=2e-10, epsrel=2e-10, limit=300)[0]


def volume_half_shift(eps: float, radius: float) -> float:
    return brentq(
        lambda shift: ellipse_volume(eps, radius, shift) - 0.5,
        -0.5,
        0.5,
        xtol=2e-12,
        rtol=2e-12,
    )


def ellipse_energy(eps: float, radius: float, shift: float) -> float:
    vertical = math.sqrt(radius / (math.sqrt(2.0) * eps))

    def outer(y: float) -> float:
        left, right = ellipse_bounds(y, eps, radius, shift)
        lower = max(left, -10.0)
        if lower >= right:
            return 0.0
        inner = quad(
            lambda x: energy_density(x, y, eps) * phi(x),
            lower,
            right,
            epsabs=2e-10,
            epsrel=2e-10,
            limit=250,
        )[0]
        return phi(y) * inner

    return quad(outer, -vertical, vertical, epsabs=3e-9, epsrel=3e-9, limit=300)[0]


def main() -> None:
    exact_coefficient = -((4.0 - math.pi) ** 2) / (16.0 * math.pi)
    # The intermediate values make the symbolic identity transparent:
    # base=1, D=2, L=(pi+4)/(2 sqrt(2 pi)).
    linear = (math.pi + 4.0) / (2.0 * SQRT_2PI)
    coefficient_from_quadratic = 1.0 - linear * linear / 2.0
    print(f"A_opt={A_OPT:.15g}")
    print(f"coefficient_exact={exact_coefficient:.15g}")
    print(f"coefficient_quadratic={coefficient_from_quadratic:.15g}")
    print(f"identity_error={abs(exact_coefficient-coefficient_from_quadratic):.3g}")

    for eps in (0.03, 0.02, 0.01):
        asymptotic = 0.5 + exact_coefficient * eps * eps
        print(f"parabolic_asymptotic eps={eps:.3g} energy={asymptotic:.12g}")
        for radius in (100.0, 500.0, 2000.0):
            shift = volume_half_shift(eps, radius)
            volume = ellipse_volume(eps, radius, shift)
            energy = ellipse_energy(eps, radius, shift)
            print(
                f"ellipse eps={eps:.3g} R={radius:.0f} shift={shift:.10g} "
                f"volume={volume:.12g} energy={energy:.12g} deficit={energy-0.5:.12g}"
            )


if __name__ == "__main__":
    main()
