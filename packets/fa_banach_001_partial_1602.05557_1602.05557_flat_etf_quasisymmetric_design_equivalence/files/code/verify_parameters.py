#!/usr/bin/env python3
from fractions import Fraction


def parameters(q: int) -> dict[str, int]:
    assert q > 0 and q % 2 == 0
    v = q * q + q - 1
    b = q * v
    k = q * (q + 1) // 2
    r = q * q * (q + 1) // 2
    lam = q * q * (q + 1) // 4
    x1 = q * q // 4
    x2 = q * (q + 2) // 4
    degree = (q - 1) * (q + 1) * (q + 2) // 2
    rho = (q * q - 2) // 2
    sigma = -(q + 2) // 2
    graph_lam = (q + 4) * (q * q - 2) // 4
    graph_mu = q * q * (q + 2) // 4
    f = v - 1
    g = b - v

    assert b * k == v * r
    assert lam * (v - 1) == r * (k - 1)
    assert x2 - x1 == q // 2
    assert degree * (degree - graph_lam - 1) == (b - degree - 1) * graph_mu
    assert 1 + f + g == b
    assert degree + f * rho + g * sigma == 0
    assert rho + sigma == graph_lam - graph_mu
    assert rho * sigma == graph_mu - degree

    # The Welch coherence is exactly 1/(q+1).
    d = v
    welch_sq = Fraction(b - d, d * (b - 1))
    assert welch_sq == Fraction(1, (q + 1) ** 2)

    return locals()


for q in range(2, 52, 2):
    parameters(q)

p = parameters(6)
for key in (
    "v", "b", "k", "r", "lam", "x1", "x2", "degree", "graph_lam",
    "graph_mu", "rho", "sigma", "f", "g",
):
    print(f"{key}={p[key]}")
print("all_even_q_parameter_identities_through_50=verified")
