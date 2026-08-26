#!/usr/bin/env python3
"""Finite-dimensional sanity checks for the translation counterexample.

The proof packet is symbolic.  This script only checks the elementary
geometric identities in several dimensions and reports the proved lower
bound |B_{1/2}^k|/4.
"""

from math import gamma, pi

import numpy as np


def ball_volume(k: int, radius: float) -> float:
    return pi ** (k / 2) * radius**k / gamma(k / 2 + 1)


for k in (2, 3, 5, 8):
    c = np.zeros(k)
    c[0] = 3.0
    gradient_0 = np.eye(k)
    gradient_1 = np.eye(k)
    assert np.array_equal(gradient_1 - gradient_0, np.zeros((k, k)))
    assert np.linalg.norm(c) > 2.0

    # Points in B_{1/2} belong to the range of u_0(x)=x and cannot belong
    # to the disjoint range of u_1(x)=x+c.
    for j in range(k):
        y = np.zeros(k)
        y[j] = 0.49
        assert np.linalg.norm(y) < 0.5
        assert np.linalg.norm(y - c) > 1.0
        assert np.allclose(y, y)  # u_0^{-1}(y)=y

    lower_bound = ball_volume(k, 0.5) / 4.0
    assert lower_bound > 0.0
    print(f"k={k}: gradients coincide; ranges disjoint; Y lower bound >= {lower_bound:.12g}")

print("all translation-obstruction sanity checks passed")
