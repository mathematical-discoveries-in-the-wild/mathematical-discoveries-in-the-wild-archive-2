"""Finite stress tests for the odd-projection lemma; not a proof."""

from itertools import combinations, product
from math import gcd


def primitive_2d(dx, dy):
    g = gcd(abs(dx), abs(dy))
    dx, dy = dx // g, dy // g
    if dx < 0 or (dx == 0 and dy < 0):
        dx, dy = -dx, -dy
    return dx, dy


def planar_has_odd_projection(points):
    directions = {
        primitive_2d(q[0] - p[0], q[1] - p[1])
        for p, q in combinations(points, 2)
    }
    return any(
        len({-dy * x + dx * y for x, y in points}) % 2 == 1
        for dx, dy in directions
    )


def primitive_3d(vector):
    g = 0
    for coordinate in vector:
        g = gcd(g, abs(coordinate))
    vector = tuple(coordinate // g for coordinate in vector)
    for coordinate in vector:
        if coordinate:
            return tuple(-x for x in vector) if coordinate < 0 else vector
    raise ValueError("zero vector")


def cross(u, v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def cube_has_odd_projection(points):
    differences = {
        primitive_3d(tuple(q[i] - p[i] for i in range(3)))
        for p, q in combinations(points, 2)
    }

    # A generic kernel plane containing exactly one difference direction.
    for direction in differences:
        if len({cross(direction, p) for p in points}) % 2 == 1:
            return True

    # Every exceptional kernel plane is spanned by two difference directions.
    normals = set()
    for first, second in combinations(differences, 2):
        normal = cross(first, second)
        if normal != (0, 0, 0):
            normals.add(primitive_3d(normal))
    return any(len({dot(normal, p) for p in points}) % 2 == 1 for normal in normals)


def main():
    grid = list(product(range(4), repeat=2))
    checked_grid = 0
    for size in range(2, len(grid) + 1, 2):
        for points in combinations(grid, size):
            checked_grid += 1
            assert planar_has_odd_projection(points), points

    cube = list(product(range(2), repeat=3))
    checked_cube = 0
    for size in range(2, len(cube) + 1, 2):
        for points in combinations(cube, size):
            checked_cube += 1
            assert cube_has_odd_projection(points), points

    print(f"planar grid cases checked: {checked_grid}")
    print(f"Boolean cube cases checked: {checked_cube}")
    print("no counterexample found")


if __name__ == "__main__":
    main()
