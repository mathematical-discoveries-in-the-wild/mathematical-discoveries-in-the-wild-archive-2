#!/usr/bin/env python3
"""Exact finite-tree check of the right-inverse normalization in the packet.

This is an illustration, not a proof of the general theorem.  It uses the
disjoint maps f_0(k)=2k and f_1(k)=2k+1, rational weights 3/2 and -2,
and verifies T^N R_N=I on finitely many rows with Fraction arithmetic.
"""

from fractions import Fraction


COEFFS = (Fraction(3, 2), Fraction(-2, 1))
DEPTH = 4
ROWS = range(1, 9)


def child(branch: int, k: int) -> int:
    return 2 * k + branch


def descendants(k: int, depth: int):
    states = {(k, Fraction(1))}
    for _ in range(depth):
        states = {
            (child(branch, index), weight * COEFFS[branch])
            for index, weight in states
            for branch in range(2)
        }
    return dict(states)


def right_inverse_column(k: int):
    row = descendants(k, DEPTH)
    squared_dual_norm = sum(weight * weight for weight in row.values())
    return {
        index: weight / squared_dual_norm for index, weight in row.items()
    }, squared_dual_norm


def apply_power_to_sparse(vector, k: int):
    row = descendants(k, DEPTH)
    return sum(weight * vector.get(index, 0) for index, weight in row.items())


def main() -> None:
    columns = {}
    supports = []
    expected_dual_norm_squared = sum(c * c for c in COEFFS) ** DEPTH

    for k in ROWS:
        column, dual_norm_squared = right_inverse_column(k)
        assert dual_norm_squared == expected_dual_norm_squared
        columns[k] = column
        supports.append(set(column))

    for i, left in enumerate(supports):
        for right in supports[i + 1 :]:
            assert left.isdisjoint(right)

    for k in ROWS:
        for j in ROWS:
            value = apply_power_to_sparse(columns[k], j)
            assert value == (1 if j == k else 0)

    test_vector = {k: Fraction((-1) ** k * (k + 1), 7) for k in ROWS}
    lifted = {}
    for k, scalar in test_vector.items():
        for index, value in columns[k].items():
            lifted[index] = lifted.get(index, 0) + scalar * value
    recovered = {k: apply_power_to_sparse(lifted, k) for k in ROWS}
    assert recovered == test_vector

    # Every column has squared ell_2 norm C^(-2N), strictly below one.
    column_norm_squared = sum(v * v for v in columns[1].values())
    assert column_norm_squared == 1 / expected_dual_norm_squared
    assert column_norm_squared < 1

    print("PASS: disjoint supports, exact T^N R_N = I, and contraction verified")
    print(f"depth={DEPTH}, rows={len(tuple(ROWS))}, C^2={sum(c*c for c in COEFFS)}")


if __name__ == "__main__":
    main()
