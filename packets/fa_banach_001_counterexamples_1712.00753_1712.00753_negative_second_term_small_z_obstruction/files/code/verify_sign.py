#!/usr/bin/env python3
"""Numerically verify the universal small-z sign obstruction."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--leading", type=float, default=1.0,
                        help="C_{n,gamma} times |F| (positive)")
    parser.add_argument("--second", type=float, default=1.0,
                        help="proposed positive C(alpha,beta)")
    parser.add_argument("--power", type=float, default=1.0,
                        help="n+gamma-2 (nonnegative in the source setting)")
    args = parser.parse_args()
    if args.leading <= 0 or args.second <= 0 or args.power < 0:
        raise SystemExit("Require leading>0, second>0, and power>=0")
    z = args.second / (2.0 * args.leading)
    rhs = z ** args.power * (args.leading * z - args.second)
    print(f"z={z:.12g}")
    print(f"right_hand_side={rhs:.12g}")
    print("riesz_mean_lower_bound=0")
    assert rhs < 0


if __name__ == "__main__":
    main()
