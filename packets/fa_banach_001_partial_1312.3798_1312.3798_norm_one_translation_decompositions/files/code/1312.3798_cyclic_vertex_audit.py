#!/usr/bin/env python3
"""Exhaust finite cyclic quotient-ball vertices for selected translation triples."""

from __future__ import annotations

import importlib.util
import itertools
from pathlib import Path

import numpy as np
from scipy.linalg import qr


SEARCH = Path(__file__).with_name("1312.3798_cyclic_constant_search.py")
SPEC = importlib.util.spec_from_file_location("cyclic_search", SEARCH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def independent_columns(a: np.ndarray) -> np.ndarray:
    _, _, pivots = qr(a, pivoting=True, mode="economic")
    rank = np.linalg.matrix_rank(a)
    return a[:, pivots[:rank]]


def audit(q: int, triple: tuple[int, int, int]) -> None:
    a = np.concatenate([MODULE.fixed_basis(q, d) for d in triple], axis=1)
    b = independent_columns(a)
    rank = b.shape[1]
    seen: set[tuple[float, ...]] = set()
    best = 0.0
    best_f = None
    for rows in itertools.combinations(range(q), rank):
        square = b[list(rows), :]
        if abs(np.linalg.det(square)) < 1e-9:
            continue
        for signs in itertools.product((-1.0, 1.0), repeat=rank):
            z = np.linalg.solve(square, np.asarray(signs))
            f = b @ z
            if np.max(np.abs(f)) > 1.0 + 1e-8:
                continue
            key = tuple(np.round(f, 9))
            if key in seen:
                continue
            seen.add(key)
            quotient, _ = MODULE.quotient_norm(a, f)
            if quotient > best + 1e-8:
                best = quotient
                best_f = f.copy()
    print(
        f"q={q}, triple={triple}, rank={rank}, vertices={len(seen)}, "
        f"max quotient={best:.12g}"
    )
    if best_f is not None:
        print("best f=", np.round(best_f, 9).tolist())


def main() -> None:
    for triple in [(1, 2, 3), (1, 2, 6), (1, 3, 4), (2, 3, 4)]:
        audit(12, triple)


if __name__ == "__main__":
    main()
