#!/usr/bin/env python3
"""Decompose a critical reverse extremizer over the Vicsek cell tree."""

import argparse
import collections
import math

import numpy as np

from finite_vicsek_probe import frac_matrix, induced_p_norm, matrices, vicsek


def addressed_edges(level):
    vertices = {(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    edge_address = {
        tuple(sorted(((0, 0), (1, 1)))): (),
        tuple(sorted(((0, 0), (1, -1)))): (),
        tuple(sorted(((0, 0), (-1, 1)))): (),
        tuple(sorted(((0, 0), (-1, -1)))): (),
    }
    radius = 1
    for _ in range(level):
        shifts = [(0, 0), (2 * radius, 2 * radius),
                  (2 * radius, -2 * radius), (-2 * radius, 2 * radius),
                  (-2 * radius, -2 * radius)]
        old_vertices, old = vertices, edge_address
        vertices = set()
        edge_address = {}
        for digit, (sx, sy) in enumerate(shifts):
            vertices.update((x + sx, y + sy) for x, y in old_vertices)
            for (a, b), address in old.items():
                shifted = tuple(sorted(((a[0] + sx, a[1] + sy),
                                        (b[0] + sx, b[1] + sy))))
                edge_address[shifted] = (digit,) + address
        radius *= 3
    return edge_address


def main(level, p, starts, iters):
    D = math.log(5.0) / math.log(3.0)
    beta = D + 1.0
    gamma = 1.0 / beta + (D - 1.0) / (beta * p)
    vals, vecs, sqrtm, mass, _B, T, _radius = matrices(level)
    verts, edges, _ = vicsek(level)
    reverse = frac_matrix(vals, vecs, sqrtm, gamma) @ T
    norm, omega = induced_p_norm(reverse, p, np.ones(len(edges)), mass,
                                 starts=starts, iters=iters, seed=731)
    output = reverse @ omega
    edge_keys = [tuple(sorted((verts[i], verts[j]))) for i, j in edges]
    addresses = addressed_edges(level)
    print(f"level={level} p={p:g} gamma={gamma:.10f} norm={norm:.10g}")
    for depth in range(1, level + 1):
        buckets = collections.defaultdict(float)
        for value, edge in zip(omega, edge_keys):
            buckets[addresses[edge][:depth]] += abs(value) ** p
        ranked = sorted(buckets.items(), key=lambda item: item[1], reverse=True)
        print(f"input depth={depth}",
              [(address, round(value, 8)) for address, value in ranked[:12]])
    # Assign a vertex to every top-level cell containing it, splitting shared
    # junction mass equally. This is only diagnostic and preserves total mass.
    top_cells = collections.defaultdict(set)
    for edge, address in addresses.items():
        top_cells[address[:1]].update(edge)
    for depth in range(1, level + 1):
        cells = collections.defaultdict(set)
        for edge, address in addresses.items():
            cells[address[:depth]].update(edge)
        membership = collections.Counter(v for cell in cells.values() for v in cell)
        buckets = []
        index = {v: i for i, v in enumerate(verts)}
        for address, cell in cells.items():
            value = sum(mass[index[v]] * abs(output[index[v]]) ** p /
                        membership[v] for v in cell)
            buckets.append((address, value))
        buckets.sort(key=lambda item: item[1], reverse=True)
        print(f"output depth={depth}",
              [(address, round(value, 8)) for address, value in buckets[:12]])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", type=int, default=4)
    ap.add_argument("--p", type=float, default=4.0)
    ap.add_argument("--starts", type=int, default=12)
    ap.add_argument("--iters", type=int, default=500)
    args = ap.parse_args()
    main(args.level, args.p, args.starts, args.iters)
