#!/usr/bin/env python3
"""Exact certificate for the Dirichlet composition--differentiation packet.

All proof-critical calculations use fractions.  The only decimal output is a
human-readable rendering of an exact rational number.
"""

from fractions import Fraction
from math import comb


Q = Fraction


def convolve(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def power_to_bernstein(power: list[Q], degree: int) -> list[Q]:
    """Return degree-``degree`` Bernstein coefficients on [0,1]."""
    assert degree >= len(power) - 1
    return [
        sum(
            (
                power[j] * Q(comb(k, j), comb(degree, j))
                for j in range(min(k, len(power) - 1) + 1)
            ),
            Q(0),
        )
        for k in range(degree + 1)
    ]


def main() -> None:
    # K(t) >= P(t) = sum_{n=0}^8 t^n/(n+1).
    p = [Q(1, n + 1) for n in range(9)]

    # F(t) <= N(t).  The first eight terms are exact; the geometric tail
    # is bounded by 2(t/2)^8, which contributes 1/128 at degree eight.
    n_majorant = [Q(n + 1, n + 2) / (2**n) for n in range(8)]
    n_majorant.append(Q(1, 128))

    p_squared = convolve(p, p)
    t_n_squared = [Q(0)] + convolve(n_majorant, n_majorant)
    length = max(len(p_squared), len(t_n_squared))
    q = [
        Q(81, 400) * (p_squared[k] if k < len(p_squared) else Q(0))
        - (t_n_squared[k] if k < len(t_n_squared) else Q(0))
        for k in range(length)
    ]

    bernstein_degree = 32
    bernstein = power_to_bernstein(q, bernstein_degree)
    minimum = min(bernstein)
    minimum_index = bernstein.index(minimum)
    expected_minimum = Q(55075026511, 201587097600000)

    assert len(q) - 1 == 17
    assert len(bernstein) == 33
    assert all(coefficient > 0 for coefficient in bernstein)
    assert minimum == expected_minimum
    assert minimum_index == 28

    # The numerical-radius compression and the rational Berezin threshold
    # are separated exactly by 7/24 - (9/20)^2 = 107/1200.
    compression_radius_squared = Q(7, 24)
    berezin_threshold_squared = Q(81, 400)
    threshold_gap = compression_radius_squared - berezin_threshold_squared
    assert threshold_gap == Q(107, 1200) > 0

    # Squared weights alpha_1^2 and alpha_2^2 of D_{z/2}.
    assert Q(1, 2) + Q(2, 3) == Q(7, 6)

    print("q degree:", len(q) - 1)
    print("Bernstein elevation degree:", bernstein_degree)
    print("positive Bernstein coefficients:", len(bernstein), "of", len(bernstein))
    print("minimum coefficient index:", minimum_index)
    print("minimum coefficient (exact):", minimum)
    print("minimum coefficient (decimal):", float(minimum))
    print("7/24 - (9/20)^2:", threshold_gap)
    print("CERTIFIED: b < 9/20 < sqrt(7/24)")


if __name__ == "__main__":
    main()
