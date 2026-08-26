#!/usr/bin/env python3
"""Numerically verify the 4-by-4 Ritz-envelope support polynomial.

The checks compare the complementary-minor polynomial with direct nullspace
compressions and test the one-dimensional support maximization. They are not
a proof.
"""

from __future__ import annotations

import itertools
import math

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.optimize import linprog


def weight_segment(lam: np.ndarray, mu: complex) -> tuple[np.ndarray, np.ndarray, float, float]:
    matrix = np.vstack([np.ones(4), lam.real, lam.imag])
    rhs = np.array([1.0, mu.real, mu.imag])
    t0 = np.linalg.lstsq(matrix, rhs, rcond=None)[0]
    _, _, vh = np.linalg.svd(matrix)
    direction = vh[-1]
    direction /= np.linalg.norm(direction)
    lower, upper = -np.inf, np.inf
    for value, slope in zip(t0, direction):
        if slope > 1.0e-14:
            lower = max(lower, -value / slope)
        elif slope < -1.0e-14:
            upper = min(upper, -value / slope)
        elif value < -1.0e-12:
            raise AssertionError("empty weight segment")
    if not lower <= upper + 1.0e-12:
        raise AssertionError((t0, direction, lower, upper))
    return t0, direction, lower, upper


def poly_coefficients(lam: np.ndarray, t: np.ndarray, theta: float) -> np.ndarray:
    h = np.real(np.exp(-1j * theta) * lam)
    coeff = np.zeros(3)
    for i, j in itertools.combinations(range(4), 2):
        rest = [ell for ell in range(4) if ell not in (i, j)]
        factor = t[i] * t[j] * abs(lam[i] - lam[j]) ** 2
        h0, h1 = h[rest]
        coeff += factor * np.array([1.0, -(h0 + h1), h0 * h1])
    return coeff


def poly_ds_coefficients(
    lam: np.ndarray, t: np.ndarray, direction: np.ndarray, theta: float
) -> np.ndarray:
    h = np.real(np.exp(-1j * theta) * lam)
    coeff = np.zeros(3)
    for i, j in itertools.combinations(range(4), 2):
        rest = [ell for ell in range(4) if ell not in (i, j)]
        factor = (direction[i] * t[j] + t[i] * direction[j]) * abs(
            lam[i] - lam[j]
        ) ** 2
        h0, h1 = h[rest]
        coeff += factor * np.array([1.0, -(h0 + h1), h0 * h1])
    return coeff


def polynomial_roots(lam: np.ndarray, t: np.ndarray, theta: float) -> np.ndarray:
    coeff = poly_coefficients(lam, t, theta)
    aa, bb, cc = coeff
    discriminant = bb * bb - 4.0 * aa * cc
    tolerance = 2.0e-11 * (1.0 + bb * bb + abs(aa * cc))
    if discriminant < -tolerance:
        raise AssertionError((coeff, discriminant))
    root_gap = math.sqrt(max(discriminant, 0.0))
    return np.array([(-bb - root_gap) / (2.0 * aa), (-bb + root_gap) / (2.0 * aa)])


def direct_roots(lam: np.ndarray, t: np.ndarray, theta: float) -> np.ndarray:
    u = np.sqrt(np.maximum(t, 0.0))
    q = np.column_stack([u, lam * u])
    _, singular, vh = np.linalg.svd(q.conj().T, full_matrices=True)
    rank = int(np.sum(singular > 1.0e-10))
    if rank != 2:
        raise AssertionError((lam, t, singular))
    f = vh.conj().T[:, rank:]
    h = np.real(np.exp(-1j * theta) * lam)
    compression = f.conj().T @ np.diag(h) @ f
    return np.linalg.eigvalsh(compression)


def rplus(lam: np.ndarray, t0: np.ndarray, direction: np.ndarray, s: float, theta: float) -> float:
    return float(polynomial_roots(lam, t0 + s * direction, theta)[-1])


def support_maximum(
    lam: np.ndarray,
    t0: np.ndarray,
    direction: np.ndarray,
    lower: float,
    upper: float,
    theta: float,
) -> tuple[float, float]:
    grid = np.linspace(lower, upper, 201)
    values = np.array([rplus(lam, t0, direction, s, theta) for s in grid])
    candidates: list[tuple[float, float]] = [
        (float(values[0]), float(grid[0])),
        (float(values[-1]), float(grid[-1])),
    ]
    for k in range(1, len(grid) - 1):
        if values[k] >= values[k - 1] and values[k] >= values[k + 1]:
            result = minimize_scalar(
                lambda s: -rplus(lam, t0, direction, s, theta),
                bounds=(grid[k - 1], grid[k + 1]),
                method="bounded",
                options={"xatol": 1.0e-13},
            )
            candidates.append((-float(result.fun), float(result.x)))
    return max(candidates)


def source_like_example() -> tuple[np.ndarray, complex]:
    lam = np.array([1j, 0.0 + 0.0j, 1.0 + 0.0j, 0.35 + 0.33j])
    mu = 0.10 + 0.30j
    return lam, mu


