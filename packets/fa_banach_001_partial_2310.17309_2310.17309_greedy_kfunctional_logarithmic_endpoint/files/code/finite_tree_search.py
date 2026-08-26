"""Finite balanced-tree search for greedy instability in V_{1,2}.

This is exploratory: it exactly evaluates the ring-variation seminorm on
functions constant on the leaves of a finite dyadic tree.  The maximization
over disjoint atoms/rings is a binary linear program.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import csc_matrix


def atoms(depth: int) -> list[tuple[int, int]]:
    leaf_count = 1 << depth
    out = []
    for level in range(depth + 1):
        width = leaf_count >> level
        for start in range(0, leaf_count, width):
            out.append((start, start + width))
    return out


def candidate_masks(depth: int) -> list[np.ndarray]:
    leaf_count = 1 << depth
    tree_atoms = atoms(depth)
    masks: dict[bytes, np.ndarray] = {}
    for a, b in tree_atoms:
        mask = np.zeros(leaf_count, dtype=np.int8)
        mask[a:b] = 1
        masks[mask.tobytes()] = mask
        for c, d in tree_atoms:
            if a <= c and d <= b and (c, d) != (a, b):
                ring = mask.copy()
                ring[c:d] = 0
                masks[ring.tobytes()] = ring
    return list(masks.values())


def haar_vectors(depth: int) -> list[np.ndarray]:
    leaf_count = 1 << depth
    out = []
    for level in range(depth):
        width = leaf_count >> level
        for start in range(0, leaf_count, width):
            half = width // 2
            h = np.zeros(leaf_count)
            h[start : start + half] = math.sqrt(leaf_count / width)
            h[start + half : start + width] = -math.sqrt(leaf_count / width)
            out.append(h)
    return out


class Variation:
    def __init__(self, depth: int):
        self.leaf_count = 1 << depth
        self.masks = candidate_masks(depth)
        incidence = np.stack(self.masks, axis=1)
        self.constraint = LinearConstraint(csc_matrix(incidence), 0, 1)
        self.integrality = np.ones(len(self.masks))
        self.bounds = Bounds(0, 1)

    def seminorm(self, values: np.ndarray) -> float:
        weights = []
        for mask in self.masks:
            indices = np.flatnonzero(mask)
            restricted = values[indices]
            centered = restricted - restricted.mean()
            weights.append(np.linalg.norm(centered) / math.sqrt(self.leaf_count))
        result = milp(
            c=-np.asarray(weights),
            integrality=self.integrality,
            bounds=self.bounds,
            constraints=self.constraint,
            options={"time_limit": 10},
        )
        if not result.success:
            raise RuntimeError(result.message)
        return -float(result.fun)

    def norm(self, values: np.ndarray) -> float:
        return np.linalg.norm(values) / math.sqrt(self.leaf_count) + self.seminorm(values)


def search(depth: int, trials: int, seed: int) -> None:
    rng = np.random.default_rng(seed)
    haar = haar_vectors(depth)
    variation = Variation(depth)
    best = (0.0, None)
    for trial in range(trials):
        # Log-uniform magnitudes make many different greedy cutoffs visible.
        magnitudes = np.exp(rng.uniform(-3.0, 0.0, len(haar)))
        coefficients = magnitudes * rng.choice([-1.0, 1.0], len(haar))
        order = np.argsort(-np.abs(coefficients))
        f = sum((coefficient * h for coefficient, h in zip(coefficients, haar)), np.zeros(1 << depth))
        f_norm = variation.norm(f)
        projection = np.zeros_like(f)
        for rank, index in enumerate(order, start=1):
            projection += coefficients[index] * haar[index]
            ratio = variation.norm(projection) / f_norm
            if ratio > best[0]:
                best = (ratio, (trial, rank, coefficients.copy(), order.copy(), f_norm))
                print(f"best ratio={ratio:.6f} trial={trial} rank={rank} f_norm={f_norm:.6f}", flush=True)
    ratio, data = best
    if data is not None:
        trial, rank, coefficients, order, f_norm = data
        print("FINAL", ratio, trial, rank, f_norm)
        print("COEFFICIENTS", coefficients.tolist())
        print("ORDER", order.tolist())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, default=4)
    parser.add_argument("--trials", type=int, default=100)
    parser.add_argument("--seed", type=int, default=231017309)
    args = parser.parse_args()
    search(args.depth, args.trials, args.seed)
