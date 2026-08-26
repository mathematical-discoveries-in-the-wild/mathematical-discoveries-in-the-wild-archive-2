#!/usr/bin/env python3
"""Finite-tree sanity check for the Rubio de Francia decomposition.

This does not prove the analytic theorem.  It computes the dyadic maximal
operator and the exact antichain JN_p seminorm on a finite binary tree.
"""

from __future__ import annotations

import math
import random


DEPTH = 8
P = 2.0
TRIALS = 40
ITERATIONS = 60
SEED = 210700492


def intervals(depth: int):
    n = 1 << depth
    for level in range(depth + 1):
        width = 1 << (depth - level)
        for j in range(1 << level):
            yield level, j, j * width, (j + 1) * width


def dyadic_max(values: list[float], depth: int) -> list[float]:
    n = len(values)
    out = [0.0] * n
    for _, _, left, right in intervals(depth):
        average = sum(abs(x) for x in values[left:right]) / (right - left)
        for i in range(left, right):
            out[i] = max(out[i], average)
    return out


def oscillation(values: list[float], left: int, right: int) -> float:
    average = sum(values[left:right]) / (right - left)
    return sum(abs(x - average) for x in values[left:right]) / (right - left)


def jn_semipower(values: list[float], depth: int, p: float) -> float:
    """Exact maximum over dyadic antichains by tree dynamic programming."""

    n = len(values)

    def visit(left: int, right: int) -> float:
        mass = (right - left) / n
        take_node = mass * oscillation(values, left, right) ** p
        if right - left == 1:
            return take_node
        middle = (left + right) // 2
        take_children = visit(left, middle) + visit(middle, right)
        return max(0.0, take_node, take_children)

    return visit(0, n)


def xnorm(values: list[float], depth: int, p: float) -> float:
    average = abs(sum(values) / len(values))
    return average + jn_semipower(values, depth, p) ** (1.0 / p)


def pointwise_add(a: list[float], b: list[float], scale: float = 1.0):
    return [x + scale * y for x, y in zip(a, b)]


def run_trial(rng: random.Random):
    n = 1 << DEPTH
    f = [rng.gauss(0.0, 1.0) for _ in range(n)]
    g = [abs(x) for x in f]

    iterates = [g]
    ratios = []
    for _ in range(ITERATIONS):
        nxt = dyadic_max(iterates[-1], DEPTH)
        denominator = xnorm(iterates[-1], DEPTH, P)
        ratios.append(xnorm(nxt, DEPTH, P) / max(denominator, 1e-15))
        iterates.append(nxt)

    # A is a certified bound along this finite orbit (with a safety margin).
    a_bound = max(1.0, 1.05 * max(ratios))
    rubio = [0.0] * n
    coefficient = 1.0
    for item in iterates:
        rubio = pointwise_add(rubio, item, coefficient)
        coefficient /= 2.0 * a_bound

    u = [2.0 * w + x for w, x in zip(rubio, f)]
    v = [2.0 * w for w in rubio]
    maximal_rubio = dyadic_max(rubio, DEPTH)
    maximal_u = dyadic_max(u, DEPTH)

    decomposition_error = max(abs((x - y) - z) for x, y, z in zip(u, v, f))
    majorant_slack = min(w - abs(x) for w, x in zip(rubio, f))
    a1_rubio = max(m / w for m, w in zip(maximal_rubio, rubio) if w > 0)
    a1_u = max(m / x for m, x in zip(maximal_u, u) if x > 0)
    norm_ratio = (xnorm(u, DEPTH, P) + xnorm(v, DEPTH, P)) / xnorm(f, DEPTH, P)

    assert decomposition_error < 1e-12
    assert majorant_slack > -1e-12
    assert a1_rubio <= 2.0 * a_bound + 1e-9
    assert a1_u <= 6.0 * a_bound + 1e-9
    return decomposition_error, majorant_slack, a1_rubio, a1_u, norm_ratio


def main() -> None:
    rng = random.Random(SEED)
    results = [run_trial(rng) for _ in range(TRIALS)]
    print(f"seed={SEED} depth={DEPTH} p={P:g} trials={TRIALS}")
    print(f"worst decomposition residual={max(x[0] for x in results):.3e}")
    print(f"smallest majorant slack={min(x[1] for x in results):.3e}")
    print(f"largest Rubio A1 ratio={max(x[2] for x in results):.6f}")
    print(f"largest u A1 ratio={max(x[3] for x in results):.6f}")
    print(f"largest decomposition norm ratio={max(x[4] for x in results):.6f}")
    print("PASS")


if __name__ == "__main__":
    main()

