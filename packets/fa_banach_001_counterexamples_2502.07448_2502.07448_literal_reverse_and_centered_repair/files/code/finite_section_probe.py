"""Finite-section probe for the naturally centered reverse inequality.

For nu(dx)=dx/(2 cosh(pi x/2)), the orthonormal Meixner--Pollaczek
polynomials satisfy x P_n=(n+1)P_{n+1}+nP_{n-1} and
P_n'=sum_{r<=n, r odd} (-1)^((r-1)/2) P_{n-r}/r.
"""

import argparse

import numpy as np
from scipy.linalg import eigh


def matrices(n: int, pad: int):
    size = n + pad + 1
    jacobi = np.zeros((size, size))
    for k in range(size - 1):
        jacobi[k, k + 1] = jacobi[k + 1, k] = k + 1

    nodes, vectors = eigh(jacobi)
    values = np.log(np.e + np.abs(nodes)) ** 2
    multiplication = (vectors * values) @ vectors.T
    multiplication = multiplication[1 : n + 1, 1 : n + 1]

    derivative = np.zeros((n + 1, n + 1))
    for column in range(1, n + 1):
        for r in range(1, column + 1, 2):
            derivative[column - r, column] = (-1) ** ((r - 1) // 2) / r
    derivative_gram = (derivative.T @ derivative)[1:, 1:]

    weights = np.log(np.e + np.arange(1, n + 1)) ** 2
    weight_matrix = np.diag(weights)
    return multiplication, derivative_gram, weight_matrix


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sizes", nargs="+", type=int, default=[32, 64, 128, 256])
    parser.add_argument("--pad", type=int, default=384)
    args = parser.parse_args()

    for n in args.sizes:
        multiplication, derivative, weight = matrices(n, args.pad)
        spectrum = eigh(multiplication + derivative, weight, eigvals_only=True)
        print(
            f"n={n:4d} min={spectrum[0]:.6f} "
            f"median={np.median(spectrum):.6f} max={spectrum[-1]:.6f}"
        )


if __name__ == "__main__":
    main()
