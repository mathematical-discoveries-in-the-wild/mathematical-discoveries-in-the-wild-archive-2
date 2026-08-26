"""Exact checks for the squared-binomial Hahn identity used in the packet.

Run with:
    conda run --no-capture-output -n sandbox python verify_hahn_identity.py
"""

import sympy as sp


def verify(max_n: int = 12) -> None:
    x = sp.symbols("x")
    for n in range(1, max_n + 1):
        nu = [sp.binomial(n, k) ** 2 / sp.binomial(2 * n, n)
              for k in range(n + 1)]
        hahn = []
        reciprocal_norms = []
        for j in range(n + 1):
            polynomial = sum(
                sp.rf(-j, r) * sp.rf(j - 2 * n - 1, r) * sp.rf(-x, r)
                / (sp.rf(-n, r) ** 2 * sp.factorial(r))
                for r in range(j + 1)
            )
            polynomial = sp.expand_func(sp.simplify(polynomial))
            assert polynomial.subs(x, 0) == 1
            expected_reciprocal = (
                sp.binomial(2 * n, j)
                - (sp.binomial(2 * n, j - 1) if j else 0)
            )
            norm = sp.simplify(sum(
                nu[k] * polynomial.subs(x, k) ** 2
                for k in range(n + 1)
            ))
            assert sp.simplify(norm - 1 / expected_reciprocal) == 0
            for previous in hahn:
                cross = sp.simplify(sum(
                    nu[k] * polynomial.subs(x, k) * previous.subs(x, k)
                    for k in range(n + 1)
                ))
                assert cross == 0
            hahn.append(polynomial)
            reciprocal_norms.append(expected_reciprocal)
            assert sum(reciprocal_norms) == sp.binomial(2 * n, j)
        print(f"n={n}: all degrees verified")


if __name__ == "__main__":
    verify()

