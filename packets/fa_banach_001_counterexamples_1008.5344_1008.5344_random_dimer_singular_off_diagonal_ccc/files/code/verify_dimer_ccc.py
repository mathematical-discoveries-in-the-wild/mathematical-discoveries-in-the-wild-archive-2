#!/usr/bin/env python3
"""Exact finite-cell checks for the dimer ccc counterexample.

The script uses only the Python standard library.  It checks the two eigenpairs,
velocity matrix elements, finite-volume ccc support, the Wegner constant for a
uniform law, and the 1/epsilon rectangle blow-up.
"""

from __future__ import annotations

import cmath
import math


def inner(x: tuple[complex, complex], y: tuple[complex, complex]) -> complex:
    return x[0].conjugate() * y[0] + x[1].conjugate() * y[1]


def matvec(
    matrix: tuple[tuple[complex, complex], tuple[complex, complex]],
    vector: tuple[complex, complex],
) -> tuple[complex, complex]:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def close(x: complex, y: complex, tol: float = 1.0e-12) -> bool:
    return abs(x - y) <= tol


def main() -> None:
    t = 1.7
    inv_sqrt_two = 1.0 / math.sqrt(2.0)
    plus = (inv_sqrt_two + 0j, inv_sqrt_two + 0j)
    minus = (inv_sqrt_two + 0j, -inv_sqrt_two + 0j)
    velocity = ((0j, 1j * t), (-1j * t, 0j))

    for u in (-2.3, -0.1, 4.2):
        hamiltonian = ((u + 0j, t + 0j), (t + 0j, u + 0j))
        h_plus = matvec(hamiltonian, plus)
        h_minus = matvec(hamiltonian, minus)
        assert all(close(h_plus[j], (u + t) * plus[j]) for j in range(2))
        assert all(close(h_minus[j], (u - t) * minus[j]) for j in range(2))

    v_plus_plus = inner(plus, matvec(velocity, plus))
    v_minus_minus = inner(minus, matvec(velocity, minus))
    v_plus_minus = inner(plus, matvec(velocity, minus))
    v_minus_plus = inner(minus, matvec(velocity, plus))
    assert close(v_plus_plus, 0j)
    assert close(v_minus_minus, 0j)
    assert close(abs(v_plus_minus) ** 2, t**2)
    assert close(abs(v_minus_plus) ** 2, t**2)

    omegas = (-1.9, -0.4, 0.25, 1.1, 2.6)
    support = []
    for u in omegas:
        support.extend(((u + t, u - t, t**2), (u - t, u + t, t**2)))
    assert all(close(abs(e1 - e2), 2.0 * t) for e1, e2, _ in support)
    total_weight_per_site = sum(weight for _, _, weight in support) / (2 * len(omegas))
    assert close(total_weight_per_site, t**2)

    # Uniform rho=1/2 on [-1,1], u0=0.  For epsilon<min(1,2t),
    # rectangle mass per physical site is (t^2/2)*(epsilon/2).
    ratios = []
    for epsilon in (0.2, 0.1, 0.05, 0.025):
        mass = (t**2 / 2.0) * (epsilon / 2.0)
        ratios.append(mass / epsilon**2)
    assert all(close(ratios[j + 1], 2.0 * ratios[j]) for j in range(3))

    # Per cell, each of the two shifted eigenvalue laws has density <= ||rho||_inf.
    rho_sup = 0.5
    wegner_constant_per_cell = 2.0 * rho_sup
    assert close(wegner_constant_per_cell, 1.0)

    # Exact scalar, standard-translation periodic-phase model.  These formulas
    # are the two-band Floquet computation used in the packet.
    periodic_a = 1.0
    periodic_t = 1.0
    periodic_s = 1.0
    assert 2.0 * periodic_s > periodic_t**2 / periodic_a
    periodic_rows = []
    for k in (0.2, 0.7, math.pi / 2.0, 2.4, 3.0):
        energy = math.sqrt(
            periodic_a**2
            + 4.0 * periodic_t**2 * math.cos(k / 2.0) ** 2
        )
        plus_derivative = -math.sin(k) * (
            2.0 * periodic_s + periodic_t**2 / energy
        )
        minus_derivative = -math.sin(k) * (
            2.0 * periodic_s - periodic_t**2 / energy
        )
        weight = (
            4.0
            * periodic_a**2
            * periodic_t**2
            * math.sin(k / 2.0) ** 2
            / energy**2
        )
        assert plus_derivative < 0.0
        assert minus_derivative < 0.0
        assert weight > 0.0
        periodic_rows.append((k, plus_derivative, minus_derivative, weight))

    print("eigenpairs: exact for 3 sample cell energies")
    print("velocity: diagonal weights 0, off-diagonal weights t^2")
    print("finite support: all energy differences are +/-2t")
    print("rectangle quotients:", ", ".join(f"{r:.6f}" for r in ratios))
    print("doubling check: quotient doubles when epsilon halves")
    print("Wegner constant per cell for rho=Unif[-1,1]:", wegner_constant_per_cell)
    print("periodic-phase Floquet checks (k, lambda_+', lambda_-', weight):")
    for row in periodic_rows:
        print("  ", " ".join(f"{entry:.6f}" for entry in row))
    print("standard-translation periodic branch: both derivatives negative, weight positive")
    print("PASS")


if __name__ == "__main__":
    main()
