#!/usr/bin/env python3
"""High-precision checks for the Ferrers positivity proof.

This is an independent numerical verifier, not part of the proof.  It checks
the source transcendental expression, the recurrence reduction, the
Mehler--Dirichlet representation, the monotonic reduction to lambda=1/2, and
the complete-elliptic-integral evaluation of that endpoint.
"""

from __future__ import annotations

import itertools
import mpmath as mp


mp.mp.dps = 60
PI = mp.pi


def ferrers_p(degree: mp.mpf, order: int, x: mp.mpf) -> mp.mpf:
    return mp.legenp(degree, order, x, type=2)


def source_expression(theta: mp.mpf, lam: mp.mpf) -> mp.mpf:
    x = mp.cos(theta)
    return (lam + 1) * ferrers_p(lam, -1, x) - ferrers_p(lam - 1, 0, x)


def reduced_expression(theta: mp.mpf, lam: mp.mpf) -> mp.mpf:
    x = mp.cos(theta)
    s = mp.sin(theta)
    return ((1 - s) * ferrers_p(-lam, 0, x) - x * ferrers_p(lam, 0, x)) / s


def mehler_p(theta: mp.mpf, degree: mp.mpf) -> mp.mpf:
    """Nonsingular change of variables in the Mehler--Dirichlet integral."""
    p = mp.sin(theta / 2)

    def integrand(y: mp.mpf) -> mp.mpf:
        a = mp.asin(p * mp.sin(y))
        return mp.cos(2 * (degree + mp.mpf("0.5")) * a) / mp.sqrt(
            1 - p * p * mp.sin(y) ** 2
        )

    return (2 / PI) * mp.quad(integrand, [0, PI / 2])


def endpoint_closed_form(theta: mp.mpf) -> mp.mpf:
    p = mp.sin(theta / 2)
    q = mp.cos(theta / 2)
    elliptic_k = mp.ellipk(p * p)
    elliptic_e = mp.ellipe(p * p)
    return (4 * (p - q) / PI) * ((p + q) * elliptic_e - q * elliptic_k)


def h_expression(theta: mp.mpf, lam: mp.mpf) -> mp.mpf:
    x = mp.cos(theta)
    s = mp.sin(theta)
    return (1 - s) * ferrers_p(-lam, 0, x) - x * ferrers_p(lam, 0, x)


def j(theta: mp.mpf, lam: mp.mpf, t: mp.mpf) -> mp.mpf:
    p = mp.sin(theta / 2)
    q = mp.cos(theta / 2)
    return p * mp.cos(t / 2) * mp.cos(lam * t) - q * mp.sin(t / 2) * mp.sin(
        lam * t
    )


def main() -> None:
    deltas = [
        mp.mpf("1e-6"),
        mp.mpf("1e-4"),
        mp.mpf("0.003"),
        mp.mpf("0.01"),
        mp.mpf("0.03"),
    ]
    deltas += [mp.mpf(j) * (PI / 2 - mp.mpf("0.08")) / 25 for j in range(1, 26)]
    deltas += [PI / 2 - mp.mpf("0.03"), PI / 2 - mp.mpf("1e-4")]
    thetas = sorted(set(PI / 2 + d for d in deltas if d < PI / 2))
    lambdas = [mp.mpf(-1) / 2 + mp.mpf(j) / 40 for j in range(41)]

    max_recurrence_error = mp.mpf(0)
    minimum_source_value = mp.inf
    minimum_location = None
    for theta, lam in itertools.product(thetas, lambdas):
        direct = source_expression(theta, lam)
        reduced = reduced_expression(theta, lam)
        max_recurrence_error = max(max_recurrence_error, abs(direct - reduced))
        if direct < minimum_source_value:
            minimum_source_value = direct
            minimum_location = (theta, lam)
        if not direct > 0:
            raise AssertionError(f"nonpositive source expression at {theta=}, {lam=}")

    # Check the integral representation at selected interior and near-endpoint values.
    max_mehler_error = mp.mpf(0)
    sample_thetas = [PI / 2 + mp.mpf("1e-4"), mp.mpf("2.0"), mp.mpf("2.6"), PI - mp.mpf("0.01")]
    sample_degrees = [mp.mpf("-0.5"), mp.mpf("-0.2"), mp.mpf(0), mp.mpf("0.2"), mp.mpf("0.5")]
    for theta, degree in itertools.product(sample_thetas, sample_degrees):
        lhs = ferrers_p(degree, 0, mp.cos(theta))
        rhs = mehler_p(theta, degree)
        max_mehler_error = max(max_mehler_error, abs(lhs - rhs))

    # Check pointwise monotonic reduction J_lambda >= J_{1/2} for 0<=lambda<=1/2.
    minimum_monotonic_margin = mp.inf
    for theta in thetas:
        for lam in [mp.mpf(j) / 80 for j in range(41)]:
            for m in range(1, 80):
                t = theta * mp.mpf(m) / 80
                margin = j(theta, lam, t) - j(theta, mp.mpf("0.5"), t)
                minimum_monotonic_margin = min(minimum_monotonic_margin, margin)
                if margin < -mp.mpf("1e-50"):
                    raise AssertionError("monotonic endpoint reduction failed")

    max_endpoint_error = mp.mpf(0)
    minimum_elliptic_margin = mp.inf
    for theta in thetas:
        p = mp.sin(theta / 2)
        q = mp.cos(theta / 2)
        elliptic_k = mp.ellipk(p * p)
        elliptic_e = mp.ellipe(p * p)
        minimum_elliptic_margin = min(minimum_elliptic_margin, elliptic_e - q * elliptic_k)
        exact_h = h_expression(theta, mp.mpf("0.5"))
        closed_h = endpoint_closed_form(theta)
        max_endpoint_error = max(max_endpoint_error, abs(exact_h - closed_h))
        if not (elliptic_e - q * elliptic_k > 0 and exact_h > 0):
            raise AssertionError("endpoint positivity failed")

    print("VERDICT: PASS")
    print(f"apertures={len(thetas)} lambda_values={len(lambdas)}")
    print(f"source_grid_cases={len(thetas) * len(lambdas)}")
    print(f"minimum_source_expression={mp.nstr(minimum_source_value, 14)}")
    print(
        "minimum_location=(omega={}, lambda={})".format(
            mp.nstr(minimum_location[0], 14), mp.nstr(minimum_location[1], 14)
        )
    )
    print(f"max_recurrence_error={mp.nstr(max_recurrence_error, 6)}")
    print(f"max_mehler_error={mp.nstr(max_mehler_error, 6)}")
    print(f"minimum_monotonic_margin={mp.nstr(minimum_monotonic_margin, 6)}")
    print(f"minimum_E_minus_qK={mp.nstr(minimum_elliptic_margin, 14)}")
    print(f"max_endpoint_formula_error={mp.nstr(max_endpoint_error, 6)}")


if __name__ == "__main__":
    main()
