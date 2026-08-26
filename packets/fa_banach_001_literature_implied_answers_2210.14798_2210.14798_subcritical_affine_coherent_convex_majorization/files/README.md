# Subcritical affine coherent-state inequality

Status: `literature_implied_answer (full affirmative answer in the natural finite-value regime)`.

Rupert Frank asks in Remark 20 of arXiv:2210.14798 whether his affine
coherent-state Theorem 8 extends to `0 < beta < 1/2`.  It does.  With
`alpha=2 beta`, the affine transform is the Dirichlet-range RKHS
`A_alpha^2`, and the missing norm constraint is the renormalized level-set
identity proved by Brevig--Kulikov--Seip--Zlotnikov in arXiv:2510.14333.
Combining that identity with Kulikov's hyperbolic level-set monotonicity gives
every hinge inequality `(u^2-s)_+`; integration against the curvature measure
of a convex function gives the full convex inequality and the optimizer
classification.

The later authors do not cite arXiv:2210.14798 or state the affine coherent-
state consequence.  The status is therefore literature-implied rather than
literature-already-answered.  The packet contains the complete implication,
including the one-variable extremal calculation.

The exact formula is meaningful as a finite variational statement precisely
when the coherent-state integral is finite.  For nonnegative convex functions
with infinite coherent-state integral, both sides of the supremum formula are
`+infinity` because a coherent state already realizes that value.  Signed
divergent integrals are excluded as undefined.

Human review should focus on the Stieltjes form of the renormalized norm
identity and the passage from the disk RKHS back to the affine normalization.

