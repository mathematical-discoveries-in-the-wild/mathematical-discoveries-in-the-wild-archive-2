#!/usr/bin/env python3
"""Illustrate the logarithmic exponent gap; this is not the proof."""

import math


def main() -> None:
    q = 2.0
    varsigma = 2.0
    rho = 1.0 + varsigma * (q - 1.0)
    print(f"q={q:g}, varsigma={varsigma:g}, rho={rho:g}, gap={rho-q:g}")
    print("N\tlower-target/(source-upper)^q")
    for exponent in (2, 4, 8, 16, 32):
        n = math.exp(exponent)
        target_lower = exponent**rho / (2.0**rho * rho)
        source_q_upper = (q ** (1.0 - 1.0 / q) * (1.0 + exponent)) ** q
        print(f"exp({exponent})\t{target_lower/source_q_upper:.8g}")


if __name__ == "__main__":
    main()
