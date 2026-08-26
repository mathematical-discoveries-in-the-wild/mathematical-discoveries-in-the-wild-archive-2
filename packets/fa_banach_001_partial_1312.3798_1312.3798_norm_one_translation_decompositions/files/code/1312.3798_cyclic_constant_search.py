#!/usr/bin/env python3
"""Search finite cyclic translation systems for a C_3 > 1 witness."""

from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import linprog


def fixed_basis(q: int, step: int) -> np.ndarray:
    """Indicator basis for functions on Z/q fixed by translation by step."""
    d = math.gcd(q, step)
    basis = np.zeros((q, d))
    for x in range(q):
        basis[x, x % d] = 1.0
    return basis


def quotient_norm(a: np.ndarray, f: np.ndarray) -> tuple[float, np.ndarray]:
    """Return min ||c||_infty subject to A c=f, with an optimizer."""
    d = a.shape[1]
    objective = np.r_[np.zeros(d), 1.0]
    aub = np.zeros((2 * d, d + 1))
    bub = np.zeros(2 * d)
    for k in range(d):
        aub[2 * k, k] = 1.0
        aub[2 * k, d] = -1.0
        aub[2 * k + 1, k] = -1.0
        aub[2 * k + 1, d] = -1.0
    aeq = np.c_[a, np.zeros(a.shape[0])]
    result = linprog(
        objective,
        A_ub=aub,
        b_ub=bub,
        A_eq=aeq,
        b_eq=f,
        bounds=[(None, None)] * d + [(0.0, None)],
        method="highs",
    )
    if not result.success:
        raise RuntimeError(result.message)
    return float(result.x[-1]), result.x[:-1]


def range_vertex(a: np.ndarray, direction: np.ndarray) -> np.ndarray | None:
    """Maximize a random functional on range(A) intersected with the cube."""
    d = a.shape[1]
    result = linprog(
        -(direction @ a),
        A_ub=np.r_[a, -a],
        b_ub=np.ones(2 * a.shape[0]),
        bounds=[(None, None)] * d,
        method="highs",
    )
    if not result.success:
        return None
    return a @ result.x


def main() -> None:
    rng = np.random.default_rng(20260811)
    best = (1.0, None)
    component_count = 4
    for q in range(4, 49):
        # The fixed space depends only on gcd(q, step), so enumerate those
        # distinct patterns rather than every step.
        divisors = [d for d in range(1, q) if q % d == 0]
        triples = itertools.combinations(divisors, component_count)
        print(f"q={q}, proper divisors={divisors}", flush=True)
        for triple in triples:
            blocks = [fixed_basis(q, d) for d in triple]
            a = np.concatenate(blocks, axis=1)
            rank = np.linalg.matrix_rank(a)
            if rank <= 2:
                continue
            directions = list(np.eye(q)) + list(-np.eye(q))
            directions += [rng.normal(size=q) for _ in range(16)]
            for direction in directions:
                f = range_vertex(a, direction)
                if f is None:
                    continue
                norm_f = float(np.max(np.abs(f)))
                if norm_f < 1e-9:
                    continue
                t, coeffs = quotient_norm(a, f)
                ratio = t / norm_f
                if ratio > best[0] + 1e-7:
                    best = (ratio, (q, triple, f / norm_f, coeffs / norm_f, rank))
                    print(f"best ratio={ratio:.12g}, q={q}, steps={triple}, rank={rank}")
                    print("f=", np.round(f / norm_f, 10).tolist())
                    if ratio > 1.0001:
                        return
    print("final best", best)


if __name__ == "__main__":
    main()
