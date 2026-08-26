from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction


def has_cycle(vertices, edges):
    adjacency = [set() for _ in vertices]
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = set()
    for root in range(len(vertices)):
        if root in seen:
            continue
        stack = [(root, -1)]
        while stack:
            u, parent = stack.pop()
            if u in seen:
                return True
            seen.add(u)
            stack.extend((v, u) for v in adjacency[u] if v != parent)
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--box", type=int, default=100)
    args = parser.parse_args()
    box = args.box
    parameter_bound = Fraction(4 * box, 5)

    points_by_parameter = defaultdict(list)
    labels_by_x = defaultdict(set)
    labels_by_y = defaultdict(set)
    for x in range(-box, box + 1):
        for y in range(-box, box + 1):
            if x == y or (x == 0 and y == 0):
                continue
            parameter = Fraction(x * x + y * y, x - y)
            if parameter == 0 or parameter.denominator == 1:
                continue
            if abs(parameter) > parameter_bound:
                continue
            points_by_parameter[parameter].append((x, y))
            labels_by_x[x].add(parameter)
            labels_by_y[y].add(parameter)

    checked_pairs = set()
    for a, points in points_by_parameter.items():
        edge_counts = Counter()
        for x, y in points:
            edge_counts.update(labels_by_x[x] - {a})
            edge_counts.update(labels_by_y[y] - {a})
        for b, count in edge_counts.items():
            pair = tuple(sorted((a, b)))
            if count < 4 or pair in checked_pairs:
                continue
            checked_pairs.add(pair)
            vertices = [(a, p) for p in points_by_parameter[a]]
            vertices += [(b, p) for p in points_by_parameter[b]]
            edges = []
            for i, (label, p) in enumerate(vertices):
                for j in range(i + 1, len(vertices)):
                    other_label, other = vertices[j]
                    if label != other_label and (
                        p[0] == other[0] or p[1] == other[1]
                    ):
                        edges.append((i, j))
            if has_cycle(vertices, edges):
                print("cycle", a, b)
                for i, vertex in enumerate(vertices):
                    neighbours = [vertices[v] for u, v in edges if u == i]
                    neighbours += [vertices[u] for u, v in edges if v == i]
                    if neighbours:
                        print(vertex, neighbours)
                return

    print(
        "no_cycle",
        "box=", box,
        "complete_for_abs_parameter_le=", parameter_bound,
        "parameter_classes=", len(points_by_parameter),
        "candidate_pairs=", len(checked_pairs),
    )


if __name__ == "__main__":
    main()
