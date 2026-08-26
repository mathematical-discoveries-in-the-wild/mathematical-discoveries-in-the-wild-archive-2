#!/usr/bin/env python3
"""Numerical checks for the Stolz conformal map and coefficient identity."""

from __future__ import annotations

import cmath
import math
import random


def parameters(omega: float) -> tuple[float, float, float]:
    a = 1.0 / omega
    beta = math.acos(a)
    kappa = math.pi / (2.0 * beta)
    return a, beta, kappa


def cayley_to_disc(w: complex) -> complex:
    return (w - 1.0) / (w + 1.0)


def cayley_from_disc(z: complex) -> complex:
    return (1.0 + z) / (1.0 - z)


def generalized_chebyshev(w: complex, kappa: float) -> complex:
    return cmath.cosh(kappa * cmath.acosh(w))


def stolz_map(z: complex, omega: float) -> complex:
    _, _, kappa = parameters(omega)
    t = generalized_chebyshev(cayley_from_disc(z), kappa)
    return cayley_to_disc(t)


def stolz_ratio(z: complex) -> float:
    return abs(1.0 - z) / (1.0 - abs(z))


def verify_map(omega: float) -> dict[str, float]:
    _, beta, kappa = parameters(omega)

    max_boundary_modulus_error = 0.0
    max_strip_formula_error = 0.0
    min_interior_margin = 1.0
    max_ratio_excess = -math.inf

    # The two boundary components are u=t +/- i beta.  The induced map is
    # C(cosh(kappa*u)), whose modulus is exactly one there.
    for sign in (-1.0, 1.0):
        for j in range(-80, 81):
            t = j / 10.0
            u = complex(t, sign * beta)
            w = cmath.cosh(u)
            z = cayley_to_disc(w)
            direct = cayley_to_disc(cmath.cosh(kappa * u))
            principal = stolz_map(z, omega)
            max_boundary_modulus_error = max(
                max_boundary_modulus_error, abs(abs(direct) - 1.0)
            )
            max_strip_formula_error = max(
                max_strip_formula_error, abs(direct - principal)
            )

    # Interior strip samples must land in the Stolz domain and then in D.
    for j in range(-50, 51):
        t = 6.0 * j / 50.0
        for q in range(-19, 20):
            theta = beta * q / 20.0
            u = complex(t, theta)
            w = cmath.cosh(u)
            z = cayley_to_disc(w)
            image = cayley_to_disc(cmath.cosh(kappa * u))
            min_interior_margin = min(min_interior_margin, 1.0 - abs(image))
            max_ratio_excess = max(max_ratio_excess, stolz_ratio(z) - omega)
            max_strip_formula_error = max(
                max_strip_formula_error, abs(image - stolz_map(z, omega))
            )

    # Test the explicit inverse induced by dividing the half-plane strip
    # coordinate by kappa.
    rng = random.Random(230303022)
    max_inverse_error = 0.0
    for _ in range(1000):
        radius = 0.999 * math.sqrt(rng.random())
        angle = 2.0 * math.pi * rng.random()
        target = radius * cmath.exp(1j * angle)
        right_half_plane = cayley_from_disc(target)
        u = cmath.acosh(right_half_plane) / kappa
        z = cayley_to_disc(cmath.cosh(u))
        max_inverse_error = max(max_inverse_error, abs(stolz_map(z, omega) - target))

    # At w=1 the apparent arccosh branch is removable and T'_kappa(1)=kappa^2.
    h = 1.0e-6
    quotient = (generalized_chebyshev(1.0 + h, kappa) - 1.0) / h
    vertex_derivative_error = abs(quotient - kappa * kappa)

    return {
        "max_boundary_modulus_error": max_boundary_modulus_error,
        "max_strip_formula_error": max_strip_formula_error,
        "min_interior_margin": min_interior_margin,
        "max_ratio_excess": max_ratio_excess,
        "max_inverse_error": max_inverse_error,
        "vertex_derivative_error_at_h_1e-6": vertex_derivative_error,
    }


def verify_coefficient_identity() -> float:
    rng = random.Random(99173)
    max_error = 0.0
    for m1, m2 in ((1, 1), (1, 3), (2, 4), (5, 2)):
        total = m1 + m2
        coefficients = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(25)]
        for z in (0.13 + 0.21j, -0.37 + 0.11j, 0.71 - 0.04j):
            lhs = 0.0j
            rhs = 0.0j
            for k, a_k in enumerate(coefficients, start=1):
                phi_1 = k ** (m1 - 0.5) * (1.0 - z) ** m1 * z ** (k - 1)
                phi_2 = k ** (m2 - 0.5) * (1.0 - z) ** m2 * z ** (k - 1)
                lhs += a_k * phi_1 * phi_2
                rhs += a_k * k ** (total - 1) * (1.0 - z) ** total * z ** (2 * k - 2)
            max_error = max(max_error, abs(lhs - rhs))
    return max_error


def main() -> None:
    print("Stolz conformal-map verification")
    for omega in (1.2, 2.0, 5.0):
        print(f"omega={omega}")
        for key, value in verify_map(omega).items():
            print(f"  {key}: {value:.6e}")
    print(f"coefficient_identity_max_error: {verify_coefficient_identity():.6e}")


if __name__ == "__main__":
    main()
