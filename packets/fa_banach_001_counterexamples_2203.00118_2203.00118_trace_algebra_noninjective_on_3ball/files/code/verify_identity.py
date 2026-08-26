#!/usr/bin/env python3
"""Verify the five-term Cl_3^+ identity in exact symbolic arithmetic."""

from __future__ import annotations

import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)

# Ordered basis (1, I=e12, J=e13, K=e23).
TABLE = {
    (0, 0): (1, 0), (0, 1): (1, 1), (0, 2): (1, 2), (0, 3): (1, 3),
    (1, 0): (1, 1), (2, 0): (1, 2), (3, 0): (1, 3),
    (1, 1): (-1, 0), (2, 2): (-1, 0), (3, 3): (-1, 0),
    (1, 2): (-1, 3), (2, 1): (1, 3),
    (1, 3): (1, 2), (3, 1): (-1, 2),
    (2, 3): (-1, 1), (3, 2): (1, 1),
}


def multiply(left, right):
    result = [sp.Integer(0)] * 4
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            sign, k = TABLE[i, j]
            result[k] += sign * a * b
    return tuple(sp.expand(value) for value in result)


def scale(coefficient, value):
    return tuple(sp.expand(coefficient * component) for component in value)


def add(*values):
    return tuple(sp.expand(sum(value[i] for value in values)) for i in range(4))


ONE = (1, 0, 0, 0)
I = (0, 1, 0, 0)
J = (0, 0, 1, 0)
K = (0, 0, 0, 1)
Z = (x2, -x1, 0, 0)
W = (x3, 0, -x1, 0)

terms = [
    multiply(Z, Z),
    scale(sp.Rational(1, 2), multiply(multiply(Z, W), K)),
    multiply(multiply(multiply(Z, I), W), J),
    scale(sp.Rational(1, 2), multiply(multiply(W, Z), K)),
    scale(-1, multiply(multiply(multiply(W, I), W), I)),
]

for index, term in enumerate(terms, start=1):
    print(f"term_{index} = {term}")

total = add(*terms)
expected = (x1**2 + x2**2 + x3**2, 0, 0, 0)
assert total == expected
print(f"VERIFIED: sum = {total}")
