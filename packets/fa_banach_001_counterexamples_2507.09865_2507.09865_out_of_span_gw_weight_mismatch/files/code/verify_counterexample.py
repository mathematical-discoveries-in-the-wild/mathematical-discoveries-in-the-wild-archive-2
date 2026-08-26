from fractions import Fraction as F
from itertools import permutations


def matrix(u: F, v: F) -> tuple[tuple[F, ...], ...]:
    return (
        (F(0), F(10), F(11) + u, F(12) + v),
        (F(10), F(0), F(11) - u, F(12) - v),
        (F(11) + u, F(11) - u, F(0), F(13)),
        (F(12) + v, F(12) - v, F(13), F(0)),
    )


def perm_frobenius_sq(
    left: tuple[tuple[F, ...], ...],
    right: tuple[tuple[F, ...], ...],
    perm: tuple[int, ...],
) -> F:
    return sum(
        (left[i][j] - right[perm[i]][perm[j]]) ** 2
        for i in range(4)
        for j in range(4)
    )


def ranked_costs(a: tuple[F, F], b: tuple[F, F]):
    left, right = matrix(*a), matrix(*b)
    return sorted(
        (perm_frobenius_sq(left, right, p), p)
        for p in permutations(range(4))
    )


def min_triangle_slack(a: tuple[F, F]) -> F:
    d = matrix(*a)
    return min(
        d[i][j] + d[j][k] - d[i][k]
        for i, j, k in permutations(range(4), 3)
    )


def main() -> None:
    identity = (0, 1, 2, 3)
    swap12 = (1, 0, 2, 3)
    a1 = (F(1, 5), F(0))
    a2 = (F(1, 10), F(1, 5))
    bad = (F(1, 20), -F(1, 10))
    good_half = (F(3, 20), F(1, 10))

    for a in (a1, a2, bad, good_half):
        assert min_triangle_slack(a) > 0

    assert F(7) < F(10)

    x1_x2 = ranked_costs(a1, a2)
    x1_bad = ranked_costs(a1, bad)
    x2_bad = ranked_costs(a2, bad)
    assert x1_x2[0] == (F(1, 5), identity)
    assert x1_bad[0] == (F(13, 100), identity)
    assert x2_bad[0] == (F(13, 100), swap12)
    assert all(rows[0][0] < rows[1][0] for rows in (x1_x2, x1_bad, x2_bad))

    assert x1_x2[0][0] / 16 == F(1, 80)
    assert x1_bad[0][0] / 16 == F(13, 1600)
    assert x2_bad[0][0] / 16 == F(13, 1600)

    assert bad == tuple((a1[i] - a2[i]) / 2 for i in range(2))

    def bary_param(t: F) -> tuple[F, F]:
        return (F(1, 5) - t / 10, t / 5)

    def projection_cost(t: F) -> F:
        return ranked_costs(bad, bary_param(t))[0][0] / 16

    assert projection_cost(F(1, 2)) == F(1, 100)
    assert projection_cost(F(9, 10)) == F(1, 125)
    assert projection_cost(F(9, 10)) < projection_cost(F(1, 2))

    print("all exact checks passed")
    print("template GW^2:", F(1, 80))
    print("algorithmic weight:", (F(1, 2), F(1, 2)))
    print("true projection weight:", (F(1, 10), F(9, 10)))
    print("J(algorithmic):", F(1, 100))
    print("min J:", F(1, 125))


if __name__ == "__main__":
    main()
