# Verification report

Status: candidate full positive answer, likely valid pending human review.

## Mathematical audit

- Metric identification: the lower/upper dimensions 4 and `2k+2` belong to
  the Carnot--Caratheodory metric.  CLOW's displayed quasi-distance `d` is
  comparable to `Vol(B_cc(x,d_cc(x,y)))`.
- Homogeneity: both horizontal fields have degree 1 under weights
  `(1,1,2k)`.
- Rank: `[X1,X2]=-2k(x^2+y^2)^(k-1) d_t`, and the `2k`-fold commutator
  obtained by another `2k-2` brackets with `X1` is a nonzero multiple of
  `d_t` at the origin.
- Global theorem: Theorem 7.6 of Biagi--Bonfiglioli--Bramanti assumes exactly
  1-homogeneity and the rank condition at the origin and gives a uniform
  global `(1,1)` inequality on every doubled control ball.
- Lipschitz passage: differentiation along the two unit-speed flows gives
  `|Xi f| <= lip f` almost everywhere.  Horizontal Sobolev density permits
  passage from smooth functions to control-metric Lipschitz functions.
- Exponent: Holder converts the average of `|Xf|` into its fourth-power
  average, giving the requested `(1,4)` inequality with dilation factor 2.
- Completeness: control balls are Euclidean bounded by direct integration
  of the horizontal ODE and are compact by the ball-box topology theorem.
- Dimensions: `V((z,t),r) ~= r^4(|z|+r)^(2k-2)` gives the ratio bounds with
  exponents 4 and `2k+2`.

## Computational audit

`code/verify_geometry.py` symbolically checks the bracket, terminal vertical
commutator, and dilation homogeneity for `k=2,...,8`.

## Novelty audit

Bounded run-index and web searches on August 17, 2026 covered the exact
question, all three relevant arXiv ids, the displayed fields, `partial
Omega_k`, and global Poincare inequalities for homogeneous Hormander fields.
No later explicit answer to the source question was found.  Novelty
confidence is low-to-moderate because the application appears unrecorded but
the global theorem and the remaining analytic ingredients are classical.

## Artifact audit

- The final packet compiled through `latexmk` with no LaTeX, package,
  overfull-box, underfull-box, citation, or reference warning.
- The output has four letter-size pages.  It was rendered at 144 dpi after
  the final crop and text edits, and all four pages were visually inspected.
  The source question, supporting theorem crop, formulas, page breaks,
  margins, and references are legible and unclipped.
- PDF SHA-256:
  `bde6e05f6e3dcce4174eb43da5e251d700728ca2a6cb24d4b581cd9555c74d37`.
