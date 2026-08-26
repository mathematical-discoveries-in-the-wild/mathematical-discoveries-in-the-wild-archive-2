#!/usr/bin/env python3
"""Deterministic finite checks for the Cartesian tensorization packet."""

from __future__ import annotations

import itertools
import math
import random


SEED = 210906009
TOL = 2.0e-10


def entropy(values: list[float]) -> float:
    mean = sum(values) / len(values)
    return sum(x * math.log(x) for x in values) / len(values) - mean * math.log(mean)


def local_entropy(a: float, b: float) -> float:
    mean = 0.5 * (a + b)
    return 0.5 * a * math.log(a / mean) + 0.5 * b * math.log(b / mean)


def graph_energy(values: list[float], edges: list[tuple[int, int, float]]) -> float:
    # The source sums ordered pairs with a prefactor 2/n.  Each undirected
    # edge therefore contributes 4/n times its local two-point entropy.
    return (4.0 / len(values)) * sum(
        weight * local_entropy(values[i], values[j]) for i, j, weight in edges
    )


def random_edges(rng: random.Random, n: int) -> list[tuple[int, int, float]]:
    edges: list[tuple[int, int, float]] = []
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.58:
                edges.append((i, j, 0.15 + 2.0 * rng.random()))
    if not edges:
        edges.append((0, 1, 0.15 + 2.0 * rng.random()))
    return edges


def product_edges(
    n: int,
    m: int,
    edges_g: list[tuple[int, int, float]],
    edges_h: list[tuple[int, int, float]],
) -> list[tuple[int, int, float]]:
    edges: list[tuple[int, int, float]] = []
    index = lambda i, u: i * m + u
    for u in range(m):
        edges.extend((index(i, u), index(j, u), w) for i, j, w in edges_g)
    for i in range(n):
        edges.extend((index(i, u), index(i, v), w) for u, v, w in edges_h)
    return edges


def check_two_factor_products(rng: random.Random) -> None:
    worst_tensorization = 0.0
    worst_decomposition = 0.0
    for _ in range(2000):
        n = rng.randint(2, 6)
        m = rng.randint(2, 6)
        edges_g = random_edges(rng, n)
        edges_h = random_edges(rng, m)
        values = [math.exp(rng.uniform(-5.0, 5.0)) for _ in range(n * m)]

        rows = [values[i * m : (i + 1) * m] for i in range(n)]
        columns = [[values[i * m + u] for i in range(n)] for u in range(m)]
        tensor_rhs = sum(entropy(col) for col in columns) / m
        tensor_rhs += sum(entropy(row) for row in rows) / n
        tensor_error = entropy(values) - tensor_rhs
        worst_tensorization = max(worst_tensorization, tensor_error)
        assert tensor_error <= TOL * max(1.0, tensor_rhs)

        product = product_edges(n, m, edges_g, edges_h)
        exact = graph_energy(values, product)
        fibers = sum(graph_energy(col, edges_g) for col in columns) / m
        fibers += sum(graph_energy(row, edges_h) for row in rows) / n
        decomposition_error = abs(exact - fibers)
        worst_decomposition = max(worst_decomposition, decomposition_error)
        assert decomposition_error <= TOL * max(1.0, exact, fibers)

    print(
        "two-factor products: PASS",
        f"(worst tensorization excess {worst_tensorization:.3e},",
        f"worst energy error {worst_decomposition:.3e})",
    )


def check_weighted_k2(rng: random.Random) -> None:
    worst = 0.0
    for _ in range(100):
        weight = math.exp(rng.uniform(-4.0, 4.0))
        values = [math.exp(rng.uniform(-7.0, 7.0)) for _ in range(2)]
        quotient = graph_energy(values, [(0, 1, weight)]) / entropy(values)
        error = abs(quotient - 2.0 * weight)
        worst = max(worst, error)
        assert error <= TOL * max(1.0, 2.0 * weight)
    print("weighted K2: PASS", f"(worst quotient error {worst:.3e})")


def hypercube_edges(weights: list[float]) -> list[tuple[int, int, float]]:
    dimension = len(weights)
    edges: list[tuple[int, int, float]] = []
    for vertex in range(1 << dimension):
        for coordinate, weight in enumerate(weights):
            other = vertex ^ (1 << coordinate)
            if vertex < other:
                edges.append((vertex, other, weight))
    return edges


def check_hypercubes(rng: random.Random) -> None:
    smallest_slack = math.inf
    for _ in range(1200):
        dimension = rng.randint(1, 6)
        weights = [math.exp(rng.uniform(-3.0, 3.0)) for _ in range(dimension)]
        values = [
            math.exp(rng.uniform(-6.0, 6.0)) for _ in range(1 << dimension)
        ]
        lhs = 2.0 * min(weights) * entropy(values)
        rhs = graph_energy(values, hypercube_edges(weights))
        slack = rhs - lhs
        smallest_slack = min(smallest_slack, slack)
        assert slack >= -TOL * max(1.0, lhs, rhs)
    print("weighted hypercubes: PASS", f"(smallest slack {smallest_slack:.3e})")


def main() -> None:
    rng = random.Random(SEED)
    check_two_factor_products(rng)
    check_weighted_k2(rng)
    check_hypercubes(rng)
    print("all deterministic checks: PASS")


if __name__ == "__main__":
    main()

