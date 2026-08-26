#!/usr/bin/env python3
"""Exact sanity checks for the two examples used in the packet.

These computations are not a proof of the abstract theorem.  They check the
orientation convention and the L2-versus-L1 calculation in Remark 5.10.
"""

from fractions import Fraction


def disjoint_interval_partial_sums(n_max: int = 1000) -> tuple[Fraction, int]:
    """Return squared L2 and L1 barycenter norms for the first n_max edges."""
    l2_squared = Fraction(0)
    l1 = 0
    for n in range(1, n_max + 1):
        length = n * n
        weight = Fraction(1, n * n)
        l2_squared += length * weight * weight
        l1 += length * weight
    return l2_squared, l1


def boundary(start: str | None, end: str | None) -> dict[str, int]:
    """Boundary of an oriented open-ended curve: end minus start."""
    answer: dict[str, int] = {}
    if end is not None:
        answer[end] = answer.get(end, 0) + 1
    if start is not None:
        answer[start] = answer.get(start, 0) - 1
    return {key: value for key, value in answer.items() if value}


def main() -> None:
    l2_squared, l1 = disjoint_interval_partial_sums()
    assert l1 == 1000
    assert l2_squared < Fraction(2)
    # The increasing half-line starts at 0 and escapes at the right end.
    assert boundary("0", None) == {"0": -1}
    # Since partial(t_loc(b))=-div(b), this represents div(b)=delta_0.
    print(f"sum_(n<=1000) 1/n^2 = {float(l2_squared):.12f} < 2")
    print(f"partial L1 occupation = {l1} (diverges linearly)")
    print("ray boundary = -delta_0; derivation divergence = +delta_0")


if __name__ == "__main__":
    main()
