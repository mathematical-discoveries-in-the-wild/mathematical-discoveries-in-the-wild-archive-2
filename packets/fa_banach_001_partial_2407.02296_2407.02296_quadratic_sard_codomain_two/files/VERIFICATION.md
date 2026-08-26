# Verification Report

Status: candidate_partial_result_likely_valid.

## Mathematical checks

- Re-derived the quadratic representation from the finite-dimensional
  restriction definition and checked that weak-to-operator-norm continuity of
  Df makes both self-adjoint Hessian operators compact.
- Checked all three common-kernel cases. Rank two of the restricted linear
  part makes every derivative surjective; rank one fixes a unique projective
  multiplier and puts every critical value on one affine line; rank zero lets
  the common kernel be removed exactly.
- Verified weak compactness of the bounded multiplier incidence set. Compact
  Hessians turn weak convergence of points into norm convergence of the
  stationarity equations, and the quadratic map itself is weakly continuous on
  bounded sets.
- Expanded the two Taylor formulas and verified the slab identity

  ~~~text
  (lambda+mu) dot (f(z)-f(x))
    = <A_(lambda-mu)(z-x),z-x>.
  ~~~

- Checked that the projective sign ambiguity is harmless after choosing
  aligned unit representatives on each short arc.
- Verified the active-fiber formula in the affine chart
  `B_t=A_2-tA_1`: on `x_t+ker(B_t)`, the change in `f_2` is exactly `t`
  times the change in `f_1`.
- Rechecked both countability arguments. If the restricted quadratic form is
  nonzero, `(A_1 h_t,k_t)` is biorthogonal across distinct parameters. If it
  vanishes but the restricted linear term is nonzero, stationarity and
  self-adjointness make `(g_t,v_t)` biorthogonal. The elementary separability
  lemma then makes the set of active multiplier directions countable.
- Checked that on the complement of the active set, `f` is constant on every
  fiber of the compact incidence projection. The compact-to-Hausdorff quotient
  property therefore produces a continuous, hence uniformly continuous,
  selected critical value without requiring a unique stationary point.
- Checked the measure estimate separately on small arcs covering the
  countable active set and on its compact complement. The former has area
  bounded by a constant times total arc length; the latter is covered by
  O(1/delta) strips of area O(delta*omega(delta)), where uniform continuity
  gives omega(delta) -> 0.

## Computational sanity check

Run:

~~~text
conda run --no-capture-output -n sandbox python \
  runs/fa_banach_001/solutions/partial/2407.02296_quadratic_sard_codomain_two/code/check_slab_identity.py
~~~

The script samples finite-dimensional symmetric quadratic maps, constructs
stationary points for random multipliers, and compares both sides of the slab
identity. This is a numerical sanity check, not a proof.

## Literature boundary

The arXiv source, its January 2026 accepted-paper listing, exact-phrase web
searches, and close searches involving quadratic Sard maps, active stationary
fibers, and self-adjoint pencils were checked. No matching theorem was found.
The source still presents global quadratic Sard as expected future work.
Novelty confidence is moderate, not definitive.

## Render audit

The upgraded packet compiled in two LaTeX passes with no undefined
references, underfull boxes, overfull boxes, or warnings. All five pages were
rendered to PNG at 150 dpi and inspected at original resolution. The source
question crop is complete and readable; no clipping, overlap, broken glyphs,
or margin defects were found. The numerical script checked 2,000 random
instances and reported worst scaled identity error 3.737e-14. The final PDF
has SHA-256 digest
`955ead4d511f6440868f4edc94ef29a8ff2030fa11baf15c3b8b22211d57e056`.

## Human-review focus

Review the two biorthogonality constructions in the active-direction lemma,
the compact-incidence quotient step on the complement of the active set, and
the strip outer-measure estimate over a countable open cover. Also check
whether the unrestricted planar theorem is already implicit in
operator-pencil or caustic literature under different terminology.
