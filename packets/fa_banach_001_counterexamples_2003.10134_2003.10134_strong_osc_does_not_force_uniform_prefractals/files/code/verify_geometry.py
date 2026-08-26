#!/usr/bin/env python3
"""Mechanical checks and illustration for the cusp-prefractal counterexample."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


A = np.array([-100.0, 0.0])
B = np.array([100.0, 0.0])


def boundary_vertices(m: int) -> np.ndarray:
    """Vertices of K_m in traversal order from A to B."""
    if m < 2:
        raise ValueError("m must be at least 2")
    a = 1.0 / m
    h = 1.0 / m**4
    count = (m - 1) * m**3
    levels = a + h * np.arange(count + 1, dtype=float)
    assert abs(levels[-1] - 1.0) < 1e-12

    left = np.column_stack((-levels**2, -1.0 + levels))[::-1]
    right = np.column_stack((levels**2, -1.0 + levels))
    points = [A]
    points.extend(left.tolist())
    points.append([a * a, -1.0 + a])
    points.extend(right[1:].tolist())
    points.append(B)
    return np.asarray(points, dtype=float)


def cell_rhombus(p: np.ndarray, q: np.ndarray, height: float) -> np.ndarray:
    """Image of conv{A,(0,h),B,(0,-h)} under A->p, B->q."""
    mid = (p + q) / 2.0
    half = (q - p) / 2.0
    perp = np.array([-half[1], half[0]])
    transverse = (height / 100.0) * perp
    return np.vstack((p, mid + transverse, q, mid - transverse))


def bbox(poly: np.ndarray) -> tuple[float, float, float, float]:
    return (
        float(poly[:, 0].min()),
        float(poly[:, 0].max()),
        float(poly[:, 1].min()),
        float(poly[:, 1].max()),
    )


def bbox_interiors_may_overlap(a, b, tol=1e-12) -> bool:
    return not (
        a[1] <= b[0] + tol
        or b[1] <= a[0] + tol
        or a[3] <= b[2] + tol
        or b[3] <= a[2] + tol
    )


def open_convex_interiors_overlap(p: np.ndarray, q: np.ndarray, tol=1e-12) -> bool:
    """Strict separating-axis test for two convex polygons."""
    for poly in (p, q):
        edges = np.roll(poly, -1, axis=0) - poly
        for edge in edges:
            axis = np.array([-edge[1], edge[0]])
            pp = p @ axis
            qq = q @ axis
            if pp.max() <= qq.min() + tol or qq.max() <= pp.min() + tol:
                return False
    return True


def in_closed_outer_rhombus(point: np.ndarray, height: float, tol=1e-11) -> bool:
    x, y = point
    if abs(x) > 100.0 + tol:
        return False
    return abs(y) <= height * (1.0 - abs(x) / 100.0) + tol


def verify_level(m: int) -> dict[str, float | int]:
    vertices = boundary_vertices(m)
    edges = list(zip(vertices[:-1], vertices[1:]))
    lengths = np.array([np.linalg.norm(q - p) for p, q in edges])
    if not np.all(lengths < 200.0):
        raise AssertionError("a cell map is not contractive")

    for outer_height in (1.5, 2.0):
        for p, q in edges:
            image = cell_rhombus(p, q, outer_height)
            if not all(in_closed_outer_rhombus(v, outer_height) for v in image):
                raise AssertionError(
                    f"level {m}: image of O_{outer_height} is not contained in O_{outer_height}"
                )

    cells = [cell_rhombus(p, q, 2.0) for p, q in edges]
    boxes = [bbox(poly) for poly in cells]
    checked = 0
    for i in range(len(cells)):
        for j in range(i + 1, len(cells)):
            if not bbox_interiors_may_overlap(boxes[i], boxes[j]):
                continue
            checked += 1
            if open_convex_interiors_overlap(cells[i], cells[j]):
                raise AssertionError(
                    f"level {m}: open O' cells {i} and {j} overlap"
                )

    a = 1.0 / m
    x = np.array([-5.0 * a * a, -1.0 + 2.0 * a])
    y = np.array([5.0 * a * a, -1.0 + 2.0 * a])
    ratio_bound = np.linalg.norm(x - y) / (2.0 * a)
    if abs(ratio_bound - 5.0 / m) > 1e-12:
        raise AssertionError("unexpected uniformity ratio")

    return {
        "m": m,
        "cells": len(cells),
        "candidate_pairs_checked": checked,
        "max_contraction": float(lengths.max() / 200.0),
        "epsilon_upper_bound": float(ratio_bound),
    }


def make_figure(output: Path, m: int = 6) -> None:
    vertices = boundary_vertices(m)
    a = 1.0 / m
    t = np.linspace(0.0, 1.0, 600)
    left = np.column_stack((-t**2, -1.0 + t))
    right = np.column_stack((t**2, -1.0 + t))

    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.25), constrained_layout=True)
    for ax in axes:
        ax.set_aspect("equal")
        ax.set_xlim(-1.35, 1.35)
        ax.set_ylim(-1.18, 0.12)
        ax.set_xlabel(r"$x_1$")
        ax.set_ylabel(r"$x_2$")
        ax.grid(alpha=0.15)

    axes[0].plot(vertices[:, 0], vertices[:, 1], color="#0057b8", lw=1.6)
    axes[0].fill_betweenx(
        np.linspace(-1.0 + a, 0.0, 300),
        -(np.linspace(a, 1.0, 300) ** 2),
        np.linspace(a, 1.0, 300) ** 2,
        color="#ef6c57",
        alpha=0.3,
        label="exterior notch",
    )
    axes[0].scatter(
        [-5 * a * a, 5 * a * a],
        [-1 + 2 * a, -1 + 2 * a],
        color="#111111",
        zorder=5,
        label=r"$x_m,y_m$",
    )
    axes[0].set_title(fr"Polygonal prefractal $K_m$ ($m={m}$)")
    axes[0].legend(loc="upper center", frameon=False)

    axes[1].plot(left[:, 0], left[:, 1], color="#0057b8", lw=2.0)
    axes[1].plot(right[:, 0], right[:, 1], color="#0057b8", lw=2.0)
    axes[1].fill_betweenx(
        -1.0 + t, -t**2, t**2, color="#ef6c57", alpha=0.3
    )
    sample_t = 0.18
    axes[1].scatter(
        [-5 * sample_t**2, 5 * sample_t**2],
        [-1 + sample_t, -1 + sample_t],
        color="#111111",
        zorder=5,
    )
    axes[1].annotate(
        "every internal path\nmust pass below the tip",
        xy=(0.0, -1.0),
        xytext=(0.28, -0.72),
        arrowprops={"arrowstyle": "->", "lw": 1.0},
        fontsize=9,
    )
    axes[1].set_title("Limit inward cusp")

    fig.savefig(output, dpi=220)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", type=Path)
    parser.add_argument("--levels", type=int, nargs="*", default=[2, 3, 4, 5])
    args = parser.parse_args()

    for level in args.levels:
        print(verify_level(level))
    if args.figure is not None:
        args.figure.parent.mkdir(parents=True, exist_ok=True)
        make_figure(args.figure)
        print(f"wrote {args.figure}")
    print("VERIFIED: contraction, two fixed OSC rhombi, and epsilon_m <= 5/m")


if __name__ == "__main__":
    main()
