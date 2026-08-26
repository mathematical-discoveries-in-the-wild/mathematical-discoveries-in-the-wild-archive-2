# A split Dedekind cut refutes Question 7.2 in rank one

Status: `candidate_counterexample_likely_valid`

Source: Michael Megrelishvili, *Intrinsic uniform structure on median
algebras*, arXiv:2605.16096, Question 7.2.

## Result

Question 7.2 has a negative answer even for a countable rank-one median
algebra, a discrete acting group, and a compact metrizable linearly ordered
median compactification.

Take `X=Q` with its usual order median and intrinsic (order) topology, and let
`G=Z` act by translations.  In the compact extended real line, replace the
irrational point `alpha=sqrt(2)` by two adjacent points
`alpha^-<alpha^+`.  The resulting compact order `K` contains `Q` as a dense
topologically and median embedded subalgebra, so it is a proper median
compactification.

Rational sequences approaching `alpha` from below and above converge in `K`
to `alpha^-` and `alpha^+`, respectively.  After translation by one, both
sequences converge to the single unsplit point `alpha+1`.  Any continuous
extension of translation therefore maps both split points to `alpha+1` and is
not injective.  A group action would make translation a homeomorphism, a
contradiction.

The packet proves the more general exact criterion: if `K_S` is obtained by
splitting a set `S` of nonprincipal Dedekind cuts, an increasing automorphism
extends to `K_S` exactly when its Dedekind extension preserves `S`.

## Important correction to the source's linearly ordered claim

The sentence after Question 7.2 says that the answer is positive in the
linearly ordered case and cites arXiv:2512.17314.  The relevant theorem there
assumes that every group element already extends to the chosen compactification
and proves that the resulting action is jointly continuous.  Equivalently, the
compactification must already be `G`-invariant.  It does not establish
extension to every proper ordered compactification.  The example above violates
exactly this invariance hypothesis.

## Files

- `solution_packet.pdf`: review-ready statement and proof.
- `main.tex`: self-contained LaTeX source.
- `source_paper.pdf`: locally compiled official arXiv source.
- `figures/open_problem_crop.png`: Question 7.2 on source page 25.
- `verification.md`: proof audit, citation audit, build, and visual-QA record.

## Scope and novelty

This completely settles the universal question negatively.  It also disproves
the accompanying claim as literally written for linearly ordered spaces.  It
does not classify arbitrary median compactifications, but the split-set lemma
gives an exact classification for this standard family of ordered
compactifications.

Local run indexes were searched for the arXiv id, title, exact question,
Dedekind-cut splitting, and translation terms.  Bounded primary-source web
searches found the source and general ordered-compactification literature but no
explicit answer to Question 7.2 or this example.  The construction is
elementary and uses classical split orders, so novelty beyond correcting this
specific 2026 question remains subject to expert review.

## Human-review recommendation

High priority.  Check only four points: compactness of the split order, equality
of the induced and intrinsic topologies on `Q`, continuity of the order median,
and the two one-sided limits under translation.  Also compare the source's
linearly ordered sentence with the invariance hypothesis in the cited theorem.

