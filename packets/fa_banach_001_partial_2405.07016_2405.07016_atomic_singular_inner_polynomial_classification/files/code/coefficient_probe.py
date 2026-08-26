"""Finite-section probe for monomial norms in H(K_b^2).

This is exploratory evidence only.  The candidate inner function is

    b(z) = z * product_j B_{a_j}(z),  a_j = 1 - 2^(-j-2),

with B_a(z)=(a-z)/(1-a z).  The script forms Taylor coefficient matrices for
K_b and its Schur square, then computes increasing finite-section lower bounds
for the norm of z^n.
"""

from __future__ import annotations

import numpy as np


def blaschke_factor_coefficients(a: float, degree: int) -> np.ndarray:
    out = np.empty(degree + 1, dtype=np.longdouble)
    out[0] = a
    powers = a ** np.arange(degree, dtype=np.longdouble)
    out[1:] = -(1 - a * a) * powers
    return out


def truncated_product_coefficients(degree: int, factors: int) -> np.ndarray:
    coeff = np.zeros(degree + 1, dtype=np.longdouble)
    coeff[0] = 1
    for j in range(1, factors + 1):
        a = np.longdouble(1) - np.longdouble(2) ** np.longdouble(-j - 2)
        factor = blaschke_factor_coefficients(float(a), degree)
        coeff = np.convolve(coeff, factor)[: degree + 1]
    # Prepend the zero at the origin.
    out = np.zeros(degree + 1, dtype=np.longdouble)
    out[1:] = coeff[:-1]
    return out


def kernel_matrix(b: np.ndarray) -> np.ndarray:
    size = len(b)
    toeplitz = np.zeros((size, size), dtype=np.longdouble)
    for i in range(size):
        toeplitz[i, : i + 1] = b[i::-1]
    return np.eye(size, dtype=np.longdouble) - toeplitz @ toeplitz.T


def schur_square_coefficients(k: np.ndarray) -> np.ndarray:
    size = k.shape[0]
    out = np.zeros_like(k)
    for i in range(size):
        for j in range(size):
            total = np.longdouble(0)
            for a in range(i + 1):
                total += np.dot(k[a, : j + 1], k[i - a, j::-1])
            out[i, j] = total
    return out


def main() -> None:
    degree = 90
    b = truncated_product_coefficients(degree, factors=120)
    k = kernel_matrix(b)
    k2 = schur_square_coefficients(k)
    for monomial in (0, 1, 2, 3):
        print(f"z^{monomial}")
        for size in (8, 12, 18, 26, 38, 54, 72, 90):
            section = np.asarray(k2[:size, :size], dtype=np.float64)
            unit = np.zeros(size)
            unit[monomial] = 1
            try:
                solution = np.linalg.solve(section, unit)
                norm_sq = float(unit @ solution)
                print(f"  size={size:2d} lower_bound_norm_sq={norm_sq:.8g}")
            except np.linalg.LinAlgError:
                print(f"  size={size:2d} singular")


if __name__ == "__main__":
    main()

