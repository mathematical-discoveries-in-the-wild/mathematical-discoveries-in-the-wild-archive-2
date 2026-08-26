# Quantum confinement at generic tangency points

Status: `candidate_full_solution_likely_valid_needs_human_review`.

This packet gives an affirmative answer to the tangency-point question on
page 5 of Ivan Beschastnyi, Ugo Boscain, and Eugenio Pozzoli, *Quantum
confinement for the curvature Laplacian on 2D-almost-Riemannian manifolds*,
arXiv:2011.03300v2.

For a compact generic two-dimensional almost-Riemannian structure, the
ordinary Laplace--Beltrami operator on each connected component of the
regular set is essentially self-adjoint even when isolated tangency points
are present.  Thus generic tangencies do not destroy quantum confinement.

The new issue is the quadratic tangency normal form

`X_1 = d_x,   X_2 = (y-x^2 psi(x)) exp(Psi(x,y)) d_y`.

For the canonical model, the upper component has an exact transverse Hardy
identity.  Writing `r=x/sqrt(y)`, it yields

`int |u_x|^2/(y-x^2) >= 3 int y |u|^2/(y-x^2)^3`.

The associated boundary gauge `(y-x^2)/sqrt(y)` has squared horizontal
gradient strictly below `3` in a central parabolic cone.  Ordinary Grushin
collars cover the two edge cones.  On the lower component, the vertical cone
is a complete logarithmic end, while in the horizontal cones a weighted
completion of squares gives a coefficient tending to `9/4`, strictly above
the Agmon threshold `1`.  Logarithmic angular partitions make all IMS errors
smaller than these margins.  The argument is stable under the smooth terms
in the generic normal form.

`code/verify_tangency_hardy.py` checks the exact algebraic identities with
SymPy.  It is an audit aid, not part of the analytic proof.

Human review should concentrate on Lemma 2 in `main.tex`: the boundary-local
Agmon/IMS patching lemma and the stated uniformity of the smooth-normal-form
perturbation.  The exact model identities are elementary and independently
symbolically verified.  The theorem concerns the standard generic case of
isolated quadratic tangencies; it does not claim a result for arbitrarily
flat, non-generic singular contacts.
