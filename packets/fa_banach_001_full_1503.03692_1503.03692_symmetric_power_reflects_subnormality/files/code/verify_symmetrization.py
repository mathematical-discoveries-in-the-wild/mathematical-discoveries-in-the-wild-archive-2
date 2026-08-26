#!/usr/bin/env python3
"""Sanity checks for the symmetric-power subnormality packet.

This verifies finite-dimensional algebraic identities and illustrates the
weakly-null approximate-eigenvector limit.  It is not a proof of the theorem.
"""

from __future__ import annotations

import itertools
import math
import numpy as np


RNG = np.random.default_rng(150303692)


def permutations_unique(items: tuple[int, ...]):
    return sorted(set(itertools.permutations(items)))


def sym_one_x(x: np.ndarray, y: np.ndarray, m: int) -> np.ndarray:
    """P_sym(x tensor y^{tensor(m-1)}) in the full tensor realization."""
    out = np.zeros(x.size**m, dtype=np.complex128)
    for slot in range(m):
        factors = [y] * m
        factors[slot] = x
        term = factors[0]
        for factor in factors[1:]:
            term = np.kron(term, factor)
        out += term / m
    return out


def direct_checks(cases: int = 400) -> float:
    worst = 0.0
    for _ in range(cases):
        d = int(RNG.integers(2, 5))
        m = int(RNG.integers(2, 5))
        x = RNG.normal(size=d) + 1j * RNG.normal(size=d)
        y = RNG.normal(size=d) + 1j * RNG.normal(size=d)
        t = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))

        jxy = sym_one_x(x, y, m)
        formula = (
            np.vdot(x, x).real * np.vdot(y, y).real ** (m - 1) / m
            + (m - 1)
            * abs(np.vdot(x, y)) ** 2
            * np.vdot(y, y).real ** (m - 2)
            / m
        )
        err_norm = abs(np.vdot(jxy, jxy).real - formula)

        tm = t
        for _slot in range(m - 1):
            tm = np.kron(tm, t)
        lhs = tm @ jxy
        rhs = sym_one_x(t @ x, t @ y, m)
        err_intertwine = np.linalg.norm(lhs - rhs)
        scale = 1.0 + abs(formula) + np.linalg.norm(lhs)
        worst = max(worst, err_norm / scale, err_intertwine / scale)
    return worst


def shift(v: np.ndarray) -> np.ndarray:
    out = np.zeros_like(v)
    out[1:] = v[:-1]
    return out


def power_shift(v: np.ndarray, k: int) -> np.ndarray:
    for _ in range(k):
        v = shift(v)
    return v


def singular_sequence_check(m: int = 3, max_k: int = 5):
    theta = 0.371
    lam = np.exp(1j * theta)
    dim = 2048
    x = np.zeros(dim, dtype=np.complex128)
    x[:9] = RNG.normal(size=9) + 1j * RNG.normal(size=9)
    x /= np.linalg.norm(x)

    rows = []
    for n in (32, 64, 128, 256, 512, 1024):
        y = np.zeros(dim, dtype=np.complex128)
        y[:n] = lam ** (-np.arange(n)) / math.sqrt(n)
        residual = np.linalg.norm(shift(y) - lam * y)
        moment_error = 0.0
        for k in range(max_k + 1):
            tx = power_shift(x.copy(), k)
            ty = power_shift(y.copy(), k)
            actual = (
                np.vdot(tx, tx).real * np.vdot(ty, ty).real ** (m - 1) / m
                + (m - 1)
                * abs(np.vdot(tx, ty)) ** 2
                * np.vdot(ty, ty).real ** (m - 2)
                / m
            )
            target = abs(lam) ** (2 * k * (m - 1)) * np.vdot(tx, tx).real / m
            moment_error = max(moment_error, abs(actual - target))
        rows.append((n, residual, moment_error))
    return rows


def main() -> None:
    worst = direct_checks()
    assert worst < 2e-12, worst
    rows = singular_sequence_check()
    assert rows[-1][1] < rows[0][1]
    assert rows[-1][2] < rows[0][2]
    print("PASS: 400 exact complex symmetrization/intertwining cases")
    print(f"worst relative algebraic error: {worst:.3e}")
    print("unilateral-shift singular-sequence illustration:")
    for n, residual, moment_error in rows:
        print(f"  N={n:4d} residual={residual:.6e} moment_error={moment_error:.6e}")
    print("PASS: residuals and moment-limit errors decrease")


if __name__ == "__main__":
    main()

