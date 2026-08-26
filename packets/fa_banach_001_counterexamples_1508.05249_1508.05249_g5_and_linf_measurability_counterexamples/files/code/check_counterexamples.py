#!/usr/bin/env python3
"""Numerical sanity checks for the two counterexamples in the packet.

The mathematical proof is analytic.  This script samples discrete densities,
checks the root and Lipschitz assertions, checks the exact separator norms in
the G5 example, and checks finite-Lp convergence and L-infinity separation in
the measurability example.
"""

from __future__ import annotations

import math
import random


R0 = 0.5
DELTA = 1.0 / 16.0
EPSILON = 1.0 / 4.0


def q(r: float, k: int) -> float:
    return 0.0 if r <= R0 else min(1.0, (r - R0) * k)


def a(k: int) -> float:
    if k == 1:
        return R0 + DELTA
    if k == 2:
        return R0 - DELTA
    return R0


def phi_a(r: float, k: int) -> float:
    return r - a(k) + EPSILON * q(r, k)


def expectation_a(r: float, density: list[float]) -> float:
    return sum((2.0 ** (-(k + 1))) * p * phi_a(r, k + 1)
               for k, p in enumerate(density))


def root_a(density: list[float]) -> float:
    lo, hi = R0 - DELTA, R0 + DELTA
    for _ in range(90):
        mid = (lo + hi) / 2.0
        if expectation_a(mid, density) < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def random_discrete_density(rng: random.Random, atoms: int) -> list[float]:
    masses = [rng.expovariate(1.0) for _ in range(atoms)]
    total = sum(masses)
    masses = [x / total for x in masses]
    # density p(k) is mass(k)/mu(k), with mu(k)=2^{-k}; put any omitted
    # probability-space tail at density zero.
    return [masses[k] / (2.0 ** (-(k + 1))) for k in range(atoms)]


def l1_distance_a(p: list[float], v: list[float]) -> float:
    return sum((2.0 ** (-(k + 1))) * abs(x - y)
               for k, (x, y) in enumerate(zip(p, v)))


def check_example_a() -> None:
    rng = random.Random(150805249)
    samples = [random_discrete_density(rng, 16) for _ in range(80)]
    roots = [root_a(p) for p in samples]
    assert all(R0 - DELTA - 1e-12 <= r < R0 + DELTA + 1e-12
               for r in roots)
    assert all(abs(expectation_a(r, p)) < 2e-14
               for r, p in zip(roots, samples))

    # The proof gives |Gamma(p)-Gamma(q)| <= (3/8)||p-q||_1 on this root
    # interval; use the weaker constant 1 in the sampled check.
    for i in range(len(samples) - 1):
        assert abs(roots[i] - roots[i + 1]) <= (
            l1_distance_a(samples[i], samples[i + 1]) + 1e-12
        )

    for n in range(1, 81):
        t = DELTA / (4.0 * n)
        r = R0 + t
        cutoff = math.ceil(1.0 / t)
        values = [-phi_a(r, k) for k in range(1, cutoff + 5)]
        assert abs(max(abs(x) for x in values) - (EPSILON + t)) < 1e-12

        # Pair against x=2*1_{\{1\}}, whose L1 norm is one.  The normalized
        # value tends to delta/epsilon=1/4, whereas at r0 it is one.
        pairing = (-phi_a(r, 1)) / (EPSILON + t)
        expected = (DELTA - (1.0 + EPSILON) * t) / (EPSILON + t)
        assert abs(pairing - expected) < 1e-12
    last_t = DELTA / (4.0 * 80.0)
    last_pairing = (-phi_a(R0 + last_t, 1)) / (EPSILON + last_t)
    assert abs(last_pairing - DELTA / EPSILON) < 0.003


def c(r: float) -> float:
    return (1.0 - r) / (1.0 + r)


def linf_distance_b(r: float, s: float) -> float:
    if r == s:
        return 0.0
    u = min(r, s)
    return 2.0 / (1.0 + u)


def lp_distance_b(r: float, s: float, exponent: float) -> float:
    if r == s:
        return 0.0
    u, v = sorted((r, s))
    value = ((v - u) * (2.0 / (1.0 + u)) ** exponent
             + (1.0 - v) * abs(c(u) - c(v)) ** exponent)
    return value ** (1.0 / exponent)


def check_example_b() -> None:
    grid = [j / 101.0 for j in range(1, 101)]
    assert all(linf_distance_b(grid[i], grid[j]) > 1.0
               for i in range(len(grid)) for j in range(i + 1, len(grid)))

    # Exact density witnessing that every r in (0,1) belongs to Gamma(B).
    for r in grid:
        left_height = (1.0 - r) / (2.0 * r)
        right_height = (1.0 + r) / (2.0 * (1.0 - r))
        total_mass = r * left_height + (1.0 - r) * right_height
        left_mass = r * left_height
        assert abs(total_mass - 1.0) < 1e-12
        assert abs(1.0 - r - 2.0 * left_mass) < 1e-12

    for exponent in (1.0, 2.0, 3.5, 10.0):
        for r in (0.1, 0.37, 0.8):
            distances = [lp_distance_b(r, r + 10.0 ** (-n), exponent)
                         for n in range(2, 15, 2)]
            assert all(x > y for x, y in zip(distances, distances[1:]))
            assert distances[-1] < 0.12


def main() -> None:
    check_example_a()
    check_example_b()
    print("PASS: both counterexample sanity suites completed")
    print("  example A: 80 random densities and 80 separator scales")
    print("  example B: 100 levels, pairwise L-infinity separation, finite-Lp limits")


if __name__ == "__main__":
    main()
