#!/usr/bin/env python3
"""Symbolic checks for the GRWS classification proof.

The script checks the two signed q-series coefficients and the exact signs of
the weight and CHE-ratio differences.  Hausdorff uniqueness is an analytic
argument in the packet and is not replaced by numerical tests.
"""

import sympy as sp


def main() -> None:
    x, q, n_param, d_param, u, v = sp.symbols(
        "x q N D u v", positive=True
    )

    # Squared weights a(x)=(1+Nx)/(1+Dx), with the next index x -> qx.
    a = (1 + n_param * x) / (1 + d_param * x)
    a_next = (1 + n_param * q * x) / (1 + d_param * q * x)
    weight_difference = sp.factor(a_next - a)
    expected_weight_difference = sp.factor(
        x * (1 - q) * (d_param - n_param)
        / ((1 + d_param * x) * (1 + d_param * q * x))
    )
    assert sp.factor(weight_difference - expected_weight_difference) == 0

    # If N<D and D>0, 1-a has alternating signed atoms.
    bernstein_obstruction = (d_param - n_param) * x / (1 + d_param * x)
    bernstein_series = sp.series(bernstein_obstruction, x, 0, 6).removeO()
    for k in range(1, 6):
        expected = (d_param - n_param) * (-d_param) ** (k - 1)
        assert sp.simplify(sp.expand(bernstein_series).coeff(x, k) - expected) == 0

    # In Sector III, N=-u and D=v with v>u.
    log_obstruction = sp.log((1 + v * x) / (1 - u * x))
    log_series = sp.series(log_obstruction, x, 0, 7).removeO()
    for k in range(1, 7):
        expected = (u**k + (-1) ** (k + 1) * v**k) / sp.Integer(k)
        assert sp.simplify(sp.expand(log_series).coeff(x, k) - expected) == 0

    # For delta_n=gamma_{n+1}-gamma_n, the source ratio is
    # r(x)=q(1+Nx)/(1+Dqx).  The next index again sends x to qx.
    ratio = q * (1 + n_param * x) / (1 + d_param * q * x)
    ratio_next = q * (1 + n_param * q * x) / (1 + d_param * q**2 * x)
    ratio_difference = sp.factor(ratio_next - ratio)
    expected_ratio_difference = sp.factor(
        q * x * (1 - q) * (d_param * q - n_param)
        / ((1 + d_param * q * x) * (1 + d_param * q**2 * x))
    )
    assert sp.factor(ratio_difference - expected_ratio_difference) == 0

    print(f"a_(n+1)-a_n = {weight_difference}")
    print(f"1-a signed series through x^5 = {bernstein_series}")
    print(f"-log(a) Sector-III series through x^6 = {log_series}")
    print(f"CHE ratio difference = {ratio_difference}")
    print("all symbolic identities passed")


if __name__ == "__main__":
    main()
