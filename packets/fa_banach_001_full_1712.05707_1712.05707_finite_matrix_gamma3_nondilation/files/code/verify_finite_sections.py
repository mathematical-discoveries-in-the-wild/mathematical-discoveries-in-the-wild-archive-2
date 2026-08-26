#!/usr/bin/env python3
"""Check the explicit finite sections used in the Gamma_3 proof."""

import numpy as np


def family(m: int):
    e_dim = 2
    a_dim = e_dim * m

    # Forward truncated shift on E^m.
    v = np.zeros((a_dim, a_dim), dtype=complex)
    eye_e = np.eye(e_dim, dtype=complex)
    for j in range(m - 1):
        v[(j + 1) * e_dim : (j + 2) * e_dim,
          j * e_dim : (j + 1) * e_dim] = eye_e

    x = np.zeros((a_dim, a_dim), dtype=complex)
    x[:2, :2] = np.array([[0.0, 0.25], [0.0, 0.0]], dtype=complex)

    h_dim = 4 * a_dim
    s1 = np.zeros((h_dim, h_dim), dtype=complex)
    p = np.zeros((h_dim, h_dim), dtype=complex)
    s1[2 * a_dim : 3 * a_dim, 2 * a_dim : 3 * a_dim] = x
    p[2 * a_dim : 3 * a_dim, a_dim : 2 * a_dim] = v
    p[3 * a_dim : 4 * a_dim, 0:a_dim] = np.eye(a_dim)
    s2 = np.zeros_like(s1)
    return s1, s2, p


def compress(big: np.ndarray, small_m: int) -> np.ndarray:
    """Compress blockwise from E^(m+1)^4 to E^m^4."""
    big_a = big.shape[0] // 4
    small_a = 2 * small_m
    indices = []
    for block in range(4):
        indices.extend(range(block * big_a, block * big_a + small_a))
    return big[np.ix_(indices, indices)]


def main() -> None:
    tol = 1e-12
    for m in range(1, 9):
        s1, s2, p = family(m)
        ops = (s1, s2, p)
        assert s1.shape == (8 * m, 8 * m)
        for a in ops:
            for b in ops:
                assert np.linalg.norm(a @ b) < tol
        assert abs(np.linalg.norm(s1, 2) - 0.25) < tol
        assert np.linalg.norm(p, 2) <= 1.0 + tol
        for a in (s1.conj().T, s2.conj().T, p.conj().T):
            for b in (s1.conj().T, s2.conj().T, p.conj().T):
                assert np.linalg.norm(a @ b) < tol

        if m < 8:
            bigger = family(m + 1)
            for small_op, big_op in zip(ops, bigger):
                assert np.linalg.norm(compress(big_op, m) - small_op) < tol
                assert np.linalg.norm(
                    compress(big_op.conj().T, m) - small_op.conj().T
                ) < tol
        print(
            f"m={m:2d} dimension={8*m:2d} "
            f"||S1||={np.linalg.norm(s1, 2):.2f} "
            f"||P||={np.linalg.norm(p, 2):.2f} relations=passed"
        )

    print("All finite-section checks passed.")


if __name__ == "__main__":
    main()
