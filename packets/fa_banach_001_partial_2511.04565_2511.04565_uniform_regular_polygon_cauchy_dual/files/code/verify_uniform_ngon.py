#!/usr/bin/env python3
"""Verify the closed formulas for the uniform regular-N-gon theorem."""

from __future__ import annotations

import argparse
import numpy as np


def rho_from_c(n: int, c: float) -> float:
    h = 2.0 + c*n*n
    return (h + np.sqrt(h*h - 4.0))/2.0


def formula_coefficients(n: int, rho: float) -> np.ndarray:
    d = np.array([n + k*(rho-1.0) for k in range(n+1)])
    return n*rho*(rho-1.0)**2/(d[:-1]*d[1:])


def direct_finite_kernel_coefficients(n: int, c: float, rho: float) -> np.ndarray:
    omega = np.exp(2j*np.pi/n)
    zetas = omega**np.arange(n)
    dmat = np.empty((n, n), dtype=complex)
    diagonal = c*((n-1)/2 + n/(rho-1))
    for i in range(n):
        for j in range(n):
            if i == j:
                dmat[i, j] = diagonal
            else:
                ratio = zetas[i]/zetas[j]
                dmat[i, j] = c*ratio/(1-ratio)
    # f_j numerator coefficients in degrees 0,...,n-1.
    fnum = np.array([
        [(1-rho)/n * zetas[j]**(-m) for m in range(n)]
        for j in range(n)
    ], dtype=complex)
    binv_bar = np.conjugate(np.linalg.inv(dmat))
    kfinite_num = fnum.T @ binv_bar @ np.conjugate(fnum)
    # q q* - rho s s* = (rho-1)(rho-t^n).  Subtract
    # (1-t) times the diagonal finite-kernel numerator.
    result = np.zeros((n+1, n+1), dtype=complex)
    result[0, 0] = rho*(rho-1)
    result[n, n] = -(rho-1)
    result[:n, :n] -= kfinite_num
    result[1:n+1, 1:n+1] += kfinite_num
    off_diagonal = result - np.diag(np.diag(result))
    assert np.max(abs(off_diagonal)) < 2e-7, np.max(abs(off_diagonal))
    return np.real_if_close(np.diag(result)[1:])


def verify(n: int, c: float) -> None:
    rho = rho_from_c(n, c)
    closed = formula_coefficients(n, rho)
    direct = direct_finite_kernel_coefficients(n, c, rho)
    assert np.max(abs(closed-direct)) < 2e-7
    assert np.all(closed > 0)
    assert abs(np.sum(closed)-(rho-1)**2) < 2e-7
    a = rho**(1/n)
    omega = np.exp(2j*np.pi/n)
    forbidden = np.array([
        np.sum(closed*(a*a*omega**d)**np.arange(1, n+1))
        for d in range(1, n)
    ])
    if n >= 3:
        assert np.max(abs(forbidden)) > 1e-8
    if n == 2:
        assert abs(forbidden[0]) < 1e-8
    if n >= 3:
        actual_ratio = closed[1]/closed[0]
        prescribed_root_ratio = a**-2
        assert actual_ratio < prescribed_root_ratio
    print(f"PASS n={n} c={c:.8g} rho={rho:.12g}")
    print("  max coefficient error", float(np.max(abs(closed-direct))))
    print("  min A_k", float(np.min(closed)))
    print("  forbidden magnitudes", abs(forbidden))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--c", type=float, default=1.0)
    parser.add_argument("--suite", action="store_true")
    args = parser.parse_args()
    if args.suite:
        for n in (2, 3, 4, 5, 8):
            for c in (0.03, 0.37, 1.0, 9.0):
                verify(n, c)
        print("VERDICT: PASS (20 independent reconstruction cases)")
    else:
        verify(args.n, args.c)
