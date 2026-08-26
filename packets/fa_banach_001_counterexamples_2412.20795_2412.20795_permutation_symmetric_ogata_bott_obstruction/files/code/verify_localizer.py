#!/usr/bin/env python3
"""Numerically verify the exact spin-localizer identities used in the packet."""

from __future__ import annotations

import numpy as np


def spin_matrices(n_sites: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return the spin-j generators for j=n_sites/2 in the J_z basis."""
    j = n_sites / 2
    m = np.arange(-j, j + 1, dtype=float)
    jp = np.zeros((n_sites + 1, n_sites + 1), dtype=complex)
    for k, mk in enumerate(m[:-1]):
        jp[k + 1, k] = np.sqrt((j - mk) * (j + mk + 1))
    jm = jp.conj().T
    jx = (jp + jm) / 2
    jy = (jp - jm) / (2j)
    jz = np.diag(m)
    return jx, jy, jz


def check(n_sites: int) -> dict[str, float | int]:
    tau = (
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, -1j], [1j, 0]], dtype=complex),
        np.array([[1, 0], [0, -1]], dtype=complex),
    )
    generators = spin_matrices(n_sites)
    x = tuple(a / n_sites for a in generators)
    localizer = sum(np.kron(a, t) for a, t in zip(x, tau))
    eigenvalues = np.linalg.eigvalsh(localizer)
    positive = int(np.count_nonzero(eigenvalues > 1e-10))
    negative = int(np.count_nonzero(eigenvalues < -1e-10))
    expected = np.array(
        [-0.5 - 1 / n_sites] * n_sites + [0.5] * (n_sites + 2)
    )
    casimir = sum(a @ a for a in x)
    casimir_target = (0.25 + 0.5 / n_sites) * np.eye(n_sites + 1)
    commutator_error = max(
        np.linalg.norm(x[0] @ x[1] - x[1] @ x[0] - 1j * x[2] / n_sites, 2),
        np.linalg.norm(x[1] @ x[2] - x[2] @ x[1] - 1j * x[0] / n_sites, 2),
        np.linalg.norm(x[2] @ x[0] - x[0] @ x[2] - 1j * x[1] / n_sites, 2),
    )
    return {
        "N": n_sites,
        "dimension": n_sites + 1,
        "positive": positive,
        "negative": negative,
        "spectral_error": float(np.max(np.abs(eigenvalues - expected))),
        "casimir_error": float(np.linalg.norm(casimir - casimir_target, 2)),
        "commutator_error": float(commutator_error),
        "minimum_absolute_eigenvalue": float(np.min(np.abs(eigenvalues))),
    }


def main() -> None:
    for n_sites in range(1, 25):
        result = check(n_sites)
        assert result["positive"] == n_sites + 2
        assert result["negative"] == n_sites
        assert result["spectral_error"] < 1e-12
        assert result["casimir_error"] < 1e-12
        assert result["commutator_error"] < 1e-12
        assert abs(result["minimum_absolute_eigenvalue"] - 0.5) < 1e-12
        print(result)


if __name__ == "__main__":
    main()
