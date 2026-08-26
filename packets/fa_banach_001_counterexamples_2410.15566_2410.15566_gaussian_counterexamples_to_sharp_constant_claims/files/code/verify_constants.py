#!/usr/bin/env python3
"""Verify the two explicit Gaussian counterexamples and related bounds."""

from math import e, factorial, gamma, pi


def source_gaussian_witness() -> float:
    """J(f) for n=2, a=1, b=8/5 in the source convention."""
    return (5 / 12) * (8 / 5) ** (1 / 6) * (pi * e) ** (-5 / 6)


def source_printed_constant() -> float:
    """Remark 2.2's printed 1/Q constant at n=2, m=1, Q=6."""
    return 2 ** (-5 / 2) * pi ** (-11 / 12)


def source_exact_ratio() -> float:
    return (10 / 3) * 5 ** (-1 / 6) * pi ** (1 / 12) * e ** (-5 / 6)


def suguro_gaussian_witness() -> float:
    """J(g) on standard H^1 for a=1 and central exponent c=1/6."""
    return (3 / 4) * (6 * pi**3 * e**3) ** (-1 / 4)


def suguro_candidate() -> float:
    return 1 / (2 * pi * e)


def suguro_exact_ratio() -> float:
    return (3 / 2) * (pi * e / 6) ** (1 / 4)


def lower_source(n: int) -> float:
    k = n + 1
    return (
        (2 * n + 1)
        / (2 * n * k)
        * (8 / (2 * n + 1)) ** (1 / (2 * k))
        * (pi * e) ** (-(2 * n + 1) / (2 * k))
    )


def upper_corrected(n: int) -> float:
    return factorial(n) ** (1 / (n + 1)) / (pi * n * n)


def upper_gamma_form(n: int) -> float:
    q = 2 * n + 2
    return (
        4 ** (2 / q)
        / (2 * n * (q - 2) * pi ** ((2 * n + 1) / q))
        * (gamma(2 * n + 1) / gamma((2 * n + 1) / 2)) ** (2 / q)
    )


def lower_standard(n: int) -> float:
    return 4 ** (-1 / (n + 1)) * lower_source(n)


def conjectured_standard(n: int) -> float:
    return 1 / ((n + 1) * pi * e)


j_source = source_gaussian_witness()
c_print = source_printed_constant()
r_source = source_exact_ratio()
assert abs(j_source / c_print - r_source) <= 1e-14
assert r_source > 1

j_suguro = suguro_gaussian_witness()
c_suguro = suguro_candidate()
r_suguro = suguro_exact_ratio()
assert abs(j_suguro / c_suguro - r_suguro) <= 1e-14
assert r_suguro > 1

print("Counterexample 1: printed source constant on H^2")
print(f"  J(f)       = {j_source:.15g}")
print(f"  C_print    = {c_print:.15g}")
print(f"  exact ratio= {r_source:.15g} > 1")
print("Counterexample 2: Suguro exact candidate on H^1")
print(f"  J(g)       = {j_suguro:.15g}")
print(f"  1/(2*pi*e) = {c_suguro:.15g}")
print(f"  exact ratio= {r_suguro:.15g} > 1")
print("Corrected upper bound and Gaussian-family comparison")

for dimension in range(1, 21):
    corrected = upper_corrected(dimension)
    gamma_form = upper_gamma_form(dimension)
    assert abs(corrected - gamma_form) <= 1e-12 * corrected
    assert lower_source(dimension) < corrected
    ratio = lower_standard(dimension) / conjectured_standard(dimension)
    print(
        f"  n={dimension:2d}  L_source={lower_source(dimension):.12g}  "
        f"U_source={corrected:.12g}  candidate_ratio={ratio:.12g}"
    )
    if dimension <= 6:
        assert ratio > 1
    else:
        assert ratio < 1
