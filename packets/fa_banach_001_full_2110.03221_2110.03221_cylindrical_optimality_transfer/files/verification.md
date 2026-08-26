# Verification report

Verdict: candidate full result, likely valid pending specialist review.

## Embedded hard subclass

Choose a fixed nonzero `g in C_c^2((-1,1))`. After a fixed rescaling of the
amplitudes, the tensor map

`Ju(x,t)=u(x)g(t)/||g||_2`

maps the ordinary 3D C2 cartoon class into the source's 4D class `E(A)`. The
surface class is exactly compatible: its boundaries are C2 2-manifolds in the
three spatial coordinates. The map is an L2 isometry.

## Projection of approximation schemes

The adjoint `J*` is contraction and satisfies `J*J=I`. For every N-term
approximant `A_N(Ju)`, therefore,

`||u-J*A_N(Ju)||_2 <= ||Ju-A_N(Ju)||_2`.

Projecting each selected atom preserves its index and the polynomial-depth
selection rule. Projected atoms have norm at most one; zero atoms can be
deleted, and nonzero atoms normalized with the norm absorbed into the scalar
coefficient. Hence any forbidden 4D exponent would produce the same forbidden
3D exponent.

## Lower benchmark and upper match

The standard information-theoretic optimality theorem for ordinary 3D C2
cartoons says that no representation scheme under polynomial-depth search can
uniformly attain squared L2 error `O(N^{-1-epsilon})` for any positive
`epsilon`. The projection argument transfers this benchmark to `E(A)`. The
source proves `O(N^{-1}(log N)^2)` for cylindrical shearlets, so exponent one
is optimal up to logarithms.

## Literature and scope

Bounded exact-title, exact-conjecture, and cylindrical-cartoon optimality
searches on 13 August 2026 found no explicit later answer for this 4D class.
Bubba--Heikkila--Labate--Ratti (arXiv:2405.06337) proves an analogous optimality
result for a distinct L2(R3) class of two-spatial-dimensional cartoons evolving
in time; its exponent is two. The present transfer is short, so novelty
confidence is modest.

The theorem uses the same polynomial-depth notion of feasibility as the
optimality literature cited by the source. With completely unrestricted
dictionaries, universal N-term lower bounds are meaningless because one can
enumerate arbitrarily fine nets. The result proves the optimal power exponent,
not removal of the logarithmic gap.

