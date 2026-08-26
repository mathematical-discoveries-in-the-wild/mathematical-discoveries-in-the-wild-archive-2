"""Non-proof sanity checks for the five-digit irrational-mask packet."""

import sympy as sp


def mask_checks() -> None:
    z = sp.symbols("z")
    polynomial = 1 + z + z**3 + z**5 + z**6
    reciprocal_cubic = sp.symbols("x") ** 3 + sp.symbols("x") ** 2 - 3 * sp.symbols("x") - 1
    print("mask polynomial:", polynomial)
    print("factor over Q:", sp.factor(polynomial))
    print("factor mod 3:", sp.factor(polynomial, modulus=3))
    print("reciprocal cubic roots:", sp.nroots(reciprocal_cubic))


def bounded_formal_clique_check() -> None:
    import networkx as nx

    x = sp.symbols("x")
    examples = [x, 1 / x, x + 1 / x, (x**2 + 1) / (x + 1), 2 + 1 / x]
    evaluation_point = sp.Rational(27, 10)

    for rational_function in examples:
        formal_set = {
            sp.cancel(x**k * (rational_function + n))
            for k in range(1, 7)
            for n in range(-5, 6)
        }
        elements = list(formal_set)
        values = [sp.N(item.subs(x, evaluation_point)) for item in elements]
        graph = nx.Graph()
        graph.add_nodes_from(range(len(elements)))

        for i in range(len(elements)):
            for j in range(i + 1, len(elements)):
                high, low = (i, j) if values[i] > values[j] else (j, i)
                if sp.cancel(elements[high] - elements[low]) in formal_set:
                    graph.add_edge(i, j)

        maximum = max(nx.find_cliques(graph), key=len)
        print(rational_function, "bounded maximum clique:", len(maximum))


if __name__ == "__main__":
    mask_checks()
    bounded_formal_clique_check()
