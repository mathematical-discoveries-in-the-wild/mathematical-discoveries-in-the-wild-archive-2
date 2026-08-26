"""Search for triangle-inequality violations for complex negative-moment gauges.

For K={x in C^2: max_j |<x,a_j>| <= 1} and q=-p in (1,2), polar
coordinates reduce the gauge (up to a body-independent constant) to

  N(u)=|u| [int_{CP^1} |<v,u/|u|>|^{-q} rho_K(v)^{4-q} dv]^{-1/q}.

We choose Hopf coordinates based at u, so |<v,u/|u|>|^2=t.  A
Gauss-Jacobi rule absorbs the singular weight t^{-q/2}; only a smooth
two-dimensional quadrature remains.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

import numpy as np
from scipy.special import roots_jacobi


@dataclass
class Gauge:
    rows: np.ndarray
    q: float
    nt: int
    nphi: int

    def __post_init__(self) -> None:
        # roots_jacobi uses (1-x)^alpha (1+x)^beta; t=(1+x)/2.
        x, w = roots_jacobi(self.nt, 0.0, -self.q / 2.0)
        self.t = (x + 1.0) / 2.0
        # The omitted power of two and 2*pi factor are independent of u.
        self.tw = w
        self.phases = np.exp(2j * np.pi * (np.arange(self.nphi) + 0.37) / self.nphi)

    def __call__(self, u: np.ndarray) -> float:
        unorm = np.linalg.norm(u)
        e = u / unorm
        # Hermitian-orthogonal unit vector.
        f = np.array([-np.conj(e[1]), np.conj(e[0])])
        v = (
            np.sqrt(self.t)[:, None, None] * e[None, None, :]
            + np.sqrt(1.0 - self.t)[:, None, None]
            * self.phases[None, :, None]
            * f[None, None, :]
        )
        h = np.max(np.abs(np.einsum("tpk,jk->tpj", v, np.conj(self.rows))), axis=2)
        integrand = h ** (-(4.0 - self.q))
        integral = np.dot(self.tw, np.mean(integrand, axis=1))
        return float(unorm * integral ** (-1.0 / self.q))


def random_unit(rng: np.random.Generator, count: int) -> np.ndarray:
    z = rng.normal(size=(count, 2)) + 1j * rng.normal(size=(count, 2))
    return z / np.linalg.norm(z, axis=1)[:, None]


def random_body(rng: np.random.Generator, facets: int) -> np.ndarray:
    rows = random_unit(rng, facets)
    # Random facet depths give non-Reinhardt, non-ellipsoidal examples.
    depths = np.exp(rng.uniform(-1.2, 1.2, size=facets))
    return rows / depths[:, None]


def as_complex(x: np.ndarray) -> np.ndarray:
    return np.array([x[0] + 1j * x[1], x[2] + 1j * x[3]])


def numerical_hessian(gauge: Gauge, u: np.ndarray, step: float) -> np.ndarray:
    x = np.array([u[0].real, u[0].imag, u[1].real, u[1].imag])
    basis = np.eye(4)
    hess = np.empty((4, 4))
    f0 = gauge(u)
    for i in range(4):
        hess[i, i] = (
            gauge(as_complex(x + step * basis[i]))
            - 2.0 * f0
            + gauge(as_complex(x - step * basis[i]))
        ) / step**2
        for j in range(i):
            hess[i, j] = hess[j, i] = (
                gauge(as_complex(x + step * basis[i] + step * basis[j]))
                - gauge(as_complex(x + step * basis[i] - step * basis[j]))
                - gauge(as_complex(x - step * basis[i] + step * basis[j]))
                + gauge(as_complex(x - step * basis[i] - step * basis[j]))
            ) / (4.0 * step**2)
    return hess


def scan_hessians(
    seed: int,
    bodies: int,
    directions: int,
    facets: int,
    q: float,
    nt: int,
    nphi: int,
    step: float,
) -> dict:
    rng = np.random.default_rng(seed)
    worst = {"min_eigenvalue": float("inf")}
    for body_idx in range(bodies):
        rows = random_body(rng, facets)
        gauge = Gauge(rows, q, nt, nphi)
        for direction_idx, u in enumerate(random_unit(rng, directions)):
            hess = numerical_hessian(gauge, u, step)
            values = np.linalg.eigvalsh(hess)
            # Homogeneity forces one zero eigenvalue.  Record the smallest
            # genuinely tangent eigenvalue, i.e. the second ordered value.
            tangent_min = float(values[1])
            if tangent_min < worst["min_eigenvalue"]:
                _, vectors = np.linalg.eigh(hess)
                worst = {
                    "min_eigenvalue": tangent_min,
                    "all_eigenvalues": values.tolist(),
                    "hessian": hess.tolist(),
                    "eigenvectors": vectors.tolist(),
                    "body_idx": body_idx,
                    "direction_idx": direction_idx,
                    "rows": [[float(z.real), float(z.imag)] for row in rows for z in row],
                    "u": [[float(z.real), float(z.imag)] for z in u],
                }
        print(json.dumps({"body": body_idx, "worst_tangent": worst["min_eigenvalue"]}), flush=True)
    return worst


def scan_chords(
    seed: int,
    bodies: int,
    directions: int,
    facets: int,
    q: float,
    nt: int,
    nphi: int,
) -> dict:
    rng = np.random.default_rng(seed)
    best = {"midpoint_gap": float("inf")}
    for body_idx in range(bodies):
        rows = random_body(rng, facets)
        gauge = Gauge(rows, q, nt, nphi)
        us = random_unit(rng, directions)
        raw = rng.normal(size=(directions, 4))
        ux = np.column_stack((us[:, 0].real, us[:, 0].imag, us[:, 1].real, us[:, 1].imag))
        raw -= np.sum(raw * ux, axis=1)[:, None] * ux
        raw /= np.linalg.norm(raw, axis=1)[:, None]
        hs = np.exp(rng.uniform(np.log(0.04), np.log(0.6), size=directions))
        for direction_idx, (u, wx, h) in enumerate(zip(us, raw, hs)):
            x = np.array([u[0].real, u[0].imag, u[1].real, u[1].imag])
            f0 = gauge(u)
            fplus = gauge(as_complex(x + h * wx))
            fminus = gauge(as_complex(x - h * wx))
            gap = fplus + fminus - 2.0 * f0
            scaled_gap = gap / h**2
            if scaled_gap < best.get("scaled_gap", float("inf")):
                best = {
                    "midpoint_gap": float(gap),
                    "scaled_gap": float(scaled_gap),
                    "midpoint_ratio": float(2.0 * f0 / (fplus + fminus)),
                    "h": float(h),
                    "body_idx": body_idx,
                    "direction_idx": direction_idx,
                    "rows": [[[float(z.real), float(z.imag)] for z in row] for row in rows],
                    "u": [[float(z.real), float(z.imag)] for z in u],
                    "w_real": wx.tolist(),
                }
        print(json.dumps({"body": body_idx, "best_scaled_gap": best["scaled_gap"]}), flush=True)
    return best


def replay_hessian(
    seed: int,
    body_index: int,
    direction_index: int,
    directions: int,
    facets: int,
    q: float,
    nt: int,
    nphi: int,
    step: float,
) -> dict:
    rng = np.random.default_rng(seed)
    for body_idx in range(body_index + 1):
        rows = random_body(rng, facets)
        us = random_unit(rng, directions)
    u = us[direction_index]
    gauge = Gauge(rows, q, nt, nphi)
    hess = numerical_hessian(gauge, u, step)
    values, vectors = np.linalg.eigh(hess)
    chords = []
    f0 = gauge(u)
    x = np.array([u[0].real, u[0].imag, u[1].real, u[1].imag])
    for eig_idx in range(4):
        direction = vectors[:, eig_idx]
        for scale in (0.5, 1.0, 2.0, 4.0, 8.0):
            h = step * scale
            fplus = gauge(as_complex(x + h * direction))
            fminus = gauge(as_complex(x - h * direction))
            chords.append(
                {
                    "eigenvector": eig_idx,
                    "h": h,
                    "midpoint_gap": fplus + fminus - 2.0 * f0,
                    "midpoint_ratio": 2.0 * f0 / (fplus + fminus),
                }
            )
    return {
        "all_eigenvalues": values.tolist(),
        "hessian": hess.tolist(),
        "eigenvectors": vectors.tolist(),
        "chords": chords,
        "rows": [[[float(z.real), float(z.imag)] for z in row] for row in rows],
        "u": [[float(z.real), float(z.imag)] for z in u],
    }


def scan(seed: int, bodies: int, pairs: int, facets: int, q: float, nt: int, nphi: int) -> dict:
    rng = np.random.default_rng(seed)
    best = {"ratio": 0.0}
    for body_idx in range(bodies):
        rows = random_body(rng, facets)
        gauge = Gauge(rows, q, nt, nphi)
        us = random_unit(rng, pairs)
        vs = random_unit(rng, pairs)
        # Vary relative magnitudes as well as complex directions.
        us *= np.exp(rng.uniform(-1.5, 1.5, size=pairs))[:, None]
        vs *= np.exp(rng.uniform(-1.5, 1.5, size=pairs))[:, None]
        for pair_idx, (u, v) in enumerate(zip(us, vs)):
            nu = gauge(u)
            nv = gauge(v)
            nw = gauge(u + v)
            ratio = nw / (nu + nv)
            if ratio > best["ratio"]:
                best = {
                    "ratio": ratio,
                    "body_idx": body_idx,
                    "pair_idx": pair_idx,
                    "rows": [[float(z.real), float(z.imag)] for row in rows for z in row],
                    "u": [[float(z.real), float(z.imag)] for z in u],
                    "v": [[float(z.real), float(z.imag)] for z in v],
                    "parts": [nu, nv, nw],
                }
        print(json.dumps({"body": body_idx, "best_ratio": best["ratio"]}), flush=True)
    return best


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=230400794)
    parser.add_argument("--bodies", type=int, default=20)
    parser.add_argument("--pairs", type=int, default=100)
    parser.add_argument("--facets", type=int, default=8)
    parser.add_argument("--q", type=float, default=1.5)
    parser.add_argument("--nt", type=int, default=40)
    parser.add_argument("--nphi", type=int, default=128)
    parser.add_argument("--hessian-directions", type=int, default=0)
    parser.add_argument("--chord-directions", type=int, default=0)
    parser.add_argument("--step", type=float, default=0.002)
    parser.add_argument("--replay-body", type=int)
    parser.add_argument("--replay-direction", type=int)
    args = parser.parse_args()
    if args.replay_body is not None:
        answer = replay_hessian(
            args.seed,
            args.replay_body,
            args.replay_direction,
            args.hessian_directions,
            args.facets,
            args.q,
            args.nt,
            args.nphi,
            args.step,
        )
    elif args.chord_directions:
        answer = scan_chords(
            args.seed,
            args.bodies,
            args.chord_directions,
            args.facets,
            args.q,
            args.nt,
            args.nphi,
        )
    elif args.hessian_directions:
        answer = scan_hessians(
            args.seed,
            args.bodies,
            args.hessian_directions,
            args.facets,
            args.q,
            args.nt,
            args.nphi,
            args.step,
        )
    else:
        answer = scan(args.seed, args.bodies, args.pairs, args.facets, args.q, args.nt, args.nphi)
    print("BEST " + json.dumps(answer))
