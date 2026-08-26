"""Discretized L2 sanity check for strict complex-to-real norm loss.

This finite-dimensional calculation is not part of the proof.  Piecewise
constant input cells are integrated exactly against the kernel at output-cell
midpoints, and the matrix spectral norm is compared at complex and real order.
"""

from __future__ import annotations

import numpy as np
from scipy.special import gamma


def collocation_matrix(xi: complex, n: int) -> np.ndarray:
    h = 1.0 / n
    x = (np.arange(n) + 0.5) * h
    matrix = np.zeros((n, n), dtype=np.complex128)
    gamma_next = gamma(xi + 1.0)

    for i, x_i in enumerate(x):
        for j in range(i + 1):
            left = j * h
            right = min((j + 1) * h, x_i)
            if right <= left:
                continue
            matrix[i, j] = ((x_i - left) ** xi - (x_i - right) ** xi) / gamma_next
    return matrix


def spectral_norm(xi: complex, n: int) -> float:
    return float(np.linalg.svd(collocation_matrix(xi, n), compute_uv=False)[0])


def main() -> None:
    n = 320
    orders = [0.8 + 0.9j, 1.0 + 1.5j, 1.7 - 0.6j]

    for xi in orders:
        tau = xi.real
        complex_norm = spectral_norm(xi, n)
        real_norm = spectral_norm(complex(tau, 0.0), n)
        domination = gamma(tau) / abs(gamma(xi)) * real_norm
        ratio = complex_norm / domination
        print(
            f"xi={xi}, discrete_norm={complex_norm:.10f}, "
            f"scaled_real={domination:.10f}, ratio={ratio:.10f}"
        )
        assert complex_norm < domination
        assert ratio < 0.999


if __name__ == "__main__":
    main()
