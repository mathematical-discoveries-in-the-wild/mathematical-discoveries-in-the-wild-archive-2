"""Exhaustively verify the binary signed-graph theorem for three vertices.

For each sign pattern on the triangle and each subset Gamma of {0,1}^3,
we use finite linear programming to test whether Gamma is c-splitting (hence
c-cyclically monotone in this finite setting), and then test cyclical
monotonicity of its three two-coordinate projections.  The universal
projection property should hold exactly for balanced sign patterns.
"""

from itertools import combinations, product

import numpy as np
from scipy.optimize import linprog


POINTS = list(product((0, 1), repeat=3))
EDGES = ((0, 1), (0, 2), (1, 2))


def cost(x, signs):
    return sum(sign * x[i] * x[j] for sign, (i, j) in zip(signs, EDGES))


def is_splitting(gamma, signs):
    """Test existence of node potentials dominating c, equal on Gamma."""
    # Variables are u_i(0),u_i(1), i=0,1,2.
    a_ub = []
    b_ub = []
    for x in POINTS:
        row = np.zeros(6)
        for i in range(3):
            row[2 * i + x[i]] = -1
        a_ub.append(row)
        b_ub.append(-cost(x, signs))

    a_eq = []
    b_eq = []
    for x in gamma:
        row = np.zeros(6)
        for i in range(3):
            row[2 * i + x[i]] = 1
        a_eq.append(row)
        b_eq.append(cost(x, signs))

    result = linprog(
        np.zeros(6),
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=np.asarray(a_eq) if a_eq else None,
        b_eq=np.asarray(b_eq) if b_eq else None,
        bounds=[(None, None)] * 6,
        method="highs",
    )
    return result.success


def projection_is_cyclic(gamma, edge, sign):
    """On two binary coordinates, test every permutation inequality."""
    projection = {(x[edge[0]], x[edge[1]]) for x in gamma}
    for (a, b), (c, d) in combinations(projection, 2):
        original = sign * (a * b + c * d)
        swapped = sign * (a * d + c * b)
        if swapped > original:
            return False
    return True


def main():
    for signs in product((-1, 1), repeat=3):
        universal = True
        witness = None
        for mask in range(1 << len(POINTS)):
            gamma = [x for k, x in enumerate(POINTS) if mask & (1 << k)]
            if not is_splitting(gamma, signs):
                continue
            if not all(
                projection_is_cyclic(gamma, edge, sign)
                for edge, sign in zip(EDGES, signs)
            ):
                universal = False
                witness = gamma
                break

        balanced = np.prod(signs) == 1
        print(
            f"signs={signs} balanced={balanced} universal={universal}"
            + (f" witness={witness}" if witness is not None else "")
        )
        assert universal == balanced


if __name__ == "__main__":
    main()
