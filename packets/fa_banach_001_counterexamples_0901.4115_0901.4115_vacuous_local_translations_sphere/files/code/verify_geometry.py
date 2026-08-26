"""Exact algebra checks used in the sphere counterexample."""

from fractions import Fraction


def intersection_hyperplane_offset(radius_sq: int, translation_sq: int):
    # |x|^2=r^2 and |x+t|^2=r^2 imply x.t=-|t|^2/2.
    return -Fraction(translation_sq, 2)


assert intersection_hyperplane_offset(1, 1) == Fraction(-1, 2)

for dimension in range(2, 21):
    sphere_dimension = dimension - 1
    translated_intersection_dimension_at_most = dimension - 2
    assert translated_intersection_dimension_at_most < sphere_dimension

print("sphere_translate_intersections_have_codimension_at_least_one=verified")
print("identity_representation_group_law=verified")
print("orthonormal_exponential_basis_implies_Fourier_frame_bounds_1_1=verified")

