#!/usr/bin/env python3
"""Numerically verify the signed-Krawtchouk PPT spectrum.

This is a finite-dimensional audit only; the packet contains the proof.
"""

from functools import reduce
from math import atan, comb, cos, sin

import numpy as np


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)


def tensor(factors):
    return reduce(np.kron, factors)


def krawtchouk(n, r, c):
    lower = max(0, r - (n - c))
    upper = min(r, c)
    return sum((-1) ** j * comb(c, j) * comb(n - c, r - j)
               for j in range(lower, upper + 1))


def clifford_basis(n):
    k = n // 2
    generators = []
    for j in range(k):
        generators.append(tensor([Z] * j + [X] + [I2] * (k - j - 1)))
        generators.append(tensor([Z] * j + [Y] + [I2] * (k - j - 1)))

    basis = []
    for mask in range(1 << n):
        indices = [i for i in range(n) if (mask >> i) & 1]
        q = len(indices) * (len(indices) - 1) // 2
        value = (1j ** q) * np.eye(1 << k, dtype=complex)
        for i in indices:
            value = value @ generators[i]
        basis.append(value)
    return basis


def predicted_spectrum(n, phi):
    values = []
    for c in range(n + 1):
        mu = sum(
            phi[r] * (-1) ** (r * (r - 1) // 2 + r * c)
            * krawtchouk(n, r, c)
            for r in range(n + 1)
        ) / (1 << n)
        values.extend([mu] * comb(n, c))
    return np.sort(np.asarray(values))


def explicit_spectrum(n, phi):
    basis = clifford_basis(n)
    size = 1 << (n // 2)
    rho = sum(
        phi[mask.bit_count()] * np.kron(u.T, u)
        for mask, u in enumerate(basis)
    ) / (size * size)
    partial_transpose = (
        rho.reshape(size, size, size, size)
        .transpose(2, 1, 0, 3)
        .reshape(size * size, size * size)
    )
    return np.sort(np.linalg.eigvalsh(partial_transpose))


def ou_closed_form(n, t):
    theta = atan(t)
    scale = (1 + t * t) ** (n / 2) / (1 << n)
    return np.asarray([
        scale * (cos((n - 2 * c) * theta)
                 + (-1) ** c * sin((n - 2 * c) * theta))
        for c in range(n + 1)
    ])


def main():
    for n in (2, 4, 6):
        phi = np.asarray([1.0] + [0.07 * (-1) ** r + 0.013 * r
                                 for r in range(1, n + 1)])
        matrix_error = np.max(np.abs(
            explicit_spectrum(n, phi) - predicted_spectrum(n, phi)
        ))

        t = 0.11
        ou_phi = np.asarray([t ** r for r in range(n + 1)])
        transform_values = []
        for c in range(n + 1):
            transform_values.append(sum(
                ou_phi[r] * (-1) ** (r * (r - 1) // 2 + r * c)
                * krawtchouk(n, r, c)
                for r in range(n + 1)
            ) / (1 << n))
        closed_error = np.max(np.abs(
            np.asarray(transform_values) - ou_closed_form(n, t)
        ))

        print(f"n={n}: matrix_error={matrix_error:.3e}, "
              f"ou_closed_error={closed_error:.3e}")
        assert matrix_error < 1e-12
        assert closed_error < 1e-12


if __name__ == "__main__":
    main()

