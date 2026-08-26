"""Independent algebraic and numerical sanity checks for the packet.

The written proof is exact and does not depend on this script.  This file
checks representative parameter choices, random submultiplicativity tests,
and one numerical subconvolution profile.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.integrate import quad


def w0(x: float, a: float, b: float) -> float:
    return (1.0 + x) ** a if x >= 0 else (1.0 + abs(x)) ** b


def v0(x: float, a: float, b: float, r: float) -> float:
    return w0(x, a, b) ** (-r)


def convolution_constant(a: float, b: float, r: float) -> tuple[float, float, float]:
    c_plus = 2.0 / (b * r - 1.0) + 2.0 ** (a * r + 1.0) / (a * r - 1.0)
    c_minus = 2.0 / (a * r - 1.0) + 2.0 ** (b * r + 1.0) / (b * r - 1.0)
    return c_plus, c_minus, max(c_plus, c_minus)


def check_case(q: float, a: float, b: float) -> None:
    s = (a + b) / 2.0 + 1.0 / q
    source_tail = q * (s - b)
    reflected_tail = q * (s - a)
    assert source_tail > 1.0
    assert reflected_tail < 1.0
    print(
        f"q={q:g}: a={a:g}, b={b:g}, s={s:g}, "
        f"source exponent={source_tail:g}>1, reflected exponent={reflected_tail:g}<1"
    )

    rng = np.random.default_rng(250716516 + int(100 * q))
    for x, y in rng.uniform(-100.0, 100.0, size=(50_000, 2)):
        assert w0(x + y, a, b) <= w0(x, a, b) * w0(y, a, b) * (1.0 + 1e-12)
    print("  50,000 random submultiplicativity checks: passed")

    if q > 1.0:
        r = q / (q - 1.0)
        assert a > b > 1.0 / r
        c_plus, c_minus, c = convolution_constant(a, b, r)
        scale = max(1.0, c ** (1.0 / r))
        assert c * scale ** (-r) <= 1.0 + 1e-12
        integral = 1.0 / (a * r - 1.0) + 1.0 / (b * r - 1.0)
        print(
            f"  q'={r:g}, integral(v0)={integral:.8g}, "
            f"C+={c_plus:.8g}, C-={c_minus:.8g}, L={scale:.8g}"
        )

        # The exact proof bounds (v0*v0)(x)/v0(x) by C.  Quadrature at
        # representative points is only an additional implementation check.
        ratios = []
        for x in (-20.0, -5.0, -1.0, 0.0, 1.0, 5.0, 20.0):
            integrand = lambda y: v0(y, a, b, r) * v0(x - y, a, b, r)
            conv, err = quad(integrand, -math.inf, math.inf, epsabs=1e-10, limit=500)
            ratio = conv / v0(x, a, b, r)
            assert ratio <= c + max(1e-7, 10.0 * err / v0(x, a, b, r))
            ratios.append(ratio)
        print(f"  quadrature ratios (v0*v0)/v0: max={max(ratios):.8g} <= C={c:.8g}")


def main() -> None:
    check_case(q=1.0, a=1.0, b=0.0)
    check_case(q=2.0, a=1.0, b=0.75)
    check_case(q=3.0, a=1.25, b=0.75)
    print("all checks passed")


if __name__ == "__main__":
    main()
