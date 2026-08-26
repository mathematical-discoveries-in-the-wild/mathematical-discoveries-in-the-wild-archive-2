"""Numerical sanity checks for the finite sparse-comb estimates.

This is not part of the proof.  It evaluates the exact one-dimensional
Hilbert-kernel integral and samples the Frostman quotient for moderate N.
"""

from __future__ import annotations

import math


def comb_integral(z: float, n: int, ell: float) -> float:
    total = 0.0
    for k in range(n):
        left = k / n
        right = left + ell
        total += math.log(abs(z - left) / abs(z - right))
    return total


def interval_mass(left: float, right: float, n: int, ell: float, delta: float) -> float:
    mass = 0.0
    for k in range(n):
        a = k / n + ell + delta
        b = a + delta
        mass += max(0.0, min(right, b) - max(left, a)) / (n * delta)
    return mass


def check(q: float, n: int) -> None:
    inv_q = 1.0 / q
    gap = inv_q - 1.0
    # Put r fairly far from 1 so that the asymptotic separation is visible
    # at computationally reasonable N, while retaining p-r>0.
    r = 1.0 + 0.72 * gap
    p = 1.0 + 0.90 * gap
    ell = n ** (-r)
    delta = n ** (-p)

    values = []
    test_indices = sorted({0, n // 8, n // 4, n // 2, 3 * n // 4, 7 * n // 8, n - 1})
    for k in test_indices:
        z = k / n + ell + 1.5 * delta
        values.append(comb_integral(z, n, ell))
    predicted = (p - r) * math.log(n)

    # Sample intervals with endpoints near the grid and the target intervals.
    endpoints = {0.0, 1.0}
    sampled_indices = sorted({int(j * (n - 1) / 15) for j in range(16)})
    for k in sampled_indices:
        a = k / n + ell + delta
        b = a + delta
        endpoints.update((max(0.0, a - delta), a, b, min(1.0, b + delta)))
    points = sorted(endpoints)
    max_ratio = 0.0
    for i, left in enumerate(points):
        for right in points[i + 1 :]:
            length = right - left
            if length:
                max_ratio = max(max_ratio, interval_mass(left, right, n, ell, delta) / length**q)

    print(
        f"q={q:.2f} N={n} r={r:.4f} p={p:.4f} "
        f"min_integral={min(values):.5f} predicted_local={predicted:.5f} "
        f"sampled_frostman_constant={max_ratio:.5f}"
    )
    assert min(values) > 0.45 * predicted
    assert max_ratio < 8.0
    assert n * delta**q >= 1.0


if __name__ == "__main__":
    # Near q=1 the proof remains valid but its asymptotic scale becomes too
    # large for a useful floating-point smoke test.
    for q_value, size in ((0.25, 30), (0.45, 400), (0.65, 50_000)):
        check(q_value, size)
