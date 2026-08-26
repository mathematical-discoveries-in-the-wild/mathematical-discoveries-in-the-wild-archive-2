"""Exact and numerical checks for the residue-class factorization theorem."""

import math

import numpy as np
import sympy as sp


t = sp.symbols("t")
rt2 = sp.sqrt(2)
a = -1 / rt2


def U(k):
    if k == -1:
        return sp.Integer(0)
    return sp.chebyshevu(k, t)


def T(k):
    return sp.chebyshevt(k, t)


def q(n):
    c = sp.simplify(U(n - 1).subs(t, a))
    return sp.cancel(U(n) - (U(n - 1) - c) / (2 * (t - a)))


def numerator_factor(n):
    c = sp.simplify(U(n - 1).subs(t, a))
    if c == 0:
        return U(n + 1) + rt2 * U(n)
    if n % 2:
        m = (n + 1) // 2
        if c == 1:
            return 2 * T(m) * (U(m) + rt2 * U(m - 1))
        if c == -1:
            return 2 * U(m - 1) * (T(m + 1) + rt2 * T(m))
    else:
        m = n // 2
        if c == -rt2:
            return 2 * T(m + 1) * (U(m) + rt2 * U(m - 1))
        if c == rt2:
            return 2 * U(m) * (T(m + 1) + rt2 * T(m))
    raise AssertionError((n, c))


for n in range(81):
    lhs = sp.expand(2 * (t - a) * q(n))
    rhs = sp.expand(numerator_factor(n))
    assert sp.simplify(lhs - rhs) == 0, n
    assert sp.rem(sp.Poly(rhs, t, extension=rt2),
                  sp.Poly(t - a, t, extension=rt2)) == 0, n


def eig_u_combo(k):
    """Zeros of U_k+sqrt(2)U_(k-1) via a symmetric Jacobi matrix."""
    if k == 0:
        return np.empty(0)
    mat = np.diag(np.r_[np.zeros(k - 1), -1 / math.sqrt(2)])
    if k > 1:
        off = np.full(k - 1, 0.5)
        mat += np.diag(off, 1) + np.diag(off, -1)
    return np.linalg.eigvalsh(mat)


def eig_t_combo(k):
    """Zeros of T_k+sqrt(2)T_(k-1) via a symmetric Jacobi matrix."""
    if k == 0:
        return np.empty(0)
    if k == 1:
        return np.array([-math.sqrt(2)])
    mat = np.diag(np.r_[np.zeros(k - 1), -1 / math.sqrt(2)])
    if k > 1:
        off = np.full(k - 1, 0.5)
        off[0] = 1 / math.sqrt(2)
        mat += np.diag(off, 1) + np.diag(off, -1)
    return np.linalg.eigvalsh(mat)


for k in range(1, 201):
    ru = eig_u_combo(k)
    rs = eig_t_combo(k)
    assert len(ru) == k and len(rs) == k
    assert np.max(np.abs(np.imag(ru))) == 0
    assert np.max(np.abs(np.imag(rs))) == 0
    assert np.sum(ru < -1) == (1 if k >= 3 else 0)
    assert np.sum(ru > 1) == 0
    assert np.sum(rs < -1) == 1
    assert np.sum(rs > 1) == 0
    assert np.min(np.diff(ru)) > 0 if k > 1 else True
    assert np.min(np.diff(rs)) > 0 if k > 1 else True

print("PASS: 81 exact factorizations and real-root/location checks through degree 200")
