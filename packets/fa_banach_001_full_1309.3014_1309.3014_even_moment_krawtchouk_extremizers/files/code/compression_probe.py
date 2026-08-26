#!/usr/bin/env python3
"""Search for failures of Aaronson's pair-compression at higher moments."""

from itertools import combinations
import argparse
import numpy as np

from level_extremizer_probe import walsh_level


def compress(coeff, subsets, i, j):
    out = coeff.copy()
    lookup = {s: q for q, s in enumerate(subsets)}
    for q, s in enumerate(subsets):
        si, sj = i in s, j in s
        if si == sj:
            continue
        partner = tuple(sorted((set(s) ^ {i, j})))
        r = np.sqrt((coeff[q] ** 2 + coeff[lookup[partner]] ** 2) / 2.0)
        out[q] = r
        out[lookup[partner]] = r
    return out


def main(n, a, p, samples, seed):
    w, subsets = walsh_level(n, a)
    rng = np.random.default_rng(seed)
    worst = (float("inf"), None)
    for sample in range(samples):
        mode = sample % 4
        if mode == 0:
            coeff = rng.exponential(size=len(subsets))
        elif mode == 1:
            coeff = np.exp(3 * rng.normal(size=len(subsets)))
        elif mode == 2:
            coeff = rng.random(len(subsets)) ** 5
        else:
            coeff = (rng.random(len(subsets)) < 0.25) * rng.random(len(subsets))
        if not np.any(coeff):
            continue
        before = np.mean((w @ coeff) ** p)
        after_coeff = compress(coeff, subsets, 0, 1)
        after = np.mean((w @ after_coeff) ** p)
        ratio = after / before
        if ratio < worst[0]:
            worst = ratio, coeff
        if ratio < 1 - 1e-10:
            print(f"FAIL n={n} a={a} p={p} sample={sample} ratio={ratio:.15g}")
            print("coeff=" + repr(coeff.tolist()))
            return
    print(f"PASS samples={samples} worst_ratio={worst[0]:.15g}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("a", type=int)
    parser.add_argument("p", type=int)
    parser.add_argument("--samples", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    main(args.n, args.a, args.p, args.samples, args.seed)
