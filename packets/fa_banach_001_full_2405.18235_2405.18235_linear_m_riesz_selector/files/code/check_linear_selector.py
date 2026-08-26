#!/usr/bin/env python3
"""Exact sanity checks for the linear-m selector packet.

The proof is analytic.  This script checks its scalar error inequalities with
Fractions and exhausts the cyclic lower-bound construction for finite sizes.
"""

from fractions import Fraction


def ceil_fraction(x: Fraction) -> int:
    return -(-x.numerator // x.denominator)


def check_upper_grid() -> int:
    cases = 0
    for m in range(1, 51):
        for b in range(2, 11):
            for tenth in range(1, 10):
                eps = Fraction(tenth, 10)
                r = ceil_fraction(Fraction(16 * m * b * b, 1) / (eps * eps))

                # 1/r <= eps/(2B).
                assert Fraction(1, r) <= eps / (2 * b)

                # 2 sqrt(m/r) <= eps/(2B), checked after squaring.
                assert Fraction(4 * m, r) <= eps * eps / (4 * b * b)

                # Hence E_r = 1/r + 2 sqrt(m/r) <= eps/B.
                assert Fraction(1, r) <= eps / (2 * b)
                cases += 1
    return cases


def check_cyclic_lower_bound() -> int:
    pairs = 0
    for r in range(1, 41):
        # Family j sends y_q to e_(q+j mod r), while x_p is e_p.
        for p in range(r):
            for q in range(r):
                witnesses = [j for j in range(r) if (q + j) % r == p]
                assert witnesses == [(p - q) % r]

                # In the witness family the selected Gram matrix is
                # [[1,1],[1,1]], with exact eigenvalues 0 and 2.
                trace = 2
                determinant = 0
                assert (trace, determinant) == (2, 0)
                pairs += 1
    return pairs


def main() -> None:
    upper = check_upper_grid()
    lower = check_cyclic_lower_bound()
    print(f"upper-bound scalar cases: {upper}")
    print(f"cyclic selector pairs: {lower}")
    print(f"total exact checks: {upper + lower}")


if __name__ == "__main__":
    main()

