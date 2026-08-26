#!/usr/bin/env python3
"""Exact rational verification of the S_3 convolution counterexample."""

from fractions import Fraction


Permutation = tuple[int, int, int]
Element = dict[Permutation, Fraction]

E: Permutation = (1, 2, 3)
S: Permutation = (2, 1, 3)  # (12)
A: Permutation = (1, 3, 2)  # (23)


def mul(p: Permutation, q: Permutation) -> Permutation:
    """Composition p*q, acting first by q and then by p."""
    return tuple(p[q[i] - 1] for i in range(3))  # type: ignore[return-value]


def add(u: Element, v: Element) -> Element:
    result = dict(u)
    for group_element, coefficient in v.items():
        result[group_element] = result.get(group_element, Fraction(0)) + coefficient
    return {g: coefficient for g, coefficient in result.items() if coefficient}


def scale(scalar: Fraction, u: Element) -> Element:
    return {g: scalar * coefficient for g, coefficient in u.items() if scalar * coefficient}


def conv(u: Element, v: Element) -> Element:
    result: Element = {}
    for g, coefficient_g in u.items():
        for h, coefficient_h in v.items():
            gh = mul(g, h)
            result[gh] = result.get(gh, Fraction(0)) + coefficient_g * coefficient_h
    return {g: coefficient for g, coefficient in result.items() if coefficient}


def norm(u: Element) -> Fraction:
    return sum((abs(coefficient) for coefficient in u.values()), Fraction(0))


identity = {E: Fraction(1)}
q = {E: Fraction(1, 2), S: Fraction(1, 2)}
delta_a = {A: Fraction(1)}
x = conv(conv(add(identity, scale(Fraction(-1), q)), delta_a), q)
mu = add(q, x)

expected_x = {
    (1, 3, 2): Fraction(1, 4),   # (23)
    (3, 1, 2): Fraction(1, 4),   # (132)
    (2, 3, 1): Fraction(-1, 4),  # (123)
    (3, 2, 1): Fraction(-1, 4),  # (13)
}

assert x == expected_x
assert conv(q, q) == q
assert conv(q, x) == {}
assert conv(x, q) == x
assert conv(x, x) == {}
assert conv(mu, mu) == mu
assert conv(mu, q) == mu
assert conv(q, mu) == q
assert norm(q) == 1
assert norm(x) == 1
assert norm(mu) == 2

print("All exact S_3 convolution identities passed.")
print(f"||q||_1={norm(q)}, ||x||_1={norm(x)}, ||mu||_1={norm(mu)}")
