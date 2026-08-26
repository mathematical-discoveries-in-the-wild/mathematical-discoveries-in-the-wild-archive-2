#!/usr/bin/env python3
"""Finite-dimensional sanity checks for identities used in the packet."""

import numpy as np


def normalized_logdet(matrix: np.ndarray) -> float:
    sign, value = np.linalg.slogdet(matrix)
    if sign == 0:
        raise AssertionError("unexpected singular matrix")
    return float(value / matrix.shape[0])


def gue(rng: np.random.Generator, size: int) -> np.ndarray:
    z = (rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))) / np.sqrt(2 * size)
    return (z + z.conj().T) / np.sqrt(2)


def main() -> None:
    rng = np.random.default_rng(240615922)
    m, n, size = 3, 4, 5
    coefficients = []
    for _ in range(n):
        b = np.triu(rng.integers(-3, 4, size=(m, m))).astype(complex)
        coefficients.append(b)
    # Ensure every diagonal scalar pencil is nonzero.
    coefficients[0] += np.eye(m)
    x = [gue(rng, size) for _ in range(n)]
    block = sum(np.kron(b, y) for b, y in zip(coefficients, x))
    diagonal_blocks = [sum(b[j, j] * y for b, y in zip(coefficients, x)) for j in range(m)]
    lhs = normalized_logdet(block)
    rhs = sum(normalized_logdet(y) for y in diagonal_blocks) / m
    if not np.isclose(lhs, rhs, atol=2e-11, rtol=2e-11):
        raise AssertionError((lhs, rhs))

    p = rng.normal(size=(m, m))
    q = rng.normal(size=(m, m))
    p += 3 * np.eye(m)
    q += 3 * np.eye(m)
    transformed_coefficients = [np.linalg.inv(p) @ b @ np.linalg.inv(q) for b in coefficients]
    a = sum(np.kron(c, y) for c, y in zip(transformed_coefficients, x))
    reconstructed = np.kron(p, np.eye(size)) @ a @ np.kron(q, np.eye(size))
    if not np.allclose(reconstructed, block, atol=2e-11, rtol=2e-11):
        raise AssertionError("left/right reconstruction failed")
    predicted = normalized_logdet(a) + (np.log(abs(np.linalg.det(p))) + np.log(abs(np.linalg.det(q)))) / m
    if not np.isclose(predicted, normalized_logdet(block), atol=2e-11, rtol=2e-11):
        raise AssertionError("normalized determinant multiplier failed")

    print("block-triangular determinant factorization: OK")
    print("left/right normalized determinant multiplier: OK")


if __name__ == "__main__":
    main()