def coefficient_slice_support(lam: np.ndarray, mu: complex, theta: float) -> float:
    """LP support of the fixed-root slice of the compression-polynomial hull."""
    pairs = list(itertools.combinations(range(4), 2))
    values = np.array([(mu - lam[i]) * (mu - lam[j]) for i, j in pairs])
    remaining_root = np.array([lam[i] + lam[j] - mu for i, j in pairs])
    objective = -np.real(np.exp(-1j * theta) * remaining_root)
    equality = np.vstack([np.ones(len(pairs)), values.real, values.imag])
    result = linprog(
        objective,
        A_eq=equality,
        b_eq=np.array([1.0, 0.0, 0.0]),
        bounds=(0.0, None),
        method="highs",
    )
    if not result.success:
        raise AssertionError(result.message)
    return -float(result.fun)


def random_example(rng: np.random.Generator) -> tuple[np.ndarray, complex]:
    triangle = np.array(
        [
            0.0 + 0.0j,
            1.0 + 0.0j,
            rng.uniform(-0.15, 0.25) + 1j * rng.uniform(0.8, 1.4),
        ]
    )
    interior_weights = rng.dirichlet(np.ones(3) * 2.0)
    interior = np.dot(interior_weights, triangle)
    lam = np.append(triangle, interior)
    mu = np.dot(rng.dirichlet(np.ones(4) * 1.5), lam)
    return lam, complex(mu)


def main() -> None:
    rng = np.random.default_rng(20260817)
    root_checks = 0
    stationary_checks = 0
    worst_root_error = 0.0
    worst_stationary_residual = 0.0

    examples = [source_like_example()] + [random_example(rng) for _ in range(24)]
    for lam, mu in examples:
        t0, direction, lower, upper = weight_segment(lam, mu)
        if upper - lower < 1.0e-9:
            continue
        for _ in range(24):
            s = rng.uniform(lower, upper)
            theta = rng.uniform(0.0, 2.0 * math.pi)
            t = t0 + s * direction
            algebraic = polynomial_roots(lam, t, theta)
            direct = direct_roots(lam, t, theta)
            error = float(np.max(np.abs(algebraic - direct)))
            worst_root_error = max(worst_root_error, error)
            if error > 3.0e-9:
                raise AssertionError((lam, mu, t, theta, algebraic, direct))
            root_checks += 1

        for _ in range(8):
            theta = rng.uniform(0.0, 2.0 * math.pi)
            value, s_star = support_maximum(
                lam, t0, direction, lower, upper, theta
            )
            dense_grid = np.linspace(lower, upper, 1001)
            dense = max(rplus(lam, t0, direction, s, theta) for s in dense_grid)
            if value + 2.0e-7 < dense:
                raise AssertionError((value, dense, s_star, theta))
            if lower + 2.0e-6 < s_star < upper - 2.0e-6:
                t = t0 + s_star * direction
                ds_coeff = poly_ds_coefficients(lam, t, direction, theta)
                residual = abs(np.polyval(ds_coeff, value))
                scale = 1.0 + np.linalg.norm(ds_coeff) * (1.0 + abs(value) ** 2)
                normalized = float(residual / scale)
                worst_stationary_residual = max(
                    worst_stationary_residual, normalized
                )
                if normalized > 2.0e-7:
                    raise AssertionError((normalized, value, s_star, theta))
                stationary_checks += 1

    # Confirm that the source-like interior-eigenvalue example genuinely needs
    # an interior segment parameter: endpoint ellipses alone miss support.
    lam, mu = source_like_example()
    t0, direction, lower, upper = weight_segment(lam, mu)
    max_gap = 0.0
    max_gap_theta = 0.0
    interior_directions = 0
    slice_relaxation_gap = 0.0
    for theta in np.linspace(0.0, 2.0 * math.pi, 361, endpoint=False):
        value, s_star = support_maximum(lam, t0, direction, lower, upper, theta)
        endpoint = max(
            rplus(lam, t0, direction, lower, theta),
            rplus(lam, t0, direction, upper, theta),
        )
        gap = value - endpoint
        if gap > max_gap:
            max_gap = gap
            max_gap_theta = theta
        if lower + 1.0e-5 < s_star < upper - 1.0e-5:
            interior_directions += 1
        slice_value = coefficient_slice_support(lam, mu, theta)
        if slice_value + 5.0e-8 < value:
            raise AssertionError((slice_value, value, theta))
        slice_relaxation_gap = max(slice_relaxation_gap, slice_value - value)

    if max_gap < 1.0e-3 or interior_directions == 0:
        raise AssertionError((max_gap, interior_directions))

    print(f"direct compression root checks passed: {root_checks}")
    print(f"interior stationary checks passed: {stationary_checks}")
    print(f"worst root error: {worst_root_error:.3e}")
    print(f"worst normalized stationary residual: {worst_stationary_residual:.3e}")
    print(f"source-like endpoint-only support gap: {max_gap:.12f}")
    print(f"gap direction theta: {max_gap_theta:.12f}")
    print(f"directions with an interior maximizing weight: {interior_directions}/361")
    print(f"coefficient-slice relaxation maximum gap: {slice_relaxation_gap:.12f}")


if __name__ == "__main__":
    main()
