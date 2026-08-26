#!/usr/bin/env python3
"""Exact algebra checks and finite regularity tests for the packet.

The algebra is represented in the degree-three free bimodule
  V tensor Lambda^2(V)  direct-sum  Lambda^2(V) tensor V.
No Peiffer relation occurs in degree three.
"""

from collections import defaultdict
from fractions import Fraction
from math import sqrt


def add_term(target, key, coefficient):
    target[key] += Fraction(coefficient)
    if target[key] == 0:
        del target[key]


def wedge(i, j):
    """Return sign and the increasing representative of e_i wedge e_j."""
    if i == j:
        return 0, (i, j)
    return (1, (i, j)) if i < j else (-1, (j, i))


def action_bracket(x, i, j):
    """[e_x,e_i wedge e_j] = e_x.(...) - (...).e_x."""
    sign, pair = wedge(i, j)
    out = defaultdict(Fraction)
    add_term(out, ((x,), pair, ()), sign)
    add_term(out, ((), pair, (x,)), -sign)
    return out


def delta_basis(key):
    left, (i, j), right = key
    out = defaultdict(Fraction)
    add_term(out, left + (i, j) + right, 1)
    add_term(out, left + (j, i) + right, -1)
    return out


def delta(element):
    out = defaultdict(Fraction)
    for key, coefficient in element.items():
        for word, value in delta_basis(key).items():
            add_term(out, word, coefficient * value)
    return dict(out)


def omega_element():
    out = defaultdict(Fraction)
    for x, i, j in ((1, 2, 3), (2, 3, 1), (3, 1, 2)):
        for key, coefficient in action_bracket(x, i, j).items():
            add_term(out, key, coefficient)
    return dict(out)


def regularity_grid_check():
    worst = (0.0, None)
    for rho in (0.501, 0.55, 0.6, 2.0 / 3.0):
        for p in range(1, 65):
            for q in range(1, 65):
                a, b = p / 64.0, q / 64.0
                rhs = a**rho * b ** (2 * rho) + a ** (2 * rho) * b**rho
                ratio = a * b / rhs
                if ratio > worst[0]:
                    worst = (ratio, (rho, a, b))
                assert ratio <= 1.0 + 1e-12
    return worst


def area_additivity_check():
    horizontal = 0
    for i in range(11):
        for j in range(i, 11):
            for k in range(j, 11):
                s1, s2, s3 = Fraction(i, 10), Fraction(j, 10), Fraction(k, 10)
                for p in range(11):
                    for q in range(p, 11):
                        t1, t2 = Fraction(p, 10), Fraction(q, 10)
                        whole = (s3 - s1) * (t2 - t1)
                        split = (s2 - s1) * (t2 - t1) + (s3 - s2) * (t2 - t1)
                        assert whole == split
                        horizontal += 1
    vertical = 0
    for i in range(11):
        for j in range(i, 11):
            s1, s2 = Fraction(i, 10), Fraction(j, 10)
            for p in range(11):
                for q in range(p, 11):
                    for r in range(q, 11):
                        t1, t2, t3 = Fraction(p, 10), Fraction(q, 10), Fraction(r, 10)
                        whole = (s2 - s1) * (t3 - t1)
                        split = (s2 - s1) * (t2 - t1) + (s2 - s1) * (t3 - t2)
                        assert whole == split
                        vertical += 1
    return horizontal, vertical


def main():
    omega = omega_element()
    assert len(omega) == 6
    assert all(abs(coefficient) == 1 for coefficient in omega.values())
    assert delta(omega) == {}

    # P_3=0 because every Peiffer generator has total degree at least 2+2=4.
    norm_squared = sum(coefficient * coefficient for coefficient in omega.values())
    assert norm_squared == 6

    horizontal, vertical = area_additivity_check()
    worst_ratio, worst_input = regularity_grid_check()
    print("nonzero degree-three coefficients:", len(omega))
    print("delta(Omega):", delta(omega))
    print("||Omega||^2:", norm_squared, "and ||Omega||:", sqrt(float(norm_squared)))
    print("rational horizontal-additivity tuples checked:", horizontal)
    print("rational vertical-additivity tuples checked:", vertical)
    print("largest tested mixed-regularity ratio:", worst_ratio)
    print("attained at (rho, ds, dt):", worst_input)
    print("PASS")


if __name__ == "__main__":
    main()
