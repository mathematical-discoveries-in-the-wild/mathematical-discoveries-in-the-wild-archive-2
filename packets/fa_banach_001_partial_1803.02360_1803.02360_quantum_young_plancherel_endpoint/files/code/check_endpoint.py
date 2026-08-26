#!/usr/bin/env python3
"""Finite-sector sanity checks for the (2,2,infinity) endpoint theorem.

The proof uses Weyl Plancherel and is analytic.  This script checks the exact
beam-splitter isometry on a finite input Fock sector, tests the sharp inequality
on deterministic random matrices, and checks convergence of thermal ratios to
the claimed beam-splitter and squeezer constants.
"""

from __future__ import annotations

import math
import numpy as np


def beamsplitter_isometry(d: int, lam: float) -> np.ndarray:
    out = 2 * d - 1
    U = np.zeros((out, out, d, d), dtype=np.complex128)
    rl, ro = math.sqrt(lam), math.sqrt(1.0 - lam)
    fact = [math.factorial(k) for k in range(out)]
    for m in range(d):
        for n in range(d):
            total = m + n
            for s in range(total + 1):
                amp = 0.0
                for i in range(max(0, s - n), min(m, s) + 1):
                    j = s - i
                    amp += (math.comb(m, i) * math.comb(n, j)
                            * rl**i * (-ro)**(m-i) * ro**j * rl**(n-j))
                amp *= math.sqrt(fact[s] * fact[total-s] / (fact[m] * fact[n]))
                U[s, total-s, m, n] = amp
    gram = np.einsum("semn,seij->mnij", U.conj(), U)
    assert np.max(np.abs(gram - np.eye(d*d).reshape(d, d, d, d))) < 2e-12
    return U


def mix(U: np.ndarray, X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    return np.einsum("semn,mi,nj,teij->st", U, X, Y, U.conj(), optimize=True)


def hs(X: np.ndarray) -> float:
    return float(np.linalg.norm(X, "fro"))


def op(X: np.ndarray) -> float:
    return float(np.linalg.svd(X, compute_uv=False)[0])


def thermal_ratio(lam: float, ea: float, eb: float, n: int = 1) -> float:
    if 0.0 < lam < 1.0:
        eout = lam * ea + (1.0 - lam) * eb
    elif lam > 1.0:
        eout = lam * ea + (lam - 1.0) * (eb + 1.0)
    else:
        raise ValueError("nondegenerate parameter required")
    return (((2.0 * ea + 1.0) * (2.0 * eb + 1.0)) ** (n / 2.0)
            / (eout + 1.0) ** n)


def main() -> None:
    rng = np.random.default_rng(180302360)
    draws = 300
    d = 4
    for lam in (0.2, 0.5, 0.8):
        U = beamsplitter_isometry(d, lam)
        sharp = 1.0 / math.sqrt(lam * (1.0 - lam))
        worst_fraction = 0.0
        for _ in range(draws):
            X = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
            Y = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
            fraction = op(mix(U, X, Y)) / (sharp * hs(X) * hs(Y))
            worst_fraction = max(worst_fraction, fraction)
            assert fraction <= 1.0 + 2e-12
        a, b = lam, 1.0 - lam
        ratios = [thermal_ratio(lam, b*t, a*t) for t in (1e2, 1e4, 1e6)]
        assert abs(ratios[-1] / sharp - 1.0) < 2e-6
        print(f"beam lam={lam}: max tested fraction={worst_fraction:.9f}; "
              f"thermal/sharp={ratios[-1]/sharp:.9f}")

    for lam in (1.2, 2.0, 5.0):
        a, b = lam, lam - 1.0
        sharp = 1.0 / math.sqrt(a * b)
        ratios = [thermal_ratio(lam, b*t, a*t) for t in (1e2, 1e4, 1e6)]
        assert abs(ratios[-1] / sharp - 1.0) < 3e-6
        print(f"squeezer lam={lam}: thermal/sharp={ratios[-1]/sharp:.9f}")

    print("PASS: Plancherel-endpoint sanity checks completed")


if __name__ == "__main__":
    main()
