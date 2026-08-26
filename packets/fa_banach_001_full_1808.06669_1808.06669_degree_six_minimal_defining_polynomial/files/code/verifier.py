#!/usr/bin/env python3
"""Exact verifier for the degree-six minimality proof.

The script works over Q(sqrt(2)) and performs no numerical approximation.  It
checks the rank-one realization classification, constructs the four possible
degree-four atoms, verifies their joint nilpotence, and proves by coefficient
rank that none has a nonzero affine-linear right symmetrizer.
"""

from itertools import product

import sympy as sp

X, Y = "x", "y"
RT2 = sp.sqrt(2)


def add(*polys):
    out = {}
    for poly in polys:
        for word, coeff in poly.items():
            out[word] = sp.expand(out.get(word, 0) + coeff)
    return {word: coeff for word, coeff in out.items() if coeff != 0}


def scale(scalar, poly):
    return {word: sp.expand(scalar * coeff) for word, coeff in poly.items()}


def multiply(left, right):
    out = {}
    for u, a in left.items():
        for v, b in right.items():
            word = u + v
            out[word] = sp.expand(out.get(word, 0) + a * b)
    return {word: coeff for word, coeff in out.items() if coeff != 0}


def adjoint(poly):
    swap = {X: Y, Y: X}
    return {
        tuple(swap[letter] for letter in reversed(word)): sp.conjugate(coeff)
        for word, coeff in poly.items()
    }


ONE = {(): sp.Integer(1)}
XP = {(X,): sp.Integer(1)}
YP = {(Y,): sp.Integer(1)}
H = add(XP, YP)
F1 = add(
    ONE,
    scale(-1, H),
    scale(-2, multiply(H, H)),
    scale(-2, multiply(YP, XP)),
    multiply(multiply(H, H), H),
    scale(2, multiply(multiply(H, H), multiply(YP, XP))),
)
S = add(ONE, scale(-1, multiply(H, H)))
F = multiply(F1, S)
assert add(F, scale(-1, adjoint(F))) == {}
assert max(map(len, F)) == 6


# L=I-Ax*x-Ay*y from Section 5.2 of the source paper.
AX = sp.Matrix(
    [
        [sp.Rational(1, 2), RT2, -sp.Rational(1, 2), 0],
        [RT2, 0, 0, 0],
        [-sp.Rational(1, 2), 0, sp.Rational(1, 2), 0],
        [-1, 0, 1, 0],
    ]
)
AY = AX.T

z, zb = sp.symbols("z zb")
L = sp.eye(4) - AX * z - AY * zb
ADJ_L = L.adjugate().applyfunc(sp.expand)


# Solve trace(M adj(L))=1 linearly.  The seven free entries are named as in
# the packet, then the rank-one condition is the vanishing of all 2x2 minors.
mvars = sp.symbols("m0:16")
M_generic = sp.Matrix(4, 4, mvars)
linear_polynomial = sp.Poly(sp.expand(sp.trace(M_generic * ADJ_L) - 1), z, zb)
linear_solution = sp.linsolve(linear_polynomial.coeffs(), mvars)

a, b, c, d, e, fpar, g = sp.symbols("a b c d e f g")
M = sp.Matrix(
    [
        [RT2 * fpar / 2 - b + 1, RT2 * e / 2 + RT2 * g / 4 - a, g - b - c - 1, e],
        [a, b, -RT2 * e / 2 - RT2 * g / 4 - d, fpar],
        [c, d, -RT2 * fpar / 2 - g, g / 2],
        [e, fpar, g / 2, g],
    ]
)
assert sp.Poly(sp.expand(sp.trace(M * ADJ_L) - 1), z, zb).is_zero

# The parametrization is exhaustive, not merely a family of solutions.
expected_linear_tuple = tuple(
    M.subs(
        {
            a: mvars[4],
            b: mvars[5],
            c: mvars[8],
            d: mvars[9],
            e: mvars[12],
            fpar: mvars[13],
            g: mvars[15],
        }
    )
)
assert linear_solution == sp.FiniteSet(expected_linear_tuple)
print("Adjugate identity: exhaustive seven-parameter affine solution verified")

minors = []
for i in range(4):
    for j in range(i + 1, 4):
        for k in range(4):
            for ell in range(k + 1, 4):
                minors.append(sp.expand(M[i, k] * M[j, ell] - M[i, ell] * M[j, k]))
