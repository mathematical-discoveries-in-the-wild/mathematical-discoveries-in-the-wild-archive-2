#!/usr/bin/env python3
"""Exact symbolic checks for the scalar CMQd counterexample."""

import sympy as sp


def check_zero(label: str, expression: sp.Expr) -> None:
    reduced = sp.factor(sp.expand(expression))
    if reduced != 0:
        raise AssertionError(f"{label}: residual {reduced}")
    print(f"PASS: {label}")


def main() -> None:
    s, t, a, c, u, v, y, z = sp.symbols("s t a c u v y z", real=True)
    lam = sp.symbols("lambda", positive=True)

    quasidensity = (s - a) * (lam * s - c) + sp.Rational(1, 2) * (
        (s - a) ** 2 + (lam * s - c) ** 2
    )
    quasidensity_square = sp.Rational(1, 2) * (
        (1 + lam) * s - (a + c)
    ) ** 2
    check_zero("quasidensity completed square", quasidensity - quasidensity_square)

    p_integrand = (s - u) * (lam * s - v)
    p_completed = lam * (s - (v + lam * u) / (2 * lam)) ** 2 - (
        v - lam * u
    ) ** 2 / (4 * lam)
    check_zero("P_M completed square", p_integrand - p_completed)

    g_integrand = (lam * s - y) * (s - z)
    g_completed = lam * (s - (y + lam * z) / (2 * lam)) ** 2 - (
        y - lam * z
    ) ** 2 / (4 * lam)
    check_zero("G_M completed square", g_integrand - g_completed)

    p_formula = (v - lam * u) ** 2 / (4 * lam)
    f_objective = p_formula + (y - v) * (z - u)
    f_normal_form = (lam * u + v) ** 2 / (4 * lam) - y * u - z * v + y * z
    check_zero("F_M objective normal form", f_objective - f_normal_form)

    diagonal_case = sp.simplify(f_objective.subs(y, lam * z))
    diagonal_square = (lam * u + v - 2 * lam * z) ** 2 / (4 * lam)
    check_zero("F_M on y=lambda*z", diagonal_case - diagonal_square)

    null_direction = sp.simplify(f_objective.subs({u: t, v: -lam * t}))
    check_zero(
        "F_M null-direction drift",
        null_direction - ((lam * z - y) * t + y * z),
    )

    witness = sp.simplify(
        f_objective.subs({lam: 1, y: 0, z: 1, u: -t, v: t})
    )
    check_zero("lambda=1 witness tends to -infinity", witness + t)

    g_witness = ((y - lam * z) ** 2 / (4 * lam)).subs(
        {lam: 1, y: 0, z: 1}
    )
    if g_witness != sp.Rational(1, 4):
        raise AssertionError(f"wrong G_M witness: {g_witness}")
    print("PASS: G_M(0,1)=1/4 for lambda=1")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
