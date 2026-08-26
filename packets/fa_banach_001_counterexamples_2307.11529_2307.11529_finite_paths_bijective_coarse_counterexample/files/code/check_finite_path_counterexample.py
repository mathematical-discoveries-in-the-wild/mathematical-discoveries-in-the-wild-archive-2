#!/usr/bin/env python3
"""Finite sanity checks for the path-component counterexample.

The proof in main.tex is exact.  This script only checks the displayed floor
formulas and their uniform constants over a large finite range.
"""


def f_map(n: int, k: int) -> int:
    if not (0 <= k < 4 * n):
        raise ValueError("k is outside P_n")
    if k < 2 * n:
        return k // 2
    return n + (3 * (k - 2 * n)) // 2


def g_map(n: int, j: int) -> int:
    if not (0 <= j < 4 * n):
        raise ValueError("j is outside P_n")
    if j < n:
        return 2 * j
    return 2 * n + (2 * (j - n)) // 3


def main() -> None:
    max_f_step = 0
    max_g_step = 0
    max_gf_error = 0
    max_fg_error = 0

    for n in range(1, 2001):
        f_values = [f_map(n, k) for k in range(4 * n)]
        g_values = [g_map(n, j) for j in range(4 * n)]
        assert all(0 <= value < 4 * n for value in f_values)
        assert all(0 <= value < 4 * n for value in g_values)

        max_f_step = max(
            max_f_step,
            max(abs(f_values[k + 1] - f_values[k]) for k in range(4 * n - 1)),
        )
        max_g_step = max(
            max_g_step,
            max(abs(g_values[j + 1] - g_values[j]) for j in range(4 * n - 1)),
        )

        gf_error = max(abs(g_map(n, f_map(n, k)) - k) for k in range(4 * n))
        fg_error = max(abs(f_map(n, g_map(n, j)) - j) for j in range(4 * n))
        max_gf_error = max(max_gf_error, gf_error)
        max_fg_error = max(max_fg_error, fg_error)

        assert set(f_values[: 2 * n]) == set(range(n))
        # Monotonicity, endpoint control, and gaps of size at most two imply
        # that the image is 1-dense without an unnecessary quadratic scan.
        assert f_values == sorted(f_values)
        assert f_values[0] == 0
        assert f_values[-1] >= 4 * n - 2
        assert max(f_values[k + 1] - f_values[k] for k in range(4 * n - 1)) <= 2

    assert max_f_step <= 2
    assert max_g_step <= 2
    assert max_gf_error <= 1
    assert max_fg_error <= 1

    for closeness_bound in range(501):
        n = closeness_bound + 1
        target_neighborhood_size = n + closeness_bound
        assert target_neighborhood_size < 2 * n

    print("checked components n=1,...,2000")
    print(f"max adjacent f-step: {max_f_step}")
    print(f"max adjacent g-step: {max_g_step}")
    print(f"max |g(f(k))-k|: {max_gf_error}")
    print(f"max |f(g(j))-j|: {max_fg_error}")
    print("image of each component is 1-dense")
    print("counting obstruction checked for closeness bounds C=0,...,500")


if __name__ == "__main__":
    main()
