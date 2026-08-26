# Full Solution Packet: Integer-to-Linear Kalton Embeddings

Run: `fa_banach_001`

Result type: `full`

Current verdict: `likely valid` (candidate full solution, pending human review)

## Source Problem

- Dikran Dikranjan, Dmitri Shakhmatov, and Jan Spěvák, *Direct sums and
  products in topological groups and vector spaces*, arXiv:1508.00667;
  Journal of Mathematical Analysis and Applications 437 (2016), 1257-1282.
- Exact location: Section 10, Question 10.6, PDF page 20; parsed source lines
  1371-1376.
- Evidence crop: `figures/open_problem_crop.png`.

If the integer Kalton map associated with a subset `A` of a topological vector
space is a topologically isomorphic embedding, Question 10.6 asks whether the
linear Kalton map associated with `A` must also be a topologically isomorphic
embedding.

## Candidate Result

Yes. Every topologically independent, absolutely Cauchy summable subset of a
real Hausdorff topological vector space has continuous real coordinate
projections. Consequently, the linear Kalton map is injective, continuous,
and open onto its image.

## Proof Intuition

Assume one real coordinate projection is discontinuous. Then arbitrarily
small finite real combinations can be chosen with that coordinate equal to
one. Absolute Cauchy summability makes the full real span of all but finitely
many vectors lie in a prescribed small neighbourhood. On the remaining
finite head, simultaneous Dirichlet approximation rounds a bounded multiple
of all real coefficients to integers. The tail rounding error is automatically
small, irrespective of its coefficients, and the head rounding error is small
by finite-dimensional continuity. The rounded integer combination is
therefore arbitrarily small but has a nonzero integer coefficient at the
distinguished vector. This contradicts topological independence.

## Verification Summary

- The simultaneous approximation lemma is proved in the packet by the
  pigeonhole principle.
- The neighbourhood choices are non-circular: the finite exceptional set is
  fixed before the denominator bound, and the discontinuity vector is chosen
  only after that bound is known.
- Tail errors may have arbitrary real coefficients because Proposition 9.2(i)
  of the source controls the whole real tail span, not merely integer sums.
- Every rounded combination has finite support.
- Proposition 10.2 of the source converts continuity of all coordinate
  projections exactly into openness of the linear Kalton map.
- No computation is relevant; the proof is qualitative and self-contained
  apart from elementary source equivalences that are restated explicitly.
- A same-context adversarial check is recorded in `verification_report.md`.

## Novelty Check

The run indexes were searched for arXiv:1508.00667, `linear Kalton map`, the
exact wording of Question 10.6, `topologically independent`, and `absolutely
Cauchy summable`. A bounded external search used the exact question, the paper
title and authors, and the phrases `linear Kalton map topologically isomorphic
embedding` and `integer Kalton map`. It found the source arXiv and journal
records but no later paper claiming to answer Question 10.6. This is not an
exhaustive citation search, so novelty confidence is moderate.

## Scope and Limitations

- The packet answers Question 10.6 affirmatively for the real linear Kalton
  map used by the source. A complex space can be viewed as a real topological
  vector space, which gives the same stated real-linear conclusion.
- It does not answer Question 9.8 for an arbitrary absolutely Cauchy summable
  set without topological independence.
- The verifier was not independent of the proof-writing context.

## Human Review Recommendation

Send to human review as a candidate full solution. The most important point to
check is the three-part decomposition of the rounding error in the main proof:
bounded multiple of the small vector, finite-head Dirichlet error, and
arbitrary-coefficient tail error.
