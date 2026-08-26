"""Symbolic sanity checks for the structured incompressible packet.

These finite examples do not prove the theorems.  They check the two algebraic
determinant mechanisms and one explicit inverse identity.
"""

import sympy as sp


def require_one(label: str, expression: sp.Expr) -> None:
    simplified = sp.trigsimp(sp.simplify(expression))
    print(f"{label}: {simplified}")
    if simplified != 1:
        raise AssertionError(f"{label} did not simplify to 1")


def triangular_checks() -> None:
    x, y, z, w = sp.symbols("x y z w", real=True)

    f3 = sp.Matrix(
        [
            x + y**2 + y * z + sp.sin(z),
            y + z**3,
            z + 2,
        ]
    )
    require_one("unitriangular dimension 3", f3.jacobian((x, y, z)).det())

    f4 = sp.Matrix(
        [
            x + y * z + sp.exp(w),
            y + z**2 + z * w,
            z + sp.sin(w),
            w - 3,
        ]
    )
    require_one(
        "unitriangular dimension 4", f4.jacobian((x, y, z, w)).det()
    )


def radial_twist(dimension: int) -> None:
    coordinates = sp.symbols(f"x0:{dimension}", real=True)
    radius_squared = sum(value**2 for value in coordinates)
    angle = radius_squared
    cosine, sine = sp.cos(angle), sp.sin(angle)

    image = [
        cosine * coordinates[0] - sine * coordinates[1],
        sine * coordinates[0] + cosine * coordinates[1],
        *coordinates[2:],
    ]
    jacobian = sp.Matrix(image).jacobian(coordinates)
    require_one(f"radial twist dimension {dimension}", jacobian.det())

    inverse = [
        cosine * image[0] + sine * image[1],
        -sine * image[0] + cosine * image[1],
        *image[2:],
    ]
    for original, recovered in zip(coordinates, inverse):
        if sp.trigsimp(sp.simplify(recovered - original)) != 0:
            raise AssertionError("radial inverse identity failed")
    print(f"radial inverse dimension {dimension}: verified")


if __name__ == "__main__":
    triangular_checks()
    radial_twist(2)
    radial_twist(3)
    print("all symbolic checks passed")
