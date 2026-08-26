#!/usr/bin/env python3
"""Exact certificate for the degree-six unicritical disk theorem.

All decisive calculations use SymPy rationals.  The two algebraic constants
are enclosed by rational isolating intervals.  Positivity on a unit box is
certified from (possibly subdivided) tensor-product Bernstein coefficients.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class Box2:
    t0: sp.Rational
    t1: sp.Rational
    y0: sp.Rational
    y1: sp.Rational
    depth: int = 0


def bernstein_coefficients(poly: sp.Poly, variables: tuple[sp.Symbol, ...], degrees: tuple[int, ...]) -> list[sp.Rational]:
    """Return tensor-product Bernstein coefficients on the unit box."""
    monomial = {
        powers: coefficient
        for powers, coefficient in poly.terms()
    }
    answer: list[sp.Rational] = []

    def visit_indices(prefix: tuple[int, ...]) -> None:
        if len(prefix) == len(variables):
            total = sp.Rational(0)

            def visit_powers(power_prefix: tuple[int, ...]) -> None:
                nonlocal total
                axis = len(power_prefix)
                if axis == len(variables):
                    coefficient = monomial.get(power_prefix, sp.Rational(0))
                    multiplier = sp.Rational(1)
                    for index, power, degree in zip(prefix, power_prefix, degrees):
                        multiplier *= sp.binomial(index, power) / sp.binomial(degree, power)
                    total += coefficient * multiplier
                    return
                for power in range(prefix[axis] + 1):
                    visit_powers(power_prefix + (power,))

            visit_powers(())
            answer.append(sp.factor(total))
            return
        for index in range(degrees[len(prefix)] + 1):
            visit_indices(prefix + (index,))

    visit_indices(())
    return answer


def l1_coefficient_bound(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> sp.Rational:
    """Bound |expression| on [0,1]^d by the power-basis coefficient l1 norm."""
    poly = sp.Poly(sp.expand(expression), *variables)
    return sum(abs(coefficient) for _, coefficient in poly.terms())


def build_coefficients(c: sp.Symbol) -> list[sp.Expr]:
    """Return the five correlations a_{6,k} as polynomials in c=cos(pi/7)."""
    n = 6
    u = [sp.Integer(1), 2 * c]
    for _ in range(2, n + 1):
        u.append(sp.expand(2 * c * u[-1] - u[-2]))
    return [
        sp.expand(((n - k) * sp.chebyshevt(k, c) + u[n - k - 1]) / (n + 1))
        for k in range(1, n)
    ]


def certify_curve_polynomial(curve_poly: sp.Expr, t: sp.Symbol, y: sp.Symbol) -> tuple[list[tuple[Box2, sp.Rational]], sp.Rational]:
    """Adaptively certify a bivariate polynomial by Bernstein subdivision."""
    base_poly = sp.Poly(sp.expand(curve_poly), t, y)
    degrees = (base_poly.degree(t), base_poly.degree(y))
    unit_t, unit_y = sp.symbols("unit_t unit_y")
    queue: deque[Box2] = deque([Box2(sp.Rational(0), sp.Rational(1), sp.Rational(0), sp.Rational(1))])
    certified: list[tuple[Box2, sp.Rational]] = []
    while queue:
        box = queue.popleft()
        transformed = sp.Poly(
            sp.expand(
                base_poly.as_expr().subs(
                    {
                        t: box.t0 + (box.t1 - box.t0) * unit_t,
                        y: box.y0 + (box.y1 - box.y0) * unit_y,
                    }
                )
            ),
            unit_t,
            unit_y,
        )
        minimum = min(bernstein_coefficients(transformed, (unit_t, unit_y), degrees))
        if minimum >= 0:
            certified.append((box, minimum))
            continue
        if box.depth >= 20:
            raise AssertionError(f"Bernstein subdivision failed on {box}; minimum={minimum}")
        if box.t1 - box.t0 >= box.y1 - box.y0:
            midpoint = (box.t0 + box.t1) / 2
            queue.append(Box2(box.t0, midpoint, box.y0, box.y1, box.depth + 1))
            queue.append(Box2(midpoint, box.t1, box.y0, box.y1, box.depth + 1))
        else:
            midpoint = (box.y0 + box.y1) / 2
            queue.append(Box2(box.t0, box.t1, box.y0, midpoint, box.depth + 1))
            queue.append(Box2(box.t0, box.t1, midpoint, box.y1, box.depth + 1))
    return certified, min(minimum for _, minimum in certified)


def main() -> None:
    t, x, y, c, q = sp.symbols("t x y c q", real=True)
    kappa = sp.Rational(124, 125)

    # Exact rational isolating intervals.
    c_lo = sp.Rational(4504844339, 5_000_000_000)
    c_hi = sp.Rational(225242217, 250_000_000)
    c_mid = (c_lo + c_hi) / 2
    q_lo = sp.Rational(544094102, 625_000_000)
    q_hi = sp.Rational(4352752817, 5_000_000_000)
    q_mid = (q_lo + q_hi) / 2

    c_polynomial = 8 * c**3 - 4 * c**2 - 4 * c + 1
    q_polynomial = 2 * q**5 - 1
    assert c_polynomial.subs(c, c_lo) < 0 < c_polynomial.subs(c, c_hi)
    assert sp.diff(c_polynomial, c).subs(c, c_lo) > 0
    assert q_polynomial.subs(q, q_lo) < 0 < q_polynomial.subs(q, q_hi)
    assert sp.diff(q_polynomial, q).subs(q, q_lo) > 0

    a = build_coefficients(c)
    powers = range(1, 6)
    coefficients = [a[index - 1] * (-t) ** (index - 1) for index in powers]
    center_a = coefficients[1] + coefficients[3]
    endpoint_radius = coefficients[0] + coefficients[2] + coefficients[4]

    # p(z)=f_t(z)-center_a has coefficients d_j for z^j, 0<=j<=5.
    d = [-center_a] + coefficients
    modulus_squared = sum(value**2 for value in d)
    for lag in range(1, 6):
        correlation = sum(d[index] * d[index + lag] for index in range(6 - lag))
        modulus_squared += 2 * correlation * sp.chebyshevt(lag, x)
    curve_gap = sp.expand(modulus_squared - kappa**2 * endpoint_radius**2)
    curve_gap_unit = sp.expand(curve_gap.subs(x, 2 * y - 1))
    curve_at_mid = sp.expand(curve_gap_unit.subs(c, c_mid))
    boxes, curve_base_lower = certify_curve_polynomial(curve_at_mid, t, y)
    curve_derivative_bound = l1_coefficient_bound(sp.diff(curve_gap_unit, c), (t, y, c))
    curve_error = curve_derivative_bound * (c_hi - c_lo) / 2
    curve_final_lower = curve_base_lower - curve_error
    assert curve_final_lower > 0

    # The affine disk in W(M_t) has Euclidean center and radius below.
    center_m = sp.expand(t + (1 - t**2) * center_a)
    radius_m = sp.expand((1 - t**2) * kappa * endpoint_radius)
    # If F<=0, then (R^2-c^2+1)/R <= q+q^{-1}, hence rho>=q.
    f_radius = sp.expand(q * (radius_m**2 - center_m**2 + 1) - (q**2 + 1) * radius_m)
    radius_quotient = sp.cancel(f_radius / (t**2 - 1))
    assert sp.expand(f_radius - (t**2 - 1) * radius_quotient) == 0
    radius_at_mid = sp.Poly(sp.expand(radius_quotient.subs({c: c_mid, q: q_mid})), t)
    radius_degree = radius_at_mid.degree(t)
    radius_bernstein = bernstein_coefficients(radius_at_mid, (t,), (radius_degree,))
    radius_base_lower = min(radius_bernstein)
    radius_c_derivative = l1_coefficient_bound(sp.diff(radius_quotient, c), (t, c, q))
    radius_q_derivative = l1_coefficient_bound(sp.diff(radius_quotient, q), (t, c, q))
    radius_error = radius_c_derivative * (c_hi - c_lo) / 2 + radius_q_derivative * (q_hi - q_lo) / 2
    radius_final_lower = radius_base_lower - radius_error
    assert radius_final_lower > 0

    print("PASS: exact degree-six certificate")
    print(f"cos(pi/7) isolating interval: [{c_lo}, {c_hi}]")
    print(f"2^(-1/5) isolating interval: [{q_lo}, {q_hi}]")
    print(f"curve Bernstein boxes: {len(boxes)}; maximum depth: {max(box.depth for box, _ in boxes)}")
    print(f"curve lower bound after algebraic-constant error: {curve_final_lower}")
    print(f"radius Bernstein coefficient lower bound: {radius_base_lower}")
    print(f"radius lower bound after algebraic-constant error: {radius_final_lower}")


if __name__ == "__main__":
    main()
