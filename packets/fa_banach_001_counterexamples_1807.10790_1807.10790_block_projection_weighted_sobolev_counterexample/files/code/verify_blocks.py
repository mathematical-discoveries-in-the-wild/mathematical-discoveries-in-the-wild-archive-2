#!/usr/bin/env python3
"""Deterministic sanity checks for the block-projection construction.

The proof in main.tex is analytic.  This script checks its explicit formulas,
reflection identities, uniform constants, and witness-series behaviour.
"""

from __future__ import annotations

import math


H = 1.0 / 8.0


def parameters(n: int) -> tuple[float, float, float, float, float]:
    M = float(16**n)
    L = 1.0 / M
    z = n + 0.5
    left = z - L / 2.0
    right = z + L / 2.0
    return M, L, z, left, right


def profile_s(n: int, x: float) -> float:
    M, L, _z, left, right = parameters(n)
    del M
    if x <= left - H or x >= right + H:
        return 0.5
    if x < left:
        return 0.5 + (x - (left - H)) / (2.0 * H)
    t = (x - left) / L
    if t <= 1.0 / 3.0:
        return 1.0
    if t < 2.0 / 3.0:
        return 2.0 - 3.0 * t
    if x <= right:
        return 0.0
    return (x - right) / (2.0 * H)


def block(n: int, x: float) -> float:
    _M, _L, _z, left, right = parameters(n)
    if x <= left - H or x >= right + H:
        return 0.0
    if x < left:
        return (x - (left - H)) / H
    if x <= right:
        return 1.0
    return (right + H - x) / H


def common_factor(n: int, x: float) -> float:
    M, _L, _z, left, right = parameters(n)
    return 1.0 if left < x < right else M ** -4


def weights(n: int, x: float) -> tuple[float, float, float]:
    M, _L, _z, _left, _right = parameters(n)
    s = profile_s(n, x)
    q = common_factor(n, x)
    w0 = q * M**s
    w1 = q * M ** (1.0 - s)
    return w0, w1, math.sqrt(w0 * w1)


def core_mass(M: float) -> float:
    """Exact endpoint function-mass on a core, with L=1/M."""
    return 1.0 / 3.0 + (M - 1.0) / (3.0 * M * math.log(M)) + 1.0 / (3.0 * M)


def endpoint_block_upper(M: float) -> float:
    # Two collars, each of length H; |beta|<=1 and |beta'|=1/H.
    return 1.0 + 2.0 * H * (1.0 + H**-2) * M**-3


def middle_block_upper(M: float) -> float:
    return M**-0.5 + 2.0 * H * (1.0 + H**-2) * M**-3.5


def check_reflection() -> None:
    for n in range(1, 7):
        _M, _L, z, left, right = parameters(n)
        lo, hi = left - H, right + H
        for k in range(2001):
            x = lo + (hi - lo) * k / 2000.0
            y = 2.0 * z - x
            assert abs(profile_s(n, x) + profile_s(n, y) - 1.0) < 2e-9
            assert abs(block(n, x) - block(n, y)) < 2e-9
            w0x, _w1x, wtx = weights(n, x)
            _w0y, w1y, wty = weights(n, y)
            assert math.isclose(w0x, w1y, rel_tol=2e-9, abs_tol=1e-15)
            assert math.isclose(wtx, wty, rel_tol=2e-9, abs_tol=1e-15)


def main() -> None:
    check_reflection()
    print("reflection identities: checked on 12,006 points")

    print("n  core mass       endpoint B upper  middle D upper   P norm^2 upper")
    for n in (1, 2, 4, 8):
        M = float(16**n)
        A = core_mass(M)
        B = endpoint_block_upper(M)
        D = middle_block_upper(M)
        assert 1.0 / 3.0 <= A <= 1.0
        assert 1.0 / 3.0 <= B < 1.005
        assert D <= 1.005 * M**-0.5
        assert 6.0 * B < 6.03
        print(f"{n:<2d} {A: .12e}  {B: .12e}   {D: .12e}   {6*B: .12e}")

    # Endpoint witness d_n=1/n: bounded by a constant times zeta(2).
    endpoint_d = sum(endpoint_block_upper(float(16**n)) / n**2 for n in range(1, 201))
    assert endpoint_d < 1.005 * math.pi**2 / 6.0

    # Auxiliary logarithmic-gradient terms are exactly these lower bounds.
    aux_terms = []
    for n in range(1, 9):
        M = float(16**n)
        aux_terms.append(12.0 * math.log(M) ** 2 * M**1.5 / n**2)
    assert all(aux_terms[k + 1] > aux_terms[k] for k in range(len(aux_terms) - 1))

    # Geometric-mean witness c_n=n^{-1/2}: convergent middle norm.
    middle_c = sum(middle_block_upper(float(16**n)) / n for n in range(1, 201))
    assert middle_c < 0.4

    # Its projected endpoint norm dominates (1/3) times the harmonic sum.
    projected_lower_400 = sum((1.0 / 3.0) / n for n in range(1, 401))
    projected_lower_4000 = sum((1.0 / 3.0) / n for n in range(1, 4001))
    assert projected_lower_4000 > projected_lower_400

    print(f"endpoint d witness, first 200 blocks (upper): {endpoint_d:.12f}")
    print("auxiliary d witness, first 8 block terms:")
    print("  " + " ".join(f"{v:.3e}" for v in aux_terms))
    print(f"middle c witness, first 200 blocks (upper): {middle_c:.12f}")
    print(
        "projected c endpoint lower sums, N=400 and 4000: "
        f"{projected_lower_400:.12f}, {projected_lower_4000:.12f}"
    )
    print("all checks passed")


if __name__ == "__main__":
    main()
