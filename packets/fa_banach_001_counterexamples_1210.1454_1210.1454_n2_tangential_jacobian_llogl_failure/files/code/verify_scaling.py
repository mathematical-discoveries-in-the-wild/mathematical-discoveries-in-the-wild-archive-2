#!/usr/bin/env python3
"""Verify the exact scaling identities in the n=2 counterexample."""

import math


def row(k: int) -> tuple[float, float, float, float]:
    log_a = float(k * k)
    log_ell = -log_a - math.log(k)
    w11_upper = (4.0 * math.pi + 4.0) / k
    entropy = (1.0 / k) * log_a
    return log_a, log_ell, w11_upper, entropy


def main() -> None:
    print(" k   log(A_k)      log(ell_k)    W11 upper      entropy")
    for k in (2, 4, 8, 16, 32):
        log_a, log_ell, norm_bound, entropy = row(k)
        assert math.isclose(entropy, float(k))
        print(
            f"{k:2d} {log_a:10.1f} {log_ell:15.6f} "
            f"{norm_bound:12.6f} {entropy:12.6f}"
        )


if __name__ == "__main__":
    main()
