#!/usr/bin/env python3
"""Symbolic audit of the two Hardy identities used in the packet.

This is a sanity check only.  The proof in main.tex supplies the analytic
localization and perturbation arguments.
"""

import sympy as sp


def main() -> None:
    r = sp.symbols("r", real=True)
    w = 1 / (1 - r**2)
    a = 3 * r / (1 - r**2)
    upper_remainder = sp.factor(sp.diff(w * a, r) - w * a**2)
    assert sp.simplify(upper_remainder - 3 / (1 - r**2) ** 3) == 0

    x, b = sp.symbols("x b", positive=True)
    w_lower = 1 / (x**2 + b)
    a_lower = -sp.Rational(3, 2) / x
    lower_remainder = sp.factor(
        sp.diff(w_lower * a_lower, x) - w_lower * a_lower**2
    )
    lower_ratio = sp.factor(lower_remainder / (w_lower / x**2))
    expected_ratio = sp.Rational(3, 4) * (3 * x**2 - b) / (x**2 + b)
    assert sp.simplify(lower_ratio - expected_ratio) == 0

    y, z = sp.symbols("y z", positive=True)
    q = y - x**2
    rho = q / sp.sqrt(y)
    grad_rho_sq = sp.factor(sp.diff(rho, x) ** 2 + q**2 * sp.diff(rho, y) ** 2)
    scaled_grad = sp.factor(grad_rho_sq.subs(x**2, z * y))
    expected_grad = sp.Rational(1, 4) * (y * (1 - z**2) ** 2 + 16 * z)
    assert sp.simplify(scaled_grad - expected_grad) == 0

    print("upper square remainder:", upper_remainder)
    print("lower Hardy ratio:", lower_ratio)
    print("upper gauge gradient after x^2=z*y:", scaled_grad)
    print("on b <= x^2/4, lower ratio >= 33/20 > 1")
    print("on z <= 1/2 and y small, |grad rho|^2 < 3")
    print("PASS")


if __name__ == "__main__":
    main()
