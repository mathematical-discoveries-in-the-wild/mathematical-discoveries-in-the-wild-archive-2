#!/usr/bin/env python3
"""Finite checks for the spanner-based interval-selection theorem.

The proof is analytic.  This script stress-tests its two implications on
random one- and two-dimensional point sets, including unbounded intervals.
For small planar instances it constructs a greedy t-spanner, which is slow but
convenient for checking the theorem.  The packet's complexity theorem instead
uses the standard near-linear WSPD spanner construction.
"""

from __future__ import annotations

import heapq
import math
import random
from typing import Iterable, Sequence


TOL = 1.0e-9


def euclidean(p: Sequence[float], q: Sequence[float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(p, q)))


def dijkstra(
    graph: Sequence[list[tuple[int, float]]],
    initial: Iterable[tuple[int, float]],
) -> list[float]:
    dist = [math.inf] * len(graph)
    heap: list[tuple[float, int]] = []
    for vertex, value in initial:
        if value < dist[vertex]:
            dist[vertex] = value
            heapq.heappush(heap, (value, vertex))
    while heap:
        value, vertex = heapq.heappop(heap)
        if value != dist[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            candidate = value + weight
            if candidate < dist[neighbor]:
                dist[neighbor] = candidate
                heapq.heappush(heap, (candidate, neighbor))
    return dist


def all_graph_distances(
    graph: Sequence[list[tuple[int, float]]],
) -> list[list[float]]:
    return [dijkstra(graph, [(source, 0.0)]) for source in range(len(graph))]


def greedy_spanner(
    points: Sequence[Sequence[float]], stretch: float
) -> list[list[tuple[int, float]]]:
    """Construct a small-test greedy spanner (not the fast packet algorithm)."""

    count = len(points)
    graph: list[list[tuple[int, float]]] = [[] for _ in points]
    pairs = sorted(
        (euclidean(points[i], points[j]), i, j)
        for i in range(count)
        for j in range(i + 1, count)
    )
    for weight, left, right in pairs:
        current = dijkstra(graph, [(left, 0.0)])[right]
        if current > stretch * weight + TOL:
            graph[left].append((right, weight))
            graph[right].append((left, weight))
    return graph


def line_path_spanner(points: Sequence[Sequence[float]]) -> list[list[tuple[int, float]]]:
    graph: list[list[tuple[int, float]]] = [[] for _ in points]
    order = sorted(range(len(points)), key=lambda index: points[index][0])
    for left, right in zip(order, order[1:]):
        weight = abs(points[left][0] - points[right][0])
        graph[left].append((right, weight))
        graph[right].append((left, weight))
    return graph


def exact_lambda_feasible(
    points: Sequence[Sequence[float]],
    lower: Sequence[float],
    upper: Sequence[float],
    lipschitz: float,
) -> bool:
    for i, point_i in enumerate(points):
        for j, point_j in enumerate(points):
            if lower[i] > upper[j] + lipschitz * euclidean(point_i, point_j) + TOL:
                return False
    return True


def spanner_interval_algorithm(
    graph: Sequence[list[tuple[int, float]]],
    lower: Sequence[float],
    upper: Sequence[float],
    lipschitz: float,
) -> tuple[str, list[float] | None]:
    if any(a > b for a, b in zip(lower, upper)):
        return "no-go", None

    finite_upper = [index for index, value in enumerate(upper) if math.isfinite(value)]
    if not finite_upper:
        finite_lower = [value for value in lower if math.isfinite(value)]
        constant = max(finite_lower) if finite_lower else 0.0
        return "success", [constant] * len(graph)

    baseline = min(upper[index] for index in finite_upper)
    initial = [(index, upper[index] - baseline) for index in finite_upper]
    scaled_graph = [
        [(neighbor, lipschitz * weight) for neighbor, weight in adjacency]
        for adjacency in graph
    ]
    values = [baseline + distance for distance in dijkstra(scaled_graph, initial)]
    if any(a > value + TOL for a, value in zip(lower, values)):
        return "no-go", None
    return "success", values


def random_intervals(rng: random.Random, count: int) -> tuple[list[float], list[float]]:
    lower: list[float] = []
    upper: list[float] = []
    for _ in range(count):
        center = rng.uniform(-4.0, 4.0)
        radius = rng.uniform(0.0, 2.0)
        a = center - radius
        b = center + radius
        if rng.random() < 0.12:
            a = -math.inf
        if rng.random() < 0.12:
            b = math.inf
        lower.append(a)
        upper.append(b)
    if rng.random() < 0.03:
        upper = [math.inf] * count
    return lower, upper


def check_case(
    points: Sequence[Sequence[float]],
    graph: Sequence[list[tuple[int, float]]],
    claimed_stretch: float,
    lower: Sequence[float],
    upper: Sequence[float],
    lipschitz: float,
) -> tuple[str, bool]:
    graph_dist = all_graph_distances(graph)
    for i, point_i in enumerate(points):
        for j, point_j in enumerate(points):
            direct = euclidean(point_i, point_j)
            assert graph_dist[i][j] + TOL >= direct
            assert graph_dist[i][j] <= claimed_stretch * direct + TOL

    outcome, values = spanner_interval_algorithm(graph, lower, upper, lipschitz)
    exact_feasible = exact_lambda_feasible(points, lower, upper, lipschitz)
    if outcome == "no-go":
        assert not exact_feasible
        return outcome, exact_feasible

    assert values is not None
    for a, value, b in zip(lower, values, upper):
        assert a <= value + TOL
        assert value <= b + TOL
    for i, point_i in enumerate(points):
        for j, point_j in enumerate(points):
            bound = claimed_stretch * lipschitz * euclidean(point_i, point_j)
            assert abs(values[i] - values[j]) <= bound + 5 * TOL
    return outcome, exact_feasible


def main() -> None:
    rng = random.Random(20260813)
    line_cases = 600
    planar_cases = 600
    line_no_go = 0
    planar_no_go = 0
    planar_gap_success = 0

    for _ in range(line_cases):
        count = rng.randint(2, 11)
        coordinates = sorted(rng.sample(range(-100, 101), count))
        points = [(coordinate / 7.0,) for coordinate in coordinates]
        graph = line_path_spanner(points)
        lower, upper = random_intervals(rng, count)
        lipschitz = rng.uniform(0.0, 3.0)
        outcome, exact_feasible = check_case(
            points, graph, 1.0, lower, upper, lipschitz
        )
        if outcome == "no-go":
            line_no_go += 1
        else:
            # Stretch one makes the gap test exact.
            assert exact_feasible

    stretch = 1.8
    for _ in range(planar_cases):
        count = rng.randint(2, 10)
        raw = rng.sample(range(0, 10_000), count)
        points = [((value % 101) / 13.0, (value // 101) / 11.0) for value in raw]
        graph = greedy_spanner(points, stretch)
        lower, upper = random_intervals(rng, count)
        lipschitz = rng.uniform(0.0, 3.0)
        outcome, exact_feasible = check_case(
            points, graph, stretch, lower, upper, lipschitz
        )
        if outcome == "no-go":
            planar_no_go += 1
        elif not exact_feasible:
            planar_gap_success += 1

    print(f"line_cases={line_cases} line_no_go={line_no_go}")
    print(
        "planar_cases="
        f"{planar_cases} planar_no_go={planar_no_go} "
        f"valid_gap_success={planar_gap_success}"
    )
    print("VERDICT: PASS")


if __name__ == "__main__":
    main()
