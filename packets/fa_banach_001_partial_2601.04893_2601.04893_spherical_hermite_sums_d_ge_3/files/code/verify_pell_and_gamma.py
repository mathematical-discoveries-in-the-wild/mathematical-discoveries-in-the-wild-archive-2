#!/usr/bin/env python3
"""Check the exact Pell placement and Gamma-moment asymptotics.

This is a regression/sanity check, not a proof of the analytic transference.
"""

from __future__ import annotations

import itertools
import math


def source_vector(d: int) -> tuple[int, ...]:
    root = math.isqrt(d)
    if root * root != d:
        return (1,) * d
    return (1,) * (d - 1) + (2,)


def pell_solutions(D: int, count: int):
    """Generate positive solutions by powers of the fundamental unit."""
    a = math.isqrt(D) + 1
    while True:
        delta = a * a - 1
        b = math.isqrt(delta // D) if delta >= D else 0
        if b > 0 and a * a - D * b * b == 1:
            break
        a += 1

    x, y = 1, 0
    for _ in range(count):
        x, y = x * a + D * y * b, x * b + y * a
        yield x, y


def check_pell_placement() -> int:
    checks = 0
    for d in (3, 4, 5, 9, 16):
        v = source_vector(d)
        D = sum(x * x for x in v)
        assert math.isqrt(D) ** 2 != D
        assert math.gcd(*v) == 1
        # A bounded sample in H_v.  The vectors
        # v[-1] e_i - v[i] e_{d-1} generate a finite-index sublattice, which is
        # enough for regression checks of the universal algebraic identity.
        basis = []
        for i in range(d - 1):
            q = [0] * d
            q[i] = v[-1]
            q[-1] = -v[i]
            basis.append(tuple(q))
        q_sample = {(0,) * d}
        for q in basis:
            for coefficient in range(-3, 4):
                q_sample.add(tuple(coefficient * x for x in q))
        active = basis[: min(3, len(basis))]
        for coefficients in itertools.product(range(-2, 3), repeat=len(active)):
            q_sample.add(
                tuple(
                    sum(coefficient * q[j] for coefficient, q in zip(coefficients, active))
                    for j in range(d)
                )
            )
        for a, b in pell_solutions(D, 8):
            assert a * a - D * b * b == 1
            for J in (1, 2, 5):
                K = tuple(J * b * x for x in v)
                N = J * a
                for q in q_sample:
                    assert sum(vj * qj for vj, qj in zip(v, q)) == 0
                    lhs = sum((kj + qj) ** 2 for kj, qj in zip(K, q))
                    qnorm = sum(qj * qj for qj in q)
                    assert lhs == N * N - J * J + qnorm
                    assert (lhs <= N * N) == (qnorm <= J * J)
                    checks += 1
    return checks


def log_gamma_moment(K: int, q: int, p: float, s: float) -> float:
    """Log E[A_{K,q}^s] for one coordinate under normalized p-Fock mass."""
    if K + q < 0 or p * K / 2 + 1 + s * q / 2 <= 0:
        raise ValueError("indices outside the Gamma moment range")
    return (
        (s / 2) * (math.lgamma(K + 1) - math.lgamma(K + q + 1))
        - (s * q / 2) * math.log(p / 2)
        + math.lgamma(p * K / 2 + 1 + s * q / 2)
        - math.lgamma(p * K / 2 + 1)
    )


def gamma_table() -> list[tuple[float, int, int, float]]:
    rows = []
    for p in (1.0, 1.5, 3.0, 7.0):
        for q in (-4, -1, 1, 5):
            for K in (100, 1000, 10000, 100000):
                moment = math.exp(log_gamma_moment(K, q, p, p))
                rows.append((p, q, K, abs(moment - 1.0)))
    return rows


def main() -> None:
    checks = check_pell_placement()
    rows = gamma_table()
    print(f"pell_identity_checks={checks}")
    print("gamma_moment_absolute_errors (last K for each p,q)")
    for p in (1.0, 1.5, 3.0, 7.0):
        for q in (-4, -1, 1, 5):
            row = next(r for r in reversed(rows) if r[0] == p and r[1] == q)
            print(f"p={p:3.1f} q={q:2d} K={row[2]:6d} error={row[3]:.3e}")
    assert all(math.isfinite(error) for _, _, _, error in rows)
    assert max(error for _, _, K, error in rows if K == 100000) < 2e-4
    print("status=PASS")


if __name__ == "__main__":
    main()
