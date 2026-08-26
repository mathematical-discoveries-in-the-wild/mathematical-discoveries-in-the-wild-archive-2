"""Finite-section probe for an explicit non-inner extreme symbol.

Let c be the outer Schur function whose boundary modulus equals 1 on the
right semicircle and rho on the left semicircle, and set b(z)=z c(z).  Since
1-|c| vanishes on a set of positive measure, b is extreme.  The computation
tests finite-section lower bounds for monomial norms in H(K_b^2).

This is exploratory numerical evidence, not a proof.
"""

from __future__ import annotations

import numpy as np


def outer_coefficients(degree: int, rho: float = 0.35, samples: int = 1 << 17) -> np.ndarray:
    theta = 2 * np.pi * np.arange(samples) / samples
    # Right semicircle: cos(theta)>=0, modulus 1.  Left semicircle: rho.
    h = np.where(np.cos(theta) >= 0, 0.0, np.log(rho))
    fourier = np.fft.fft(h) / samples
    exponent = np.zeros(degree + 1, dtype=np.complex128)
    exponent[0] = fourier[0]
    exponent[1:] = 2 * fourier[1 : degree + 1]
    coeff = np.zeros(degree + 1, dtype=np.complex128)
    coeff[0] = np.exp(exponent[0])
    for n in range(1, degree + 1):
        coeff[n] = sum(k * exponent[k] * coeff[n - k] for k in range(1, n + 1)) / n
    return coeff


def kernel_matrix(b: np.ndarray) -> np.ndarray:
    size = len(b)
    toeplitz = np.zeros((size, size), dtype=np.complex128)
    for i in range(size):
        toeplitz[i, : i + 1] = b[i::-1]
    return np.eye(size) - toeplitz @ toeplitz.conj().T


def schur_square_coefficients(k: np.ndarray) -> np.ndarray:
    size = k.shape[0]
    out = np.zeros_like(k)
    for i in range(size):
        for j in range(size):
            total = 0j
            for a in range(i + 1):
                total += np.dot(k[a, : j + 1], k[i - a, j::-1])
            out[i, j] = total
    return out


def main() -> None:
    degree = 100
    c = outer_coefficients(degree)
    b = np.zeros(degree + 1, dtype=np.complex128)
    b[1:] = c[:-1]
    k2 = schur_square_coefficients(kernel_matrix(b))
    for monomial in range(7):
        print(f"z^{monomial}")
        for size in (8, 12, 18, 26, 38, 54, 72, 90, 101):
            if size <= monomial:
                continue
            section = (k2[:size, :size] + k2[:size, :size].conj().T) / 2
            unit = np.zeros(size, dtype=np.complex128)
            unit[monomial] = 1
            solution = np.linalg.solve(section, unit)
            norm_sq = float(np.real(unit.conj() @ solution))
            print(f"  size={size:3d} lower_bound_norm_sq={norm_sq:.10g}")


if __name__ == "__main__":
    main()

