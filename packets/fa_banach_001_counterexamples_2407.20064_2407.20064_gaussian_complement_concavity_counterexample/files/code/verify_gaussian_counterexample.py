#!/usr/bin/env python3
"""Exact arithmetic checks for the two-dimensional Gaussian example."""

from fractions import Fraction

import sympy as sp


a = sp.Integer(6)
b = sp.Integer(2)
t = sp.Rational(1, 2)
exterior_radius = sp.simplify((1 - t) * a - t * b)
assert exterior_radius == b

# e > 1 + 1 + 1/2 + 1/6 = 8/3, hence e^2 > 64/9 > 5.
partial_exp = sum((Fraction(1, 1), Fraction(1, 1),
                   Fraction(1, 2), Fraction(1, 6)))
assert partial_exp == Fraction(8, 3)
assert partial_exp**2 > 5

left = sp.exp(-2)
simple_lower_bound = (1 - sp.exp(-2)) / 4
assert sp.simplify(simple_lower_bound - left) > 0

exact_right = (sp.exp(-9) + sp.sqrt(1 - sp.exp(-2))) ** 2 / 4
assert sp.N(exact_right - left, 30) > 0

print("exterior radius =", exterior_radius)
print("left Gaussian mass = exp(-2) =", sp.N(left, 16))
print("right side =", sp.N(exact_right, 16))
print("certified lower bound for right side =", sp.N(simple_lower_bound, 16))

