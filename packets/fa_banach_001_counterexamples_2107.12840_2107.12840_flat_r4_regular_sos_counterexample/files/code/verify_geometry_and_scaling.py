#!/usr/bin/env python3
"""Exact and high-precision checks supporting the R^4 island construction.

The proof itself is analytic.  This script checks the ball geometry, the
quartic formula, the chain-rule scale factors, and representative flatness
envelopes without using floating-point underflow.
"""

from fractions import Fraction
from math import log
import random

import sympy as sp


def check_geometry(count: int = 200) -> None:
    radii = [Fraction(1, 2 ** (n + 4)) for n in range(1, count + 2)]
    rho = [r * r / 100 for r in radii]
    for i in range(count):
        # Supports have radius 2 rho_n; consecutive centers are closest.
        center_gap = radii[i] - radii[i + 1]
        support_sum = 2 * rho[i] + 2 * rho[i + 1]
        assert support_sum < center_gap
        assert 2 * rho[i] < radii[i]


def check_quartic() -> None:
    w, x, y, z = sp.symbols("w x y z", real=True)
    L = w**4 + x**2 * y**2 + y**2 * z**2 + z**2 * x**2 - 2 * w * x * y * z
    assert sp.Poly(L, w, x, y, z).total_degree() == 4
    # Numerical sampling supplements the exact AM--GM proof in the packet.
    evaluator = sp.lambdify((w, x, y, z), L, "math")
    rng = random.Random(210712840)
    for _ in range(20_000):
        point = [rng.uniform(-3.0, 3.0) for _ in range(4)]
        assert evaluator(*point) >= -1e-11


def check_chain_rule() -> None:
    rho, amplitude = sp.symbols("rho amplitude", positive=True)
    u = sp.symbols("u")
    g = sp.Function("g")
    G = g(rho * u) / sp.sqrt(amplitude)
    assert sp.diff(G, u) == rho * sp.Subs(sp.Derivative(g(sp.Symbol("_xi_1")), sp.Symbol("_xi_1")), sp.Symbol("_xi_1"), rho*u) / sp.sqrt(amplitude)
    assert sp.diff(G, u, 2) == rho**2 * sp.Subs(sp.Derivative(g(sp.Symbol("_xi_1")), (sp.Symbol("_xi_1"), 2)), sp.Symbol("_xi_1"), rho*u) / sp.sqrt(amplitude)


def check_flat_envelopes() -> None:
    # Work with logarithms.  rho=r^2/100 and a=exp(-rho^{-2}).
    # Verify representative derivative orders and desired powers over a long
    # initial range; the exact asymptotic follows since exponentials dominate
    # powers.
    for derivative_order in range(13):
        for desired_power in range(13):
            previous = None
            for n in range(4, 80):
                log_r = -(n + 4) * log(2.0)
                log_rho = 2.0 * log_r - log(100.0)
                # log(a rho^{-m} / r^N), with
                # log(a)=-rho^{-2}=-exp(-2 log(rho)).
                log_island_ratio = -sp.exp(-2.0 * log_rho) - derivative_order * log_rho - desired_power * log_r
                value = float(log_island_ratio)
                if previous is not None:
                    assert value < previous
                previous = value
            assert previous < -1e6


def main() -> None:
    check_geometry()
    check_quartic()
    check_chain_rule()
    check_flat_envelopes()
    print("PASS: disjoint support geometry (first 200 balls)")
    print("PASS: quartic degree and 20,000 seeded nonnegativity samples")
    print("PASS: first- and second-derivative rescaling factors")
    print("PASS: logarithmic flatness envelopes for sampled orders")


if __name__ == "__main__":
    main()
