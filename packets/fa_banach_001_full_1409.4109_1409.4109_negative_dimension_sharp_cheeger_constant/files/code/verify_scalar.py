"""High-precision sanity checks for the sharp 2/D model Cheeger inequality."""

import random
import mpmath as mp

mp.mp.dps = 80
rng = random.Random(20260811)


def scaled_residual(beta, x):
    if beta == 0:
        return x * mp.log(1 / x)
    return x * (1 - x**beta) / beta


def median(beta, a):
    if beta == 0:
        return mp.sqrt(a)
    return (2 * a**beta / (1 + a**beta)) ** (1 / beta)


def stationary_point(beta):
    if beta == 0:
        return mp.exp(-1)
    return (beta + 1) ** (-1 / beta)


worst = (mp.inf, None)
for _ in range(10_000):
    beta = mp.mpf(0) if rng.random() < 0.05 else mp.power(10, rng.uniform(-8, 4))
    a = mp.mpf(1) - mp.power(10, rng.uniform(-12, -0.0001))
    m = median(beta, a)
    x = max(m, stationary_point(beta))
    residual = scaled_residual(beta, x)
    ratio = (1 - a) / residual
    if ratio < worst[0]:
        worst = (ratio, (beta, a, m, x, residual))
    assert ratio >= 2

print("smallest sampled D times Cheeger constant:")
print(mp.nstr(worst[0], 40))
print(tuple(mp.nstr(value, 20) for value in worst[1]))
