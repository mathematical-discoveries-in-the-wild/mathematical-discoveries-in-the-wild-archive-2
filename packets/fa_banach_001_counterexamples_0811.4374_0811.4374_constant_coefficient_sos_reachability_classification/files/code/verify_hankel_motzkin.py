#!/usr/bin/env python3
"""Exact checks for the Hankel identity and Motzkin support argument."""

from itertools import product

import sympy as sp


def factorial_multi(alpha: tuple[int, ...]) -> int:
    out = 1
    for entry in alpha:
        out *= sp.factorial(entry)
    return int(out)


def add_multi(alpha: tuple[int, ...], beta: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(alpha, beta))


def leibniz_hankel_check() -> None:
    x, y = sp.symbols("x y")
    variables = (x, y)
    indices = [(a, b) for a in range(4) for b in range(4 - a)]
    coefficients = sp.symbols(f"c0:{len(indices)}")
    g = sum(c * x**a * y**b for c, (a, b) in zip(coefficients, indices))

    sums = sorted({add_multi(alpha, beta) for alpha in indices for beta in indices})
    q_symbols = {gamma: sp.symbols(f"q_{gamma[0]}_{gamma[1]}") for gamma in sums}

    direct = 0
    for gamma, q_gamma in q_symbols.items():
        direct += q_gamma * sp.diff(g**2, x, gamma[0], y, gamma[1])

    gram = 0
    for alpha in indices:
        derivative_alpha = sp.diff(g, x, alpha[0], y, alpha[1])
        v_alpha = derivative_alpha / factorial_multi(alpha)
        for beta in indices:
            gamma = add_multi(alpha, beta)
            derivative_beta = sp.diff(g, x, beta[0], y, beta[1])
            v_beta = derivative_beta / factorial_multi(beta)
            gram += factorial_multi(gamma) * q_symbols[gamma] * v_alpha * v_beta

    assert sp.expand(direct - gram) == 0
    print("PASS: bivariate degree-three Leibniz/Hankel identity")


def half_newton_lattice_check() -> None:
    points: list[tuple[int, int, int]] = []
    for a, b, c in product(range(4), repeat=3):
        if a + b + c != 3:
            continue
        # Barycentric coordinates in conv((2,1,0),(1,2,0),(0,0,3)).
        lam = sp.Rational(2 * a - b, 3)
        mu = sp.Rational(2 * b - a, 3)
        nu = sp.Rational(c, 3)
        if lam >= 0 and mu >= 0 and nu >= 0 and lam + mu + nu == 1:
            points.append((a, b, c))
    expected = [(0, 0, 3), (1, 1, 1), (1, 2, 0), (2, 1, 0)]
    assert sorted(points) == expected
    print("PASS: half-Newton-polytope lattice points", sorted(points))


def motzkin_coefficient_check() -> None:
    x, y, z = sp.symbols("x y z")
    a, b, c, d = sp.symbols("a b c d", real=True)
    q = a * x**2 * y + b * x * y**2 + c * z**3 + d * x * y * z
    coefficient = sp.Poly(sp.expand(q**2), x, y, z).coeff_monomial(x**2 * y**2 * z**2)
    assert coefficient == d**2
    motzkin = x**4 * y**2 + x**2 * y**4 + z**6 - 3 * x**2 * y**2 * z**2
    assert sp.Poly(motzkin, x, y, z).coeff_monomial(x**2 * y**2 * z**2) == -3
    print("PASS: SOS coefficient is d^2 >= 0, while Motzkin coefficient is -3")


if __name__ == "__main__":
    leibniz_hankel_check()
    half_newton_lattice_check()
    motzkin_coefficient_check()
    print("ALL CHECKS PASSED")
