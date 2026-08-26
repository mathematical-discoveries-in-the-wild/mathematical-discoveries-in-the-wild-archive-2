#!/usr/bin/env python3
"""Sanity checks for the square-partial-isometry deficit packet."""

from __future__ import annotations

import numpy as np


def thompson_block_ok(moduli: list[float], defect: int, tol: float = 1e-12) -> bool:
    b = np.array(sorted(moduli, reverse=True), dtype=float)
    n = len(b)
    s = np.array([1.0] * (n - defect) + [0.0] * defect)
    if np.any(b < -tol) or np.any(b > 1.0 + tol):
        return False
    if np.any(np.cumsum(b) > np.cumsum(s) + tol):
        return False
    if n:
        lhs = b[:-1].sum() - b[-1]
        rhs = s[:-1].sum() - s[-1]
        if lhs > rhs + tol:
            return False
    return True


def random_partial_isometry(n: int, defect: int, rng: np.random.Generator):
    x = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    y = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    u, _ = np.linalg.qr(x)
    w, _ = np.linalg.qr(y)
    s = np.diag([1.0] * (n - defect) + [0.0] * defect)
    return u @ s @ w.conj().T


def main() -> None:
    examples = [
        ([0.2, 0.7, 0.8, 0.9], 1),
        ([0.0, 0.4, 0.6, 0.9, 1.0], 2),
        ([0.0, 0.0, 0.5, 0.5], 3),
    ]
    for moduli, defect in examples:
        deficit = sum(1.0 - x for x in moduli)
        assert deficit + 1e-12 >= defect
        assert thompson_block_ok(moduli, defect)

    rng = np.random.default_rng(160208435)
    worst = float("inf")
    for n in range(2, 16):
        for defect in range(1, n):
            for _ in range(100):
                v = random_partial_isometry(n, defect, rng)
                initial = v.conj().T @ v
                final = v @ v.conj().T
                p = 1.0 - np.real(np.diag(initial))
                q = 1.0 - np.real(np.diag(final))
                d = np.diag(v)
                slack = 2.0 * (1.0 - np.abs(d)) - p - q
                worst = min(worst, float(slack.min()))
                assert slack.min() >= -2e-11
                assert np.sum(1.0 - np.abs(d)) + 2e-11 >= defect

    print("finite Thompson examples: PASS")
    print("random pointwise/trace inequalities: PASS")
    print(f"minimum numerical pointwise slack: {worst:.3e}")


if __name__ == "__main__":
    main()
