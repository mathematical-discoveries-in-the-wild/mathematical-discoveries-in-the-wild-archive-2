#!/usr/bin/env python3
"""Exact and randomized checks for the three upper-bild counterexamples."""

from __future__ import annotations

import math
import random

import sympy as sp


def qadd(x, y):
    return tuple(sp.simplify(a + b) for a, b in zip(x, y))


def qscale(c, x):
    return tuple(sp.simplify(c * a) for a in x)


def qconj(x):
    a, b, c, d = x
    return (a, -b, -c, -d)


def qmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        sp.expand(a * e - b * f - c * g - d * h),
        sp.expand(a * f + b * e + c * h - d * g),
        sp.expand(a * g - b * h + c * e + d * f),
        sp.expand(a * h + b * g - c * f + d * e),
    )


def conjugate_by(unit, value):
    return qmul(qmul(qconj(unit), value), unit)


def weighted_term(weight, unit, value):
    return qscale(weight, conjugate_by(unit, value))


ONE = (sp.Integer(1), 0, 0, 0)
I = (0, sp.Integer(1), 0, 0)
J = (0, 0, sp.Integer(1), 0)
ZERO = (0, 0, 0, 0)
ONE_PLUS_I = qadd(ONE, I)


assert conjugate_by(J, I) == (0, -1, 0, 0)
assert conjugate_by(J, ONE_PLUS_I) == (1, -1, 0, 0)

# Universal real witnesses used in the three families.
half = sp.Rational(1, 2)
duplicate_witness = qadd(
    weighted_term(half, ONE, ONE_PLUS_I),
    weighted_term(half, J, ONE_PLUS_I),
)
mixed_witness = qadd(
    weighted_term(half, ONE, ONE_PLUS_I),
    weighted_term(half, J, I),
)
assert duplicate_witness == (1, 0, 0, 0)
assert mixed_witness == (half, 0, 0, 0)

# Exact converse parametrization for the singular-PSD triangle.
a, b = sp.symbols("a b", real=True)
w1 = (a + b) / 2
w2 = (a - b) / 2
w0 = 1 - a
constructed = qadd(
    qadd(
        weighted_term(w1, ONE, ONE_PLUS_I),
        weighted_term(w2, J, ONE_PLUS_I),
    ),
    weighted_term(w0, ONE, ZERO),
)
assert all(sp.simplify(x - y) == 0 for x, y in zip(constructed, (a, b, 0, 0)))
assert sp.simplify(w1 + w2 + w0 - 1) == 0


def fmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        a * e - b * f - c * g - d * h,
        a * f + b * e + c * h - d * g,
        a * g - b * h + c * e + d * f,
        a * h + b * g - c * f + d * e,
    )


def fconj(x):
    return (x[0], -x[1], -x[2], -x[3])


def fqterm(q, lam):
    return fmul(fmul(fconj(q), lam), q)


rng = random.Random(200802850)
lam = (1.0, 1.0, 0.0, 0.0)
max_excess = 0.0
for _ in range(10_000):
    raw = [rng.gauss(0.0, 1.0) for _ in range(12)]
    norm = math.sqrt(sum(x * x for x in raw))
    entries = [tuple(raw[4 * k + t] / norm for t in range(4)) for k in range(3)]
    value = tuple(sum(fqterm(entries[k], lam)[t] for k in range(2)) for t in range(4))
    real = value[0]
    imag_norm = math.sqrt(sum(value[t] ** 2 for t in range(1, 4)))
    max_excess = max(max_excess, imag_norm - real)
    assert -1e-12 <= real <= 1.0 + 1e-12
    assert imag_norm <= real + 2e-12

print("exact quaternion identities: PASS")
print("symbolic singular-PSD parametrization: PASS")
print(f"10,000-vector imaginary-norm bound: PASS (max excess {max_excess:.3e})")
