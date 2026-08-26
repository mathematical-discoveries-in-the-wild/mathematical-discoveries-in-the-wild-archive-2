#!/usr/bin/env python3
"""Sanity checks for the two-level simplex-section formula.

The proof in the packet is analytic.  This script only checks the algebra and
selected Gamma overlap integrals numerically.
"""

from __future__ import annotations

import math

import mpmath as mp


mp.mp.dps = 80


def closed_density(k: int, m: int) -> mp.mpf:
    d = k + m
    return (
        mp.binomial(d - 2, k - 1)
        * mp.power(k, mp.mpf(k) - mp.mpf("0.5"))
        * mp.power(m, mp.mpf(m) - mp.mpf("0.5"))
        / mp.power(d, mp.mpf(d) - mp.mpf("1.5"))
    )


def gamma_overlap(k: int, m: int) -> mp.mpf:
    d = k + m
    alpha = mp.sqrt(mp.mpf(m) / (k * d))
    beta = mp.sqrt(mp.mpf(k) / (m * d))

    def integrand(t: mp.mpf) -> mp.mpf:
        pos = t ** (k - 1) * mp.exp(-t / alpha) / (mp.gamma(k) * alpha**k)
        neg = t ** (m - 1) * mp.exp(-t / beta) / (mp.gamma(m) * beta**m)
        return pos * neg

    return mp.quad(integrand, [0, mp.inf])


def adjacent_ratio(k: int, m: int) -> mp.mpf:
    return closed_density(k + 1, m - 1) / closed_density(k, m)


def a_function(x: int) -> mp.mpf:
    return mp.power(1 + mp.mpf(1) / x, mp.mpf(x) + mp.mpf("0.5"))


def main() -> None:
    samples = [(1, 2), (1, 9), (2, 3), (2, 5), (3, 7), (7, 12)]
    for k, m in samples:
        direct = gamma_overlap(k, m)
        closed = closed_density(k, m)
        assert mp.almosteq(direct, closed, rel_eps=mp.mpf("1e-55"))

    for d in range(3, 201):
        values = [closed_density(k, d - k) for k in range(1, d // 2 + 1)]
        assert all(values[j] < values[j + 1] for j in range(len(values) - 1))
        n = d - 1
        facet = mp.power(mp.mpf(n) / (n + 1), mp.mpf(n) - mp.mpf("0.5"))
        assert mp.almosteq(values[0], facet, rel_eps=mp.mpf("1e-60"))

        for k in range(1, d // 2):
            m = d - k
            ratio_1 = adjacent_ratio(k, m)
            ratio_2 = a_function(k) / a_function(m - 1)
            # The two expressions follow different high-precision power paths;
            # use a tolerance comfortably below the 55 digits used above.
            assert mp.almosteq(ratio_1, ratio_2, rel_eps=mp.mpf("1e-60"))
            assert ratio_1 > 1

    print("PASS: Gamma overlap, closed formula, and ratios checked through d=200")


if __name__ == "__main__":
    main()
