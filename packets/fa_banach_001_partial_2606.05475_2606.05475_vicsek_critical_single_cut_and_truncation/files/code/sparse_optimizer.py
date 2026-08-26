#!/usr/bin/env python3
"""Sparse nonlinear power iteration for critical Vicsek reverse norms."""

import argparse
import math

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

from finite_vicsek_probe import vicsek


class TreePrimitive:
    def __init__(self, verts, edges):
        neighbors = [[] for _ in verts]
        for k, (i, j) in enumerate(edges):
            neighbors[i].append((j, k, 1.0))
            neighbors[j].append((i, k, -1.0))
        root = verts.index((0, 0))
        self.parent = np.full(len(verts), -1, dtype=int)
        self.parent[root] = root
        self.parent_edge = np.full(len(verts), -1, dtype=int)
        self.coeff = np.zeros(len(verts))
        self.order = [root]
        for i in self.order:
            for j, k, sign in neighbors[i]:
                if self.parent[j] >= 0:
                    continue
                self.parent[j] = i
                self.parent_edge[j] = k
                self.coeff[j] = -sign
                self.order.append(j)

    def apply(self, omega):
        value = np.zeros(len(self.parent))
        for j in self.order[1:]:
            value[j] = (value[self.parent[j]] +
                        self.coeff[j] * omega[self.parent_edge[j]])
        return value

    def adjoint(self, value):
        subtotal = value.copy()
        result = np.zeros(len(value) - 1)
        for j in reversed(self.order[1:]):
            result[self.parent_edge[j]] = self.coeff[j] * subtotal[j]
            subtotal[self.parent[j]] += subtotal[j]
        return result


class FractionalPower:
    def __init__(self, sym, null, gamma, lambda_lower, step, margin):
        self.null = null / np.linalg.norm(null)
        low = math.log(lambda_lower) - margin / gamma
        high = margin / (1.0 - gamma)
        self.grid = np.arange(low, high + step / 2.0, step)
        self.weights = (step * math.sin(math.pi * gamma) / math.pi *
                        np.exp(gamma * self.grid))
        identity = sp.eye(sym.shape[0], format="csc")
        sym = sym.tocsc()
        self.ts = np.exp(self.grid)
        self.solvers = [spla.factorized(sym + t * identity) for t in self.ts]

    def apply(self, value):
        value = value - self.null * np.dot(self.null, value)
        result = np.zeros_like(value)
        for weight, t, solve in zip(self.weights, self.ts, self.solvers):
            result += weight * (value - t * solve(value))
        return result


def setup(level, gamma, step, margin):
    verts, edges, _radius = vicsek(level)
    rows, cols = [], []
    for i, j in edges:
        rows.extend((i, j))
        cols.extend((j, i))
    adjacency = sp.csr_matrix((np.ones(len(rows)), (rows, cols)),
                              shape=(len(verts), len(verts)))
    degree = np.asarray(adjacency.sum(axis=1)).ravel()
    mass = 2.0 * degree
    invsqrt = 1.0 / np.sqrt(degree)
    sym = 0.5 * (sp.eye(len(verts), format="csr") -
                 sp.diags(invsqrt) @ adjacency @ sp.diags(invsqrt))
    power = FractionalPower(sym, np.sqrt(mass), gamma,
                            15.0 ** (-(level + 2)), step, margin)
    return verts, edges, mass, TreePrimitive(verts, edges), power


def optimize(level, p, starts, iters, step, margin, seed, save):
    D = math.log(5.0) / math.log(3.0)
    beta = D + 1.0
    gamma = 1.0 / beta + (D - 1.0) / (beta * p)
    verts, edges, mass, primitive, power = setup(level, gamma, step, margin)
    sqrtmass = np.sqrt(mass)

    def apply(omega):
        f = primitive.apply(omega)
        return power.apply(sqrtmass * f) / sqrtmass

    def adjoint(value):
        transformed = sqrtmass * power.apply(value / sqrtmass)
        return primitive.adjoint(transformed)

    rng = np.random.default_rng(seed)
    best = 0.0
    best_omega = None
    for start in range(starts):
        omega = rng.standard_normal(len(edges))
        if start == 0:
            omega[:] = 1.0
        omega /= np.sum(np.abs(omega) ** p) ** (1.0 / p)
        old = 0.0
        for iteration in range(iters):
            output = apply(omega)
            norm = np.sum(mass * np.abs(output) ** p) ** (1.0 / p)
            dual = mass * np.sign(output) * np.abs(output) ** (p - 1.0)
            gradient = adjoint(dual)
            update = np.sign(gradient) * np.abs(gradient) ** (1.0 / (p - 1.0))
            update /= np.sum(np.abs(update) ** p) ** (1.0 / p)
            omega = update
            if abs(norm - old) <= 1e-9 * max(1.0, norm):
                break
            old = norm
        if norm > best:
            best = norm
            best_omega = omega.copy()
        print(f"start={start} iterations={iteration + 1} norm={norm:.10g}")
    print(f"level={level} vertices={len(verts)} p={p:g} gamma={gamma:.10f} "
          f"best={best:.10g} quadrature_points={len(power.grid)}")
    if save:
        np.savez_compressed(save, omega=best_omega, p=p, gamma=gamma,
                            level=level, norm=best)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", type=int, default=5)
    ap.add_argument("--p", type=float, default=4.0)
    ap.add_argument("--starts", type=int, default=4)
    ap.add_argument("--iters", type=int, default=120)
    ap.add_argument("--step", type=float, default=0.8)
    ap.add_argument("--margin", type=float, default=10.0)
    ap.add_argument("--seed", type=int, default=731)
    ap.add_argument("--save")
    args = ap.parse_args()
    optimize(args.level, args.p, args.starts, args.iters, args.step,
             args.margin, args.seed, args.save)
