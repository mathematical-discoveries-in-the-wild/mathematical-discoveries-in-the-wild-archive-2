#!/usr/bin/env python3
"""Exact arithmetic check of the Berger S^5 spectral counterexample."""

from fractions import Fraction
from math import comb


A = Fraction(5, 4)  # squared Hopf-fiber scale
M = 2               # S^(2m+1) = S^5


def harmonic_bidegree_dim(p, q):
    """Complex dimension of harmonic bihomogeneous polynomials H_{p,q}."""
    first = comb(p + M, M) * comb(q + M, M)
    second = 0 if p == 0 or q == 0 else (
        comb(p + M - 1, M) * comb(q + M - 1, M)
    )
    return first - second


def round_harmonic_dim(k):
    second = 0 if k < 2 else comb(k + 3, 5)
    return comb(k + 5, 5) - second


def berger_eigenvalue(p, q):
    k = p + q
    return Fraction(k * (k + 4), 1) + (1 / A - 1) * (p - q) ** 2


def expand_berger(kmax):
    values = []
    for k in range(kmax + 1):
        for p in range(k + 1):
            q = k - p
            values.extend([(berger_eigenvalue(p, q), (p, q))]
                          * harmonic_bidegree_dim(p, q))
    return sorted(values)


def expand_round(kmax, alpha):
    values = []
    for k in range(kmax + 1):
        value = alpha * k * (k + 4)
        values.extend([(value, k)] * round_harmonic_dim(k))
    return values


def main():
    ricci_vertical = 2 * M * A
    ricci_horizontal = 2 * M + 2 - 2 * A
    rho = min(ricci_vertical, ricci_horizontal)
    assert ricci_vertical == 5
    assert ricci_horizontal == Fraction(7, 2)
    assert rho == Fraction(7, 2)

    # The round S^5 has Ric=4g, so the rho-comparison sphere has eigenvalues
    # alpha*k(k+4), alpha=rho/4.
    alpha = rho / (2 * M)
    assert alpha == Fraction(7, 8)

    degree_dims = [round_harmonic_dim(k) for k in range(7)]
    assert degree_dims == [1, 6, 20, 50, 105, 196, 336]
    assert sum(degree_dims) == 714
    for k in range(8):
        assert sum(harmonic_bidegree_dim(p, k - p)
                   for p in range(k + 1)) == round_harmonic_dim(k)

    berger = expand_berger(7)
    round_ = expand_round(7, alpha)
    assert len(berger) == len(round_) == 1254
    assert berger[713][0] == 60
    assert berger[714] == (Fraction(336, 5), (0, 7))
    assert round_[714] == (Fraction(539, 8), 7)
    assert round_[714][0] - berger[714][0] == Fraction(7, 40)

    # Degree separation used in the proof.
    max_through_six = max(berger_eigenvalue(p, k - p)
                          for k in range(7) for p in range(k + 1))
    min_degree_seven = min(berger_eigenvalue(p, 7 - p)
                           for p in range(8))
    assert max_through_six == 60 < min_degree_seven == Fraction(336, 5)

    print("fiber scale a =", A)
    print("Ricci eigenvalues (horizontal, vertical) =",
          ricci_horizontal, ricci_vertical)
    print("comparison spectral scale =", alpha)
    print("modes of degrees 0 through 6 =", sum(degree_dims))
    print("lambda_715(Berger S^5) =", berger[714][0])
    print("lambda_715(round comparison S^5) =", round_[714][0])
    print("strict deficit =", round_[714][0] - berger[714][0])
    print("all exact checks passed")


if __name__ == "__main__":
    main()
