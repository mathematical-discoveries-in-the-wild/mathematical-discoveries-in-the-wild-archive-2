"""Numerical stress check for the two lacunary endpoint constructions.

This is diagnostic only.  The proof uses elementary geometric-series bounds.
We work in logarithms to avoid overflow from exp(2**k).  The checked weights
are W(s)=s**alpha*log(e+s)**beta, including the pure logarithmic powers
(beta=0) used in the shortest form of the counterexample.
"""

from __future__ import annotations

import math


def logaddexp(values: list[float]) -> float:
    m = max(values)
    return m + math.log(sum(math.exp(v - m) for v in values))


def log_min_power_term(log_t: float, log_height: float, log_mass: float, p: float) -> float:
    log_u = log_t + log_height
    exponent = 2.0 if log_u <= 0.0 else p
    return log_mass + exponent * log_u


def log_w(s: float, alpha: float, beta: float) -> float:
    return alpha * math.log(s) + beta * math.log(math.log(math.e + s))


def grid_terms(
    p: float,
    alpha: float,
    beta: float,
    upper: bool,
    odd_grid: bool,
    count: int = 18,
):
    terms = []
    for k in range(1, count + 1):
        index = 2 * k + 1 if odd_grid else k
        log_height = 2.0**index
        log_weight = log_w(log_height, alpha, beta)
        if upper:
            log_mass = log_weight - 2.0 * log_height
        else:
            log_mass = -log_weight - p * log_height
        terms.append((log_height, log_mass))
    return terms


def log_modular(terms, log_t: float, p: float) -> float:
    return logaddexp(
        [log_min_power_term(log_t, h, m, p) for h, m in terms]
    )


def log_target(
    log_t: float, p: float, alpha: float, beta: float, upper: bool
) -> float:
    s = 1.0 - log_t  # log(e/t)
    target_log_weight = log_w(s, alpha, beta)
    if upper:
        return 2.0 * log_t + target_log_weight
    return p * log_t - target_log_weight


def check_family(
    p: float, alpha: float, beta: float, upper: bool
) -> tuple[float, float]:
    ratios = []
    for odd in (False, True):
        terms = grid_terms(p, alpha, beta, upper, odd)
        for s in [2.0 ** (j / 4.0) for j in range(12, 49)]:
            log_t = -s
            ratios.append(
                math.exp(
                    log_modular(terms, log_t, p)
                    - log_target(log_t, p, alpha, beta, upper)
                )
            )
    return min(ratios), max(ratios)


def main() -> None:
    for p in (1.0, 1.3, 1.8):
        for alpha, beta in ((0.5, -0.5), (1.0, 0.0), (2.0, 1.0)):
            for upper in (False, True):
                lo, hi = check_family(p, alpha, beta, upper)
                label = "upper" if upper else "lower"
                print(
                    f"p={p:.1f} alpha={alpha:.2f} beta={beta:.2f} "
                    f"{label}: ratio range [{lo:.4g}, {hi:.4g}]"
                )

    # Tail separation on the gap (A_{2j+1}, A_{2j+2}).  Print logarithms of
    # the ratio between the x atom at A_{2j+2} and the next y tail atom.
    p, alpha, beta = 1.3, 1.0, 0.0
    for upper in (False, True):
        label = "upper" if upper else "lower"
        vals = []
        for j in range(2, 7):
            ix, iy = 2 * j + 2, 2 * j + 3
            hx, hy = 2.0**ix, 2.0**iy
            log_wx = log_w(hx, alpha, beta)
            log_wy = log_w(hy, alpha, beta)
            if upper:
                log_ratio = log_wx - log_wy - 2.0 * (hx - hy)
            else:
                log_ratio = -log_wx + log_wy - p * (hx - hy)
            vals.append(log_ratio / math.log(10.0))
        print(f"{label} log10 tail-separation lower bounds: {vals}")


if __name__ == "__main__":
    main()
