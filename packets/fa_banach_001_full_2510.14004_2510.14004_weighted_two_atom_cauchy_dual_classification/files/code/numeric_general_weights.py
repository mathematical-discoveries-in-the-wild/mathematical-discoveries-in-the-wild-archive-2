#!/usr/bin/env python3
"""Numerical reconnaissance for the weighted two-atom CDSP.

For mu=c1 delta_1+c2 delta_xi, construct the outer Fejer--Riesz
factor q, the coefficient Gram matrix A of the de Branges--Rovnyak
row polynomial, and the l=1 finite positivity obstruction from
Theorem 2.1 of Chavan--Ghara--Reza (as quoted in arXiv:2510.14004).
"""

from __future__ import annotations

import argparse
import cmath
import itertools

import numpy as np


def polymul2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product coefficient array for a(z)b(v)."""
    return np.outer(a, b)


def shift_zv(a: np.ndarray) -> np.ndarray:
    out = np.zeros((a.shape[0] + 1, a.shape[1] + 1), dtype=complex)
    out[1:, 1:] = a
    return out


def pad(a: np.ndarray, shape: tuple[int, int]) -> np.ndarray:
    out = np.zeros(shape, dtype=complex)
    out[: a.shape[0], : a.shape[1]] = a
    return out


def rational_derivative(num: np.ndarray, den: np.ndarray, z: complex) -> complex:
    # Coefficients are ascending.
    n = sum(num[k] * z**k for k in range(len(num)))
    d = sum(den[k] * z**k for k in range(len(den)))
    np_ = sum(k * num[k] * z ** (k - 1) for k in range(1, len(num)))
    dp = sum(k * den[k] * z ** (k - 1) for k in range(1, len(den)))
    return (np_ * d - n * dp) / d**2


def criterion_minor(roots: np.ndarray, gram: np.ndarray, ell: int) -> float:
    """Leading 2-by-2 minor in the simple-pole criterion at order ell."""
    a1, a2 = roots

    def kernel(r: complex, t: complex) -> complex:
        xr = np.array([r, r**2])
        xt = np.array([t, t**2])
        return xr @ gram @ np.conjugate(xt)

    alphas = [a1, a2]
    avec = [a1 - a2, a2 - a1]
    weights = np.empty((2, 2), dtype=complex)
    for r, t in itertools.product(range(2), repeat=2):
        weights[r, t] = (
            kernel(alphas[r], alphas[t])
            / (avec[r] * np.conjugate(avec[t]))
            * (1 - 1 / (alphas[r] * np.conjugate(alphas[t]))) ** ell
        )
    minor = np.empty((2, 2), dtype=complex)
    for m, n in itertools.product(range(2), repeat=2):
        minor[m, n] = sum(
            weights[r, t]
            / (alphas[r] ** (m + 2) * np.conjugate(alphas[t]) ** (n + 2))
            for r, t in itertools.product(range(2), repeat=2)
        )
    return float(np.linalg.det(minor).real)


def data(c1: float, c2: float, theta: float):
    xi = cmath.exp(1j * theta)
    # Ascending coefficients of the self-inversive quartic.
    f = np.array(
        [
            xi**2,
            -((c1 + 2) * xi**2 + (c2 + 2) * xi),
            xi**2 + 2 * (c1 + c2 + 2) * xi + 1,
            -((c1 + 2) + (c2 + 2) * xi),
            1,
        ],
        dtype=complex,
    )
    roots = np.roots(f[::-1])
    outer = np.array(sorted((r for r in roots if abs(r) > 1 + 1e-8), key=abs))
    if len(outer) != 2:
        raise RuntimeError((c1, c2, theta, roots))
    a1, a2 = outer
    q_desc = np.poly(outer)
    q = q_desc[::-1]  # ascending: p,-s,1
    b = abs(q[0])
    qbar = np.conjugate(q)

    # Numerators n_j=q f_j, ascending.
    q_at_1 = sum(q)
    q_at_xi = sum(q[k] * xi**k for k in range(3))
    n1 = q_at_1 / (1 - xi) * np.array([-xi, 1], dtype=complex)
    n2 = q_at_xi / (xi - 1) * np.array([-1, 1], dtype=complex)

    o1 = np.sqrt(b) * (1 - xi) / q_at_1
    o2 = np.sqrt(b) * (xi - 1) / q_at_xi
    c11 = c1 * rational_derivative(n1, q, 1)
    c22 = c2 * xi * rational_derivative(n2, q, xi)
    c12 = 1 / (o1 * np.conjugate(o2) * (1 - np.conjugate(xi)))
    C = np.array([[c11, c12], [np.conjugate(c12), c22]], dtype=complex)
    C = (C + C.conjugate().T) / 2
    Cinv = np.linalg.inv(C)

    p0 = np.sqrt(b) * np.array([xi, -(1 + xi), 1], dtype=complex)
    base = polymul2(q, qbar) - polymul2(p0, np.conjugate(p0))
    ns = [n1, n2]
    finite = np.zeros((2, 2), dtype=complex)
    for i, j in itertools.product(range(2), repeat=2):
        finite += Cinv[i, j] * polymul2(ns[j], np.conjugate(ns[i]))
    finite_padded = pad(finite, (3, 3))
    one_minus_zv = finite_padded - pad(shift_zv(finite), (3, 3))
    H = base - one_minus_zv
    # H should have only indices 1,2 in both variables.
    edge = max(
        np.max(np.abs(H[0, :])),
        np.max(np.abs(H[:, 0])),
    )
    A = H[1:3, 1:3]
    A = (A + A.conjugate().T) / 2

    def S(r: complex, t: complex) -> complex:
        xr = np.array([r, r**2])
        xt = np.array([t, t**2])
        # If A=(A_ij) is defined by
        #   sum_ij A_ij z^i conjugate(w)^j,
        # then A=P^*P and this is exactly
        # sum_j p_j(r) conjugate(p_j(t)).
        return xr @ A @ np.conjugate(xt)

    alphas = [a1, a2]
    avec = [a1 - a2, a2 - a1]
    detM = criterion_minor(outer, A, 1)
    cross = a1 * np.conjugate(a2)
    return {
        "xi": xi,
        "roots": outer,
        "q": q,
        "b": b,
        "C": C,
        "A": A,
        "edge": edge,
        "S12": S(a1, a2),
        "cross": cross,
        "detM": detM,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    args = parser.parse_args()
    if not args.scan:
        for pars in [(1, 1, np.pi / 2), (0.2, 3, 1.0), (10, 0.1, 2.4)]:
            d = data(*pars)
            print("pars", pars)
            for key in ("roots", "q", "b", "C", "A", "edge", "S12", "cross", "detM"):
                print(key, d[key])
            print("simple-pole minors ell=1,10,100", [
                criterion_minor(d["roots"], d["A"], ell) for ell in (1, 10, 100)
            ])
        return

    worst = None
    near_s12 = None
    signs = {"neg": 0, "pos": 0, "zero": 0}
    for c1 in np.geomspace(0.02, 50, 19):
        for c2 in np.geomspace(0.02, 50, 19):
            for theta in np.linspace(0.03, np.pi - 0.03, 81):
                d = data(float(c1), float(c2), float(theta))
                value = d["detM"]
                signs["neg" if value < -1e-9 else "pos" if value > 1e-9 else "zero"] += 1
                record = (value, c1, c2, theta, d["S12"], d["cross"], d["roots"])
                if worst is None or value > worst[0]:
                    worst = record
                sval = abs(d["S12"])
                if near_s12 is None or sval < near_s12[0]:
                    near_s12 = (sval,) + record[1:]
    print("signs", signs)
    print("largest detM", worst)
    print("smallest abs(S12)", near_s12)


if __name__ == "__main__":
    main()
