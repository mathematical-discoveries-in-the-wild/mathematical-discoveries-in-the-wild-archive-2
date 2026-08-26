"""Numerical checks for the covariance-whitening Polchinski conjugacy.

The proof is algebraic; this script only catches transposes, signs, and
composition-order mistakes on a noncommuting SPD example.
"""

from __future__ import annotations

import numpy as np


def sym_sqrt(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(a)
    return (vecs * np.sqrt(vals)) @ vecs.T


def sym_inv_sqrt(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(a)
    return (vecs * (1.0 / np.sqrt(vals))) @ vecs.T


rng = np.random.default_rng(220808186)
b = rng.normal(size=(4, 4))
c = b @ b.T + 2.0 * np.eye(4)
c_half = sym_sqrt(c)
c_inv_half = sym_inv_sqrt(c)

u, _ = np.linalg.qr(rng.normal(size=(4, 4)))
rates = np.array([0.35, 0.8, 1.4, 2.2])


def pieces(t: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    # The normalized residual path is monotone, but generally does not
    # commute with C in the ambient coordinates.
    residual_normalized = u @ np.diag(np.exp(-rates * t)) @ u.T
    sigma = c_half @ residual_normalized @ c_half
    c_t = c - sigma
    m_t = sym_sqrt(sigma) @ c_inv_half
    return sigma, c_t, m_t


r, s, t = 0.17, 0.73, 1.61
sigma_r, c_r, m_r = pieces(r)
sigma_s, c_s, m_s = pieces(s)
sigma_t, c_t, m_t = pieces(t)

for sigma, m in ((sigma_r, m_r), (sigma_s, m_s), (sigma_t, m_t)):
    np.testing.assert_allclose(m @ c @ m.T, sigma, rtol=2e-11, atol=2e-11)


def transition(m_left: np.ndarray, m_right: np.ndarray,
               c_left: np.ndarray, c_right: np.ndarray):
    k = np.linalg.solve(m_left, m_right)
    n = np.linalg.solve(m_left, c_right - c_left)
    n = np.linalg.solve(m_left, n.T).T
    return k, n


k_rs, n_rs = transition(m_r, m_s, c_r, c_s)
k_st, n_st = transition(m_s, m_t, c_s, c_t)
k_rt, n_rt = transition(m_r, m_t, c_r, c_t)

np.testing.assert_allclose(n_rs, c - k_rs @ c @ k_rs.T,
                           rtol=3e-11, atol=3e-11)
np.testing.assert_allclose(n_st, c - k_st @ c @ k_st.T,
                           rtol=3e-11, atol=3e-11)
np.testing.assert_allclose(k_rs @ k_st, k_rt, rtol=3e-11, atol=3e-11)
np.testing.assert_allclose(n_rs + k_rs @ n_st @ k_rs.T, n_rt,
                           rtol=3e-11, atol=3e-11)

# Infinitesimal fluctuation-dissipation identity at a generic time.
t0 = 0.91
h = 1e-6
_, c0, m0 = pieces(t0)
_, c1, m1 = pieces(t0 + h)
m_dot = (m1 - m0) / h
c_dot = (c1 - c0) / h
g = np.linalg.solve(m0, m_dot)
d_twice = np.linalg.solve(m0, c_dot)
d_twice = np.linalg.solve(m0, d_twice.T).T
d = 0.5 * d_twice
h_rot = g + d @ np.linalg.inv(c)

np.testing.assert_allclose(g @ c + c @ g.T, -2.0 * d,
                           rtol=2e-5, atol=2e-5)
np.testing.assert_allclose(h_rot @ c + c @ h_rot.T, 0.0,
                           rtol=2e-5, atol=2e-5)

print("all covariance, semigroup, and generator identities passed")
