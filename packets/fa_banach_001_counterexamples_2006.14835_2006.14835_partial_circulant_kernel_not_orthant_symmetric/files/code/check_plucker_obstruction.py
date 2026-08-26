#!/usr/bin/env python3
"""Regression checks for the 2x4 partial-circulant Pluecker obstruction.

The proof is algebraic and does not depend on this script.
"""

import random

import sympy as sp


a, b, c, d = sp.symbols("a b c d", real=True)
p01 = a * a - b * d
p02 = a * b - c * d
p03 = a * c - d * d
p12 = b * b - a * c
p13 = b * c - a * d
p23 = c * c - b * d


def q(x01, x02, x03, x12, x13, x23):
    return sp.expand(
        (x01 - x23) * (x03 + x12) - x02**2 + x13**2
    )


original = sp.factor(q(p01, p02, p03, p12, p13, p23))
flipped = sp.factor(q(-p01, -p02, -p03, p12, p13, p23))

assert original == 0
assert flipped != 0
assert flipped.subs({a: 1, b: 0, c: 1, d: 0}) == 4

for _ in range(100):
    values = {x: random.randint(-10, 10) for x in (a, b, c, d)}
    assert original.subs(values) == 0

print("PASS: Q vanishes identically on the partial-circulant row spaces")
print("PASS: the coordinate-0 flip produces a nonzero polynomial")
print("flipped Q =", flipped)
print("witness at (1,0,1,0) =", flipped.subs({a: 1, b: 0, c: 1, d: 0}))
