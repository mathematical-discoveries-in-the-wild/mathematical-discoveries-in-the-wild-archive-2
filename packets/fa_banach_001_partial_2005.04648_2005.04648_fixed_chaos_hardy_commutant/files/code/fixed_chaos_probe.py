#!/usr/bin/env python3
"""Finite-word audit of the fixed-chaos Haar-multishift norm formula.

The calculation uses the normalized Fock basis e_alpha.  It compares the
norm of the right-multiplier compression on words of length at most L with
the predicted vector-valued Hardy boundary norm.  The compression norms
must increase toward (and never exceed) the prediction.
"""

from __future__ import annotations

from itertools import product

import numpy as np


def words_upto(depth: int) -> list[str]:
    return ["".join(bits) for n in range(depth + 1) for bits in product("01", repeat=n)]


def suffixes_and_coefficients() -> tuple[
    dict[tuple[int, int, int], complex], dict[str, complex], dict[str, list[complex]]
]:
    """Return one finite order-three source symbol in normalized form."""

    xi: dict[tuple[int, int, int], complex] = {
        (0, 0, 0): 1.00,
        (1, 0, 0): 0.55,
        (2, 0, 0): -0.20,
        (0, 1, 0): 0.45j,
        (1, 1, 0): 0.30,
        (0, 0, 1): -0.35,
        (1, 0, 1): 0.20j,
        (0, 1, 1): 0.18,
    }
    normalized: dict[str, complex] = {}
    polynomials: dict[str, list[complex]] = {}
    for (k1, k2, k3), value in xi.items():
        gamma = "1" + "0" * k2 + "1" + "0" * k3
        beta = "0" * k1 + gamma
        normalized[beta] = value * 2.0 ** (-len(beta) / 2.0)
        coeffs = polynomials.setdefault(gamma, [])
        if len(coeffs) <= k1:
            coeffs.extend([0j] * (k1 + 1 - len(coeffs)))
        coeffs[k1] = normalized[beta]
    return xi, normalized, polynomials


def is_suffix_free(words: list[str]) -> bool:
    return all(not v.endswith(u) for u in words for v in words if u != v)


def compression_norm(depth: int, coefficients: dict[str, complex]) -> float:
    domain = words_upto(depth)
    outputs = sorted({alpha + beta for alpha in domain for beta in coefficients})
    row = {word: i for i, word in enumerate(outputs)}
    matrix = np.zeros((len(outputs), len(domain)), dtype=np.complex128)
    for j, alpha in enumerate(domain):
        for beta, value in coefficients.items():
            matrix[row[alpha + beta], j] += value
    return float(np.linalg.svd(matrix, compute_uv=False)[0])


def hardy_norm(polynomials: dict[str, list[complex]], samples: int = 262_144) -> float:
    theta = 2.0 * np.pi * np.arange(samples) / samples
    z = np.exp(1j * theta)
    square = np.zeros(samples)
    for coeffs in polynomials.values():
        values = np.polynomial.polynomial.polyval(z, np.asarray(coeffs))
        square += np.abs(values) ** 2
    return float(np.sqrt(square.max()))


def source_mixed_norm(
    xi: dict[tuple[int, int, int], complex], samples: int = 262_144
) -> float:
    """Evaluate 2^(-1) sup ||hat f(w,.)||_H2 for d=3, |w|=2^(-1/2)."""

    theta = 2.0 * np.pi * np.arange(samples) / samples
    w = 2.0 ** (-0.5) * np.exp(1j * theta)
    tails = sorted({(k2, k3) for _, k2, k3 in xi})
    square = np.zeros(samples)
    for k2, k3 in tails:
        max_k1 = max(k1 for k1, j2, j3 in xi if (j2, j3) == (k2, k3))
        coeffs = [xi.get((k1, k2, k3), 0j) for k1 in range(max_k1 + 1)]
        values = np.polynomial.polynomial.polyval(w, np.asarray(coeffs))
        square += 2.0 ** (-(2 + k2 + k3)) * np.abs(values) ** 2
    return float(np.sqrt(square.max()))


def main() -> None:
    xi, coefficients, polynomials = suffixes_and_coefficients()
    gammas = sorted(polynomials)
    predicted = hardy_norm(polynomials)
    mixed = source_mixed_norm(xi)
    assert abs(predicted - mixed) < 2e-12
    print(f"suffixes={gammas}")
    print(f"suffix_free={is_suffix_free(gammas)}")
    print(f"predicted_vector_Hinf={predicted:.12f}")
    print(f"source_mixed_Hinf_H2={mixed:.12f}")
    previous = 0.0
    for depth in range(0, 9):
        observed = compression_norm(depth, coefficients)
        assert previous <= observed + 1e-11
        assert observed <= predicted + 2e-6
        print(
            f"depth={depth:2d} compression={observed:.12f} "
            f"gap={predicted - observed:.3e}"
        )
        previous = observed


if __name__ == "__main__":
    main()
