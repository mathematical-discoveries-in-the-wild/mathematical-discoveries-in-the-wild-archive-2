#!/usr/bin/env python3
"""Finite-dimensional algebra checks for the parity counterexample model."""

from __future__ import annotations

import numpy as np


def main() -> None:
    for size in (3, 8, 25):
        indices = np.array(list(range(-size, 0)) + list(range(1, size + 1)), dtype=float)
        t_op = np.diag(indices)
        abs_t = np.diag(np.abs(indices))
        sign = np.diag(np.sign(indices))

        odd_vectors = []
        even_vectors = []
        for n in range(1, size + 1):
            odd = np.zeros(2 * size)
            even = np.zeros(2 * size)
            minus = size - n
            plus = size + n - 1
            odd[plus], odd[minus] = 1.0 / np.sqrt(2), -1.0 / np.sqrt(2)
            even[plus], even[minus] = 1.0 / np.sqrt(2), 1.0 / np.sqrt(2)
            odd_vectors.append(odd)
            even_vectors.append(even)

        odd_basis = np.column_stack(odd_vectors)
        even_basis = np.column_stack(even_vectors)
        assert np.allclose(np.ones(2 * size) @ odd_basis, 0.0)
        assert np.allclose(even_basis.T @ (t_op @ odd_basis), np.diag(np.arange(1, size + 1)))
        assert np.allclose(odd_basis.T @ (t_op @ even_basis), np.diag(np.arange(1, size + 1)))
        assert np.allclose(odd_basis.T @ (t_op @ odd_basis), 0.0)
        assert np.allclose(even_basis.T @ (t_op @ even_basis), 0.0)
        assert np.allclose(abs_t @ odd_basis, odd_basis @ np.diag(np.arange(1, size + 1)))

        # On the odd sector, V=J and therefore W=JV=I.
        v_on_odd = sign @ odd_basis
        w_on_odd = sign @ v_on_odd
        assert np.allclose(t_op @ odd_basis, v_on_odd @ np.diag(np.arange(1, size + 1)))
        assert np.allclose(w_on_odd, odd_basis)

    partial_herglotz = [2.0 * sum(1.0 / (1.0 + n * n) for n in range(1, N + 1)) for N in (10, 100, 1000)]
    assert partial_herglotz[0] < partial_herglotz[1] < partial_herglotz[2] < np.pi
    print("PASS: parity splitting, polar identity, and Herglotz summability")


if __name__ == "__main__":
    main()
