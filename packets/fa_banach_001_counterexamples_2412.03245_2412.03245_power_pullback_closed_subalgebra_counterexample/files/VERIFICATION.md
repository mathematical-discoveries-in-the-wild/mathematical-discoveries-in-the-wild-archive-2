# Verification

Status: `candidate_counterexample_likely_valid`

## Mathematical checks

- `z -> z^m` is onto the unit disc, hence `||g(z^m)||_infinity=||g||_infinity`.
- The pullback map `J_m` is injective, unital, linear, and multiplicative, so
  its range is a closed unital subalgebra.
- `T_{a,m}=J_m C_{tau_a} J_m^{-1}` is therefore a well-defined isometric
  algebra automorphism, with inverse obtained from `tau_a^{-1}`.
- The test element `u(z)=z^m` lies in the subalgebra and satisfies
  `T_{a,m}u=tau_a(z^m)`.
- For `a != 0`, the equation `z^m=a` has `m` distinct nonzero roots in the
  disc.  The derivative of `tau_a(z^m)` is nonzero at each, so all are simple.
- Every zero of `phi^m` has multiplicity divisible by `m`.  Therefore
  `phi^m=tau_a(z^m)` is impossible for every analytic `phi`.

## Novelty/status checks

- Cheap indexes: no hit for arXiv:2412.03245 or the exact conjecture.
- Local parsed arXiv corpus: exact title/id/conjecture and power-pullback
  searches.
- Web: exact title, exact conjecture, correction/comment, and `g(z^m)`
  subalgebra searches in arXiv-indexed results through 2026-08-11.
- No later correction, answer, or prior statement of this construction was
  found.  Novelty confidence is medium because the construction is elementary.

## Artifact QA

- The source paper was compiled from the existing local arXiv source bundle
  after the external PDF download was unavailable.
- Source conjecture crop visually inspected.
- Packet LaTeX compiled with no undefined references or overfull boxes.
- Every rendered packet page visually inspected.
