#!/usr/bin/env python3
"""Exact symbolic QA for the all-order C-fraction parity proof.

The proof is formal and analytic.  This script independently runs the regular
C-fraction tail algorithm on the Euler correction through a_26, checks the
coefficients printed in arXiv:1407.3865, and verifies the opposite-pair law.
"""

import sympy as sp


X = sp.symbols("x")
NUMBER_OF_COEFFICIENTS = 26
SERIES_ORDER = NUMBER_OF_COEFFICIENTS + 5


def euler_correction_series(order: int) -> sp.Expr:
    result = sp.Rational(1, 2) * X
    for m in range(1, order // 2 + 2):
        result -= sp.bernoulli(2 * m) * X ** (2 * m) / (2 * m)
    return sp.series(result, X, 0, order).removeO()


def regular_cfraction_coefficients(count: int) -> list[sp.Rational]:
    tail = euler_correction_series(SERIES_ORDER)
    coefficients = []
    for j in range(count):
        coefficient = sp.factor(sp.expand(tail).coeff(X, 1))
        if coefficient == 0:
            raise AssertionError(f"tail {j + 1} has zero linear coefficient")
        coefficients.append(coefficient)
        remaining_order = SERIES_ORDER - j - 1
        tail = sp.series(coefficient * X / tail - 1, X, 0, remaining_order).removeO()
    return coefficients


if __name__ == "__main__":
    a = regular_cfraction_coefficients(NUMBER_OF_COEFFICIENTS)

    known_even = {
        1: sp.Rational(1, 2),
        2: sp.Rational(1, 6),
        4: sp.Rational(3, 5),
        6: sp.Rational(79, 126),
        8: sp.Rational(7230, 6241),
        10: sp.Rational(4146631, 3833346),
        12: sp.Rational(306232774533, 179081182865),
    }
    for index, expected in known_even.items():
        assert a[index - 1] == expected, (index, a[index - 1], expected)

    for k in range(1, (NUMBER_OF_COEFFICIENTS - 1) // 2 + 1):
        assert a[2 * k] == -a[2 * k - 1]

    print("PASS: source coefficients a_1,...,a_13 reproduced exactly.")
    print("PASS: a_(2k+1) = -a_(2k) for k=1,...,12.")
    print(f"a_14 = {a[13]}")
    print(f"a_15 = {a[14]}")
    print(f"a_16 = {a[15]}")
    print(f"a_17 = {a[16]}")
