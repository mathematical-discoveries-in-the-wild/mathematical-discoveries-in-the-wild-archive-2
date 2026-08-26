"""Arithmetic checks for the near-constant analytic-degree counterexample."""

import math


def analytic_degree_upper(delta):
    return math.log((1.0 + delta) / (1.0 - delta)) / math.log(4.0)


def main():
    previous = float("inf")
    for n in range(1, 13):
        epsilon = math.exp(-n)
        delta = math.exp(-2 * n)
        j0 = max(0, math.ceil(math.log(1.0 / epsilon) - 1e-12))
        degree_lower_bound = j0
        upper = analytic_degree_upper(delta)

        assert j0 == n
        assert degree_lower_bound >= n
        assert upper > 0
        assert upper < previous
        previous = upper

        # The pointwise disk bounds used for every interval and subset.
        assert (1.0 + delta) / (1.0 - delta) <= 4.0**upper * (1 + 1e-14)

    print("checked n=1,...,12")
    print("last epsilon:", f"{math.exp(-12):.12g}")
    print("last degree lower bound:", 12)
    print("last analytic-degree upper bound:", f"{previous:.12g}")
    print("all near-constant checks passed")


if __name__ == "__main__":
    main()
