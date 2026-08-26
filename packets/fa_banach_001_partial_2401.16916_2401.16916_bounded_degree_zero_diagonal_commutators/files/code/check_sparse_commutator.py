#!/usr/bin/env python3
"""Finite regression checks for the sparse compact-commutator construction."""

from __future__ import annotations

import math
import random

import numpy as np


def greedy_coloring(neighbors: list[set[int]]) -> tuple[list[int], int]:
    colors: list[int] = []
    for i, adjacent in enumerate(neighbors):
        forbidden = {colors[j] for j in adjacent if j < i}
        color = 0
        while color in forbidden:
            color += 1
        colors.append(color)
    return colors, max(colors, default=0) + 1


def factor(t: np.ndarray, neighbors: list[set[int]]) -> tuple[np.ndarray, np.ndarray, float]:
    n = t.shape[0]
    colors, number_colors = greedy_coloring(neighbors)
    roots = np.exp(2j * np.pi * np.arange(number_colors) / number_colors)

    rho = np.zeros(n)
    for i in range(n):
        for j in neighbors[i]:
            rho[i] = max(rho[i], abs(t[i, j]), abs(t[j, i]))
    scale = np.sqrt(rho)
    lam = np.array([roots[colors[i]] * scale[i] for i in range(n)])

    separation = math.inf
    for p in range(number_colors):
        for q in range(number_colors):
            if p == q:
                continue
            # Exact minimum over 0 <= s <= 1 of |root_p-s root_q|.
            cosine = float(np.real(roots[p] * np.conj(roots[q])))
            minimizer = min(1.0, max(0.0, cosine))
            value = abs(roots[p] - minimizer * roots[q])
            separation = min(separation, value)
    if number_colors == 1:
        separation = 1.0

    b = np.zeros_like(t)
    for i in range(n):
        for j in neighbors[i]:
            if t[i, j] != 0:
                denominator = lam[i] - lam[j]
                assert abs(denominator) + 1e-13 >= separation * max(scale[i], scale[j])
                b[i, j] = t[i, j] / denominator
                assert abs(b[i, j]) <= min(scale[i], scale[j]) / separation + 1e-10
    return np.diag(lam), b, separation


def random_case(n: int, degree_bound: int, rng: random.Random) -> tuple[np.ndarray, list[set[int]]]:
    neighbors = [set() for _ in range(n)]
    candidates = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rng.shuffle(candidates)
    for i, j in candidates:
        if len(neighbors[i]) >= degree_bound or len(neighbors[j]) >= degree_bound:
            continue
        if rng.random() < 0.18:
            neighbors[i].add(j)
            neighbors[j].add(i)

    t = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in neighbors[i]:
            if i < j:
                if rng.random() < 0.85:
                    t[i, j] = rng.gauss(0, 1) + 1j * rng.gauss(0, 1)
                if rng.random() < 0.85:
                    t[j, i] = rng.gauss(0, 1) + 1j * rng.gauss(0, 1)
                if t[i, j] == 0 and t[j, i] == 0:
                    t[i, j] = 1.0
    return t, neighbors


def main() -> None:
    rng = random.Random(240116916)
    tested = 0
    max_residual = 0.0
    for n in range(2, 31):
        for _ in range(100):
            t, neighbors = random_case(n, 4, rng)
            a, b, _ = factor(t, neighbors)
            residual = np.linalg.norm(t - (a @ b - b @ a), 2)
            max_residual = max(max_residual, float(residual))
            assert residual < 2e-12
            tested += 1
    print(f"passed {tested}/{tested} cases; max residual {max_residual:.3e}")


if __name__ == "__main__":
    main()
