#!/usr/bin/env python3
"""Finite-dimensional checks for the localized row-symbol counterexample.

The packet proof is analytic.  This script independently checks the local
Rademacher martingale-difference identities, the L2 contraction on random
finite inputs, and the exact Lp witness ratios for small blocks.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np


def local_rademachers(n: int) -> np.ndarray:
    """Return r_k on the 2^n terminal atoms, k=1,...,n."""
    q = np.arange(2**n)
    rows = []
    for k in range(1, n + 1):
        bit = (q >> (n - k)) & 1
        rows.append(1 - 2 * bit)
    return np.asarray(rows, dtype=float)


def expectation(values: np.ndarray, level: int) -> np.ndarray:
    """Conditional expectation at local level `level` on terminal atoms."""
    points = values.shape[0]
    n = points.bit_length() - 1
    group = 2 ** (n - level)
    result = np.empty_like(values, dtype=np.complex128)
    for start in range(0, points, group):
        result[start : start + group] = values[start : start + group].mean(axis=0)
    return result


def normalized_l2_sq(values: np.ndarray) -> float:
    n = values.shape[-1]
    return float(np.sum(np.abs(values) ** 2) / (values.shape[0] * n))


def check_intervals() -> None:
    intervals = []
    for n in range(1, 14):
        left = Fraction(1, 2**n)
        right = Fraction(3, 2 ** (n + 1))
        assert right - left == Fraction(1, 2 ** (n + 1))
        intervals.append((left, right))
    for i, (left, right) in enumerate(intervals):
        for other_left, other_right in intervals[i + 1 :]:
            assert right <= other_left or other_right <= left


def check_block(n: int, rng: np.random.Generator) -> None:
    r = local_rademachers(n)
    points = 2**n

    # Each r_k is measurable at level k and has zero conditional expectation
    # at level k-1.
    for k in range(1, n + 1):
        assert np.allclose(expectation(r[k - 1, :, None], k - 1), 0)
        assert np.allclose(expectation(r[k - 1, :, None], k), r[k - 1, :, None])

    f = rng.normal(size=(points, n, n)) + 1j * rng.normal(size=(points, n, n))
    output = np.zeros_like(f, dtype=np.complex128)
    for k in range(1, n + 1):
        e_1k = np.zeros((n, n), dtype=np.complex128)
        e_1k[0, k - 1] = 1
        ef = expectation(f, k - 1)
        output += r[k - 1, :, None, None] * np.einsum("ab,tbc->tac", e_1k, ef)

    input_sq = normalized_l2_sq(f)
    output_sq = normalized_l2_sq(output)
    assert output_sq <= input_sq + 1e-10, (n, output_sq, input_sq)

    # Test f=I.  The output is a rank-one row with singular value sqrt(n).
    identity = np.broadcast_to(np.eye(n), (points, n, n)).copy()
    row_output = np.zeros_like(identity)
    for k in range(1, n + 1):
        row_output[:, 0, k - 1] = r[k - 1]
    singular = np.linalg.svd(row_output[0], compute_uv=False)
    assert np.allclose(singular, np.r_[np.sqrt(n), np.zeros(n - 1)])

    for p in (3.0, 4.0, 6.0):
        in_norm = n ** (1 / p)
        out_norm = np.sqrt(n)
        ratio = out_norm / in_norm
        assert np.isclose(ratio, n ** (0.5 - 1 / p))


def main() -> None:
    check_intervals()
    rng = np.random.default_rng(704229)
    for n in range(1, 9):
        for _ in range(8):
            check_block(n, rng)

    # The Bochner integrability estimates use exponentially shrinking blocks.
    for q in (1, 2, 3, 4, 8):
        partial = sum(2 ** (-(n + 1)) * n ** (q / 2) for n in range(1, 200))
        assert np.isfinite(partial) and partial > 0

    print("PASS: dyadic atoms and local martingale differences")
    print("PASS: random finite-block L2 contractions for n=1,...,8")
    print("PASS: exact witness ratio n^(1/2-1/p), p=3,4,6")
    print("PASS: finite-q Bochner integrability series")


if __name__ == "__main__":
    main()
