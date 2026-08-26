#!/usr/bin/env python3
"""Sanity checks for the John-ellipsoid basis bounds.

The checks illustrate finite-dimensional algebra used in the packet.  They do
not replace the John theorem or the proof.
"""

from itertools import product

import numpy as np


RNG = np.random.default_rng(230303210)


def qnorm(x: np.ndarray, lam: np.ndarray) -> float:
    return float(np.linalg.norm(lam * x))


def check_ellipsoids() -> int:
    checks = 0
    for complex_field in (False, True):
        for n in range(1, 9):
            lam = np.exp(RNG.uniform(-3.0, 3.0, size=n))
            # The diagonalizing basis has exact constant sqrt(n), witnessed
            # by coefficients 1/lam_i.
            a = 1.0 / lam
            ratio = np.sum(np.abs(a) * lam) / qnorm(a, lam)
            assert abs(ratio - np.sqrt(n)) < 1e-12
            checks += 1

            # Any f-unit basis has a sign choice whose f-norm is <= sqrt(n).
            raw = RNG.normal(size=(n, n))
            if complex_field:
                raw = raw + 1j * RNG.normal(size=(n, n))
            cols = raw / np.linalg.norm(lam[:, None] * raw, axis=0)
            values = []
            for signs in product((-1.0, 1.0), repeat=n):
                values.append(qnorm(cols @ np.asarray(signs), lam))
            assert min(values) <= np.sqrt(n) + 1e-10
            checks += 1
    return checks


def check_john_sandwich_models() -> int:
    checks = 0
    for complex_field in (False, True):
        for n in range(2, 9):
            lam = np.exp(RNG.uniform(-2.0, 2.0, size=n))
            supports = RNG.normal(size=(4 * n, n))
            if complex_field:
                supports = supports + 1j * RNG.normal(size=(4 * n, n))
            supports /= np.linalg.norm(supports / lam, axis=1)[:, None]

            def f(x: np.ndarray) -> float:
                # q/sqrt(n) <= f <= q, hence its unit ball obeys the same
                # sandwich used in the proof.
                pairings = np.abs(supports.conj() @ x)
                return max(qnorm(x, lam) / np.sqrt(n), float(pairings.max()))

            basis_values = np.asarray([f(np.eye(n, dtype=complex)[i]) for i in range(n)])
            assert np.all(basis_values <= lam + 1e-10)
            for _ in range(2000):
                a = RNG.normal(size=n)
                if complex_field:
                    a = a + 1j * RNG.normal(size=n)
                lhs = np.sum(np.abs(a) * basis_values)
                rhs = n * f(a)
                assert lhs <= rhs + 1e-9
                checks += 1
    return checks


def main() -> None:
    checks = check_ellipsoids() + check_john_sandwich_models()
    print(f"PASS: {checks} ellipsoidal/sign/sandwich checks")


if __name__ == "__main__":
    main()
