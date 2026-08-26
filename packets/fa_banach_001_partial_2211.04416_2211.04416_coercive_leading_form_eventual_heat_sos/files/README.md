# Eventual heat-SOS for coercive leading forms

Status: `candidate_partial_result_likely_valid_pending_human_review`

Source: Raúl E. Curto, Philipp J. di Dio, Milan Korda, and Victor Magron,
*Time-dependent moments from partial differential equations and the
time-dependent set of atoms*, arXiv:2211.04416, Open Problem 5.1.

## Result

Let `f` be a real polynomial of degree `2d` in `n` variables.  If its leading
homogeneous form is a strict sum of squares (equivalently, it has a
positive-definite degree-`d` Gram matrix), then

`e^{t Delta}f`

is a sum of polynomial squares for every sufficiently large `t`.  In
particular, every bivariate polynomial whose leading form is positive on the
unit circle satisfies the conclusion of Open Problem 5.1.  This is slightly
stronger than the requested subcase because no sign assumption on the full
polynomial is needed.

After parabolic scaling, the homogenized heat orbit converges to
`e^{z^2 Delta}p`, where `p` is the leading form.  A positive-definite Gram
factorization of `p`, followed by Gaussian translation, gives a Gram matrix
for this limit.  Translations of a basis of degree-`d` forms span all
degree-`d` forms in one additional homogenizing variable, so the new Gram
matrix is itself positive definite.  The limit is therefore an interior SOS
point, and all sufficiently late normalized heat iterates remain SOS.

## Scope

The full question remains open when the leading binary form has a real
projective zero.  In that case the limiting Gaussian Gram form lies on a
proper SOS face; lower-degree terms can move through a nested family of
fat-point faces, and the interior argument no longer applies.

A bounded local-corpus and web search through 13 August 2026 used the exact
problem wording and combinations of `heat`, `eventual sum of squares`,
`coercive polynomial`, and `leading homogeneous form`.  The later
arXiv:2506.16321 cites the source but does not resolve this question.  No
explicit prior statement of the theorem in this packet was located; this is
not an exhaustive novelty claim.

## Packet contents

- `main.tex`, `solution_packet.pdf`: theorem, lemmas, and complete proof.
- `source_paper.pdf`: the arXiv source paper.
- `figures/open_problem_crop.png`: Open Problem 5.1 on PDF page 26.
- `VERIFICATION.md`: proof, source, and rendering checks.

Human review should focus on the normalized homogenization identity and on
the translation-span argument proving that the limiting Gaussian Gram matrix
is positive definite.

