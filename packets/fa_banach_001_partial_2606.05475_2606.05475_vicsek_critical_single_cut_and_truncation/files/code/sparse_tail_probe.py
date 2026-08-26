#!/usr/bin/env python3
"""Extend a fixed finite critical witness into larger Vicsek approximants.

The fractional power is evaluated by the Balakrishnan integral on the
symmetric normalized Laplacian.  This avoids dense diagonalization beyond
level four and tests whether norm growth is a genuine tail effect.
"""

import argparse
import math

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from finite_vicsek_probe import frac_matrix, induced_p_norm, matrices, vicsek


def sparse_graph(level):
    verts, edges, _radius = vicsek(level)
    n = len(verts)
    rows, cols = [], []
    for i, j in edges:
        rows.extend((i, j))
        cols.extend((j, i))
    adjacency = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
    degree = np.asarray(adjacency.sum(axis=1)).ravel()
    mass = 2.0 * degree
    invsqrt = 1.0 / np.sqrt(degree)
    sym = 0.5 * (sp.eye(n, format="csr") -
                 sp.diags(invsqrt) @ adjacency @ sp.diags(invsqrt))
    return verts, edges, mass, sym


def primitive(verts, edges, omega):
    neighbors = [[] for _ in verts]
    for k, (i, j) in enumerate(edges):
        neighbors[i].append((j, k, 1.0))
        neighbors[j].append((i, k, -1.0))
    root = verts.index((0, 0))
    values = np.zeros(len(verts))
    parent = np.full(len(verts), -1, dtype=int)
    parent[root] = root
    stack = [root]
    while stack:
        i = stack.pop()
        for j, k, sign in neighbors[i]:
            if parent[j] >= 0:
                continue
            parent[j] = i
            values[j] = values[i] - sign * omega[k]
            stack.append(j)
    return values


def fractional_action(sym, vector, null, gamma, step=0.35, margin=16.0,
                      lambda_lower=1e-10):
    # Remove the null eigenvector component explicitly.  For the normalized
    # Laplacian this vector is proportional to sqrt(degree).
    null = null / np.linalg.norm(null)
    vector = vector - null * np.dot(null, vector)
    low = math.log(lambda_lower) - margin / gamma
    high = margin / (1.0 - gamma)
    grid = np.arange(low, high + step / 2.0, step)
    result = np.zeros_like(vector)
    identity = sp.eye(sym.shape[0], format="csc")
    sym_csc = sym.tocsc()
    for s in grid:
        t = math.exp(s)
        solved = spla.spsolve(sym_csc + t * identity, vector)
        result += math.exp(gamma * s) * (vector - t * solved)
    result *= step * math.sin(math.pi * gamma) / math.pi
    return result


def keyed_edges(level):
    vertices = {(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    base_edges = sorted({
        tuple(sorted(((0, 0), (1, 1)))),
        tuple(sorted(((0, 0), (1, -1)))),
        tuple(sorted(((0, 0), (-1, 1)))),
        tuple(sorted(((0, 0), (-1, -1)))),
    })
    keys = {edge: ((), label) for label, edge in enumerate(base_edges)}
    radius = 1
    for _ in range(level):
        shifts = [(0, 0), (2 * radius, 2 * radius),
                  (2 * radius, -2 * radius), (-2 * radius, 2 * radius),
                  (-2 * radius, -2 * radius)]
        old_vertices, old_keys = vertices, keys
        vertices, keys = set(), {}
        for digit, (sx, sy) in enumerate(shifts):
            vertices.update((x + sx, y + sy) for x, y in old_vertices)
            for (a, b), (address, label) in old_keys.items():
                edge = tuple(sorted(((a[0] + sx, a[1] + sy),
                                     (b[0] + sx, b[1] + sy))))
                keys[edge] = ((digit,) + address, label)
        radius *= 3
    return keys


def main(base_level, levels, p, starts, iters, step, margin, load, prefix):
    D = math.log(5.0) / math.log(3.0)
    beta = D + 1.0
    gamma = 1.0 / beta + (D - 1.0) / (beta * p)
    base_verts, base_edges, _ = vicsek(base_level)
    if load:
        saved = np.load(load)
        base_omega = saved["omega"]
        if len(base_omega) != len(base_edges):
            raise ValueError("saved extremizer has the wrong edge count")
    else:
        vals, vecs, sqrtm, mass0, _B, T, _radius = matrices(base_level)
        reverse = frac_matrix(vals, vecs, sqrtm, gamma) @ T
        _norm, base_omega = induced_p_norm(
            reverse, p, np.ones(len(base_edges)), mass0,
            starts=starts, iters=iters, seed=731)
    base_keys = keyed_edges(base_level)
    base_map = {}
    for (i, j), value in zip(base_edges, base_omega):
        edge = tuple(sorted((base_verts[i], base_verts[j])))
        base_map[base_keys[edge]] = value
    for level in levels:
        verts, edges, mass, sym = sparse_graph(level)
        target_keys = keyed_edges(level)
        use_prefix = ([0] * (level - base_level)) if not prefix else prefix
        if len(use_prefix) != level - base_level:
            raise ValueError("prefix length must equal level minus base level")
        omega = np.zeros(len(edges))
        for k, (i, j) in enumerate(edges):
            edge = tuple(sorted((verts[i], verts[j])))
            address, label = target_keys[edge]
            if tuple(address[:len(use_prefix)]) == tuple(use_prefix):
                suffix = address[len(use_prefix):]
                omega[k] = base_map.get((suffix, label), 0.0)
        f = primitive(verts, edges, omega)
        symmetric_f = np.sqrt(mass) * f
        lower = 15.0 ** (-(level + 2))
        symmetric_out = fractional_action(sym, symmetric_f, np.sqrt(mass),
                                            gamma, step, margin, lower)
        out = symmetric_out / np.sqrt(mass)
        inorm = np.sum(np.abs(omega) ** p) ** (1.0 / p)
        onorm = np.sum(mass * np.abs(out) ** p) ** (1.0 / p)
        print(f"base={base_level} level={level} n={len(verts)} p={p:g} "
              f"gamma={gamma:.10f} input={inorm:.10g} output={onorm:.10g} "
              f"ratio={onorm/inorm:.10g}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-level", type=int, default=4)
    ap.add_argument("--levels", default="4,5")
    ap.add_argument("--p", type=float, default=4.0)
    ap.add_argument("--starts", type=int, default=12)
    ap.add_argument("--iters", type=int, default=500)
    ap.add_argument("--step", type=float, default=0.35)
    ap.add_argument("--margin", type=float, default=16.0)
    ap.add_argument("--load")
    ap.add_argument("--prefix", default="",
                    help="outer cell digits, e.g. 3,4; empty means central embedding")
    args = ap.parse_args()
    prefix = [] if not args.prefix else [int(x) for x in args.prefix.split(",")]
    main(args.base_level, [int(x) for x in args.levels.split(",")], args.p,
         args.starts, args.iters, args.step, args.margin, args.load, prefix)
