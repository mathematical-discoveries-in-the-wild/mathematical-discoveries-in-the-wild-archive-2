#!/usr/bin/env python3
"""Interval-check the parameter inequalities in the generalized cutoff lemma.

Frankel--Urschel's Lemma 3.2 supplies C-hat and y for every pair
    t >= 4, n >= 4t, n even.
The packet's generalized projection lemma rules out those objects when the
strict inequalities checked below hold.  Published Theorem 1.2 already covers
n >= 1000, so only the finite range 158 <= n <= 998 is checked here.

All arithmetic is interval arithmetic (mpmath.iv at 80 decimal digits).  A
dimension is accepted only when the lower endpoint of the final contradiction
margin is strictly positive.
"""

from __future__ import annotations

import mpmath as mp


mp.iv.dps = 80
IV = mp.iv.mpf


def lower(x):
    """Lower endpoint, retained as a point interval for directed comparison."""
    return x.a


def upper(x):
    """Upper endpoint, retained as a point interval for directed comparison."""
    return x.b


def interval_margin(n: int, t: int):
    """Return the interval lower-bound data for one admissible (n,t)."""
    if n % 2 or t < 4 or n < 4 * t:
        return None

    nn, tt = IV(n), IV(t)
    s = nn - tt
    m = tt + 1
    q = IV((n + 3) // 4)  # ceil(n/4)
    gamma = nn / q

    eps_plus = (
        (nn - 1) / (4 * (nn - 2) * nn)
        + 5 / (4 * s)
        + 1 / ((8 * s - 4) * mp.iv.sqrt(s))
    )
    eps_zero = (
        (2 * nn**2 - 4 * nn + 1) / (4 * (nn - 2) * (nn - 1) * nn)
        + 5 / (4 * s)
        + 1 / ((8 * s - 4) * mp.iv.sqrt(s))
    )

    separation = IV(1) / 4 - eps_plus - eps_zero
    mu_lower = (tt * (IV(1) / 4 - eps_plus) - eps_zero) / m
    variance_lower = tt * separation**2 / m**2
    kappa = nn / (4 * m * s)
    radicand_upper = (
        kappa
        - gamma * variance_lower
        - gamma * (1 - gamma / 4) * mu_lower**2
    )

    if lower(separation) <= 0 or lower(mu_lower) <= 0:
        return None

    # Parameters with a radicand interval crossing zero are simply skipped;
    # every certified dimension below has a strictly positive radicand.
    if lower(radicand_upper) <= 0:
        return None
    alpha_lower = gamma * mu_lower / 2 - mp.iv.sqrt(radicand_upper)
    complement_upper = mp.iv.sqrt(nn / (8 * s))
    margin = alpha_lower - eps_zero - complement_upper

    return {
        "margin": margin,
        "eps_plus": eps_plus,
        "eps_zero": eps_zero,
        "separation": separation,
        "mu_lower": mu_lower,
        "radicand_upper": radicand_upper,
    }


def main() -> None:
    certificates: list[tuple[int, int, mp.mpf]] = []
    for n in range(158, 1000, 2):
        choices = []
        for t in range(4, n // 4 + 1):
            data = interval_margin(n, t)
            if data is not None and lower(data["margin"]) > 0:
                choices.append((float(lower(data["margin"])), t, lower(data["margin"])))
        if not choices:
            raise AssertionError(f"no certified parameter for n={n}")
        _, best_t, best_margin = max(choices)
        certificates.append((n, best_t, best_margin))

    weakest = min(certificates, key=lambda item: float(item[2]))
    print(f"certified_even_dimensions={len(certificates)}")
    print("range=158..998")
    print(
        "weakest_certificate="
        f"n={weakest[0]},t={weakest[1]},lower_margin={weakest[2]}"
    )
    print("first_t_choices=" + ",".join(f"{n}:{t}" for n, t, _ in certificates[:12]))
    print("last_t_choices=" + ",".join(f"{n}:{t}" for n, t, _ in certificates[-12:]))


if __name__ == "__main__":
    main()
