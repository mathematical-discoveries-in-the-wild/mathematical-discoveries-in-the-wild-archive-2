"""Numerical regression check for the padded-Pauli pencil identity."""

from __future__ import annotations

import numpy as np


def block_diag(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    result = np.zeros(
        (first.shape[0] + second.shape[0], first.shape[1] + second.shape[1]),
        dtype=complex,
    )
    result[: first.shape[0], : first.shape[1]] = first
    result[first.shape[0] :, first.shape[1] :] = second
    return result


def main() -> None:
    pauli = (
        np.array([[1, 0], [0, -1]], dtype=complex),
        np.array([[0, 1], [1, 0]], dtype=complex),
        np.array([[0, 1j], [-1j, 0]], dtype=complex),
    )
    rng = np.random.default_rng(250720325)
    checked = 0

    for d in (3, 4, 5):
        assert 3 < d * d - d + 2
        padded = tuple(block_diag(p, np.zeros((d - 2, d - 2))) for p in pauli)
        for n in (1, 2, 3):
            for _ in range(10):
                xs = []
                for _ in range(3):
                    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
                    xs.append((raw + raw.conj().T) / 2)

                lp = np.eye(2 * n, dtype=complex)
                la = np.eye(d * n, dtype=complex)
                for p, a, x in zip(pauli, padded, xs):
                    lp -= np.kron(p, x)
                    la -= np.kron(a, x)

                expected = block_diag(lp, np.eye((d - 2) * n, dtype=complex))
                np.testing.assert_allclose(la, expected, atol=1e-12, rtol=1e-12)
                checked += 1

    print(f"verified {checked} seeded block identities")


if __name__ == "__main__":
    main()
