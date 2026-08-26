# Full Solution Packet: Multiplicity Two for Multiplication by the Coordinate

Run: `fa_banach_001`

Result type: `full`

Current verdict: `likely valid` (candidate full solution, pending human review)

## Source Problem

- March T. Boedihardjo, *Multiplication operators on L^p*, arXiv:1707.04798;
  Studia Mathematica 244 (2019), 309-319.
- Exact location: Section 4, Problem 1, PDF page 9; the note about the Hilbert
  case continues on PDF page 10. Parsed source lines 291-295.
- Evidence crop: `figures/open_problem_crop.png`.

For `1 < p < infinity`, `p != 2`, let `M f(t)=t f(t)` on `L^p[0,1]`. The
source asks whether there is a compact `K` such that `M direct-sum M` is
similar to `M+K`.

## Candidate Result

Yes. In fact, the conclusion holds for every `1 < p < infinity`, including
`p=2`. The similarity can be chosen as an explicit rearrangement of the
standard dyadic Haar basis.

## Proof Intuition

Diagonalize `M` modulo compact operators on the standard Haar basis by giving
the Haar function on a dyadic interval `I` the diagonal value equal to the
center of `I`. Two copies of this diagonal operator can be fitted into one Haar
basis: send the Haar function indexed by `I` in the first copy to the function
indexed by the left child of `I`, and send its counterpart in the second copy
to the right child. Constants occupy the two remaining coordinates.

The non-obvious point is that each fixed-child rearrangement is an isomorphism
on `L^p`. This follows from the Haar square-function equivalence and Stein's
vector-valued conditional-expectation inequality. After the rearrangement, a
parent's diagonal value is repeated on its children. It differs from either
child's own center by one quarter of the parent's length, which tends to zero
down the tree. The resulting diagonal discrepancy is compact.

## Verification Summary

- The Haar-diagonal compactness estimate is levelwise and summable.
- The child rearrangement was checked in both directions; the inverse bound is
  exactly where Stein's inequality is needed.
- The images of the two Haar copies, together with the constant and root Haar
  coordinates, partition the target Haar basis.
- The conjugated diagonal discrepancy is a null diagonal sequence, hence
  compact on an unconditional basis.
- `code/verify_dyadic_absorption.py` checks finite dyadic truncations, exact
  coordinate coverage, center discrepancies, and randomized norm ratios. It
  is finite-dimensional evidence only, not part of the proof.
- Command: `conda run --no-capture-output -n sandbox python
  code/verify_dyadic_absorption.py --samples 500 --max-depth 8 --seed
  170704798`. Result: exact coverage and center checks passed; across
  `p=1.2,1.5,3,5`, all randomized ratios were between `0.644458` and
  `1.687973`, with no finite-dimensional contradiction.
- A separate same-context adversarial report is in `verification_report.md`.

## Novelty Check

The run indexes were searched for arXiv:1707.04798, the exact problem wording,
`M_mu direct-sum M_mu`, `multiplicity two`, `compact perturbation`, and Haar
rearrangement terms. A bounded external search used the exact question,
paper title and author, arXiv id, and close operator-theoretic phrases. It found
the source arXiv and journal records and unrelated work on multiplication
operators, but no later paper claiming to solve Problem 1. This is not an
exhaustive citation search, so novelty confidence is moderate.

## Scope and Limitations

- The packet answers Problem 1 completely and strengthens it by including
  `p=2` with the same construction.
- It does not answer Problem 2 about a 1-summing perturbation for multiplication
  on a square in the complex plane.
- The proof uses two standard martingale facts: Haar square-function
  equivalence and Stein's vector-valued inequality.
- The verifier was not independent of the proof-writing context. Human review
  should focus on the lower bound for the child rearrangement and the final
  conjugation identity.

## Human Review Recommendation

Send to human review as a candidate full solution. The most important line to
check is the application of Stein's inequality in Lemma 1 of the packet; once
that is accepted, the compact-perturbation calculation is direct.
