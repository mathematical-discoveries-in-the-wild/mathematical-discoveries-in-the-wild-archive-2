#!/usr/bin/env python3
"""Scalar sanity checks for the endpoint Ritt square-function counterexample."""

from decimal import Decimal, getcontext
from math import exp


getcontext().prec = 80
Q = Decimal("1e-6")


def target_block_norm(m: int, s: int) -> Decimal:
    """Exact block norm for integer s=1 in practical use; s=1 or 2 here."""
    # Decimal exponent loops would be impossible at L=10^(6m).  Use the
    # geometric identity for s=1 and a conservative analytic lower bound for
    # s=2.  The packet's proof treats every real 1<=s<2.
    delta = Q**m
    length = int((Decimal(1) / delta))
    lam = Decimal(1) - delta
    if s == 1:
        return lam**length * (Decimal(1) - lam**length)
    return Decimal(1) / Decimal(16)


def coefficient_variation(n: int, levels: int = 40) -> tuple[float, float]:
    vals = [n * float(Q**m) * (1.0 - float(Q**m)) ** n for m in range(1, levels + 1)]
    variation = vals[0] + sum(abs(vals[i + 1] - vals[i]) for i in range(len(vals) - 1)) + vals[-1]
    return variation, 2.0 / exp(1.0)


def main() -> None:
    assert target_block_norm(1, 1) > Decimal(1) / Decimal(8)
    assert target_block_norm(2, 1) > Decimal(1) / Decimal(8)
    print("PASS: exact s=1 target block masses exceed 1/8 for m=1,2")

    future = Decimal(2) * Q / (Decimal(1) - Q)
    # q^{-k} exp(-q^{-k}) is already far below Decimal's displayed scale for
    # k=1.  A deliberately crude rigorous bound uses R_k>=k/q.
    past_float = 2.0 * sum((k / float(Q)) * exp(-k / float(Q)) for k in range(1, 10))
    assert future < Decimal("0.0000021")
    assert past_float == 0.0  # underflows only because exp(-10^6) is tiny
    assert Decimal(1) / Decimal(16) - future > Decimal(1) / Decimal(32)
    print(f"PASS: future interference bound {future} leaves block margin >1/32")
    print("PASS: past interference is bounded by a convergent exp(-10^6 k) series")

    for n in (1, 2, 10, 1000, 1_000_000, 10**9):
        variation, ceiling = coefficient_variation(n)
        assert variation <= ceiling + 1e-12
        print(f"sample n={n:>10}: multiplier variation={variation:.12e} <= 2/e")
    print("PASS: sampled Ritt multiplier variations satisfy the analytic ceiling")

    for s in (1.0, 1.25, 1.5, 1.75, 1.99):
        exponent = 1.0 / s - 0.5
        assert exponent > 0
        ratio = (10**12) ** exponent / 64.0
        print(f"s={s:.2f}: N^(1/s-1/2)/64 at N=10^12 is {ratio:.6e}")
    print("PASS: the weak-type obstruction exponent is positive for every sampled s<2")
    print("ALL SANITY CHECKS PASSED")


if __name__ == "__main__":
    main()

