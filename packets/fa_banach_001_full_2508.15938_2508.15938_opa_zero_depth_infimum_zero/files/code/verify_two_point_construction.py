import cmath
import math
import numpy as np


def check(m):
    d = m * m
    zeta = cmath.exp(2j * math.pi / d)
    points = [(zeta ** (m * k), zeta ** ((m + 1) * k)) for k in range(d)]
    assert len({(round(z.real, 12), round(z.imag, 12),
                 round(w.real, 12), round(w.imag, 12))
                for z, w in points}) == d
    for k in range(d):
        assert (m * (m * k)) % d == 0
        assert ((m - 1) * (m * k) + m * ((m + 1) * k)) % d == 0

    a, b = points[1]
    matrix = np.array([[1, 1], [a, b]], dtype=complex)
    coeff = np.linalg.solve(matrix, np.array([-1, -1], dtype=complex))
    q1, q2 = coeff
    assert abs(1 + q1 + q2) < 1e-10
    assert abs(1 + q1 * a + q2 * b) < 1e-10

    chord = abs(a - b)
    rho_inf = 1 / (abs(q1) + abs(q2))
    rho_2 = 1 / math.sqrt(abs(q1) ** 2 + abs(q2) ** 2)
    rho_1 = 1 / max(abs(q1), abs(q2))
    formula_inf = (
        math.sin(math.pi / (m * m))
        / (
            math.sin(math.pi / m)
            + math.sin(math.pi / m + math.pi / (m * m))
        )
    )
    assert abs(rho_inf - formula_inf) < 1e-11
    assert abs(chord - 2 * math.sin(math.pi / (m * m))) < 1e-11
    return rho_1, rho_2, rho_inf


print("m rho_1 rho_2 rho_inf")
for m in (3, 5, 10, 20, 50, 100):
    values = check(m)
    print(m, *(f"{x:.12g}" for x in values))
print("all_group_relations_and_depth_formulas_verified=true")
