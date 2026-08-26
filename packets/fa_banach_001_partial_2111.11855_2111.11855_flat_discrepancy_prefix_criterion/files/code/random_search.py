#!/usr/bin/env python3
"""Numerically probe Conjecture 7.1 of arXiv:2111.11855.

The cumulative discrepancy values satisfy
    sum_{i<=k} delta_i(A) = min_z ||A-zI||_(k),
where ||.||_(k) is the Ky Fan k-norm.  We solve these two-real-variable
convex problems repeatedly and test every weak-majorization prefix.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
from scipy.optimize import minimize


def ky_fan_shift_value(matrix: np.ndarray, z: complex, k: int) -> float:
    shifted = matrix - z * np.eye(matrix.shape[0], dtype=complex)
    return float(np.linalg.svd(shifted, compute_uv=False)[:k].sum())


def discrepancy(matrix: np.ndarray, restarts: int = 5) -> tuple[np.ndarray, np.ndarray]:
    n = matrix.shape[0]
    center = np.trace(matrix) / n
    scale = max(1.0, float(np.linalg.norm(matrix, 2)))
    seeds = [
        center,
        0j,
        center + scale,
        center + 1j * scale,
        center - scale - 1j * scale,
    ][:restarts]
    cumulative = np.zeros(n + 1)
    minimizers = np.zeros(n, dtype=complex)
    for k in range(1, n + 1):
        best = None
        for seed in seeds:
            result = minimize(
                lambda xy: ky_fan_shift_value(matrix, xy[0] + 1j * xy[1], k),
                np.array([seed.real, seed.imag]),
                method="Powell",
                options={"xtol": 1e-11, "ftol": 1e-11, "maxiter": 1200},
            )
            if best is None or result.fun < best.fun:
                best = result
        assert best is not None
        cumulative[k] = best.fun
        minimizers[k - 1] = best.x[0] + 1j * best.x[1]
    return np.diff(cumulative), minimizers


@dataclass
class Probe:
    margin: float
    prefix: int
    lhs: np.ndarray
    rhs: np.ndarray
    delta_a: np.ndarray
    delta_b: np.ndarray
    alpha_a: np.ndarray
    alpha_b: np.ndarray
    a: np.ndarray
    b: np.ndarray


def evaluate(a: np.ndarray, b: np.ndarray, min_prefix: int = 1) -> Probe:
    delta_a, alpha_a = discrepancy(a)
    delta_b, alpha_b = discrepancy(b)
    lhs = np.linalg.svd(a @ b - b @ a, compute_uv=False)
    rhs = 2.0 * delta_a * delta_b
    gaps = np.cumsum(lhs) - np.cumsum(rhs)
    if not 1 <= min_prefix <= len(gaps):
        raise ValueError(f"min_prefix must lie in [1, {len(gaps)}]")
    prefix = int(np.argmax(gaps[min_prefix - 1 :])) + min_prefix
    return Probe(
        margin=float(gaps[prefix - 1]),
        prefix=prefix,
        lhs=lhs,
        rhs=rhs,
        delta_a=delta_a,
        delta_b=delta_b,
        alpha_a=alpha_a,
        alpha_b=alpha_b,
        a=a,
        b=b,
    )


def random_matrix(
    rng: np.random.Generator, n: int, mode: str, epsilon: float = 0.05
) -> np.ndarray:
    if mode == "real":
        matrix = rng.integers(-3, 4, size=(n, n)).astype(complex)
    elif mode == "complex":
        matrix = rng.integers(-3, 4, size=(n, n)) + 1j * rng.integers(
            -3, 4, size=(n, n)
        )
    elif mode == "rank_one":
        x = rng.integers(-3, 4, size=n) + 1j * rng.integers(-3, 4, size=n)
        y = rng.integers(-3, 4, size=n) + 1j * rng.integers(-3, 4, size=n)
        matrix = np.outer(x, np.conjugate(y))
    elif mode == "rank_two":
        x = rng.integers(-3, 4, size=(n, 2)) + 1j * rng.integers(-3, 4, size=(n, 2))
        y = rng.integers(-3, 4, size=(n, 2)) + 1j * rng.integers(-3, 4, size=(n, 2))
        matrix = x @ np.conjugate(y).T
    elif mode == "upper":
        matrix = np.triu(
            rng.integers(-3, 4, size=(n, n))
            + 1j * rng.integers(-3, 4, size=(n, n)),
            1,
        )
    elif mode == "weighted_shift":
        matrix = np.zeros((n, n), dtype=complex)
        weights = rng.integers(-4, 5, size=n) + 1j * rng.integers(-4, 5, size=n)
        for i in range(n - 1):
            matrix[i, i + 1] = weights[i]
        matrix[n - 1, 0] = weights[n - 1]
    elif mode == "normal":
        eigenvalues = rng.normal(size=n) + 1j * rng.normal(size=n)
        gaussian = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        unitary, triangular = np.linalg.qr(gaussian)
        phases = np.diag(triangular)
        phases = np.where(np.abs(phases) > 0, phases / np.abs(phases), 1.0)
        unitary = unitary @ np.diag(np.conjugate(phases))
        matrix = unitary @ np.diag(eigenvalues) @ np.conjugate(unitary).T
    elif mode in {"near_e12", "near_e21"}:
        if n < 2:
            raise ValueError("matrix-unit perturbations require n >= 2")
        matrix = epsilon * (
            rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
        )
        i, j = (0, 1) if mode == "near_e12" else (1, 0)
        matrix[i, j] += 1.0
    else:
        raise ValueError(mode)
    matrix -= np.trace(matrix) / n * np.eye(n)
    norm = np.linalg.norm(matrix, "fro")
    return matrix / norm if norm else matrix


def print_probe(probe: Probe) -> None:
    np.set_printoptions(precision=12, suppress=True, linewidth=200)
    print(f"margin={probe.margin:.12g} prefix={probe.prefix}")
    print("lhs singular values", probe.lhs)
    print("rhs products", probe.rhs)
    print("prefix gaps", np.cumsum(probe.lhs) - np.cumsum(probe.rhs))
    print("delta(A)", probe.delta_a)
    print("delta(B)", probe.delta_b)
    print("alpha(A)", probe.alpha_a)
    print("alpha(B)", probe.alpha_b)
    print("A=")
    print(probe.a)
    print("B=")
    print(probe.b)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=3)
    parser.add_argument("--trials", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=211111855)
    parser.add_argument("--epsilon", type=float, default=0.05)
    parser.add_argument(
        "--min-prefix",
        type=int,
        default=1,
        help="Ignore smaller weak-majorization prefixes when ranking candidates.",
    )
    parser.add_argument(
        "--mode",
        choices=[
            "real",
            "complex",
            "rank_one",
            "rank_two",
            "upper",
            "weighted_shift",
            "normal",
            "near_units",
        ],
        default="real",
    )
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    best = None
    for trial in range(1, args.trials + 1):
        if args.mode == "near_units":
            a = random_matrix(rng, args.n, "near_e12", args.epsilon)
            b = random_matrix(rng, args.n, "near_e21", args.epsilon)
        else:
            a = random_matrix(rng, args.n, args.mode, args.epsilon)
            b = random_matrix(rng, args.n, args.mode, args.epsilon)
        probe = evaluate(a, b, min_prefix=args.min_prefix)
        if best is None or probe.margin > best.margin:
            best = probe
            print(f"trial={trial}")
            print_probe(best)
        if probe.margin > 1e-6:
            print("COUNTEREXAMPLE_CANDIDATE")
            break


if __name__ == "__main__":
    main()
