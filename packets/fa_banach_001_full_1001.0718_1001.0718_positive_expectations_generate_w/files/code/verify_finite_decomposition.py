#!/usr/bin/env python3
"""Random finite-dimensional checks of the common-slack decomposition."""

from __future__ import annotations

import numpy as np


def verify(seed: int, trials: int = 500) -> None:
    rng = np.random.default_rng(seed)
    for _ in range(trials):
        group_coordinates = int(rng.integers(2, 9))
        coefficient_coordinates = int(rng.integers(2, 9))
        c = float(rng.normal())

        xi = rng.normal(size=(group_coordinates, coefficient_coordinates))
        # Force the coefficient sum to be the scalar constant c.
        xi[-1] += c - xi.sum(axis=0)

        a = np.maximum(xi, 0.0)
        b = np.maximum(-xi, 0.0)
        A = a.sum(axis=0)
        B = b.sum(axis=0)
        R = float(np.max(A + B) + 1.0)
        slack = R - A

        p = a.copy()
        q = b.copy()
        p[0] += slack
        q[0] += slack

        assert np.all(slack >= -1e-12)
        assert np.all(p >= -1e-12) and np.all(q >= -1e-12)
        assert np.allclose(p.sum(axis=0), R)
        assert np.allclose(q.sum(axis=0), R - c)
        assert R - c > 0
        assert np.allclose(xi, p - q)
        assert np.allclose(xi, R * (p / R) - (R - c) * (q / (R - c)))


if __name__ == "__main__":
    verify(seed=10010718)
    print("common-slack decomposition passed 500 randomized finite checks")
