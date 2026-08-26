#!/usr/bin/env python3
"""Exact audits for the weak-octonionic Stiefel local model."""

from __future__ import annotations

from fractions import Fraction
import random


ComplexQ = tuple[Fraction, Fraction]


def cadd(x: ComplexQ, y: ComplexQ) -> ComplexQ:
    return (x[0] + y[0], x[1] + y[1])


def cmul(x: ComplexQ, y: ComplexQ) -> ComplexQ:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x: ComplexQ) -> ComplexQ:
    return (x[0], -x[1])


def cscale(a: Fraction, x: ComplexQ) -> ComplexQ:
    return (a * x[0], a * x[1])


def inner(row1: tuple[ComplexQ, ComplexQ], row2: tuple[ComplexQ, ComplexQ]) -> ComplexQ:
    return cadd(cmul(row1[0], cconj(row2[0])), cmul(row1[1], cconj(row2[1])))


def rational_sphere2(q1: Fraction, q2: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    den = 1 + q1 * q1 + q2 * q2
    return ((1 - q1 * q1 - q2 * q2) / den, 2 * q1 / den, 2 * q2 / den)


def rational_circle(q: Fraction) -> ComplexQ:
    den = 1 + q * q
    return ((1 - q * q) / den, 2 * q / den)


def audit_unitary_forms() -> int:
    rng = random.Random(260507226)
    checks = 0
    one = (Fraction(1), Fraction(0))
    zero = (Fraction(0), Fraction(0))
    for _ in range(10_000):
        q1 = Fraction(rng.randint(-9, 9), rng.randint(1, 10))
        q2 = Fraction(rng.randint(-9, 9), rng.randint(1, 10))
        q3 = Fraction(rng.randint(-9, 9), rng.randint(1, 10))
        r, s, t = rational_sphere2(q1, q2)
        if r < 0:
            r, s, t = -r, -s, -t
        eta = rational_circle(q3)
        z = (s, t)
        row1 = ((r, Fraction(0)), z)
        row2 = (cscale(Fraction(-1), cmul(eta, cconj(z))), cscale(r, eta))

        assert inner(row1, row1) == one
        assert inner(row2, row2) == one
        assert inner(row1, row2) == zero
        checks += 3

        # Exact recovery used in the inverse chart.
        recovered_s = row1[1][0]
        recovered_b = row1[1][1]
        recovered_eta = cscale(Fraction(1, 1) / r, row2[1]) if r else eta
        assert recovered_s == s
        assert recovered_b == t
        if r:
            assert recovered_eta == eta
        checks += 3
    return checks


def audit_rank_one_minors() -> int:
    rng = random.Random(260507227)
    checks = 0
    for _ in range(1_000):
        u = [rng.randint(-20, 20) for _ in range(7)]
        v1 = rng.randint(-20, 20)
        v2 = rng.randint(-20, 20)
        a = [v1 * value for value in u]
        b = [v2 * value for value in u]
        for i in range(7):
            for j in range(i + 1, 7):
                assert a[i] * b[j] - a[j] * b[i] == 0
                checks += 1
    return checks


def main() -> None:
    checks = audit_unitary_forms() + audit_rank_one_minors()
    print(f"PASS: {checks:,} exact unitary, recovery, and rank-minor checks")


if __name__ == "__main__":
    main()
