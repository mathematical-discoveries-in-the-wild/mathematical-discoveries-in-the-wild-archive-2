#!/usr/bin/env python3
"""Finite symbolic and numerical checks for the monomial stability packet."""

import numpy as np
import sympy as sp


def reversal(n):
    matrix = sp.zeros(n)
    for i in range(n):
        matrix[i, n - 1 - i] = 1
    return matrix


x, z = sp.symbols("x z")
for degree in range(2, 13):
    a = reversal(degree)
    d = sp.zeros(degree)
    for i in range(1, degree):
        d[i, degree - i] = 1
    j = sp.zeros(degree)
    j[0, 0] = 1
    pencil = (1 - z) * j - d + x * a
    assert sp.factor((pencil * a).det()) == x**degree - z + 1
    assert sp.factor(pencil.inv()[0, 0]) == 1 / (x**degree - z + 1)


def semicircle_stieltjes(root):
    """Integral of 1/(x-root) against the standard semicircle law."""
    square_root = np.sqrt(root * root - 4)
    if abs(root - square_root) > abs(root + square_root):
        square_root = -square_root
    return (-root + square_root) / 2


for degree in (3, 4, 7, 10):
    for spectral_parameter in (0.4 + 0.2j, 2.5 + 0.7j, -1.3 + 0.4j):
        roots = np.roots([1] + [0] * (degree - 1) + [-(spectral_parameter - 1)])
        values = np.array([semicircle_stieltjes(root) for root in roots])
        residuals = values * values + roots * values + 1
        assert np.max(np.abs(residuals)) < 1e-9
        products = np.abs(1 - np.outer(values, values))
        assert np.min(products) > 1e-5

print("Verified degrees 2 through 12 and representative stability spectra.")
