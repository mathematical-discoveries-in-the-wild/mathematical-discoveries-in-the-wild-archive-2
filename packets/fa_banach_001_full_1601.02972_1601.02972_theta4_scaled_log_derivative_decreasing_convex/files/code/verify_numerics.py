"""High-precision smoke tests for the two analytic formulas in the packet."""

import mpmath as mp


mp.mp.dps = 60
PI = mp.pi


def phi_derivatives(x):
    ex = mp.exp(x)
    first = x * ((2 - x) * ex - 2) / (ex - 1) ** 2
    numerator = (
        (x * x - 4 * x + 2) * ex * ex
        + (x * x + 4 * x - 4) * ex
        + 2
    )
    second = numerator / (ex - 1) ** 3
    return first, second


def signs_large(s):
    first = mp.mpf("0")
    second = mp.mpf("0")
    for m in range(1, 10000):
        weight = 2 if m % 2 else 1
        x = PI * m * s
        phi_first, phi_second = phi_derivatives(x)
        first += weight * phi_first
        second += weight * PI * m * phi_second
        if m > 1 and abs(phi_first) + abs(phi_second) < mp.mpf("1e-70"):
            break
    return first, second


def signs_small(s):
    first = -mp.mpf("0.5")
    second = mp.mpf("0")
    for n in range(1, 1000):
        row_first = mp.mpf("0")
        row_second = mp.mpf("0")
        for j in range(1000):
            c = 2 * PI * n * (2 * j + 1)
            d = 2 * PI * n * (2 * j + 2)
            exp_c = mp.exp(-c / s)
            exp_d = mp.exp(-d / s)
            term_first = (c * exp_c - 3 * d * exp_d) / (s * s)
            term_second = (
                c * (c - 2 * s) * exp_c
                - 3 * d * (d - 2 * s) * exp_d
            ) / (s ** 4)
            row_first += term_first
            row_second += term_second
            if j > 0 and abs(term_first) + abs(term_second) < mp.mpf("1e-75"):
                break
        first += 2 * PI * n * row_first
        second += 2 * PI * n * row_second
        if n > 1 and abs(row_first) + abs(row_second) < mp.mpf("1e-70"):
            break
    return first, second


worst_first = -mp.inf
worst_second = mp.inf
for index in range(121):
    s = mp.power(10, -3 + 6 * index / 120)
    first, second = signs_small(s) if s <= 1 else signs_large(s)
    assert first < 0, (s, first)
    assert second > 0, (s, second)
    worst_first = max(worst_first, first)
    worst_second = min(worst_second, second)

print("all sampled first derivatives are negative")
print("all sampled second derivatives are positive")
print("largest sampled H' =", mp.nstr(worst_first, 20))
print("smallest sampled H'' =", mp.nstr(worst_second, 20))
