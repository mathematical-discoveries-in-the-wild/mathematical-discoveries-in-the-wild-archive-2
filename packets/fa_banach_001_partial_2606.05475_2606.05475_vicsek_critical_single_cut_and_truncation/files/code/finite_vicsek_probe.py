#!/usr/bin/env python3
"""Finite self-similar Vicsek-tree endpoint probe.

The level-zero graph is an X.  A new level is the union of five translated
copies (centre plus four diagonal corners), with adjacent copies sharing one
vertex.  This gives |V_n| = 5 |V_{n-1}| - 4 and radius 3^(n+1).

We use the lazy normalized Laplacian and edge-incidence norms.  On a bounded
degree tree the latter are uniformly equivalent to the paper's pointwise
gradient norm, so growth with level is the relevant signal.
"""

from __future__ import annotations

import argparse
import math
import numpy as np
import scipy.linalg


def vicsek(level: int):
    vertices = {(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)}
    edges = {
        tuple(sorted(((0, 0), (1, 1)))),
        tuple(sorted(((0, 0), (1, -1)))),
        tuple(sorted(((0, 0), (-1, 1)))),
        tuple(sorted(((0, 0), (-1, -1)))),
    }
    radius = 1
    for _ in range(level):
        shifts = [(0, 0), (2 * radius, 2 * radius), (2 * radius, -2 * radius),
                  (-2 * radius, 2 * radius), (-2 * radius, -2 * radius)]
        old_vertices, old_edges = vertices, edges
        vertices = set()
        edges = set()
        for sx, sy in shifts:
            vertices.update((x + sx, y + sy) for x, y in old_vertices)
            edges.update(tuple(sorted(((a[0] + sx, a[1] + sy),
                                       (b[0] + sx, b[1] + sy))))
                         for a, b in old_edges)
        radius *= 3
    verts = sorted(vertices)
    index = {v: i for i, v in enumerate(verts)}
    edge_ids = [(index[a], index[b]) for a, b in sorted(edges)]
    return verts, edge_ids, radius


def matrices(level: int):
    verts, edges, radius = vicsek(level)
    n, m = len(verts), len(edges)
    adjacency = np.zeros((n, n))
    incidence = np.zeros((m, n))
    for k, (i, j) in enumerate(edges):
        adjacency[i, j] = adjacency[j, i] = 1.0
        incidence[k, i] = 1.0
        incidence[k, j] = -1.0
    degree = adjacency.sum(axis=1)
    # Add a self-loop of weight degree: m=2 degree and P=(I+D^-1 A)/2.
    mass = 2.0 * degree
    delta = 0.5 * (np.eye(n) - adjacency / degree[:, None])
    sqrtm = np.sqrt(mass)
    sym = sqrtm[:, None] * delta / sqrtm[None, :]
    vals, vecs = scipy.linalg.eigh(sym)
    vals[np.abs(vals) < 1e-11] = 0.0

    root = verts.index((0, 0))
    primitive = np.zeros((n, m))
    neighbors = [[] for _ in range(n)]
    for k, (i, j) in enumerate(edges):
        neighbors[i].append((j, k, 1.0))
        neighbors[j].append((i, k, -1.0))
    parent = [-1] * n
    stack = [root]
    parent[root] = root
    while stack:
        i = stack.pop()
        for j, k, sign in neighbors[i]:
            if parent[j] != -1:
                continue
            parent[j] = i
            primitive[j] = primitive[i]
            # incidence row is f_i-f_j. To realize incidence*f=omega,
            # moving i->j changes f by -sign*omega_k.
            primitive[j, k] += -sign
            stack.append(j)
    assert all(x != -1 for x in parent)
    return vals, vecs, sqrtm, mass, incidence, primitive, radius


def frac_matrix(vals, vecs, sqrtm, gamma, inverse=False):
    powers = np.zeros_like(vals)
    good = vals > 1e-11
    powers[good] = vals[good] ** (-gamma if inverse else gamma)
    sympow = (vecs * powers[None, :]) @ vecs.T
    return sympow * sqrtm[None, :] / sqrtm[:, None]


def induced_p_norm(A, p, win, wout, starts=24, iters=500, seed=0):
    rng = np.random.default_rng(seed)
    best = 0.0
    bestx = None
    n = A.shape[1]
    for s in range(starts):
        x = rng.standard_normal(n)
        if s == 0:
            x[:] = 1.0
        x /= np.sum(win * np.abs(x) ** p) ** (1.0 / p)
        old = 0.0
        for _ in range(iters):
            y = A @ x
            ny = np.sum(wout * np.abs(y) ** p) ** (1.0 / p)
            u = wout * np.sign(y) * np.abs(y) ** (p - 1.0)
            z = A.T @ u
            xnew = np.sign(z) * (np.abs(z) / win) ** (1.0 / (p - 1.0))
            nx = np.sum(win * np.abs(xnew) ** p) ** (1.0 / p)
            if nx == 0:
                break
            x = xnew / nx
            if abs(ny - old) <= 1e-10 * max(1.0, ny):
                break
            old = ny
        y = A @ x
        ny = np.sum(wout * np.abs(y) ** p) ** (1.0 / p)
        if ny > best:
            best, bestx = ny, x.copy()
    return best, bestx


def run(levels, ps, offset, starts, iters):
    D = math.log(5.0) / math.log(3.0)
    beta = D + 1.0
    print(f"D={D:.10f} beta={beta:.10f}")
    for level in levels:
        vals, vecs, sqrtm, mass, B, T, radius = matrices(level)
        print(f"level={level} vertices={len(mass)} edges={len(B)} radius={radius}")
        for p in ps:
            critical = 1.0 / beta + (D - 1.0) / (beta * p)
            for gamma in (critical - offset, critical, critical + offset):
                inv = frac_matrix(vals, vecs, sqrtm, gamma, inverse=True)
                pos = frac_matrix(vals, vecs, sqrtm, gamma, inverse=False)
                riesz = B @ inv
                reverse = pos @ T
                nr, _ = induced_p_norm(riesz, p, mass, np.ones(B.shape[0]),
                                       starts=starts, iters=iters,
                                       seed=level * 100 + int(10 * p))
                nrr, _ = induced_p_norm(reverse, p, np.ones(B.shape[0]), mass,
                                        starts=starts, iters=iters,
                                        seed=10000 + level * 100 + int(10 * p))
                print(f"  p={p:g} gamma={gamma:.6f} delta={gamma-critical:+.3f} "
                      f"R={nr:.6g} RR={nrr:.6g}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", default="0,1,2,3")
    ap.add_argument("--ps", default="1.5,3,4")
    ap.add_argument("--offset", type=float, default=0.06)
    ap.add_argument("--starts", type=int, default=16)
    ap.add_argument("--iters", type=int, default=500)
    args = ap.parse_args()
    run([int(x) for x in args.levels.split(",")],
        [float(x) for x in args.ps.split(",")], args.offset,
        args.starts, args.iters)
