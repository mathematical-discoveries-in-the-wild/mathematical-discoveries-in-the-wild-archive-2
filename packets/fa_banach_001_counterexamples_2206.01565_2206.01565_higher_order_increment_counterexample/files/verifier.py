"""Exact finite-set verifier for the arXiv:2206.01565 counterexample."""

from itertools import product


Point = tuple[int, int]


def minkowski(a: set[Point], b: set[Point]) -> set[Point]:
    return {(x + u, y + v) for (x, y), (u, v) in product(a, b)}


def iterate_delta(e: set[Point], increments: list[set[Point]]):
    stages = [e]
    for p in increments:
        e = minkowski(e, p) - e
        stages.append(e)
    return stages


def subset_sum(increments: list[set[Point]], mask: int) -> set[Point]:
    result = {(0, 0)}
    for i, p in enumerate(increments):
        if mask & (1 << i):
            result = minkowski(result, p)
    return result


def main() -> None:
    e0 = {(-1, 0), (1, -2), (-1, -2)}
    increments = [
        {(-2, 0), (-2, -1), (0, 0)},
        {(1, 0), (0, 0)},
        {(1, -1), (0, 0)},
        {(0, -1), (0, 0)},
        {(2, -1), (-1, -1), (0, 0)},
    ]

    stages = iterate_delta(e0, increments)
    expected_stages = [
        {(-1, 0), (1, -2), (-1, -2)},
        {(-3, -3), (-3, -2), (-3, -1), (-3, 0), (-1, -3)},
        {(-2, -3), (-2, -2), (-2, -1), (-2, 0), (0, -3)},
        {(-1, -4), (-1, -3), (-1, -2), (-1, -1), (1, -4)},
        {(-1, -5), (1, -5)},
        {(-2, -6), (0, -6), (1, -6), (3, -6)},
    ]
    assert stages == expected_stages

    cardinalities = []
    totals_by_size = [0] * 6
    alternating = 0
    for mask in range(32):
        size = len(minkowski(e0, subset_sum(increments, mask)))
        cardinalities.append(size)
        totals_by_size[mask.bit_count()] += size
        alternating += (-1) ** (5 - mask.bit_count()) * size

    assert cardinalities == [
        3, 8, 6, 16, 6, 16, 12, 26,
        6, 12, 12, 24, 12, 24, 18, 33,
        9, 22, 17, 34, 16, 35, 26, 45,
        16, 30, 26, 43, 27, 44, 35, 55,
    ]
    assert totals_by_size == [3, 35, 151, 270, 200, 55]
    assert alternating == 6
    assert len(stages[-1]) == 4
    assert len(stages[-1]) < alternating

    print("stage_cardinalities =", [len(stage) for stage in stages])
    print("subset_cardinalities =", cardinalities)
    print("totals_by_subset_size =", totals_by_size)
    print("lhs_coefficient =", len(stages[-1]))
    print("rhs_coefficient =", alternating)
    print("deficit =", len(stages[-1]) - alternating)
    print("PASS")


if __name__ == "__main__":
    main()
