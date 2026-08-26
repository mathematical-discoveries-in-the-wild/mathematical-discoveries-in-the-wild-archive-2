"""Symbolically audit the three sl(2,R) orbit kernels in the packet."""

import sympy as sp


def determinant_kernel(x_matrix: sp.Matrix, v: sp.Matrix, u: sp.Symbol) -> sp.Expr:
    row_u = (v.T * sp.exp(u * x_matrix))
    row_0 = v.T
    return sp.simplify(sp.det(sp.Matrix.vstack(row_u, row_0)) / u)


def main() -> None:
    u, a = sp.symbols("u a", positive=True, real=True)
    cases = {
        "elliptic": (sp.Matrix([[0, -a], [a, 0]]), sp.Matrix([1, 0]), sp.sin(a * u) / u),
        "parabolic": (sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([1, 0]), -1),
        "hyperbolic": (sp.Matrix([[a, 0], [0, -a]]), sp.Matrix([1, 1]), 2 * sp.sinh(a * u) / u),
    }
    for name, (matrix, vector, expected) in cases.items():
        actual = determinant_kernel(matrix, vector, u)
        assert sp.simplify(actual - expected) == 0, (name, actual, expected)
        print(f"{name}: {actual}")

    d = sp.symbols("d", positive=True, real=True)
    hyperbolic_gram_det = sp.simplify(1 - (sp.sinh(a * d) / (a * d)) ** 2)
    assert hyperbolic_gram_det.subs({a: 1, d: 1}) < 0
    print(f"hyperbolic normalized two-point Gram determinant: {hyperbolic_gram_det} < 0")


if __name__ == "__main__":
    main()
