"""Independent algebraic and finite-dimensional checks for the packet."""

from __future__ import annotations

import math

import numpy as np


def boolean_meet(p: float, q: float) -> float:
    if p == 0.0 or q == 0.0:
        return 0.0
    return p * q / (p + q - p * q)


def chi(p: float) -> float:
    return 0.0 if p == 0.0 else math.exp(1.0 - 1.0 / p)


def orthogonal_basis_with_first(v: np.ndarray) -> np.ndarray:
    """Return an orthogonal matrix whose first column is the unit vector v."""
    n = len(v)
    columns = [v]
    for e in np.eye(n):
        w = e.copy()
        for u in columns:
            w -= np.dot(u, w) * u
        if np.linalg.norm(w) > 1e-11:
            columns.append(w / np.linalg.norm(w))
        if len(columns) == n:
            break
    return np.column_stack(columns)


def canonical_copy(values: np.ndarray, weights: np.ndarray, side: int,
                   other_dim: int) -> tuple[np.ndarray, np.ndarray]:
    """Canonical Boolean copy and its common vacuum in finite dimensions."""
    m = len(values)
    basis = orthogonal_basis_with_first(np.sqrt(weights))
    multiplication = np.diag(values)
    if side == 1:
        total = 1 + (m - 1) + (other_dim - 1)
        isometry = np.zeros((total, m))
        isometry[0, 0] = 1.0
        isometry[1:m, 1:m] = np.eye(m - 1)
    else:
        total = 1 + (other_dim - 1) + (m - 1)
        isometry = np.zeros((total, m))
        isometry[0, 0] = 1.0
        start = other_dim
        isometry[start:start + m - 1, 1:m] = np.eye(m - 1)
    change = isometry @ basis.T
    copied = change @ multiplication @ change.T
    vacuum = np.eye(total)[0]
    return copied, vacuum


def spectral_projection(a: np.ndarray, threshold: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(a)
    chosen = eigenvectors[:, eigenvalues <= threshold + 1e-10]
    return chosen @ chosen.T


def meet_projection(p: np.ndarray, q: np.ndarray) -> np.ndarray:
    stacked = np.vstack((np.eye(len(p)) - p, np.eye(len(p)) - q))
    _, singular, vh = np.linalg.svd(stacked)
    null = vh[singular < 1e-8].T
    return null @ null.T if null.size else np.zeros_like(p)


def empirical_cdf(values: np.ndarray, weights: np.ndarray, t: float) -> float:
    return float(weights[values <= t].sum())


def predicted(f: float, g: float, t: float) -> float:
    if t < 0:
        return float(abs(f - 1.0) < 1e-12 and abs(g - 1.0) < 1e-12)
    return boolean_meet(f, g)


def finite_dimensional_check() -> None:
    cases = [
        (
            np.array([-3.0, -1.0, 2.0]), np.array([0.2, 0.3, 0.5]),
            np.array([-2.0, 1.0, 4.0]), np.array([0.4, 0.35, 0.25]),
            [-3.5, -2.5, -1.5, -0.5, 0.0, 1.5, 3.0, 5.0],
        ),
        (
            np.array([-4.0, -2.0]), np.array([0.6, 0.4]),
            np.array([-3.0, -1.0]), np.array([0.25, 0.75]),
            [-5.0, -3.5, -2.5, -1.5, -0.5, 0.0],
        ),
    ]
    for xval, xwt, yval, ywt, thresholds in cases:
        x, omega = canonical_copy(xval, xwt, 1, len(yval))
        y, omega2 = canonical_copy(yval, ywt, 2, len(xval))
        assert np.allclose(omega, omega2)
        for t in thresholds:
            p = spectral_projection(x, t)
            q = spectral_projection(y, t)
            actual = float(omega @ meet_projection(p, q) @ omega)
            f = empirical_cdf(xval, xwt, t)
            g = empirical_cdf(yval, ywt, t)
            expect = predicted(f, g, t)
            assert abs(actual - expect) < 2e-8, (t, actual, expect)


def semigroup_and_limits_check() -> None:
    for p in np.linspace(0.03, 1.0, 25):
        for q in np.linspace(0.03, 1.0, 25):
            assert abs(chi(boolean_meet(p, q)) - chi(p) * chi(q)) < 2e-14

    alpha = 1.7
    for n in (100, 1000, 10000):
        # Type II at x=1.3.
        x = 1.3
        classical = (1.0 - x ** (-alpha) / n) ** n
        boolean = 1.0 / (1.0 - math.log(classical))
        assert abs(boolean - 1.0 / (1.0 + x ** (-alpha))) < 0.01

        # Type I at x=0.4.
        x = 0.4
        classical = (1.0 - math.exp(-x) / n) ** n
        boolean = 1.0 / (1.0 - math.log(classical))
        assert abs(boolean - 1.0 / (1.0 + math.exp(-x))) < 0.01

        # Type III at x=-0.6.
        x = -0.6
        classical = (1.0 - (-x) ** alpha / n) ** n
        boolean = 1.0 / (1.0 - math.log(classical))
        assert abs(boolean - 1.0 / (1.0 + (-x) ** alpha)) < 0.01


if __name__ == "__main__":
    finite_dimensional_check()
    semigroup_and_limits_check()
    print("all Boolean-maximum formula checks passed")
