# Hölder fixed-point retractions in strongly convex Banach spaces

Status: `candidate_partial_likely_valid`

Source: Andrzej Wiśnicki, *Hölder continuous retractions and amenable
semigroups of uniformly Lipschitzian mappings in Hilbert spaces*,
arXiv:1204.6464, final problem, PDF page 6.

## Result

The source asks whether, under the Goebel--Kirk uniformly convex hypotheses,
the fixed-point set is a Lipschitz or Hölder retract. The unrestricted problem
is not resolved here.

This packet proves a quantitative non-Hilbert subcase. Suppose the squared
norm of a reflexive Banach space has strong-convexity constant `c`, in the
precise subgradient sense stated in the packet. If a discrete left amenable
semigroup is uniformly `k`-Lipschitzian on a bounded closed convex set and

`k^2 < 2c`,

then its common fixed-point set is a Hölder retract. In particular, by the
sharp Ball--Carlen--Lieb inequality, this holds in `L^p`, `3/2<p<=2`, whenever
`k<sqrt(2(p-1))`. Applying the theorem to the power semigroup of one map gives
a substantial subcase of the source's final problem for every
`3/2<p<2`.

The construction uses the vector barycenter of an invariant mean. It is
`k`-Lipschitz. Strong convexity replaces the Hilbert-space variance identity
and makes its iterates converge geometrically; the standard balance between
geometric tails and `k^n` then gives a Hölder limit.

## Evidence and verification

- `source_paper.pdf`: the complete canonical arXiv TeX source, locally
  rendered because a fresh PDF download was unavailable.
- `figures/open_problem_crop.png`: full-width crop of source PDF page 6.
- `main.tex`, `solution_packet.pdf`: complete partial-result packet.
- `code/check_lp_convexity.py`: randomized finite-dimensional regression of
  the Ball--Carlen--Lieb midpoint inequality and threshold algebra.
- `VERIFICATION.md`: formal proof and scope audit.

Eight focused attempts are recorded in
`attempts/1204.6464_uniformly_convex_holder_retract_upgrade_attempts.md`.

Bounded run-index and web/arXiv searches on 2026-08-17 found continuous
retraction theorems, the source's Hilbert result, and Hölder results under
asymptotic regularity, but no explicit answer to the exact general question
or this invariant-mean criterion. Novelty confidence is moderate pending
expert review.
