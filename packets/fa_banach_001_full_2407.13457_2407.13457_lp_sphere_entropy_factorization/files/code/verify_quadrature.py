"""Deterministic quadrature smoke tests for the full entropy inequality.

This is supporting QA, not part of the proof.  It checks n=3, uniform weights
on the three two-coordinate blocks (so theta_**=1/3), five symmetric
Dirichlet parameters including boundary-singular cases, and three genuinely
sign-dependent positive test functions.  Gauss-Jacobi quadrature integrates
the Beta conditional laws.
"""

from itertools import product

import numpy as np
from scipy.special import beta, roots_jacobi


SIGNS = np.array(list(product((-1.0, 1.0), repeat=3)))


def beta_rule(a: float, b: float, order: int = 90):
    """Nodes and normalized weights for Beta(a,b) on [0,1]."""
    x, w = roots_jacobi(order, b - 1.0, a - 1.0)
    u = (x + 1.0) / 2.0
    scale = 2.0 ** (-(a + b - 1.0)) / beta(a, b)
    return u, w * scale


def test_function(kind: int, z: np.ndarray, s: np.ndarray) -> float:
    if kind == 0:
        logf = 0.7 * s[0] * np.sqrt(z[0]) - 0.45 * s[1] * z[1] ** 0.3
        logf += 0.55 * s[0] * s[2] * z[2]
    elif kind == 1:
        logf = 0.4 * s[0] * s[1] * np.sqrt(z[0] * z[1])
        logf += 0.65 * s[2] * z[2] ** 0.2 + 0.3 * z[0] * z[1]
    else:
        logf = 0.35 * sum(s[i] * z[(i + 1) % 3] ** 0.4 for i in range(3))
        logf += 0.6 * s.prod() * (z.prod() ** 0.15)
    return float(np.exp(logf))


def expectation_full(alpha: float, kind: int):
    # Stick breaking: z0=v, z1=(1-v)u, z2=(1-v)(1-u),
    # v~Beta(alpha,2alpha), u~Beta(alpha,alpha), independently.
    vs, vw = beta_rule(alpha, 2 * alpha)
    us, uw = beta_rule(alpha, alpha)
    mean = elog = 0.0
    for v, wv in zip(vs, vw):
        for u, wu in zip(us, uw):
            z = np.array([v, (1 - v) * u, (1 - v) * (1 - u)])
            weight = wv * wu / 8.0
            for s in SIGNS:
                f = test_function(kind, z, s)
                mean += weight * f
                elog += weight * f * np.log(f)
    return mean, elog - mean * np.log(mean)


def entropy_conditional_expectation(alpha: float, kind: int, fixed: int):
    # E_A f is indexed by the singleton complement coordinate `fixed`.
    qs, qw = beta_rule(alpha, 2 * alpha)
    us, uw = beta_rule(alpha, alpha)
    mean_h = elog_h = 0.0
    moving = [i for i in range(3) if i != fixed]
    for q, wq in zip(qs, qw):
        for sfixed in (-1.0, 1.0):
            h = 0.0
            for u, wu in zip(us, uw):
                z = np.zeros(3)
                z[fixed] = q
                z[moving[0]] = (1 - q) * u
                z[moving[1]] = (1 - q) * (1 - u)
                for smoving in product((-1.0, 1.0), repeat=2):
                    s = np.zeros(3)
                    s[fixed] = sfixed
                    s[moving] = smoving
                    h += wu * test_function(kind, z, s) / 4.0
            weight = wq / 2.0
            mean_h += weight * h
            elog_h += weight * h * np.log(h)
    return elog_h - mean_h * np.log(mean_h)


def main():
    worst_slack = float("inf")
    cases = 0
    for alpha in (0.2, 0.5, 1.0, 2.0, 5.0):
        for kind in range(3):
            _, ent_f = expectation_full(alpha, kind)
            marginal_entropies = [
                entropy_conditional_expectation(alpha, kind, j) for j in range(3)
            ]
            # For theta uniform on the three pairs, RHS conditional entropy is
            # Ent(f) - average_j Ent(E_{[3]\{j}} f).
            rhs = ent_f - sum(marginal_entropies) / 3.0
            slack = rhs - ent_f / 3.0
            if slack < -2e-10:
                raise AssertionError((alpha, kind, ent_f, rhs, slack))
            worst_slack = min(worst_slack, slack)
            cases += 1
    print(f"passed {cases} deterministic quadrature cases; min slack={worst_slack:.6e}")


if __name__ == "__main__":
    main()
