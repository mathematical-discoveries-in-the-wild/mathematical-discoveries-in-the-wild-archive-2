"""Finite-window checks for the infinite-empty-word transition matrix.

This is not a proof of the limiting assertions.  It mechanically checks the
column formula, parent paths, and the predicted fixed-coordinate stabilization
over growing finite windows.
"""

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Symbol:
    kind: str
    j: int = 0
    k: int = 0


O = Symbol("o")


def B(j: int) -> Symbol:
    return Symbol("b", j)


def V(j: int, k: int) -> Symbol:
    return Symbol("v", j, k)


def parent(x: Symbol) -> Symbol:
    if x.kind == "b":
        return O if x.j == 1 else B(x.j // 2)
    if x.kind == "v":
        return B(x.j) if x.k == 1 else V(x.j, x.k - 1)
    raise ValueError("the hub has no parent")


def children(x: Symbol) -> set[Symbol]:
    if x == O:
        return {B(1)}
    if x.kind == "b":
        return {B(2 * x.j), B(2 * x.j + 1), V(x.j, 1)}
    return {V(x.j, x.k + 1)}


def column(x: Symbol) -> set[Symbol]:
    result = {O} | children(x)
    if x.kind == "v":
        result.add(B(x.j))
    return result


def reaches_hub(x: Symbol) -> bool:
    seen = set()
    while x != O and x not in seen:
        seen.add(x)
        x = parent(x)
    return x == O


def main() -> None:
    symbols = [O]
    symbols += [B(j) for j in range(1, 65)]
    symbols += [V(j, k) for j in range(1, 17) for k in range(1, 33)]

    assert all(len(column(x)) <= 4 for x in symbols)
    assert all(reaches_hub(x) for x in symbols)
    assert all(O in column(x) for x in symbols)

    # On any fixed finite coordinate window, a ray column stabilizes to
    # {o,b_j}, and classes with j escaping stabilize to {o}.
    for j in range(1, 9):
        window = {O} | {B(i) for i in range(1, 9)} | {
            V(i, k) for i in range(1, 9) for k in range(1, 9)
        }
        assert column(V(j, 64)) & window == {O, B(j)}
    for j in range(65, 81):
        assert column(B(j)) & window == {O}
        assert column(V(j, 1)) & window == {O}

    print("finite-window construction checks passed")


if __name__ == "__main__":
    main()
