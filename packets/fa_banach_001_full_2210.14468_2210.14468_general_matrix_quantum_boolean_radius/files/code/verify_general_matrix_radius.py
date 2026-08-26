#!/usr/bin/env python3
"""Numerical sanity checks for the general-matrix radius packet.

The script is not part of the proof.  It verifies the concrete unitary family
and the scalar phase-average identity used in the exact argument.
"""

from __future__ import annotations

import math

import numpy as np


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = factors[0]
    for factor in factors[1:]:
        out = np.kron(out, factor)
    return out


def verify_unitary_family() -> tuple[int, float, float]:
    identity2 = np.eye(2, dtype=complex)
    sigma1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    samples = (0.5, 0.9, 0.99, 0.9999)
    cases = 0
    max_unitarity_error = 0.0
    max_radius_error = 0.0

    for n in (1, 2, 3):
        identity = np.eye(2**n, dtype=complex)
        pauli = kron_all([sigma1] + [identity2] * (n - 1))
        for a in samples:
            b = math.sqrt(1.0 - a * a)
            matrix = a * identity + 1j * b * pauli
            error = np.linalg.norm(
                matrix.conj().T @ matrix - identity, ord=2
            )
            max_unitarity_error = max(max_unitarity_error, float(error))

            computed_radius = (1.0 - a) / b
            closed_radius = math.sqrt((1.0 - a) / (1.0 + a))
            max_radius_error = max(
                max_radius_error, abs(computed_radius - closed_radius)
            )
            cases += 1

    return cases, max_unitarity_error, max_radius_error


def verify_phase_average() -> tuple[int, float]:
    coefficients = np.array(
        [1 + 2j, -3 + 0.25j, 0.4 - 1.7j, -2.2 - 0.8j], dtype=complex
    )
    sample_count = 1 << 18
    theta = 2.0 * math.pi * np.arange(sample_count) / sample_count
    rotations = np.exp(-1j * theta)
    sampled = np.abs(
        np.real(rotations[:, np.newaxis] * coefficients[np.newaxis, :])
    ).mean(axis=0)
    exact = (2.0 / math.pi) * np.abs(coefficients)
    return sample_count, float(np.max(np.abs(sampled - exact)))


def verify_classical_family() -> tuple[int, float, float]:
    samples = (0.5, 0.9, 0.99, 0.9999)
    max_norm_error = 0.0
    max_radius_error = 0.0
    for a in samples:
        b = math.sqrt(1.0 - a * a)
        values = np.array([a + 1j * b, a - 1j * b])
        max_norm_error = max(
            max_norm_error, abs(float(np.max(np.abs(values))) - 1.0)
        )
        max_radius_error = max(
            max_radius_error,
            abs((1.0 - a) / b - math.sqrt((1.0 - a) / (1.0 + a))),
        )
    return len(samples), max_norm_error, max_radius_error


def main() -> None:
    cases, unitary_error, radius_error = verify_unitary_family()
    phase_samples, phase_error = verify_phase_average()
    classical_cases, classical_norm_error, classical_radius_error = (
        verify_classical_family()
    )
    print(f"unitary_cases={cases}")
    print(f"max_unitarity_error={unitary_error:.3e}")
    print(f"max_radius_formula_error={radius_error:.3e}")
    print(f"classical_cases={classical_cases}")
    print(f"max_classical_norm_error={classical_norm_error:.3e}")
    print(f"max_classical_radius_error={classical_radius_error:.3e}")
    print(f"phase_samples={phase_samples}")
    print(f"max_phase_average_error={phase_error:.3e}")
    if (
        unitary_error > 1e-12
        or radius_error > 1e-12
        or classical_norm_error > 1e-12
        or classical_radius_error > 1e-12
        or phase_error > 1e-9
    ):
        raise SystemExit("verification tolerance exceeded")


if __name__ == "__main__":
    main()
