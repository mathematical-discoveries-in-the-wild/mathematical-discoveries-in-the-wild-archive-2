#!/usr/bin/env python3
"""Exact finite checks for the C3 Lip_p state-span counterexample."""

from fractions import Fraction


X = range(3)
DIST = (
    (0, 1, 2),
    (1, 0, 1),
    (2, 1, 0),
)


def push(mu, x):
    """Push mu under g -> x+g mod 3."""
    out = [Fraction(0) for _ in X]
    for g, mass in enumerate(mu):
        out[(x + g) % 3] += mass
    return tuple(out)


def min_transport_cost(alpha, beta, power):
    """Successive shortest augmenting paths, with exact rational capacities."""
    source, sink = 6, 7
    n = 8
    graph = [[] for _ in range(n)]

    def add_edge(u, v, cap, cost):
        graph[u].append([v, len(graph[v]), cap, cost])
        graph[v].append([u, len(graph[u]) - 1, Fraction(0), -cost])

    for i, mass in enumerate(alpha):
        add_edge(source, i, mass, 0)
    for i in X:
        for j in X:
            add_edge(i, 3 + j, Fraction(1), DIST[i][j] ** power)
    for j, mass in enumerate(beta):
        add_edge(3 + j, sink, mass, 0)

    flow = Fraction(0)
    cost = Fraction(0)
    while flow < 1:
        dist = [None] * n
        prev = [None] * n
        dist[source] = Fraction(0)
        for _ in range(n - 1):
            changed = False
            for u in range(n):
                if dist[u] is None:
                    continue
                for ei, edge in enumerate(graph[u]):
                    v, _rev, cap, edge_cost = edge
                    candidate = dist[u] + edge_cost
                    if cap > 0 and (dist[v] is None or candidate < dist[v]):
                        dist[v] = candidate
                        prev[v] = (u, ei)
                        changed = True
            if not changed:
                break
        assert dist[sink] is not None

        amount = Fraction(1) - flow
        v = sink
        while v != source:
            u, ei = prev[v]
            amount = min(amount, graph[u][ei][2])
            v = u
        v = sink
        while v != source:
            u, ei = prev[v]
            edge = graph[u][ei]
            rev = edge[1]
            edge[2] -= amount
            graph[v][rev][2] += amount
            v = u
        flow += amount
        cost += amount * dist[sink]
    return cost


def det3(rows):
    a, b, c = rows
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def verify_power(power):
    one_third = Fraction(1, 3)
    h = (one_third, one_third, one_third)
    epsilon = Fraction(1, 2 ** (power + 3))
    mu0 = h
    mu1 = (one_third + epsilon, one_third, one_third - epsilon)
    mu2 = (one_third, one_third + epsilon, one_third - epsilon)
    states = (mu0, mu1, mu2)
    assert det3(states) == epsilon * epsilon

    checked = 0
    for mu in states:
        for x in X:
            for y in X:
                cost = min_transport_cost(push(mu, x), push(mu, y), power)
                assert cost <= DIST[x][y] ** power
                checked += 1

    delta_one = (Fraction(0), Fraction(1), Fraction(0))
    bad_cost = min_transport_cost(push(delta_one, 1), push(delta_one, 2), power)
    assert bad_cost == 2 ** power
    assert bad_cost > DIST[1][2] ** power
    return checked, epsilon, bad_cost


def main():
    total = 0
    for power in (1, 2, 3, 4, 5, 8):
        checked, epsilon, bad_cost = verify_power(power)
        total += checked
        print(
            f"p={power}: {checked} good transport inequalities; "
            f"epsilon={epsilon}; bad p-cost={bad_cost}"
        )
    print(f"PASS: {total} exact good-state transport checks plus 6 violations")


if __name__ == "__main__":
    main()

