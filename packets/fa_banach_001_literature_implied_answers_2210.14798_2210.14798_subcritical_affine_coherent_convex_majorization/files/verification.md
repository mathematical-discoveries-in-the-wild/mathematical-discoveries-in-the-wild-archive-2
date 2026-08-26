# Verification notes

1. **Exact source.** Frank's Remark 20, PDF page 25, asks whether Theorem 8
   extends to `beta in (0,1/2)`.
2. **Disk normalization.** The generalized Laguerre basis of `L^2(R_+)`
   maps to the normalized monomial basis of the RKHS with kernel
   `(1-z conjugate(w))^(-alpha)`, `alpha=2 beta`.  For a normalized vector,
   the overlap squared is `V_f=|f|^2(1-|z|^2)^alpha`, and affine Haar measure
   is four-pi times normalized hyperbolic measure.
3. **Supporting identity.** Lemma 3.2 and the closing remark after the proof
   of Theorem 1.3 in arXiv:2510.14333 identify the Dirichlet-range norm with
   `t_0^alpha + alpha integral t^(alpha-1) d nu(t)`.  Dilation gives the same
   formula for arbitrary functions in the space.
4. **Monotonicity.** Lemma 3.1 of arXiv:2510.14333, taken from Kulikov,
   says that `G(t)=t(mu(t)+1)` is nonincreasing.  Hence `nu=-dG` is positive.
5. **One-variable extremal step.** The included script symbolically verifies
   the simplification of the upper bound `Q_tau(T)`, its derivative
   `tau^(alpha-1)(T^(-alpha)-1)`, and the coherent endpoint value.
6. **Convex passage.** Finite coherent integral forces both the constant and
   linear terms at zero to vanish.  The standard hinge representation of a
   convex function therefore uses only a positive curvature measure, so
   Tonelli applies without cancellation.
7. **Equality.** The supporting paper's sharp point-evaluation theorem and
   boundary decay imply that a non-kernel unit vector has `max V_f<1`.
   The hinge comparison is then strict at every threshold in `(0,1)`.
8. **Numerical stress tests.** Before the proof route was found, exact Gamma-
   window formulas, the full second variation, noninteger power searches, and
   hinge searches on polynomial sections found only coherent kernels.  These
   checks are corroborative and are not used in the proof.
9. **Literature boundary.** Local run indexes and bounded arXiv/web searches
   through 2026-08-13 covered the exact source question, affine coherent
   states below `beta=1/2`, Dirichlet-range contractive inequalities, and the
   cited papers arXiv:1906.00223, 2205.07998, 2211.03655, 2112.09962, and
   2510.14333.  No explicit later statement of the full affine convex
   majorization was found.  arXiv:2510.14333 does not cite arXiv:2210.14798;
   the connection is the implication proved in this packet.

