#!/usr/bin/env python3
"""Monte Carlo sanity check for the finite-coordinate random-line witness.

This script is not part of the proof.  It estimates
L_n / (sqrt(n) * a**(n+1)) for the exact semiaxes sigma_j=a**j.
"""

from __future__ import annotations

import argparse
import math

import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=float, default=0.5)
    parser.add_argument("--samples", type=int, default=20_000)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--dimensions", type=int, nargs="+", default=[10, 20, 50, 100, 200])
    args = parser.parse_args()
    if not 0.0 < args.a < 1.0:
        raise SystemExit("--a must lie strictly between 0 and 1")

    rng = np.random.default_rng(args.seed)
    for n in args.dimensions:
        g = rng.standard_normal((args.samples, n + 1))
        weights = args.a ** (2.0 * np.arange(n, -1, -1))
        q = np.sum(g * g * weights, axis=1)
        normalized = np.linalg.norm(g, axis=1) / (math.sqrt(n) * np.sqrt(q))
        print(f"n={n:4d}  mean normalized witness={normalized.mean():.8f}")


if __name__ == "__main__":
    main()
