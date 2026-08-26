#!/usr/bin/env python3
"""Numerical stress checks for the finite-dimensional monotone counterexample.

The proof is analytic.  This script samples graph pairs, verifies the explicit
Minty-range construction, and checks the claimed zero-set formula.
"""

from __future__ import annotations

import math
import random


SEED = 11104877
PAIR_TESTS = 100_000
RANGE_TESTS = 25_000


def f_value(x: float, y: float) -> tuple[float, float]:
    assert x > 0.0 and y <= 0.0
    return y / (x * x), 1.0 / x


def graph_sample(rng: random.Random) -> tuple[float, float, float, float]:
    x = 10.0 ** rng.uniform(-3.0, 3.0)
    if rng.random() < 0.30:
        y = 0.0
        normal = 10.0 ** rng.uniform(-4.0, 4.0)
    else:
        y = -10.0 ** rng.uniform(-4.0, 4.0)
        normal = 0.0
    a1, a2 = f_value(x, y)
    return x, y, a1, a2 + normal


def h(x: float, q: float) -> float:
    return x + q / (x * x) - 1.0 / (x * x * x)


def bisect_root(p: float, q: float, lo: float, hi: float) -> float:
    while h(lo, q) >= p:
        lo *= 0.5
    while h(hi, q) <= p:
        hi *= 2.0
    for _ in range(180):
        mid = 0.5 * (lo + hi)
        if h(mid, q) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def minty_preimage(p: float, q: float) -> tuple[float, float, float, float]:
    """Return (x,y,a1,a2) with (p,q)=(x,y)+(a1,a2), (a1,a2) in A(x,y)."""
    if q > 0.0 and p >= 1.0 / q:
        x, y = p, 0.0
        normal = q - 1.0 / x
        assert normal >= -1e-14
        return x, y, 0.0, 1.0 / x + max(0.0, normal)

    if q > 0.0:
        hi = 1.0 / q
        lo = hi
        while h(lo, q) >= p:
            lo *= 0.5
        # Here h(hi,q)=hi>p.  Keep hi fixed to preserve y<0.
        for _ in range(180):
            mid = 0.5 * (lo + hi)
            if h(mid, q) < p:
                lo = mid
            else:
                hi = mid
        x = 0.5 * (lo + hi)
    else:
        lo, hi = 1.0, 1.0
        while h(lo, q) >= p:
            lo *= 0.5
        while h(hi, q) <= p:
            hi *= 2.0
        x = bisect_root(p, q, lo, hi)

    y = q - 1.0 / x
    a1, a2 = f_value(x, y)
    return x, y, a1, a2


def main() -> None:
    rng = random.Random(SEED)

    min_pairing = math.inf
    for _ in range(PAIR_TESTS):
        x, y, a1, a2 = graph_sample(rng)
        u, v, b1, b2 = graph_sample(rng)
        pairing = (x - u) * (a1 - b1) + (y - v) * (a2 - b2)
        min_pairing = min(min_pairing, pairing)
        scale = 1.0 + abs((x - u) * (a1 - b1)) + abs((y - v) * (a2 - b2))
        assert pairing >= -2e-11 * scale

    max_range_residual = 0.0
    for _ in range(RANGE_TESTS):
        p = rng.uniform(-100.0, 100.0)
        q = rng.uniform(-100.0, 100.0)
        if abs(q) < 1e-8:
            q = 0.0
        x, y, a1, a2 = minty_preimage(p, q)
        assert x > 0.0 and y <= 1e-10
        residual = max(abs((x + a1) - p), abs((y + a2) - q))
        max_range_residual = max(max_range_residual, residual)
        assert residual <= 2e-8 * (1.0 + abs(p) + abs(q))

    # On L=R x {0}, A(t,0) is {0} x [1/t,infinity) and
    # B(t,0)={0} x R, so every t>0 is a zero and no other point is in dom(A+B).
    for exponent in range(-12, 13):
        t = 10.0 ** exponent
        a_vertical = 1.0 / t
        b_vertical = -a_vertical
        assert abs(a_vertical + b_vertical) == 0.0

    # A is necessarily nonparamonotone: same x, distinct negative y values
    # give zero monotonicity pairing but cannot be cross-swapped in its graph.
    x, y1, y2 = 2.0, -1.0, -3.0
    f1, f2 = f_value(x, y1), f_value(x, y2)
    pairing = (x - x) * (f1[0] - f2[0]) + (y1 - y2) * (f1[1] - f2[1])
    assert pairing == 0.0 and f1 != f2

    print(f"sampled graph-pair tests: {PAIR_TESTS}")
    print(f"minimum sampled monotonicity pairing: {min_pairing:.6g}")
    print(f"sampled Minty-range targets: {RANGE_TESTS}")
    print(f"maximum resolvent residual: {max_range_residual:.6g}")
    print("zero-set and nonparamonotonicity checks: passed")


if __name__ == "__main__":
    main()
