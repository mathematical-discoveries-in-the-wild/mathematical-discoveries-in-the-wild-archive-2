#!/usr/bin/env python3
"""Numerical search for counterexamples to arXiv:2510.16846, Conjecture 3.1.

The variables are arbitrary complex n-by-n matrices.  We maximize

    ||sum A_k||_p / ||sum |A_k|||_p

with Adam and compare against the conjectured closed-form constant.  The
script is a heuristic only; any apparent violation must be exported and
verified with certified arithmetic before promotion.
"""

from __future__ import annotations

import argparse
import math

import scipy.optimize
import torch


torch.set_default_dtype(torch.float64)


def conjectured_constant(p: float, m: int) -> tuple[float, float]:
    root = scipy.optimize.brentq(
        lambda x: x**p - 2.0 * x - (m - 1.0), 1.0, 1.0e8
    )
    value = math.sqrt(root * (root + m - 1.0)) / (
        root**p + m - 1.0
    ) ** (1.0 / p)
    return value, root


def matrix_abs(a: torch.Tensor) -> torch.Tensor:
    _, singular, vh = torch.linalg.svd(a, full_matrices=False)
    return vh.mH @ torch.diag_embed(singular.to(a.dtype)) @ vh


def schatten_p(a: torch.Tensor, p: float) -> torch.Tensor:
    singular = torch.linalg.svdvals(a)
    return singular.pow(p).sum().pow(1.0 / p)


def ratio(raw: torch.Tensor, p: float) -> torch.Tensor:
    mats = torch.complex(raw[..., 0], raw[..., 1])
    numerator = schatten_p(mats.sum(dim=0), p)
    denominator = schatten_p(matrix_abs(mats).sum(dim=0), p)
    return numerator / denominator


def optimize_once(
    p: float, m: int, n: int, steps: int, seed: int, learning_rate: float
) -> tuple[float, torch.Tensor]:
    generator = torch.Generator().manual_seed(seed)
    raw = torch.randn(m, n, n, 2, generator=generator, requires_grad=True)
    optimizer = torch.optim.Adam([raw], lr=learning_rate)
    best_value = -math.inf
    best_raw = raw.detach().clone()
    for step in range(steps):
        optimizer.zero_grad()
        value = ratio(raw, p)
        (-torch.log(value)).backward()
        optimizer.step()
        with torch.no_grad():
            raw /= torch.linalg.vector_norm(raw)
            current = float(ratio(raw, p))
            if current > best_value:
                best_value = current
                best_raw = raw.detach().clone()
        if step and step % 500 == 0:
            for group in optimizer.param_groups:
                group["lr"] *= 0.65
    return best_value, best_raw


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=float, required=True)
    parser.add_argument("--m", type=int, required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--restarts", type=int, default=20)
    parser.add_argument("--steps", type=int, default=1500)
    parser.add_argument("--learning-rate", type=float, default=0.03)
    parser.add_argument("--seed", type=int, default=251016846)
    parser.add_argument("--save", type=str)
    args = parser.parse_args()

    predicted, root = conjectured_constant(args.p, args.m)
    overall_value = -math.inf
    overall_raw = None
    for restart in range(args.restarts):
        value, raw = optimize_once(
            args.p,
            args.m,
            args.n,
            args.steps,
            args.seed + restart,
            args.learning_rate,
        )
        if value > overall_value:
            overall_value = value
            overall_raw = raw
        print(
            f"restart={restart:03d} best={value:.12g} "
            f"predicted={predicted:.12g} gap={value-predicted:+.4e}",
            flush=True,
        )
    print(
        f"FINAL p={args.p:g} m={args.m} n={args.n} root={root:.12g} "
        f"best={overall_value:.12g} predicted={predicted:.12g} "
        f"gap={overall_value-predicted:+.6e} ratio={overall_value/predicted:.12g}"
    )
    if args.save and overall_raw is not None:
        torch.save(
            {
                "p": args.p,
                "m": args.m,
                "n": args.n,
                "predicted": predicted,
                "best": overall_value,
                "raw": overall_raw,
            },
            args.save,
        )


if __name__ == "__main__":
    main()
