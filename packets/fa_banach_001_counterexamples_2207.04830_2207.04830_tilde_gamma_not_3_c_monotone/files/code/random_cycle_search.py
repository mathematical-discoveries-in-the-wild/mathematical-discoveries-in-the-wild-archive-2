"""Finite-cycle search for the contact-set enlargement in arXiv:2207.04830.

We scale lambda=1 and use coordinates alpha=<z,u>, beta=<z,v>.  A contact
point (a,b,alpha,beta) has (a,b) in [-1,1]^2 maximizing

    F_{alpha,beta}(s,t) = st/2 + alpha*s + beta*t.

The script samples vertex and edge maximizers, adjoins the proposed point
(0,0,0,0), and exhausts coordinate permutations for each sampled finite set.
It is only a falsification search, not a proof.
"""

from __future__ import annotations

import itertools
import random


VERTICES = tuple(itertools.product((-1.0, 1.0), repeat=2))


def value(a: float, b: float, alpha: float, beta: float) -> float:
    return 0.5 * a * b + alpha * a + beta * b


def is_contact(p: tuple[float, float, float, float], tol: float = 1e-9) -> bool:
    a, b, alpha, beta = p
    target = value(a, b, alpha, beta)
    return target + tol >= max(value(s, t, alpha, beta) for s, t in VERTICES)


def vertex_contact(rng: random.Random) -> tuple[float, float, float, float]:
    while True:
        alpha = rng.uniform(-6.0, 6.0)
        beta = rng.uniform(-6.0, 6.0)
        vals = [value(a, b, alpha, beta) for a, b in VERTICES]
        a, b = VERTICES[max(range(4), key=vals.__getitem__)]
        p = (a, b, alpha, beta)
        if is_contact(p):
            return p


def edge_contact(rng: random.Random) -> tuple[float, float, float, float]:
    # Choose one fixed boundary coordinate and force zero slope in the other.
    for _ in range(10000):
        side = rng.randrange(4)
        t = rng.uniform(-1.0, 1.0)
        free = rng.uniform(-6.0, 6.0)
        if side == 0:  # b=1, a free, hence alpha=-1/2
            p = (t, 1.0, -0.5, free)
        elif side == 1:  # b=-1, a free, hence alpha=1/2
            p = (t, -1.0, 0.5, free)
        elif side == 2:  # a=1, b free, hence beta=-1/2
            p = (1.0, t, free, -0.5)
        else:  # a=-1, b free, hence beta=1/2
            p = (-1.0, t, free, 0.5)
        if is_contact(p):
            return p
    raise RuntimeError("failed to sample an edge contact point")


def cyclic_gap(points: list[tuple[float, float, float, float]], pa, pb) -> float:
    original = sum(value(a, b, alpha, beta) for a, b, alpha, beta in points)
    permuted = 0.0
    for j, (_, _, alpha, beta) in enumerate(points):
        a = points[pa[j]][0]
        b = points[pb[j]][1]
        permuted += value(a, b, alpha, beta)
    return original - permuted


def main() -> None:
    rng = random.Random(220704830)
    zero = (0.0, 0.0, 0.0, 0.0)
    best = (float("inf"), None)
    for count in range(2, 7):  # number of nonzero contact points
        perms = list(itertools.permutations(range(count + 1)))
        trials = 3000 if count <= 3 else 12000
        for trial in range(trials):
            points = [zero]
            for _ in range(count):
                sampler = edge_contact if rng.random() < 0.35 else vertex_contact
                points.append(sampler(rng))
            if count <= 3:
                pairs = itertools.product(perms, repeat=2)
            else:
                pairs = ((rng.choice(perms), rng.choice(perms)) for _ in range(300))
            for pa, pb in pairs:
                if pa == tuple(range(count + 1)) and pb == pa:
                    continue
                gap = cyclic_gap(points, pa, pb)
                if gap < best[0]:
                    best = (gap, (points, pa, pb))
                if gap < -1e-9:
                    print("COUNTEREXAMPLE", gap, points, pa, pb)
                    return
        print("count", count, "best_gap", best[0])
    print("NO_COUNTEREXAMPLE", best)


if __name__ == "__main__":
    main()
