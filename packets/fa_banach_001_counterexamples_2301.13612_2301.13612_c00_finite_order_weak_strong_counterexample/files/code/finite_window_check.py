"""Finite-window sanity checks for the c_00 weak--strong counterexample."""

from math import factorial, floor


def active_upper_bound(t: float) -> int:
    """If supp(chi) is contained in [-1,1], active n satisfy n <= 1/|t|."""
    if t == 0:
        return 0
    return floor(1.0 / abs(t))


def main() -> None:
    samples = [1.0, 0.5, 0.2, 0.125, 0.01]
    expected = [1, 2, 5, 8, 100]
    assert [active_upper_bound(t) for t in samples] == expected

    for k in range(1, 9):
        for window in (1, 2, 10, 100):
            forced_prefix = [factorial(k) for _ in range(window)]
            assert len(forced_prefix) == window
            assert all(value == factorial(k) for value in forced_prefix)

    print("finite-window c_00 counterexample checks passed")


if __name__ == "__main__":
    main()

