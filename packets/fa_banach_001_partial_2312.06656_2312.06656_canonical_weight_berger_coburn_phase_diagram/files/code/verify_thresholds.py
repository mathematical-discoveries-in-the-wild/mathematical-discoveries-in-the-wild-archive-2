#!/usr/bin/env python3
"""Exact algebra checks for the canonical-weight Berger--Coburn packet."""

from fractions import Fraction


def thresholds(m: Fraction) -> tuple[Fraction, Fraction]:
    assert m > 2
    return 2 * m / (m + 2), 2 * m / (m - 2)


def gamma(m: Fraction, p: Fraction) -> Fraction:
    return (1 - m / 2) * (p - 2)


def in_ap(m: Fraction, p: Fraction) -> bool:
    g = gamma(m, p)
    return -2 < g < 2 * (p - 1)


def xia_radial_exponent(m: Fraction, p: Fraction) -> Fraction:
    """Exponent e in the tail integral int_R^infinity r^e dr."""
    return gamma(m, p) - 2 * p + 1


for m in map(Fraction, (3, 4, 6, 10)):
    p_minus, p_plus = thresholds(m)
    assert 1 < p_minus < 2 < p_plus
    assert 1 / p_minus + 1 / p_plus == 1
    assert gamma(m, p_minus) == 2 * (p_minus - 1)
    assert gamma(m, p_plus) == -2
    assert xia_radial_exponent(m, p_minus) == -1
    assert not in_ap(m, p_minus)
    assert in_ap(m, (p_minus + 2) / 2)
    assert in_ap(m, (2 + p_plus) / 2)
    assert not in_ap(m, p_plus)
    assert xia_radial_exponent(m, (1 + p_minus) / 2) > -1
    print(
        f"m={m}: p_-={p_minus}, p_+={p_plus}, "
        "Xia diverges through p_-, A_p holds exactly between the endpoints"
    )

for m in map(Fraction, (1, 2)):
    for p in map(Fraction, (Fraction(6, 5), 2, 5, 20)):
        assert in_ap(m, p)
    print(f"m={m}: sampled A_p checks hold for all tested p>1")

print("all exact threshold checks passed")
