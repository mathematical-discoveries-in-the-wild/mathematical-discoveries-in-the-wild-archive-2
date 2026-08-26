#!/usr/bin/env python3
"""Sanity checks for the subquadratic p-elastic principal matrix."""

import numpy as np


def principal_matrix(p: float, k: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(k)
    e = k / norm
    return norm ** (p - 2.0) * (np.eye(k.size) + (p - 2.0) * np.outer(e, e))


def main() -> None:
    k = np.array([1.5, -0.75, 2.0])
    norm = np.linalg.norm(k)
    for p in (1.01, 1.2, 1.5, 1.9, 2.0, 3.0):
        eig = np.linalg.eigvalsh(principal_matrix(p, k))
        expected = np.sort(
            np.array([norm ** (p - 2.0), norm ** (p - 2.0),
                      (p - 1.0) * norm ** (p - 2.0)])
        )
        if not np.allclose(eig, expected, rtol=1e-12, atol=1e-12):
            raise AssertionError((p, eig, expected))
        if p > 1.0 and eig[0] <= 0.0:
            raise AssertionError((p, eig))
        conjugate = p / (p - 1.0)
        print(f"p={p:4.2f}  p'={conjugate:8.4f}  eigenvalues={eig}")

    print("principal-symbol eigenvalue formula verified")
    print("for 1<p<2 one has p'>2, so the source's L^{p'} <= L^2 step reverses")


if __name__ == "__main__":
    main()
