#!/usr/bin/env python3
"""Finite-set audit of context pullbacks and spectral coverage."""


def pullback(function, point_map):
    return {point: function[image] for point, image in point_map.items()}


def main() -> None:
    # C subset D: restriction of D-characters to C-characters.
    rho_dc = {"d0": "c0", "d1": "c0", "d2": "c1"}
    f = {"c0": 7, "c1": -3}

    # A finite-dimensional representation sees d0 and d2 in D, hence both
    # characters c0 and c1 in C.
    represented_d = {"y0": "d0", "y1": "d2"}
    represented_c = {
        y: rho_dc[d] for y, d in represented_d.items()
    }

    via_c = pullback(f, represented_c)
    via_d = pullback(pullback(f, rho_dc), represented_d)
    assert via_c == via_d == {"y0": 7, "y1": -3}

    covered = set(represented_c.values())
    assert covered == set(f)
    assert all(
        any(point_map.get(y) == x for point_map in [represented_c] for y in point_map)
        for x in f
    )

    # If c1 is omitted, its point mass lies in the restriction kernel.
    missing_map = {"y0": "c0"}
    delta_c1 = {"c0": 0, "c1": 1}
    assert pullback(delta_c1, missing_map) == {"y0": 0}

    print("compatibility: passed")
    print("full spectral coverage: passed")
    print("missing-point kernel witness: passed")


if __name__ == "__main__":
    main()

