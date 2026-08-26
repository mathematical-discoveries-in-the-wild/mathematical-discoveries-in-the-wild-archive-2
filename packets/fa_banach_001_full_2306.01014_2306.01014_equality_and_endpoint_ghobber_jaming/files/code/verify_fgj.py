#!/usr/bin/env python3
"""Numerical checks for the equality and endpoint FGJ packet."""

from __future__ import annotations

import itertools
import math

import numpy as np


RNG = np.random.default_rng(230601014)


def subsets(n: int):
    for mask in range(1 << n):
        yield {j for j in range(n) if mask & (1 << j)}


def tail_lp(v: np.ndarray, keep_complement_of: set[int], p: float) -> float:
    idx = [j for j in range(len(v)) if j not in keep_complement_of]
    if not idx:
        return 0.0
    if math.isinf(p):
        return float(np.max(np.abs(v[idx])))
    return float(np.linalg.norm(v[idx], ord=p))


def check_interior_hilbert() -> int:
    tests = 0
    for n in range(2, 7):
        for _ in range(20):
            z = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
            u, _ = np.linalg.qr(z)
            coherence = float(np.max(np.abs(u)))
            for m in subsets(n):
                for nn in subsets(n):
                    alpha = math.sqrt(len(m) * len(nn)) * coherence
                    if alpha >= 1.0 - 1e-12:
                        continue
                    constant = 1.0 + 1.0 / (1.0 - alpha)
                    for _ in range(25):
                        x = RNG.normal(size=n) + 1j * RNG.normal(size=n)
                        x /= np.linalg.norm(x)
                        a = tail_lp(x, m, 2.0)
                        b = tail_lp(u @ x, nn, 2.0)
                        rhs = constant * (a + b)
                        if not rhs > 1.0 + 1e-11:
                            raise AssertionError((n, m, nn, alpha, rhs))
                        tests += 1
    return tests


def check_endpoints() -> int:
    tests = 0
    for n in range(1, 8):
        all_subsets = list(subsets(n))
        for _ in range(40):
            sigma = RNG.permutation(n)
            phase = np.exp(2j * np.pi * RNG.random(n))
            u = np.zeros((n, n), dtype=complex)
            for j in range(n):
                u[sigma[j], j] = phase[j]
            for m, nn in itertools.product(all_subsets, repeat=2):
                d = {j for j in range(n) if sigma[j] in nn}
                overlap = m & d
                if overlap:
                    j = next(iter(overlap))
                    x = np.zeros(n, dtype=complex)
                    x[j] = 1.0
                    assert tail_lp(x, m, 1.0) == 0.0
                    assert tail_lp(u @ x, nn, 1.0) == 0.0
                    tests += 1
                    continue

                x = RNG.normal(size=n) + 1j * RNG.normal(size=n)
                f1 = tail_lp(x, m, 1.0)
                g1 = tail_lp(u @ x, nn, 1.0)
                if np.linalg.norm(x, ord=1) > f1 + g1 + 1e-11:
                    raise AssertionError(("p=1", n, m, nn))

                fi = tail_lp(x, m, math.inf)
                gi = tail_lp(u @ x, nn, math.inf)
                if abs(max(fi, gi) - np.linalg.norm(x, ord=np.inf)) > 1e-11:
                    raise AssertionError(("p=inf", n, m, nn))
                tests += 1
    return tests


if __name__ == "__main__":
    interior = check_interior_hilbert()
    endpoints = check_endpoints()
    print(f"interior strictness checks: {interior}")
    print(f"endpoint support checks: {endpoints}")
    print("all checks passed")

