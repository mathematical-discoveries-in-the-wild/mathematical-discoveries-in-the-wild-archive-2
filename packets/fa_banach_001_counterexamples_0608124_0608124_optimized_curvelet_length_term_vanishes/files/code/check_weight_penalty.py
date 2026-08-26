#!/usr/bin/env python3
"""Regression checks for the exact optimized-weight penalty bound."""

import numpy as np


def qnorm(x: np.ndarray, q: float) -> float:
    if np.isinf(q):
        return float(np.max(np.abs(x)))
    return float(np.linalg.norm(x, ord=q))


def check_case(rng: np.random.Generator, m: int, q: float, eps: float) -> None:
    u = rng.normal(size=(97, m))
    rho = np.exp(rng.normal(size=97))
    theta = 1.0 / (4.0 * eps)
    a = np.array([qnorm(row, q) for row in u])
    v = np.maximum(rho - a / (2.0 * theta), 0.0)
    penalty = theta * np.sum((rho - v) ** 2)
    direct = theta * np.sum(np.minimum(rho, a / (2.0 * theta)) ** 2)
    bound = eps * np.sum(a ** 2)
    c_mq = m ** max(2.0 / q - 1.0, 0.0) if not np.isinf(q) else 1.0
    ell2_bound = eps * c_mq * np.sum(u ** 2)
    if not np.allclose(penalty, direct, rtol=1e-12, atol=1e-12):
        raise AssertionError((penalty, direct))
    tolerance = 1e-11 * max(1.0, bound, ell2_bound)
    if penalty > bound + tolerance:
        raise AssertionError((penalty, bound))
    if penalty > ell2_bound + tolerance:
        raise AssertionError((penalty, ell2_bound))
    print(f"M={m} q={q!s:>4} eps={eps:.0e} penalty={penalty:.6e} bound={ell2_bound:.6e}")


def main() -> None:
    rng = np.random.default_rng(608124)
    for m in (1, 3, 7):
        for q in (1.0, 2.0, 3.0, np.inf):
            for eps in (1e-1, 1e-3, 1e-6):
                check_case(rng, m, q, eps)
    print("all exact-formula and optimized-penalty bounds verified")


if __name__ == "__main__":
    main()