minors = list(dict.fromkeys(minors))
solutions = sp.solve(minors, [a, b, c, d, e, fpar, g], dict=True, simplify=False)
solution_tuples = {
    tuple(sp.simplify(sol.get(var, var)) for var in (a, b, c, d, e, fpar, g))
    for sol in solutions
}
expected_tuples = {
    (0, 0, -1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (-RT2, -1, 0, 0, 0, 0, 0),
    (RT2, -1, 0, 0, 0, 0, 0),
}
assert solution_tuples == expected_tuples

groebner_basis = sp.groebner(
    minors, a, b, c, d, e, fpar, g, order="lex", extension=RT2
)
print("Rank-one minor ideal: lex Groebner basis")
for basis_element in groebner_basis.polys:
    print(" ", sp.factor(basis_element.as_expr(), extension=RT2))


REALIZATION_PAIRS = [
    (sp.Matrix([1, 0, -1, 0]), sp.Matrix([1, 0, 0, 0])),
    (sp.Matrix([1, 0, 0, 0]), sp.Matrix([1, 0, -1, 0])),
    (sp.Matrix([RT2, -1, 0, 0]), sp.Matrix([RT2, 1, 0, 0])),
    (sp.Matrix([RT2, 1, 0, 0]), sp.Matrix([RT2, -1, 0, 0])),
]


def realization_polynomial(v, row_as_column):
    row = row_as_column.T
    projection = sp.eye(4) - v * row
    nx, ny = AX * projection, AY * projection
    bx, by = AX * v, AY * v
    assert (row * v)[0] == 1
    assert sp.expand((row * ADJ_L * v)[0] - 1) == 0

    matrices = {X: nx, Y: ny}
    bvecs = {X: bx, Y: by}
    poly = {(): sp.Integer(1)}
    for prefix_length in range(4):
        for prefix in product((X, Y), repeat=prefix_length):
            matrix_product = sp.eye(4)
            for letter in prefix:
                matrix_product *= matrices[letter]
            for last in (X, Y):
                coeff = sp.simplify(-(row * matrix_product * bvecs[last])[0])
                if coeff != 0:
                    poly[prefix + (last,)] = sp.expand(coeff)

    # Exact joint nilpotence: every word of length four vanishes.
    for word in product((X, Y), repeat=4):
        matrix_product = sp.eye(4)
        for letter in word:
            matrix_product *= matrices[letter]
        assert matrix_product == sp.zeros(4)
    return poly


def symmetrizer_matrix(poly):
    u0r, u0i, uxr, uxi, uyr, uyi = sp.symbols(
        "u0r u0i uxr uxi uyr uyi", real=True
    )
    variables = (u0r, u0i, uxr, uxi, uyr, uyi)
    trial = {
        (): u0r + sp.I * u0i,
        (X,): uxr + sp.I * uxi,
        (Y,): uyr + sp.I * uyi,
    }
    residual = add(multiply(poly, trial), scale(-1, adjoint(multiply(poly, trial))))
    labeled_rows = []
    for word in sorted(residual, key=lambda item: (-len(item), item)):
        coeff = residual[word]
        for part, equation in (("Re", sp.re(coeff).expand()), ("Im", sp.im(coeff).expand())):
            if equation != 0:
                row = [equation.coeff(variable) for variable in variables]
                labeled_rows.append((word, part, equation, row))
    matrix = sp.Matrix([item[3] for item in labeled_rows])
    assert matrix.rank() == 6

    selected = []
    selected_matrix = sp.zeros(0, 6)
    rank = 0
    for item in labeled_rows:
        proposed = selected_matrix.col_join(sp.Matrix([item[3]]))
        proposed_rank = proposed.rank()
        if proposed_rank > rank:
            selected.append(item)
            selected_matrix = proposed
            rank = proposed_rank
        if rank == 6:
            break
    return selected, sp.simplify(selected_matrix.det())


candidates = []
determinants = []
for index, (v, row_as_column) in enumerate(REALIZATION_PAIRS, start=1):
    candidate = realization_polynomial(v, row_as_column)
    candidates.append(candidate)
    assert max(map(len, candidate)) == 4
    selected, determinant = symmetrizer_matrix(candidate)
    determinants.append(determinant)
    print(f"Candidate p_{index}: degree 4; six-row determinant {determinant}")
    for word, part, equation, _ in selected:
        print(" ", "".join(word) or "1", part, ":", equation, "= 0")

assert add(candidates[1], scale(-1, F1)) == {}
assert determinants == [64, 64, -256, 256]
print("PASS: exactly four realization candidates; no affine symmetrizer exists.")
