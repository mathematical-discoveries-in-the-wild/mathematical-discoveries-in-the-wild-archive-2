#!/usr/bin/env python3
"""Numerical checks for the sharp ReLU Riesz bounds 2/3 and 3/2.

The script verifies finite cosine/sine block similarity, checks spectra of
initial Gram matrices, and evaluates the explicit tensor-product sharpness
witnesses. The proof is analytic; floating-point output is only an audit.
"""

from __future__ import annotations

import math

import numpy as np


LOWER = 2.0 / 3.0
UPPER = 3.0 / 2.0


def odd_part(values: np.ndarray) -> np.ndarray:
    result = values.copy()
    while np.any(result % 2 == 0):
        mask = result % 2 == 0
        result[mask] //= 2
    return result


def v2(values: np.ndarray) -> np.ndarray:
    odd = odd_part(values)
    return np.rint(np.log2(values / odd)).astype(int)


def cosine_gram(n: int) -> np.ndarray:
    indices = np.arange(1, n + 1, dtype=np.int64)
    gcd = np.gcd(indices[:, None], indices[None, :]).astype(float)
    denominator = (indices[:, None] * indices[None, :]).astype(float) ** 2
    gram = gcd**4 / denominator
    valuations = v2(indices)
    gram[valuations[:, None] != valuations[None, :]] = 0.0
    return gram


def sine_gram_from_source(n: int) -> np.ndarray:
    """Build the sine Gram matrix using the parity rule in source Lemma 2.1."""
    indices = np.arange(1, n + 1, dtype=np.int64)
    gcd = np.gcd(indices[:, None], indices[None, :])
    valuations = v2(indices)
    same_block = valuations[:, None] == valuations[None, :]
    gram = cosine_gram(n)
    half_reduced_sum = (indices[:, None] + indices[None, :]) // (2 * gcd)
    negative = same_block & (half_reduced_sum % 2 == 0)
    gram[negative] *= -1.0
    return gram


def sine_signature(n: int) -> np.ndarray:
    indices = np.arange(1, n + 1, dtype=np.int64)
    odd = odd_part(indices)
    return np.where(odd % 4 == 1, 1.0, -1.0)


def local_rayleigh(r: float, length: int, alternating: bool) -> float:
    total = 1.0
    for h in range(1, length):
        term = (-r) ** h if alternating else r**h
        total += 2.0 * (length - h) * term / length
    return total


def tensor_witness(primes: list[int], length: int, alternating: bool) -> float:
    value = 1.0
    for prime in primes:
        value *= local_rayleigh(prime ** -2, length, alternating)
    return value


def main() -> None:
    worst_similarity = 0.0
    worst_conjugacy = 0.0
    finite_rows: list[tuple[int, float, float]] = []
    for n in (16, 32, 64, 128, 256, 512):
        cosine = cosine_gram(n)
        signature = sine_signature(n)
        conjugated = signature[:, None] * cosine * signature[None, :]
        sine = sine_gram_from_source(n)
        conjugacy_error = float(np.max(np.abs(sine - conjugated)))
        worst_conjugacy = max(worst_conjugacy, conjugacy_error)
        eigen_c = np.linalg.eigvalsh(cosine)
        eigen_s = np.linalg.eigvalsh(sine)
        error = float(np.max(np.abs(eigen_c - eigen_s)))
        worst_similarity = max(worst_similarity, error)
        if eigen_c[0] < LOWER - 2.0e-12 or eigen_c[-1] > UPPER + 2.0e-12:
            raise AssertionError((n, eigen_c[0], eigen_c[-1]))
        finite_rows.append((n, float(eigen_c[0]), float(eigen_c[-1])))

    primes = [3, 5, 7, 11, 13, 17, 19, 23]
    lower_witness = tensor_witness(primes, 80, alternating=True)
    upper_witness = tensor_witness(primes, 80, alternating=False)
    lower_product = math.prod((p * p - 1) / (p * p + 1) for p in primes)
    upper_product = 1.0 / lower_product
    if not lower_product < lower_witness < lower_product + 5.0e-3:
        raise AssertionError((lower_witness, lower_product))
    if not upper_product - 8.0e-3 < upper_witness < upper_product:
        raise AssertionError((upper_witness, upper_product))

    print("finite normalized cosine Gram spectra:")
    for n, smallest, largest in finite_rows:
        print(f"  N={n:3d}: lambda_min={smallest:.12f}, lambda_max={largest:.12f}")
    print(f"worst source-sign/conjugacy entry mismatch: {worst_conjugacy:.3e}")
    print(f"worst cosine/sine spectral mismatch: {worst_similarity:.3e}")
    print(f"8-prime, length-80 lower witness: {lower_witness:.12f}")
    print(f"8-prime limiting lower product: {lower_product:.12f}")
    print(f"global sharp lower constant: {LOWER:.12f}")
    print(f"8-prime, length-80 upper witness: {upper_witness:.12f}")
    print(f"8-prime limiting upper product: {upper_product:.12f}")
    print(f"global sharp upper constant: {UPPER:.12f}")


if __name__ == "__main__":
    main()
