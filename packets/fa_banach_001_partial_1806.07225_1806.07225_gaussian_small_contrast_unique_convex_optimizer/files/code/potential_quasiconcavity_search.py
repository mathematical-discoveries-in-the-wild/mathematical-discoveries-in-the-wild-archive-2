"""Search for non-quasiconcave container potentials on convex polygons.

For a radial kernel f, the low-contrast limit of the density problem is the
bathtub problem for V(x)=int_Omega f(|x-y|)dy.  A robustly nonconvex
superlevel set of V would therefore give an asymptotic route to disproving
the B_+ convexity conjecture.
"""

from __future__ import annotations

import numpy as np


def polygon_points(n: int, kind: str) -> tuple[np.ndarray, float]:
    if kind == "triangle_6_1":
        x = np.linspace(0, 6, 3 * n + 1)
        y = np.linspace(0, 1, n + 1)
        xx, yy = np.meshgrid(x, y)
        mask = xx / 6 + yy <= 1 + 1e-12
        cell = (6 / (3 * n)) * (1 / n)
    elif kind == "trapezoid":
        x = np.linspace(0, 6, 3 * n + 1)
        y = np.linspace(-1, 1, n + 1)
        xx, yy = np.meshgrid(x, y)
        # Vertices (0,-1),(0,1),(6,0.25),(6,-0.25).
        halfheight = 1 - 0.75 * xx / 6
        mask = np.abs(yy) <= halfheight + 1e-12
        cell = (6 / (3 * n)) * (2 / n)
    elif kind == "kite":
        x = np.linspace(-3, 3, 3 * n + 1)
        y = np.linspace(-1, 1, n + 1)
        xx, yy = np.meshgrid(x, y)
        # Convex kite: (-3,0),(0,1),(3,0),(0,-0.3).
        upper = 1 - np.abs(xx) / 3
        lower = -0.3 + 0.1 * np.abs(xx)
        mask = (yy <= upper + 1e-12) & (yy >= lower - 1e-12)
        cell = (6 / (3 * n)) * (2 / n)
    else:
        raise ValueError(kind)
    return np.column_stack((xx[mask], yy[mask])), cell


def potential(eval_points: np.ndarray, source: np.ndarray, cell: float, sigma: float) -> np.ndarray:
    out = np.empty(len(eval_points))
    for start in range(0, len(eval_points), 256):
        q = eval_points[start : start + 256]
        dist = np.linalg.norm(q[:, None, :] - source[None, :, :], axis=2)
        out[start : start + len(q)] = cell * np.exp(-dist / sigma).sum(axis=1)
    return out


def main() -> None:
    rng = np.random.default_rng(7132026)
    sigmas = (0.2, 0.35, 0.6, 1.0, 2.0, 5.0, 12.0)
    for kind in ("triangle_6_1", "trapezoid", "kite"):
        source, cell = polygon_points(40, kind)
        values = {s: potential(source, source, cell, s) for s in sigmas}
        best = None
        for s1 in sigmas[:-1]:
            for s2 in sigmas:
                if s2 <= s1:
                    continue
                for weight in np.linspace(0.02, 0.98, 13):
                    v = weight * values[s1] + (1 - weight) * values[s2]
                    for quantile in (0.55, 0.65, 0.75, 0.85, 0.92):
                        cutoff = np.quantile(v, quantile)
                        eligible = np.flatnonzero(v >= cutoff)
                        if len(eligible) < 2:
                            continue
                        pairs = rng.choice(eligible, size=(100, 2), replace=True)
                        mids = (source[pairs[:, 0]] + source[pairs[:, 1]]) / 2
                        vmid = weight * potential(mids, source, cell, s1) + (1 - weight) * potential(mids, source, cell, s2)
                        vend = np.minimum(v[pairs[:, 0]], v[pairs[:, 1]])
                        idx = int(np.argmax(vend - vmid))
                        gap = float(vend[idx] - vmid[idx])
                        scale = float(v.max() - v.min())
                        relative = gap / scale if scale > 0 else 0.0
                        record = (relative, gap, kind, s1, s2, float(weight), quantile, source[pairs[idx, 0]], source[pairs[idx, 1]], mids[idx], float(vend[idx]), float(vmid[idx]))
                        if best is None or record[0] > best[0]:
                            best = record
        print(best)


if __name__ == "__main__":
    main()
