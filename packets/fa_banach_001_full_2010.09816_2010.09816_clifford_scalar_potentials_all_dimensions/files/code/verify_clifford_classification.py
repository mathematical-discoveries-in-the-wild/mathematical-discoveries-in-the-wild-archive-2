#!/usr/bin/env python3
"""Finite-dimensional checks for the Clifford scalar-potential packet.

These checks support, but do not replace, the Schur/Clifford-algebra proof.
"""

from __future__ import annotations

import numpy as np


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron_all(factors: list[np.ndarray]) -> np.ndarray:
    out = np.array([[1]], dtype=complex)
    for factor in factors:
        out = np.kron(out, factor)
    return out


def clifford_generators(n: int) -> list[np.ndarray]:
    """The standard irreducible complex Cl_n generators."""
    m = n // 2
    generators: list[np.ndarray] = []
    for j in range(m):
        prefix = [Z] * j
        suffix = [I2] * (m - j - 1)
        generators.append(kron_all(prefix + [X] + suffix))
        generators.append(kron_all(prefix + [Y] + suffix))
    if n % 2:
        generators.append(kron_all([Z] * m))
    return generators


def volume(alpha: list[np.ndarray]) -> np.ndarray:
    d = len(alpha)
    out = np.eye(alpha[0].shape[0], dtype=complex)
    for matrix in alpha:
        out = out @ matrix
    return (1j ** (d * (d - 1) // 2)) * out


def anticommutant_nullity(alpha: list[np.ndarray], tol: float = 1e-9) -> int:
    n = alpha[0].shape[0]
    columns = []
    for row in range(n):
        for col in range(n):
            basis = np.zeros((n, n), dtype=complex)
            basis[row, col] = 1
            columns.append(
                np.concatenate([(a @ basis + basis @ a).reshape(-1) for a in alpha])
            )
    linear_map = np.stack(columns, axis=1)
    singular_values = np.linalg.svd(linear_map, compute_uv=False)
    rank = int(np.sum(singular_values > tol))
    return n * n - rank


def opnorm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def main() -> None:
    rng = np.random.default_rng(20260811)
    worst_relation = 0.0
    worst_square = 0.0

    for d in range(1, 9):
        gamma = clifford_generators(d + 1)
        alpha, beta = gamma[:d], gamma[d]
        n = beta.shape[0]
        identity = np.eye(n, dtype=complex)

        for j, a in enumerate(alpha):
            worst_relation = max(worst_relation, opnorm(a @ a - identity))
            worst_relation = max(worst_relation, opnorm(a - a.conj().T))
            worst_relation = max(worst_relation, opnorm(a @ beta + beta @ a))
            for k in range(j):
                worst_relation = max(
                    worst_relation, opnorm(a @ alpha[k] + alpha[k] @ a)
                )

        gamma_d = volume(alpha)
        predicted = [beta]
        if d % 2:
            second_mass = 1j * beta @ gamma_d
            predicted.append(second_mass)

        for mass in predicted:
            worst_relation = max(worst_relation, opnorm(mass - mass.conj().T))
            worst_relation = max(worst_relation, opnorm(mass @ mass - identity))
            for a in alpha:
                worst_relation = max(worst_relation, opnorm(a @ mass + mass @ a))

        nullity = anticommutant_nullity(alpha)
        expected = 1 if d % 2 == 0 else 2
        if nullity != expected:
            raise AssertionError(f"d={d}: anticommutant nullity {nullity}, expected {expected}")

        coefficients = rng.normal(size=len(predicted))
        potential = sum(c * mass for c, mass in zip(coefficients, predicted))
        worst_square = max(
            worst_square,
            opnorm(potential @ potential - np.dot(coefficients, coefficients) * identity),
        )
        print(
            f"d={d:2d} spinor_dim={n:2d} "
            f"complex_anticommutant_dim={nullity} predicted={expected}"
        )

    # The normal regular-singular residue i*lambda*alpha_n*M has eigenvalues +/-lambda.
    for d in range(1, 9):
        gamma = clifford_generators(d + 1)
        alpha, beta = gamma[:d], gamma[d]
        for lam in (0.2, 0.49, 0.5, 0.8, 1.7):
            residue = 1j * lam * alpha[-1] @ beta
            eigenvalues = np.linalg.eigvalsh(residue)
            if not (
                abs(eigenvalues[0] + lam) < 1e-10
                and abs(eigenvalues[-1] - lam) < 1e-10
            ):
                raise AssertionError((d, lam, eigenvalues))

    # Match the second mass to the Gamma_12 displayed in source PDF page 34.
    zero = np.zeros((2, 2), dtype=complex)
    source_alpha = [np.block([[zero, s], [s, zero]]) for s in (X, Y, Z)]
    source_beta = np.block([[I2, zero], [zero, -I2]])
    source_gamma12 = np.block([[zero, -1j * I2], [1j * I2, zero]])
    source_volume = volume(source_alpha)
    source_second_mass = 1j * source_beta @ source_volume
    if opnorm(source_second_mass + source_gamma12) > 1e-10:
        raise AssertionError("source d=3 second-mass identification failed")

    print(f"worst Clifford/classification residual: {worst_relation:.3e}")
    print(f"worst mass-square residual: {worst_square:.3e}")
    print("radial residue spectra verified for d=1,...,8 and five lambda values")
    print("source d=3 identity i beta Gamma_3 = -Gamma_12 verified")


if __name__ == "__main__":
    main()
