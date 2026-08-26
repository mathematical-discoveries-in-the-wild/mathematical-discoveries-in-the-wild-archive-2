#!/usr/bin/env python3
"""Numerical stress test for Conjecture 1.1 of arXiv:2105.13356."""

from __future__ import annotations

import argparse
import json
import math

import numpy as np
from scipy.linalg import fractional_matrix_power
from scipy.optimize import differential_evolution


def hp_power(a: np.ndarray, power: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh((a + a.conj().T) / 2)
    return (vecs * np.power(vals, power)) @ vecs.conj().T


def geometric_mean(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
    ah = hp_power(a, 0.5)
    aih = hp_power(a, -0.5)
    return ah @ hp_power(aih @ b @ aih, t) @ ah


def prefix_log_ratios(a: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
    x = hp_power(a, t) @ geometric_mean(a, b, t) @ hp_power(b, 1 - t)
    sx = np.linalg.svd(x, compute_uv=False)
    sab = np.linalg.svd(a @ b, compute_uv=False)
    return np.cumsum(np.log(sx)) - np.cumsum(np.log(sab))


def real_two_by_two(params: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    a, b, theta, t = params
    rot = np.array([[math.cos(theta), -math.sin(theta)],
                    [math.sin(theta), math.cos(theta)]])
    aa = np.diag([math.exp(a), math.exp(-a)])
    bb = rot @ np.diag([math.exp(b), math.exp(-b)]) @ rot.T
    return aa, bb, t


def two_by_two_objective(params: np.ndarray) -> float:
    a, b, t = real_two_by_two(params)
    return -float(prefix_log_ratios(a, b, t)[0])


def random_positive(rng: np.random.Generator, n: int, log_radius: float,
                    complex_entries: bool) -> np.ndarray:
    z = rng.normal(size=(n, n))
    if complex_entries:
        z = z + 1j * rng.normal(size=(n, n))
    q, _ = np.linalg.qr(z)
    logs = rng.uniform(-log_radius, log_radius, size=n)
    logs -= logs.mean()
    return (q * np.exp(logs)) @ q.conj().T


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=210513356)
    parser.add_argument("--log-radius", type=float, default=8.0)
    parser.add_argument("--opt-iters", type=int, default=300)
    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    records: list[dict[str, object]] = []
    for n in range(2, 6):
        for complex_entries in (False, True):
            best = (-np.inf, None)
            for _ in range(args.samples):
                a = random_positive(rng, n, args.log_radius, complex_entries)
                b = random_positive(rng, n, args.log_radius, complex_entries)
                t = rng.uniform(0, 1)
                logs = prefix_log_ratios(a, b, t)[:-1]
                k = int(np.argmax(logs))
                if logs[k] > best[0]:
                    best = (float(logs[k]), (a, b, t, k + 1))
            assert best[1] is not None
            a, b, t, k = best[1]
            records.append({
                "kind": "random",
                "n": n,
                "complex": complex_entries,
                "best_log_ratio": best[0],
                "best_ratio": math.exp(best[0]),
                "prefix_k": k,
                "t": t,
                "A": np.asarray(a).tolist(),
                "B": np.asarray(b).tolist(),
            })

    opt = differential_evolution(
        two_by_two_objective,
        bounds=[(0, 14), (0, 14), (0, math.pi / 2), (0, 1)],
        maxiter=args.opt_iters,
        popsize=25,
        polish=True,
        seed=args.seed,
        workers=1,
    )
    a, b, t = real_two_by_two(opt.x)
    records.append({
        "kind": "optimized_real_2x2",
        "params": opt.x.tolist(),
        "best_log_ratio": -float(opt.fun),
        "best_ratio": math.exp(-float(opt.fun)),
        "t": t,
        "A": a.tolist(),
        "B": b.tolist(),
        "success": bool(opt.success),
        "message": str(opt.message),
    })
    print(json.dumps(records, indent=2, default=lambda x: [x.real, x.imag]))


if __name__ == "__main__":
    main()
