#!/usr/bin/env python3
"""Sanity checks for the smooth-operator-layer proof packet.

The analytic proof does not depend on computation.  This script verifies the
chosen fractional error allocation and the finite-dimensional algebra behind
the disjoint latent-bump encoding.
"""

from fractions import Fraction


def check_error_budget() -> None:
    source_error = Fraction(1, 2)
    output_weight_error = Fraction(1, 8)
    activation_error = Fraction(1, 8)
    output_bias_error = Fraction(1, 8)
    total = (
        source_error
        + output_weight_error
        + activation_error
        + output_bias_error
    )
    assert total == Fraction(7, 8)
    assert total < 1
    print(f"error budget: {total} epsilon < epsilon")


def check_disjoint_bump_encoding() -> None:
    # Each row models one normalized zeta_i.  Disjoint support and
    # chi_j=delta_ij on supp(zeta_i) give this exact overlap matrix.
    overlap = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    output_coefficients = [Fraction(2, 3), Fraction(-5, 4), Fraction(7, 6), 3]
    activated_features = [Fraction(1, 5), Fraction(-2, 7), Fraction(11, 9), -1]

    encoded = sum(
        output_coefficients[i]
        * sum(overlap[i][j] * activated_features[j] for j in range(4))
        for i in range(4)
    )
    finite_sum = sum(
        output_coefficients[i] * activated_features[i] for i in range(4)
    )
    assert encoded == finite_sum
    print(f"latent bump encoding: exact equality ({encoded})")


if __name__ == "__main__":
    check_error_budget()
    check_disjoint_bump_encoding()
    print("all checks passed")

