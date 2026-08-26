#!/usr/bin/env python3
"""Exhaust finite generator maps of integral l1-size at most one.

This is corroboration for the pointwise algebra in the packet, not a proof of
the profinite/condensed statement.
"""

from itertools import product


def apply_column_map(g, value):
    """Apply the linear map encoded by g to 0 or a signed basis vector."""
    if value is None:
        return None
    sign, target = value
    image = g[target]
    if image is None:
        return None
    image_sign, image_target = image
    return sign * image_sign, image_target


def check_size(n):
    values = [None] + [(sign, target) for sign in (-1, 1) for target in range(n)]
    idempotents = 0
    for g in product(values, repeat=n):
        if any(apply_column_map(g, g[s]) != g[s] for s in range(n)):
            continue
        idempotents += 1
        fixed = {t for t in range(n) if g[t] == (1, t)}
        for value in g:
            if value is not None:
                _, target = value
                assert target in fixed
        reconstructed = []
        for value in g:
            if value is None:
                reconstructed.append(None)
            else:
                sign, target = value
                reconstructed.append((sign, target))
        assert tuple(reconstructed) == g
    return idempotents


def main():
    for n in range(1, 6):
        print(f"n={n}: {check_size(n)} idempotents checked")


if __name__ == "__main__":
    main()
