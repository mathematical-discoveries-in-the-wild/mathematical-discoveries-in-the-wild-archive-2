#!/usr/bin/env python3
"""Exact Bernstein certificates for unicritical degrees 6 through 12."""

from __future__ import annotations

from collections import deque

import sympy as sp

from verify_degree6 import bernstein_coefficients, certify_curve_polynomial, l1_coefficient_bound


KAPPAS = {
    6: sp.Rational(124, 125),
    7: sp.Rational(997, 1000),
    8: sp.Rational(249, 250),
    9: sp.Rational(499, 500),
    10: sp.Rational(499, 500),
    11: sp.Rational(999, 1000),
    12: sp.Rational(999, 1000),
}


def isolating_interval(number: sp.Expr, variable: sp.Symbol, digits: int = 32) -> tuple[sp.Rational, sp.Rational, sp.Expr]:
    denominator = 10**digits
    scaled = sp.N(number, digits + 20) * denominator
    numerator = int(sp.floor(scaled))
    low = sp.Rational(numerator, denominator)
    high = sp.Rational(numerator + 1, denominator)
    polynomial = sp.minimal_polynomial(number, variable)
    exact_poly = sp.Poly(polynomial, variable)
    assert exact_poly.count_roots(low, high) == 1
    # Both constants used below are the largest real conjugates of their
    # minimal polynomials.  This makes the root identification exact rather
    # than dependent on the decimal approximation used to choose the bracket.
    assert exact_poly.count_roots(high, sp.oo) == 0
    return low, high, polynomial


def correlations(n: int, c: sp.Symbol) -> list[sp.Expr]:
    u = [sp.Integer(1), 2 * c]
    for _ in range(2, n + 1):
        u.append(sp.expand(2 * c * u[-1] - u[-2]))
    return [
        sp.expand(((n - k) * sp.chebyshevt(k, c) + u[n - k - 1]) / (n + 1))
        for k in range(1, n)
    ]


def certify_univariate(poly: sp.Poly, variable: sp.Symbol) -> tuple[int, int, sp.Rational]:
    degree = poly.degree(variable)
    unit = sp.Symbol("unit")
    queue = deque([(sp.Rational(0), sp.Rational(1), 0)])
    box_count = 0
    max_depth = 0
    lower_bounds: list[sp.Rational] = []
    while queue:
        low, high, depth = queue.popleft()
        transformed = sp.Poly(sp.expand(poly.as_expr().subs(variable, low + (high - low) * unit)), unit)
        minimum = min(bernstein_coefficients(transformed, (unit,), (degree,)))
        if minimum >= 0:
            box_count += 1
            max_depth = max(max_depth, depth)
            lower_bounds.append(minimum)
            continue
        if depth >= 30:
            raise AssertionError(f"univariate Bernstein failure on [{low},{high}]: {minimum}")
        midpoint = (low + high) / 2
        queue.append((low, midpoint, depth + 1))
        queue.append((midpoint, high, depth + 1))
    return box_count, max_depth, min(lower_bounds)


def certify_degree(n: int) -> dict[str, object]:
    t, x, y, c, q = sp.symbols("t x y c q", real=True)
    kappa = KAPPAS[n]
    c_exact = sp.cos(sp.pi / (n + 1))
    q_exact = 2 ** (-sp.Rational(1, n - 1))
    c_lo, c_hi, _ = isolating_interval(c_exact, c)
    q_lo, q_hi, _ = isolating_interval(q_exact, q)
    c_mid = (c_lo + c_hi) / 2
    q_mid = (q_lo + q_hi) / 2

    a = correlations(n, c)
    coefficients = [a[index - 1] * (-t) ** (index - 1) for index in range(1, n)]
    center_a = sum(coefficients[index - 1] for index in range(2, n, 2))
    endpoint_radius = sum(coefficients[index - 1] for index in range(1, n, 2))
    d = [-center_a] + coefficients
    modulus_squared = sum(value**2 for value in d)
    for lag in range(1, n):
        correlation = sum(d[index] * d[index + lag] for index in range(n - lag))
        modulus_squared += 2 * correlation * sp.chebyshevt(lag, x)
    curve_gap = sp.expand(modulus_squared - kappa**2 * endpoint_radius**2)
    curve_gap_unit = sp.expand(curve_gap.subs(x, 2 * y - 1))
    boxes, curve_base = certify_curve_polynomial(sp.expand(curve_gap_unit.subs(c, c_mid)), t, y)
    curve_derivative = l1_coefficient_bound(sp.diff(curve_gap_unit, c), (t, y, c))
    curve_final = curve_base - curve_derivative * (c_hi - c_lo) / 2
    assert curve_final > 0

    center_m = sp.expand(t + (1 - t**2) * center_a)
    radius_m = sp.expand((1 - t**2) * kappa * endpoint_radius)
    f_radius = sp.expand(q * (radius_m**2 - center_m**2 + 1) - (q**2 + 1) * radius_m)
    quotient = sp.cancel(f_radius / (t**2 - 1))
    assert sp.expand(f_radius - (t**2 - 1) * quotient) == 0
    radius_poly = sp.Poly(sp.expand(quotient.subs({c: c_mid, q: q_mid})), t)
    radius_boxes, radius_depth, radius_base = certify_univariate(radius_poly, t)
    radius_c_derivative = l1_coefficient_bound(sp.diff(quotient, c), (t, c, q))
    radius_q_derivative = l1_coefficient_bound(sp.diff(quotient, q), (t, c, q))
    radius_final = (
        radius_base
        - radius_c_derivative * (c_hi - c_lo) / 2
        - radius_q_derivative * (q_hi - q_lo) / 2
    )
    assert radius_final > 0
    return {
        "n": n,
        "kappa": kappa,
        "curve_boxes": len(boxes),
        "curve_depth": max(box.depth for box, _ in boxes),
        "curve_lower": curve_final,
        "radius_boxes": radius_boxes,
        "radius_depth": radius_depth,
        "radius_lower": radius_final,
    }


def main() -> None:
    for n in sorted(KAPPAS):
        result = certify_degree(n)
        print(
            "PASS "
            f"n={n} kappa={result['kappa']} "
            f"curve_boxes={result['curve_boxes']} curve_depth={result['curve_depth']} "
            f"curve_lower~{sp.N(result['curve_lower'], 8)} "
            f"radius_boxes={result['radius_boxes']} radius_depth={result['radius_depth']} "
            f"radius_lower~{sp.N(result['radius_lower'], 8)}"
        )


if __name__ == "__main__":
    main()
