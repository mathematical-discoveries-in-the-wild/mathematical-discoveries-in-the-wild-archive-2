#!/usr/bin/env python3
"""LP stress tests for the Hahn--Banach support formula in finite l1 models."""

from __future__ import annotations

import numpy as np
from scipy.optimize import linprog


def unit_l1(rng: np.random.Generator, d: int) -> np.ndarray:
    x = rng.normal(size=d)
    return x / np.abs(x).sum()


def primal_support(
    xs: list[np.ndarray], y: np.ndarray, a: np.ndarray, b: np.ndarray, c: float
) -> float:
    """Maximize the support functional under ||f_i +/- g||_infty <= 1."""
    n, d = len(xs), len(y)
    size = (n + 1) * d
    objective = np.zeros(size)
    for i, x in enumerate(xs):
        objective[i * d : (i + 1) * d] = (a[i] + b[i]) * x
        objective[n * d :] += (a[i] - b[i]) * x
    objective[n * d :] += c * y

    rows: list[np.ndarray] = []
    rhs: list[float] = []
    for i in range(n):
        for j in range(d):
            for sign_f, sign_g in [(1.0, 1.0), (-1.0, -1.0), (1.0, -1.0), (-1.0, 1.0)]:
                row = np.zeros(size)
                row[i * d + j] = sign_f
                row[n * d + j] = sign_g
                rows.append(row)
                rhs.append(1.0)
    result = linprog(
        -objective,
        A_ub=np.asarray(rows),
        b_ub=np.asarray(rhs),
        bounds=[(None, None)] * size,
        method="highs",
    )
    assert result.success, result.message
    return -float(result.fun)


def dual_decomposition(
    xs: list[np.ndarray], y: np.ndarray, a: np.ndarray, b: np.ndarray, c: float
) -> float:
    """Minimize the r_i formula with the l1 norm and 2 sum r_i = c y."""
    n, d = len(xs), len(y)
    r_size = n * d
    # Variables: r, s_plus, s_minus, where s variables majorize abs values.
    total = 3 * r_size
    objective = np.zeros(total)
    objective[r_size:] = 1.0
    rows: list[np.ndarray] = []
    rhs: list[float] = []

    for i, x in enumerate(xs):
        for j in range(d):
            r_index = i * d + j
            plus_index = r_size + r_index
            minus_index = 2 * r_size + r_index

            # |a_i x_i + r_i| <= s_plus.
            row = np.zeros(total)
            row[r_index] = 1.0
            row[plus_index] = -1.0
            rows.append(row)
            rhs.append(-a[i] * x[j])
            row = np.zeros(total)
            row[r_index] = -1.0
            row[plus_index] = -1.0
            rows.append(row)
            rhs.append(a[i] * x[j])

            # |b_i x_i - r_i| <= s_minus.
            row = np.zeros(total)
            row[r_index] = -1.0
            row[minus_index] = -1.0
            rows.append(row)
            rhs.append(-b[i] * x[j])
            row = np.zeros(total)
            row[r_index] = 1.0
            row[minus_index] = -1.0
            rows.append(row)
            rhs.append(b[i] * x[j])

    equality = np.zeros((d, total))
    for j in range(d):
        for i in range(n):
            equality[j, i * d + j] = 2.0

    result = linprog(
        objective,
        A_ub=np.asarray(rows),
        b_ub=np.asarray(rhs),
        A_eq=equality,
        b_eq=c * y,
        bounds=[(None, None)] * r_size + [(0.0, None)] * (2 * r_size),
        method="highs",
    )
    assert result.success, result.message
    return float(result.fun)


def main() -> None:
    rng = np.random.default_rng(20260809)
    worst_gap = 0.0
    cases = 0
    for d in [1, 2, 3, 5]:
        for n in [1, 2, 4]:
            for _ in range(30):
                xs = [unit_l1(rng, d) for _ in range(n)]
                y = unit_l1(rng, d)
                a = rng.random(n) * 3.0
                b = rng.random(n) * 3.0
                c = float(rng.random() * 3.0)
                primal = primal_support(xs, y, a, b, c)
                dual = dual_decomposition(xs, y, a, b, c)
                worst_gap = max(worst_gap, abs(primal - dual))
                cases += 1
    assert worst_gap < 2e-8, worst_gap
    print(f"finite l1 models checked: {cases}")
    print(f"worst primal-dual gap:   {worst_gap:.3e}")
    print("support formula: OK")


if __name__ == "__main__":
    main()

