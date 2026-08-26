"""Finite checks for the recursive even-Hankel-form construction.

The proof of positivity is analytic (compactness plus Young's inequality).
This script checks the base coefficients and the degree bookkeeping used in
the induction for a range of even orders and stages.
"""

from math import comb


def check_base(d: int) -> None:
    r = 2 * d
    moments = [0.0] * (r + 1)
    moments[0] = moments[r] = 1.0
    moments[2] = -1.0 / comb(r, 2)
    # Coefficients of L((a+bx)^r): only degrees 0, 2, r survive.
    assert comb(r, 2) * moments[2] == -1.0
    # Weighted AM-GM lower bound coefficients are strictly positive.
    assert 1.0 - (d - 1) / d > 0
    assert 1.0 - 1.0 / d > 0


def check_stage(d: int, n: int) -> None:
    r = 2 * d
    old_top = r * n
    new_top = r * (n + 1)
    for k in range(1, r):
        # Maximal moment index in the kth mixed binomial term.
        mixed_top = k * (n + 1) + (r - k) * n
        assert mixed_top == old_top + k
        assert mixed_top < new_top
    assert new_top == old_top + r


def main() -> None:
    for d in range(2, 11):
        check_base(d)
        for n in range(1, 31):
            check_stage(d, n)
    print("base forms and all tested induction degree ranges verified")


if __name__ == "__main__":
    main()
